# pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
sudo ln -s ~/.pyenv/bin/pyenv /usr/local/bin/pyenv
sudo ln -s ~/.pyenv/bin/pyenv /usr/local/sbin/pyenv
eval "$(pyenv init -)"


# python
pyenv install 3.10.7
pyenv global 3.10.7
pyenv rehash
sudo ln -fvs ~/.pyenv/shims/* /usr/local/bin/

# NOTE to test python installed correctly
# pyenv which python3
# NOTE binary
# /home/qtwu/.pyenv/versions/3.10.7/bin/python3
# NOTE path files
# /home/qtwu/.pyenv/versions/3.10.7/lib/python3.10/site-packages


# add python default path
echo "/active" > ~/.pyenv/versions/3.10.7/lib/python3.10/site-packages/qtwu.pth
