open_project dpu.build/link/vivado/vpl/prj/prj.xpr

set_property pfm_name {xilinx:kr260_som:amd_ai_base:1.0} [get_files -all {dpu.build/link/vivado/vpl/prj/prj.srcs/sources_1/bd/base/base.bd}]
set_property platform.uses_pr {false} [current_project]
write_hw_platform -hw -include_bit -force -file export/src/base_wrapper.xsa

open_run impl_1
write_bitstream -bin_file export/src/dpu.bit
