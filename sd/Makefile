# TODO: .jpg parser
# TODO: grided only
# TODO: auto zip

TXT2IMG = /active/sd/outputs/txt2img-images
IMG2IMG = /active/sd/outputs/img2img-images
GRIDTXT2IMG = /active/sd/outputs/txt2img-grids
GRIDIMG2IMG = /active/sd/outputs/img2img-grids
EXTRAIMG = /active/sd/outputs/extras-images
DIR_MODELS = /active/sd/models/Stable-diffusion

SWAP = /active/tmp/swap
PACK = /active/tmp/pack

start:
	mkdir -p /active/zip || true
	mkdir -p /active/tmp || true
	mkdir -p /active/upload || true
	mkdir -p /content/stable-diffusion-webui/models/Stable-diffusion || true
	mkdir -p /content/stable-diffusion-webui/extensions || true
	ln -s /content/stable-diffusion-webui /active/sd || true
	pip install gdown fire PyDrive loguru || true
	$(MAKE) downloads || true

.PHONY: upload
upload:
	python /active/upload.py

pack1:
	mkdir -p /active/zip || true
	mkdir -p /active/tmp || true
	rm -rf /active/tmp/*
	mv $(SRCDIR) $(SWAP)
	mkdir -p $(SRCDIR) || true
	mkdir -p $(PACK)

	file_count=$$(find $(SWAP) \( -name "*.png" -o -name "*.jpg" \) -type f | wc -l); \
	find $(SWAP) \( -name "*.png" -o -name "*.jpg" \) -type f -print0 | xargs -0 mv -t $(PACK)/; \
	current_datetime=$$(TZ='Asia/Taipei' date +"%m%d%H%M"); \
	cd $(PACK) && zip -r /active/zip/$$current_datetime-$(NAME)-$$file_count.zip ./*


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
	mkdir -p /active/sd/outputs || true

	mv /active/sd/outputs /active/archive/outputs

	# Recover directories from /active/archive/outputs
	find /active/archive/outputs -type d -exec bash -c 'mkdir -p "/active/sd/$$(realpath --relative-to=/active/archive {})"' \;

	@current_datetime=$$(TZ='Asia/Taipei' date +"%Y%m%d%H%M"); \
	mv /active/archive/outputs /active/archive/outputs-$$current_datetime

include data.makefile

# example: RUNBG=1 $(MAKE) modelMV 
model_gdown:
	$(MAKE) download_gdown URL=$(URL) TARGET=$(DIR_MODELS)
model_aria2c:
	$(MAKE) download_aria2c URL=$(URL) TARGET=$(DIR_MODELS) FNAME=$(FNAME)

# Generalized download target
download_gdown:
	@if [ "$${RUNBG}" = "1" ]; then \
		gdown --fuzzy $(URL) -O $(realpath $(TARGET))/ & \
	else \
		gdown --fuzzy $(URL) -O $(realpath $(TARGET))/ ; \
	fi

download_aria2c:
	@if [ "$${RUNBG}" = "1" ]; then \
		aria2c --console-log-level=error -c -x 16 -s 16 -k 1M $(URL) -d $(realpath $(TARGET)) -o $(FNAME) & \
	else \
		aria2c --console-log-level=error -c -x 16 -s 16 -k 1M $(URL) -d $(realpath $(TARGET)) -o $(FNAME) ; \
	fi


# make ext_git URL=https://github.com/Gourieff/sd-webui-reactor
ext_git:
	@repo_name=$$(basename $(URL) .git); \
		echo "Cloning $$repo_name..."; \
		git clone $(URL) /content/stable-diffusion-webui/extensions/$$repo_name
