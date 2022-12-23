# ubuntu 18.04 basic packages
sudo apt-get update
sudo apt-get install -y rsync
sudo apt-get install -y tmux
sudo apt-get install -y htop
sudo apt-get install -y make
sudo apt-get install -y vim
sudo apt-get install -y git
sudo apt-get install -y tree
sudo apt-get install -y g++
sudo apt-get install -y gdb
sudo apt-get install -y cmake
sudo apt-get install -y clang
sudo apt-get install -y xauth
sudo apt-get install -y bzip2
sudo apt-get install -y unzip
sudo apt-get install -y strace
sudo apt-get install -y traceroute
sudo apt-get install -y lsof
sudo apt-get install -y nload
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libz-dev
sudo apt-get install -y libreadline-dev
sudo apt-get install -y libncurses5-dev
sudo apt-get install -y libncursesw5-dev
sudo apt-get install -y libsqlite3-dev
sudo apt-get install -y liblzma-dev

# pyenv stuff
# source: https://stackoverflow.com/a/67853440
sudo apt update
sudo apt -y install \
    build-essential \
    curl \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libxml2-dev \
    libxmlsec1-dev \
    llvm \
    make \
    tk-dev \
    wget \
    xz-utils \
    zlib1g-dev

# oh my zsh
sudo apt-get install -y zsh
sh -c "$(wget https://raw.githubusercontent.com/nphard001/oh-my-zsh/master/tools/install.sh -O -)"
