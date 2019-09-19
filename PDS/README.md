# PDS (Platform Data Set) 'definition' files

**P**latform **D**ata **S**et (**PDS**) files contain configuration
 values sent by the WFX driver to the WFX firmware.

## Definitions files
The firmware-version related **definitions** files define FW-usable 
values for all human-readable `PDS section` and `PDS parameter` names,
pretty much the same way a C header file is used.

The **definitions** files are referenced with a '#include' by the
 `.pds.in` files and pre-processed by the `pds_compress` script
 (pretty much as a C pre-compiler would work) to obtain
  a more compact file and reduce the amount of data to send to the FW.

**definitions** files evolve following the `PDS API` version,
whenever new PDS fields or sections are added or removed.

See the [PDS API Release Note][1] for details on PDS API

See the [wfx-pds README][2] for details on PDS files

* definitions`.in` file (abstract)
```
/*
 * These definitions come from firmware 3.0.0 headers
 */
#ifndef DEFINITIONS_3_0_0_IN
#define DEFINITIONS_3_0_0_IN

/*
 * Nodes declarations
 */
#define HEADER              a
#define     VERSION_MAJOR           a
#define     VERSION_MINOR           b

#define PROG_PINS_CFG       b
#define     GPIO_FEM_1              a
#define     GPIO_FEM_2              b
#define     GPIO_FEM_3              c
#define     GPIO_FEM_4              d
#define     GPIO_FEM_5              e
#define     GPIO_FEM_6              f
#define     GPIO_PDET               g
#define     GPIO_PTA_TX_CONF        h
#define     GPIO_PTA_RF_ACT         i
#define     GPIO_PTA_STATUS         j
#define     GPIO_PTA_FREQ           k
#define     GPIO_WUP                l
#define     GPIO_WIRQ               m
#define     RESERVE2                n
#define         SLEW_RATE               a
#define         PULL_UP_DOWN            b
#define         SLEEP_CFG               c
#define         PIN_MODE                d
#define         GPIO_ID                 e

#define HIF_PINS_CFG        c
. . .

#define FEM_CFG                 f
. . .
#define RF_POWER_CFG       h
. . .
#define RF_ANTENNA_SEL_DIV_CFG j
. . .
/*
 * Attribute values
 */

// Generic values
#define disabled 0
#define enabled  1
#define no       0
#define yes      1
#define off      0
#define on       1
// PROG_PINS_CFG.*.PULL_UP_DOWN
// PROG_PINS_CFG.*.SLEEP_CFG
#define none  0
#define down  1
#define up    3
#define maintain   4
// PROG_PINS_CFG.*.MODE
#define tri      0
#define func     1
#define gpio     2
// RF_POWER_CFG.RF_PORT
#define RF_PORT_BOTH 0
#define RF_PORT_1  1
#define RF_PORT_2  2
. . .
#endif

```

[1]: https://github.com/SiliconLabs/wfx-firmware/blob/master/PDS/CHANGES.md
[2]: https://github.com/SiliconLabs/wfx-pds/blob/master/README.md
