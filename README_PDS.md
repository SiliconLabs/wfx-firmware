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

  * Example `.pds` file, resulting from `pds_compress example.pds.in example.pds`
   (using example files listed below)
```
{a:{a:1,b:3},b:{a:{a:4,b:0,c:0,d:0,e:A},b:{a:4,b:0,c:0,d:0,e:B},c:{a:4,b:0,c:0,d:0,e:C}}}
```

### Startup PDS file
During WFX driver startup, after WFX firmware download, the driver 
sends the `.pds` file to the WFX firmware, 
in order to configure the WFX hardware to match the application.

* Startup PDS file name and location

Linux LMAC driver | MCU FMAC WFX driver
---|---
/lib/firmware/wf200.pds|[TBC] wf200.pds
can use symbolic links|[TBC]


_PDS `.pds.in` and **definitions** files can easily be edited with any text editor and benefit from code coloring and
 folding if the editor treats them as C files, for instance._
  
_Resulting `.pds` files can be displayed for checking but
  should not be edited. It is recommended to always start from human-readable files such as `.pds.in` files_

### Sending a PDS file during execution
It is possible to send additional PDS content during execution. 
This is typically useful when using the TEST_FEATURE to perform continuous Tx testing.

To support this, the write-only `/sys/kernel/debug/ieee80211/phy*/wfx/send_pds` file has been added to the filesystem.
_Upon writing to this file, the data is sent to the FW by the driver as PDS data._

Linux | MCU (TBD)
---|---
Send an already existing .pds file: `cat <file>.pds /sys/kernel/debug/ieee80211/phy*/wfx/send_pds`|
Compress and send a .pds.in file:`pds_compress <file>.pds.in /sys/kernel/debug/ieee80211/phy*/wfx/send_pds`|

## PDS files details

A firmware-version related **definitions** file is referenced with a '#include' by the `.pds.in` file and pre-processed 
by pds_compress (pretty much as a C pre-compiler would work) to obtain a more compact file.

### PDS input files examples

#### `example.pds.in` file

The `.pds.in` file starts with a '#include' directive to select the definitions file. It
contains the documentation and settings related to each PDS **node** 
or **attribute** value, using either decimal values or values
 from the definitions file.

```
#include "definitions-1.2.14.in"

    /**********************/
    /* Pins configuration */
    /**********************/

    // Information about this PDS version
    HEADER_ELT: {
        VERSION_MAJOR: 1,
        VERSION_MINOR: 3,
    },

    // Pad configuration of programmable pins
    PROG_PINS_CFG_ELT: {
        // For each PROGrammable PIN in this section
        // SLEW_RATE sets the maximum slew rate on the pin. Type: integer value between 0 and 6 (6=max drive strength)
        // PULL_UP_DOWN allows to add a pull-up or pull-down on the pad. Type: enum = 'none', 'down', 'up'
        // SLEEP_CFG allows to add a pull-up or pull-down on the pad while in sleep mode. Type: enum = 'tri', 'down', 'up', 'maintain'
        //          for the case of pads used as gpio it is also possible to maintain the current driven gpio value
        // PIN_MODE allows to configure the pin in tristate, functionnal mode or gpio. Type: enum = 'tri', 'func', 'gpio'
        // GPIO_ID allows to assign a GPIO_ID to a given pin when configured as gpio. Type = char must be an UPPER case letter
        GPIO_FEM_1: {
            SLEW_RATE: 4,
            PULL_UP_DOWN: none,
            SLEEP_CFG: tri,
            PIN_MODE: tri,
            GPIO_ID: A,
        },
        GPIO_FEM_2: {
            SLEW_RATE: 4,
            PULL_UP_DOWN: none,
            SLEEP_CFG: tri,
            PIN_MODE: tri,
            GPIO_ID: B
        },
        GPIO_FEM_3: {
            SLEW_RATE: 4,
            PULL_UP_DOWN: none,
            SLEEP_CFG: tri,
            PIN_MODE: tri,
            GPIO_ID: C
        },

```

#### `definitions-x.y.z.in` file

This file contains the definitions (as _letters_) corresponding to each known **PDS node**, 
as well as definitions (as _numbers_) for each **attribute value**. It corresponds to a specific FW version. Higher firmware versions should remain compatible with a given definitions file.

```
/*
 * Nodes declarations
 */
#define HEADER_ELT              a
#define     VERSION_MAJOR           a
#define     VERSION_MINOR           b
#define PROG_PINS_CFG_ELT       b
#define     GPIO_FEM_1              a
#define     GPIO_FEM_2              b
#define     GPIO_FEM_3              c
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
// PROG_PINS_CFG_ELT.*.PULL_UP_DOWN
#define none  0
#define down  1
#define up    3
#define maintain   4
// PROG_PINS_CFG_ELT.*.MODE
#define tri      0
#define func     1
#define gpio     2

```
 
#### `TEST_FEATURE.pds.in` minimal file for continuous Tx testing

```
#include "definitions-1.2.14.in"

    /*************************/
    /* Tests and debug modes */
    /*************************/
    TEST_FEATURE_CFG_ELT: {
        // Wi-Fi channel to use. Accepted range is from 1 to 14.
        TEST_CHANNEL: 11,
        // TEST_MODE selects the activated test feature: enum = 'rx', 'tx_packet', 'tx_cw'
        TEST_MODE: tx_cw,
        // TEST_IND period in ms at which an indication message is sent.
        //       In the case of rx test, it returns the measurement results (PER)
        TEST_IND: 1000,

        // CFG_TX_CW: additional configuration for tx_cw mode
        CFG_TX_CW: {
            // CW_MODE CW mode: enum 'single' or 'dual'
            CW_MODE: single,
            // FREQ1 frequency offset -31 to 31 (in 312.5kHz)
            FREQ1: 1,
            // FREQ2 frequency offset -31 to 31 (in 312.5kHz)
            FREQ2: 2,
            // MAX_OUTPUT_POWER indicates the max Tx power value in quarters of dBm
            MAX_OUTPUT_POWER: 68
        },
    },
```

## pds_compress details

Use `pds_compress [options] INPUT [OUTPUT]` to compress a `.pds.in` file to a `.pds` file,
 ready to be sent to the WFX firmware.

The `.pds` format is convenient to save time during execution, but is not human-friendly.

The `-t` or `--tinypds` option allows an easier readout. It's useful to check the output
 of pds_compress:
  * Example output abstract, resulting from `pds_compress example.pds.in --tynipds`

```
{
    a: {
        a: 1,
        b: 3
    },
    b: {
        a: {
            a: 4,
            b: 0,
            c: 0,
            d: 0,
            e: A
        },
    }
}

``` 

NB: Use `pds_compress --help' to get more information about possible pds_compress options.

## Advanced PDS files management

### `.pds.in` file inclusion
It is possible to `#include` a `.pds.in` file from another `.pds.in` file.

For example, if the goal is to directly start using the TEST_FEATURE as soon as the driver is loaded, use (for Linux):
 
```
pds_compress TEST_FEATURE.pds.in direct_tx_cw_channel_11_68dBm.pds
sudo ln -sfn direct_tx_cw_channel_11_68dBm.pds /lib/firmware/wf200.pds
sudo wfx_driver_reload
```

based on the following file:

#### `TEST_FEATURE.pds.in` file for continuous Tx testing at startup

```
#include "example.pds.in"

    /*************************/
    /* Tests and debug modes */
    /*************************/
    TEST_FEATURE_CFG_ELT: {
        // Wi-Fi channel to use. Accepted range is from 1 to 14.
        TEST_CHANNEL: 11,
        // TEST_MODE selects the activated test feature: enum = 'rx', 'tx_packet', 'tx_cw'
        TEST_MODE: tx_cw,
        // TEST_IND period in ms at which an indication message is sent.
        //       In the case of rx test, it returns the measurement results (PER)
        TEST_IND: 1000,

        // CFG_TX_CW: additional configuration for tx_cw mode
        CFG_TX_CW: {
            // CW_MODE CW mode: enum 'single' or 'dual'
            CW_MODE: single,
            // FREQ1 frequency offset -31 to 31 (in 312.5kHz)
            FREQ1: 1,
            // FREQ2 frequency offset -31 to 31 (in 312.5kHz)
            FREQ2: 2,
            // MAX_OUTPUT_POWER indicates the max Tx power value in quarters of dBm
            MAX_OUTPUT_POWER: 68
        },
    },
    
```

Note that the only difference is in the `#include` line, where '#including' the original file
allows using the resulting `.pds` file at startup. 

### Using `#define` in `.pds.in` files
It is possible to 

* Replace an attribute value by a TEXT_NAME in a `.pds.in` low-level file
* `#define` the TEXT_NAME in the top-level `.pds.in` file
* `#include` the low-level `.pds.in` file from the top-level `.pds.in` file

#### Example `TEST_FEATURE_CHANNEL_UNDER_TEST.pds.in`

```
#include "example.pds.in"

    /*************************/
    /* Tests and debug modes */
    /*************************/
    TEST_FEATURE_CFG_ELT: {
        /* Wi-Fi channel to use. Accepted range is from 1 to 14. */
        TEST_CHANNEL: CHANNEL_UNDER_TEST,
        /* TEST_MODE selects the activated test feature: enum = 'rx', 'tx_packet', 'tx_cw'
        TEST_MODE: tx_cw,
           TEST_IND period in ms at which an indication message is sent.
               In the case of rx test, it returns the measurement results (PER)
        TEST_IND: 1000,

           CFG_TX_CW: additional configuration for tx_cw mode
        */
        CFG_TX_CW: {
            /* CW_MODE CW mode: enum 'single' or 'dual' */
            CW_MODE: single,
            /* FREQ1 frequency offset -31 to 31 (in 312.5kHz) */
            FREQ1: 1,
            /* FREQ2 frequency offset -31 to 31 (in 312.5kHz) */
            FREQ2: 2,
            /* MAX_OUTPUT_POWER indicates the max Tx power value in quarters of dBm
            MAX_OUTPUT_POWER: 68 */
        },
    },
    
```
#### Example `TEST_CHANNEL.pds.in`
     

```
#define CHANNEL_UNDER_TEST 11
#include "TEST_FEATURE_CHANNEL_UNDER_TEST.pds.in"
```
This would make it easy to sweep between channels in a test environment, 
while keeping all other parameters identical

#### Example execution (under Linux)

```
pds_compress TEST_CHANNEL.pds.in /sys/kernel/debug/ieee80211/phy*/wfx/send_pds
```

It would then be easy to change the CHANNEL_UNDER_TEST value in a script and create a test loop.
