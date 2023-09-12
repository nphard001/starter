mkdir -p /content/stable-diffusion-webui/models/Stable-diffusion || true
mkdir -p /content/stable-diffusion-webui/extensions || true
mkdir -p /active/zip
mkdir -p /active/tmp
ln -s /content/stable-diffusion-webui /active/sd
wget https://raw.githubusercontent.com/nphard001/starter/master/sd/Makefile -O /active/Makefile

