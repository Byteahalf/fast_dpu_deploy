# HOW USE FAST DEPLOTMENT SCRIPT

1. Make sure
    * src/base_wrapper.xsa is a valid vitis extensible platform
    * dpu.xo, sfm.xo is exist

2. Makefile command
    * **make all**: 
        * Generate all files, need about 2-3 hours
    * **make pack**: 
        * Pack the export file
    * **make pack_pynq**: 
        * Pack the export file for pynq-dpu
    * **make clean**: 
        * Clean Vitis generated file
    * **make clean_log**: 
        * Clean the log file