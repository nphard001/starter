# TODO: .jpg parser
# TODO: grided only
# TODO: auto zip

TXT2IMG = /active/sd/outputs/txt2img-images
IMG2IMG = /active/sd/outputs/img2img-images
GRIDTXT2IMG = /active/sd/outputs/txt2img-grids
GRIDIMG2IMG = /active/sd/outputs/img2img-grids
EXTRAIMG = /active/sd/outputs/extras-images

SWAP = /active/tmp/swap
PACK = /active/tmp/pack

start:
	mkdir -p /content/stable-diffusion-webui/models/Stable-diffusion || true
	mkdir -p /content/stable-diffusion-webui/extensions || true
	ln -s /content/stable-diffusion-webui /active/sd || true
	pip install gdown
	$(MAKE) downloads

pack1:
	mkdir -p /active/zip || true
	mkdir -p /active/tmp || true
	rm -rf /active/tmp/*
	mv $(SRCDIR) $(SWAP)
	mkdir -p $(SRCDIR) || true
	mkdir -p $(PACK)

	@PTYPE=$${PTYPE:-png}; \
	find $(SWAP) -name "*.$$PTYPE" -type f -print0 | xargs -0 mv -t $(PACK)/

	@current_datetime=$$(TZ='Asia/Taipei' date +"%j%H%M"); \
	cd $(PACK) && zip -r /active/zip/$$current_datetime-$(NAME).zip ./*

packti packii packtig packiig packex: pack%:
	@target_dir=$$(\
		case "$*" in \
			ti) echo "$(TXT2IMG)" ;; \
			ii) echo "$(IMG2IMG)" ;; \
			tig) echo "$(GRIDTXT2IMG)" ;; \
			iig) echo "$(GRIDIMG2IMG)" ;; \
			ex) echo "$(EXTRAIMG)" ;; \
		esac \
	); \
	name=$$(\
		case "$*" in \
			ti) echo "txt" ;; \
			ii) echo "img" ;; \
			tig) echo "txt-grid" ;; \
			iig) echo "img-grid" ;; \
			ex) echo "extra" ;; \
		esac \
	); \
	echo "Packing code short for $*, name $$name, target directory is $$target_dir"; \
	$(MAKE) -e pack1 NAME=$$name SRCDIR=$$target_dir

zip2:
	mkdir -p /active/zip || true
	mkdir -p /active/archive || true
	@current_datetime=$$(TZ='Asia/Taipei' date +"%Y%m%d%H%M"); \
	mv /active/zip /active/archive/zip-$$current_datetime
	mkdir -p /active/zip || true


out2:
	mkdir -p /active/archive || true

	@current_datetime=$$(TZ='Asia/Taipei' date +"%Y%m%d%H%M"); \
	echo "Moving /active/sd/outputs to /active/archive/outputs-$$current_datetime"; \
	mv /active/sd/outputs /active/archive/outputs-$$current_datetime; \
	
	@echo "Rebuilding empty directories under /active/sd/outputs"; \
	find /active/archive/outputs-$$current_datetime -type d -exec bash -c 'mkdir -p "/active/sd/outputs/$$(realpath --relative-to=/active/archive/outputs-$$current_datetime {})"' \;

include data.makefile

# example: RUNBG=1 $(MAKE) modelMV 
# Generalized download target
model_gdown:
	@actual_url=$(URL_$(MODEL)); \
	echo "Downloading from $$actual_url"; \
	if [ "$${RUNBG}" = "1" ]; then \
		gdown --fuzzy $$actual_url -O /content/stable-diffusion-webui/models/Stable-diffusion/ & \
	else \
		gdown --fuzzy $$actual_url -O /content/stable-diffusion-webui/models/Stable-diffusion/; \
	fi

# make ext_git URL=https://github.com/Gourieff/sd-webui-reactor
ext_git:
	@if [ -z "$(URL)" ]; then \
		echo "URL must be specified."; \
		exit 1; \
	fi
	@repo_name=$$(basename $(URL) .git); \
		echo "Cloning $$repo_name..."; \
		git clone $(URL) /content/stable-diffusion-webui/extensions/$$repo_name

