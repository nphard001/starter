TXT2IMG = /active/sd/outputs/txt2img-images
IMG2IMG = /active/sd/outputs/img2img-images
GRIDTXT2IMG = /active/sd/outputs/txt2img-grids
GRIDIMG2IMG = /active/sd/outputs/img2img-grids
EXTRAIMG = /active/sd/outputs/extras-images

SWAP = /active/tmp/swap
PACK = /active/tmp/pack

pack1:
	mkdir -p /active/zip || true
	mkdir -p /active/tmp || true
	rm -rf /active/tmp/*
	mv $(SRCDIR) $(SWAP)
	mkdir -p $(SRCDIR) || true
	mkdir -p $(PACK)
	find $(SWAP) -name "*.png" -type f -print0 | xargs -0 mv -t $(PACK)/
	@current_datetime=$$(date +"%Y%m%d%H%M"); \
	cd $(PACK) && zip -r /active/zip/$$current_datetime-$(NAME).zip ./*

packti packii packgti packgii packex: pack%:
	@target_dir=$$(\
		case "$*" in \
			ti) echo "$(TXT2IMG)" ;; \
			ii) echo "$(IMG2IMG)" ;; \
			gti) echo "$(GRIDTXT2IMG)" ;; \
			gii) echo "$(GRIDIMG2IMG)" ;; \
			ex) echo "$(EXTRAIMG)" ;; \
		esac \
	); \
	name=$$(\
		case "$*" in \
			ti) echo "txt2img" ;; \
			ii) echo "img2img" ;; \
			gti) echo "txt2img-grid" ;; \
			gii) echo "img2img-grid" ;; \
			ex) echo "extra" ;; \
		esac \
	); \
	echo "Packing code short for $*, name $$name, target directory is $$target_dir"; \
	$(MAKE) -e pack1 NAME=$$name SRCDIR=$$target_dir

URL1_anythingQing = https://drive.google.com/file/d/1ewTAAcPkyZoVV9-n0sHf7ODZ-9ejWx9z/view?usp=drive_link
URL3_realisticVision = https://drive.google.com/file/d/1HcLe4nNAkw8I_5v6LkKns8m7U63NXLRn/view?usp=drive_link

modelAQ modelSD modelRV: model%:
	@URL=$$(\
		case "$*" in \
			AQ) echo "$(URL1_anythingQing)" ;; \
			SD) echo "$(URL2_stablediffusion2)" ;; \
			RV) echo "$(URL3_realisticVision)" ;; \
		esac \
	); \
	echo "Downloading from $$URL"; \
	gdown --fuzzy $$URL -O /content/stable-diffusion-webui/models/Stable-diffusion/


