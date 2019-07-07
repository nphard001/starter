# Starter Scripts
> inspired by https://github.com/robbyrussell/oh-my-zsh
> + `sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"`


## Add user to sudoers with `NOPASSWD`
`
sh -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/nopasswd.sh --no-cache --quiet -O -) YOUR_USERNAME"
`

## Check python3==3.5.3
`
sh -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/check353.sh --no-cache --quiet -O -)"
`

## Install "basic" packages on Debian
`
python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/debian.py --no-cache --quiet -O -)"
`

## Install ALL
`
python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/all.py --no-cache --quiet -O -)"
`

## The "ALL" List
+ `
python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/debian.py --no-cache --quiet -O -)"
`
+ `
python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/ohmyzsh.py --no-cache --quiet -O -)"
`
+ `
python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/pyenv.py --no-cache --quiet -O -)"
`
+ `
python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/pkg368.py --no-cache --quiet -O -)"
`
+ `
python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/pkg368_jupyter.py --no-cache --quiet -O -)"
`