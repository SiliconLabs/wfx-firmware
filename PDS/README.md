# PDS (Platform Data Set) files

**P**latform **D**ata **S**et (**PDS**) files contain configuration values sent
 by the WFX driver to the WFX firmware, either at startup (for basic hardware
  configuration) or during execution (typical case: using TEST_FEATURE for RF testing).

## PDS flow
For easy editing, PDS **node** and **attribute** values are stored in `.pds.in`  files in
human-readable format, with inline documentation. (Refer to this documentation for
 details on nodes and attributes).

To save time during execution, `.pds.in` files are compressed using the **pds_compress**
(_python3 script_) tool to the `.pds` file format.

### Compressing PDS files
Use `pds_compress [options] INPUT [OUTPUT]` to compress a `.pds.in` file to a `.pds` file,
 ready to be sent to the WFX firmware.

### Startup PDS file
During WFX driver startup, after WFX firmware download, the driver
sends the `.pds` file to the WFX firmware,
in order to configure the WFX hardware to match the application.

* Startup PDS file name and location

| | Linux LMAC driver | MCU FMAC WFX driver
|---|---|---
Final Location|/lib/firmware/wf200.pds| wf200_pds.h (by default)
Compressed using|`pds_compress --out=pds <my_pds.pds.in> wf200.pds`|`pds_compress --out=c <my_pds.pds.in> wf200_pds.h`
Info|can use symbolic links| Header file loaded at runtime


_PDS `.pds.in` and **definitions** files can easily be edited with any text editor and benefit from code coloring and
 folding if the editor treats them as C files, for instance._

_Resulting `.pds` files can be displayed for checking but
  should not be edited. It is recommended to always start from human-readable files such as `.pds.in` files_

### Linux: Sending a PDS file during execution
It is possible to send additional PDS content during execution.
This is typically useful when using the TEST_FEATURE to perform continuous Tx testing.

To support this under Lniux, the write-only `/sys/kernel/debug/ieee80211/phy*/wfx/send_pds` file has been added to the filesystem.
_Upon writing to this file, the data is sent to the FW by the driver as PDS data._

| Linux | MCU
---|---|---
Send an already existing .pds file|`cat <file>.pds /sys/kernel/debug/ieee80211/phy*/wfx/send_pds`| load pds file at runtime
Compress and send a .pds.in file|`pds_compress <file>.pds.in /sys/kernel/debug/ieee80211/phy*/wfx/send_pds`| Compress first and send if OS unable to pipe the operations

## PDS files details

### Definitions file
A firmware-version related **definitions** file is referenced with a '#include' by the `.pds.in` file and pre-processed
by pds_compress (pretty much as a C pre-compiler would work) to obtain a more compact file.

### .pds.in file inclusion
It is possible to `#include` a `.pds.in` file from another `.pds.in` file.

## pds_compress options
Use `pds_compress --help` to display the help
```
usage: pds_compress [options] INPUT [OUTPUT]

Generate a compressed version of PDS from a full PDS

positional arguments:
  INPUT                 input file (except C format, all output formats can be
                        used as input)
  OUTPUT                output file (standard output if not specified)

optional arguments:
  -h, --help            show this help message and exit
  -I DIR, --include DIR
                        search includes in this subdirectory
  -D DEF[=VAL], --define DEF[=VAL]
                        predefine DEF with value VAL
  -f, --force           try to produce (probably broken) output even if errors
                        are detected
  --out {pds,tinypds,c,json}
                        specify output format. Accepted values: pds
                        (compressed PDS), tinypds (indented PDS), c (C file),
                        json. Default: pds
  -j                    shortcut for --out=json
  -c                    shortcut for --out=c
  -p                    shortcut for --out=pds
  -t                    shortcut for --out=tinypds
```

## pds_compress input examples

Use `pds_compress [options] INPUT [OUTPUT]` to compress a `.pds.in` file to a `.pds` file,
 ready to be sent to the WFX firmware.

(PDS output examples below are based on the following files)

* definitions`.in` file (abstract)
```
/*
 * These definitions come from firmware 2.0.0 headers
 */
#ifndef DEFINITIONS_2_0_0_IN
#define DEFINITIONS_2_0_0_IN

/*
 * Nodes declarations
 */
#define HEADER_ELT              a
#define     VERSION_MAJOR           a
#define     VERSION_MINOR           b
. . .
#define RF_ANTENNA_SEL_DIV_CONF j
#define     RF_PORTS                a
#define     DIVERSITY               b
#define     EXT_SWITCH_CONTROL      c
#define         NB_ANTENNA              a
#define         NB_GPIO                 b
#define         GPIO_ID_1               c
#define         GPIO_ID_2               d
#define         GPIO_ID_3               e
. . .

/*
 * Attribute values
 * These value should more or less follow output of
 *   sed -ne "s/[\t ]*PDS_\([A-Z0-9_]*\)[\t ]*=[\t ]*'\?\([0-9A-Z_]*\)'\?,\?/#define \1 \2/p" export/pds_parser_defs.h | tr "[A-Z]" "[a-z]"
 */


// Generic values
#define disabled 0
#define enabled  1
#define no       0
#define yes      1
#define off      0
#define on       1
. . .
// RF_ANTENNA_SEL_DIV_CONF.RF_PORTS
#define TX1_RX1   0
#define TX2_RX2   1
#define TX2_RX1   2
#define TX1_RX2   3
#define TX12_RX12 4
// DRF_ANTENNA_SEL_DIV_CONF.DIVERSITY
#define OFF      0
#define INTERNAL 1
#define EXTERNAL 2
. . .
#endif

```

* RF_ANTENNA_SEL`.pds.in` file

        #include "definitions.in"
        . . .

        RF_ANTENNA_SEL_DIV_CONF: {
            /*
             * Antenna selection:
             *   - TX1_RX1
             *   - TX2_RX2
             *   - TX1_RX2
             *   - TX2_RX1
             *   - TX1&2_RX1&2
             */
            RF_PORTS: TX1_RX1,

            /*
             * Diversity control mode:
             *   - OFF
             *   - INTERNAL
             *   - EXTERNAL
             * For the INTERNAL value, RF_PORTS must be set to TX1&2_RX1&2
             */
            DIVERSITY: OFF,
        },

## pds_compress output examples

(PDS output examples below are based on the preceding files)

### `pds` output format (default)
The `.pds` format is convenient to save time during execution, but is not human-friendly:
`pds_compress [--out=pds] RF_ANTENNA.pds.in RF_ANTENNA.pds`
```
{j:{a:0,b:0}}
```

### tinypds output format (human-readable)
The `-t` or `--out=tinypds` option allows an easier readout. It's useful to check the output
 of pds_compress: `pds_compress --out=tinypd RF_ANTENNA.pds.in RF_ANTENNA.tinypds`
(this format can only be used for checks, it can't be sent to the FW 'as is')

    {
        j: {
            a: 0,
            b: 0
        }
    }

### c output format (non-linux applications)
The `-c` or `--out=c` formats the PDS data as a PDS_COMPRESS_MSG structure. The resulting file is ready to be included
  from C code as part of a MCU application or a GeckoOS application:
   `pds_compress --out=c RF_ANTENNA.pds.in RF_ANTENNA.h`

    /* AUTOMATICALLY GENERATED -- DO NOT EDIT BY HAND */
    /*
     * Copyright 2018, Silicon Laboratories Inc.  All rights reserved.
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *     http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     *
     */

    /**
     * \file wf200_pds.h
     * \brief contains the PDS configuration specific to a hardware configuration.
     */

    #ifndef WF200_PDS_H
    #define WF200_PDS_H

    static const char* const wf200_pds[] = {
        "{j:{a:0,b:0}}",
    };

    #endif

