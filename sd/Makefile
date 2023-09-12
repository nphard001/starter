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
	pip install gdown
	RUNBG=1 $(MAKE) modelURP
	RUNBG=1 $(MAKE) modelAQ

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
	@current_datetime=$$(TZ='Asia/Taipei' date +"%Y%m%d%H%M"); \
	mv /active/zip /active/zip-$$current_datetime
	mkdir -p /active/zip || true


URL1_anythingQing = https://drive.google.com/file/d/1ewTAAcPkyZoVV9-n0sHf7ODZ-9ejWx9z/view?usp=drive_link
URL3_realisticVision = https://drive.google.com/file/d/1HcLe4nNAkw8I_5v6LkKns8m7U63NXLRn/view?usp=drive_link
URL4_movie = https://drive.google.com/file/d/16Vi_cNM4w_g16HWr9gqSAtLkZtNA1B-N/view?usp=drive_link
URL5_URP = https://drive.google.com/file/d/1-ZjJ-jcZbuzcw2QpC8uNKOx9kOcv6yb5/view?usp=drive_link

# example: RUNBG=1 $(MAKE) modelMV
modelAQ modelRV modelMV modelURP: model%:
	@URL=$$(\
		case "$*" in \
			AQ) echo "$(URL1_anythingQing)" ;; \
			RV) echo "$(URL3_realisticVision)" ;; \
			MV) echo "$(URL4_movie)" ;; \
			URP) echo "$(URL5_URP)" ;; \
		esac \
	); \
	echo "Downloading from $$URL"; \
	if [ "$${RUNBG}" = "1" ]; then \
		gdown --fuzzy $$URL -O /content/stable-diffusion-webui/models/Stable-diffusion/ & \
	else \
		gdown --fuzzy $$URL -O /content/stable-diffusion-webui/models/Stable-diffusion/; \
	fi


