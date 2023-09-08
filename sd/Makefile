TXT2IMG = /active/sd/outputs/txt2img-images
IMG2IMG = /active/sd/outputs/img2img-images
GRIDTXT2IMG = /active/sd/outputs/txt2img-grids
GRIDIMG2IMG = /active/sd/outputs/img2img-grids
EXTRAIMG = /active/sd/outputs/extras-images

SWAP = /active/tmp/swap
PACK = /active/tmp/pack

pack1:
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
			ti) echo "$(TXT2IMG)"; name="txt2img" ;; \
			ii) echo "$(IMG2IMG)"; name="img2img" ;; \
			gti) echo "$(GRIDTXT2IMG)"; name="txt2img-grid" ;; \
			gii) echo "$(GRIDIMG2IMG)"; name="img2img-grid" ;; \
			ex) echo "$(EXTRAIMG)"; name="extra" ;; \
		esac \
	); \
	echo "Packing code short for $*, name $$name, target directory is $$target_dir"; \
	$(MAKE) -e pack1 NAME=$$name SRCDIR=$$target_dir

