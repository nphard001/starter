import os, sys, json, inspect
import datetime
import subprocess


def make_path(base):
    def _f(*args):
        path = os.path.join(base, *args)
        path = os.path.abspath(path)
        return path
    return _f


def mkdir(fname):
    return os.makedirs(fname, exist_ok=True)


def touch(fname):
    try:
        os.utime(fname, None)
    except OSError:
        open(fname, 'a').close()


def run(cmd, return_stdout=False):
    st = datetime.datetime.now().timestamp()
    print('[run]', cmd, file=sys.stderr)
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    rc = proc.returncode
    print('[run:%4d] (%10.2f) %s'%(rc, datetime.datetime.now().timestamp()-st, cmd))
    if return_stdout:
        return proc.stdout
    return rc


def run_utf8(cmd):
    return run(cmd, True).decode('utf-8')


jpath = run_utf8("jupyter --paths --json")
jpath = json.loads(jpath)
_JupyterHome = make_path(jpath['config'][0])
_JupyterShare = make_path(jpath['data'][0])


def _script():
    print(_JupyterHome())
    print(_JupyterShare())
    
    mkdir(_JupyterHome("custom"))
    touch(_JupyterHome('custom/custom.js'))
    touch(_JupyterHome('custom/custom.css'))
    mkdir(_JupyterShare('nbextensions/snippets'))
    touch(_JupyterShare('nbextensions/snippets/snippets.json'))
    run(f'pip install jupyter_nbextensions_configurator')
    run(f'pip install jupyter_contrib_nbextensions')
    # BUG: 'b_nbextensions"' is not recognized as an internal or external command,
    #      operable program or batch file.
    # run(f'jupyter contrib nbextension install --user') # stuck, why?
    print('install done')
    # --------==== Javascript: sublime keymap, resize ====--------
    print("js path:", _JupyterHome("custom/custom.js"))
    print("access:", os.access(_JupyterHome("custom/custom.js"), os.R_OK))
    with open(_JupyterHome("custom/custom.js"), 'w') as f:
        f.write(r'''
window.addEventListener("resize", myFunction);
function myFunction() {
    document.querySelector("#site").style.height = "100%";
}
myFunction(); // resize when first load

require(["codemirror/keymap/sublime", "notebook/js/cell", "base/js/namespace"],
    function(sublime_keymap, cell, IPython) {
        cell.Cell.options_default.cm_config.keyMap = 'sublime';
        cell.Cell.options_default.cm_config.extraKeys["Ctrl-Enter"] = function(cm) {}
        var cells = IPython.notebook.get_cells();
        for(var cl=0; cl< cells.length ; cl++){
            cells[cl].code_mirror.setOption('keyMap', 'sublime');
            cells[cl].code_mirror.setOption("extraKeys", {
                "Ctrl-Enter": function(cm) {}
            });
        }
    } 
);
        '''.strip())

    # --------==== CSS: basic style ====--------
    with open(_JupyterHome("custom/custom.css"), 'w') as f:
        f.write(r'''
@import url(https://fonts.googleapis.com/earlyaccess/notosanstc.css);

div.rendered_html{
font-family: 'Noto Sans TC', sans-serif !important;
font-weight: 400 !important;
font-size: 100% !important;
line-height: 1.8em !important;
}

div.text_cell_render.rendered_html > h1{
border-style: solid;
border-width: 0px 0px 1px 0px;
padding: 0px 0px 0.2em 0px;
margin: 1.3em 0px 0.65em 0px;
}
div.text_cell_render.rendered_html > h2{margin: 0.6em 0em 0.4em 0;}
div.text_cell_render.rendered_html > h3{margin: 0.6em 0em 0.4em 0;}
div.text_cell_render.rendered_html > h4{margin: 0.5em 0em 0.35em 0;}
div.text_cell_render.rendered_html > h5{margin: 0.5em 0em 0.35em 0;}
div.text_cell_render.rendered_html > h6{margin: 0.5em 0em 0.35em 0;}
div.tooltipbuttons { opacity: 0.5; }
body, table, select, input, img {
font-size: 1em !important;
}
body {
position: relative !important;
}
    '''.strip())


if __name__ == '__main__':
    _script()
