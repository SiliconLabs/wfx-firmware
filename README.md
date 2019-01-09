# WFX_FIRMWARE

Contains WFx secured firmware and PDS file examples.

* Secured Firmware image **.sec** file is an authenticated and encrypted 
binary for WFx family of chips and modules.
* Platform Data Set (i.e. PDS) (**.pds** under Linux, **.h** otherwise) 
 is a platform-dependent configuration file. It is generated from a 
 **.pds.in** file using the `pds_compress` tool (available from 
 https://github.com/SiliconLabs/wfx-linux-tools).

Both files need to be downloaded to the chip/module at boot.

**`git clone` this repository on your system.**

Linux driver from Silicon Laboratories from
 https://github.com/SiliconLabs/wfx-linux-driver are expecting the 
 firmware and pds files to be located in `/lib/firmware` and named 
 `wfm_wf200.sec` and `wf200.pds`, respectively.
You need to create a symbolic link or a copy into `/lib/firmware` and
 rename the files accordingly.


> **Linux naming convention:**
> - The sec file should be named `/lib/firmware/wfm_wf200.sec`
> - The pds file should be named `/lib/firmware/wf200.pds`


