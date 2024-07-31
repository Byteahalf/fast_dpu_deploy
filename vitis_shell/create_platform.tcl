platform create -name {amd_ai_platform} \
    -hw {src/base_wrapper.xsa} \
    -proc {psu_cortexa53} \
    -os {linux} \
    -arch {64-bit} \
    -no-boot-bsp \
    -fsbl-target {psu_cortexa53_0} -out {./platform/}

domain config -generate-bif

platform -generate
