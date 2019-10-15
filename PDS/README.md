# PDS (Platform Data Set) template and definitions files

**P**latform **D**ata **S**et (**PDS**) files contain firmware configuration values to match the hardware (I/O pinout) and the application (activating features/configuring the behavior).

## PDS `template.pds.in`

`template.pds.in` lists all possible PDS sections and parameters which can be sent to WFx firmware. It
 contains inline documentation on PDS sections and parameters.

When looking for the latest information on PDS sections and parameters, refer to the PDS template.

When creating a custom PDS file, refer to the PDS template and copy required sections to your custom PDS file, using the inline documentation to select PDS parameter values.

## PDS `definitions.in`

`definitions.in` defines values for all **PDS sections** and **PDS parameters**. It is referenced by custom PDS files and PDS files provided in the [wfx-pds repository][PDS_REPO] to obtain the final `.pds` file.

## Hardware-specific PDS files

Hardware-specific PDS files are created based on the PDS template and PDS definitions files to match various boards.

Hardware-specific PDS files for Silicon Labs evaluation boards are stored in the [wfx-pds repository][PDS_REPO].

## PDS flow

PDS input files are like C header files while PDS output data uses a compressed format:

* For easy editing, PDS input files (`.pds.in`) are in a human-readable format, with inline documentation.

* To fit embedded applications, `.pds.in` files are compressed using the [pds_compress][PDS_CMP] (_python3 script_) tool to the `.pds` file format.

The PDS generation flow is:

* Edit
  * Copy/paste an existing PDS file or start from `template.pds.in`
  * In `<custom>.pds.in`, include `definitions.in`
  * Use the inline comments to define
    * The sections to use
    * The values to set
  * Remove unused sections
  * Add required sections from `template.pds.in` if starting from an existing PDS file
  * Set values (from `definitions.in`) to match the hardware and define the behavior
* Compress
  * compress your `.pds.in` file to `.pds` using [pds_compress][PDS_CMP]
* Store
  * Linux: copy the `.pds` file under /lib/firmware/wf200.pds
  * RTOS: recompile with the new PDS data
* Send (by the WFx driver)
  * During each start-up phase, the WFx driver sends the `.pds` file after FW download & FW start

### Compressing PDS files

Use `pds_compress [options] INPUT [OUTPUT]` to compress a `.pds.in` file to a `.pds` file,
 ready to be sent to the WFX firmware.

Use `pds_compress --help` to display the help

Typical use:

* Linux: `pds_compress <custom>.pds.in <custom>.pds`
* RTOS: `pds_compress --out=c <custom>.pds.in <custom>.h`

_Resulting `.pds` files should not be edited. It is recommended to always start from human-readable files such as `.pds.in` files_

[FW_REPO]: https://github.com/SiliconLabs/wfx-firmware
[PDS_DOC]: https://github.com/SiliconLabs/wfx-pds/blob/master/README.md
[PDS_REPO]: https://github.com/SiliconLabs/wfx-pds
