# platform: create base platform by vivado xsa

NAME ?= dpu

all: export/$(NAME).xclbin export/$(NAME).bin export/${NAME}.dtbo export/$(NAME).hwh export/shell.json export/src/arch.json


collect:
	-mkdir src
	cp ../vivado/amd/*.xsa src/base_wrapper.xsa

platform: 
	-rm -r platform
	xsct create_platform.tcl
	mv platform/amd_ai_platform/export/amd_ai_platform temp
	rm -r ./platform
	mv temp platform

$(NAME).xclbin: platform
	-rm -r dpu.build dpu.mdb
	v++ --target hw --link --config config.cfg -o"${NAME}.xclbin" dpu.xo sfm.xo

export/$(NAME).xclbin: $(NAME).xclbin
	cp $(NAME).xclbin export/$(NAME).xclbin

export/$(NAME).bin: $(NAME).xclbin
	-mkdir export
	-mkdir export/src
	vivado -mode batch -source export_final_xsa.tcl
	mv export/src/dpu.bin export/dpu.bin
	mv export/src/dpu.bit export/dpu.bit

device-tree-xlnx:
	git clone https://github.com/Xilinx/device-tree-xlnx.git --branch xlnx_rel_v2022.2

export/src/$(NAME).dtsi: $(NAME).xclbin
	xsct create_device_tree.tcl

export/${NAME}.dtbo: export/src/$(NAME).dtsi
	dtc -@ -O dtb -o export/${NAME}.dtbo export/src/dpu.dtsi/pl.dtsi

export/shell.json:
	echo '{' > shell.json
	echo '    "shell_type" : "XRT_FLAT",' >> shell.json
	echo '    "num_slots" : "1"' >> shell.json
	echo '}' >> shell.json	
	mv shell.json export/shell.json

export/$(NAME).hwh:
	cp dpu.build/link/vivado/vpl/prj/prj.gen/sources_1/bd/base/hw_handoff/base.hwh export/$(NAME).hwh

export/src/arch.json: $(NAME).xclbin
	cp dpu.build/link/vivado/vpl/prj/prj.gen/sources_1/bd/base/ip/base_DPUCZDX8G_1_0/arch.json export/src/arch.json
	cp dpu.build/link/vivado/vpl/prj/prj.gen/sources_1/bd/base/ip/base_DPUCZDX8G_1_0/arch.json export/arch.json

pack:
	tar -czvf export/pack.tar.gz export/$(NAME).*  export/arch.json export/shell.json

pack_pynq:
	tar -czvf export/pynq.tar.gz export/dpu.xclbin export/dpu.bit export/dpu.hwh

clean: clean_log
	-rm -r .ipcache .Xil dpu.build platform
	-rm -r dpu.xclbin dpu.xclbin.* dpu.mdb

clean_log:
	-rm *.log *.str *.jou dpu.mdb dpu.xclbin.*


.PHONY: clean
