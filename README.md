# WFX firmware

This repository contains:

* WFx secured firmware file
* The [WFx release note][FW_RELEASE]
* PDS (Platform Data Set) files
  * PDS definitions
  * PDS template

## WFx secured firmware files

The secured firmware **wfm_wf200_C0.sec** file is an authenticated and encrypted binary for the WFx family of chips and modules.

## PDS (Platform Data Set) files

Look into [wfx-firmware/PDS/README.md][FW_DOC] for details about `PDS/definitions.in` and `PDS/template.pds.in`.

## Related drivers

The WFx firmware is loaded by:

* The [wfx-linux-driver][DRV_LINUX_REPO] for Linux applications
* The [wfx-fullMAC-driver][DRV_FMAC_REPO] for RTOS or bare-metal applications

[DRV_LINUX_REPO]: https://github.com/SiliconLabs/wfx-linux-driver
[DRV_FMAC_REPO]: https://github.com/SiliconLabs/wfx-fullMAC-driver
[FW_RELEASE]: CHANGES.md
[FW_DOC]: https://github.com/SiliconLabs/wfx-firmware/blob/master/PDS/README.md
