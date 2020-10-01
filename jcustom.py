import os, sys, json, inspect
import datetime
import subprocess
if os.system('ls /home')==0:  # linux
    _JupyterHome = lambda *args: os.path.abspath(os.path.join(
        f'~/.jupyter', *args))
    _JupyterShare = lambda *args: os.path.abspath(os.path.join(
        f'~/.local/share/jupyter/', *args))
else:  # osx
    _JupyterHome = lambda *args: os.path.abspath(os.path.join(
        f'~/.jupyter', *args))
    _JupyterShare = lambda *args: os.path.abspath(os.path.join(
        f'~/Library/Jupyter', *args))
def run(cmd):
    st = datetime.datetime.now().timestamp()
    print('[run]', cmd, file=sys.stderr)
    rc = subprocess.run(cmd, shell=True).returncode
    print('[run:%4d] (%10.2f) %s'%(rc, datetime.datetime.now().timestamp()-st, cmd))
    return rc

# before custom (2019-04-19 09:52:00)
run(f'mkdir -p '+_JupyterHome("custom"))
run(f'touch '+_JupyterHome('custom/custom.js'))
run(f'touch '+_JupyterHome('custom/custom.css'))
run(f'mkdir -p '+_JupyterShare('nbextensions/snippets'))
run(f'touch '+_JupyterShare('nbextensions/snippets/snippets.json'))
run(f'pip install jupyter_nbextensions_configurator')
run(f'pip install jupyter_contrib_nbextensions')
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
