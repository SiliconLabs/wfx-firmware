# WFX_FIRMWARE

Contains WFx secured firmware and pds file examples.

Secured Firmware image .sec file is an authenticated and encrypted binary for WFx family of chips and modules.
Platform data set, PDS, .json file is a platform dependant configuration file. 
They both need to be downloaded to the chip/module at boot.

git clone this repository on your system.

Linux driver from Silicon Laboratories from https://github.com/SiliconLabs/wfx_linux_driver_code are expecting the firmware and pds files to be located in /lib/firmware
You need to create a symbolic link or a copy into /lib/firmware and rename the files accordingly.

> **Naming convention:**
> - The pds file should be named /lib/firmware/pds_wf200.json
> - The sec file should be named /lib/firmware/wfm_wf200.sec


