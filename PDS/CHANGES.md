Platform Data Set (PDS) API release note
====================================
# Version 4.1
## FW compatibility
* PDS API version 4.1 is required for FW 3.5.0

## New Features/Improvements
* Added external PA configuration section (only in template and definition files)
* TEST_IND type defined as unsigned word - min value set to 50 (only in template and definition files)

# Version 4.0
## FW compatibility
* PDS API version 4.0 is required for FW 3.2.0

## New Features/Improvements
* HIF_PINS_CFG / SDIO_* / SLEEP_CFG : by default no pulls are set
* HIF_PINS_CFG / SDIO_* / PULL_UP_DOWN : by default no pulls are set.
* FEM matrix configuration simplified
* FRONT_END_LOSS_CORRECTION_QDB renamed as FRONT_END_LOSS_TX_QDB (value in 1/4dB)
* RSSI_CORRECTION renamed as FRONT_END_LOSS_RX_QDB (value in 1/4dB)


# Version 3.0
## FW compatibility
* PDS API version 3.0 is required for FW 3.0.0

## New Features/Improvements
* Removed PTA_CFG section (PTA is now controlled via FW API)


# Version 2.4
## FW compatibility
* PDS API version 2.4 is required for FW 2.2.3

## New Features/Improvements
* PTA API updates (new fields). NB: PTA section commented/disabled in pds.in files


# Version 2.3
## FW compatibility
* PDS API version 2.3 is required for FW 2.2.2

## New Features/Improvements
* MAX_TX_POWER_CFG section renamed to RF_POWER_CFG
* RSSI_CORRECTION field is added in RF_POWER_CFG section to take into account the loss on the RF path in RSSI estimation.
* REG_MODE (Regulatory modes) enumerates have been renamed for better clarity (TEST_FEATURE_CFG section)

## Bug fixes
* correction of a mistake in Version 2.2 where all PTA_TX_CONF were renamed to PTA_TX_CFG. The new name is PTA_TX_CONF (as in the data sheet).


# Version 2.2
## FW compatibility
* PDS version 2.2 is required for FW 2.2.0 and 2.2.1

## New Features/Improvements
* General: Cosmetic changes on names: 1) _ELT, removed, 2) _CONF suffixes renames to _CFG 3) sections re-ordered
* FEM: 1) merged FEM_CTRL_PINS_MATRIX and FEM_TIMINGS sections into a new FEM_CFG section, 2) bits FEM_5 & FEM_6 swapped for better clarity
* PTA: enable configuration into 1-wire and 2-wire PTA modes
* typos fixed


# Version 2.1
## FW compatibility
* PDS version 2.1 is required for FW 2.1.0

## New Features/Improvements
* General: top-level braces removed to allow PDS includes
* programmable pins: 1) SLEEP_CFG: `tri` enumerate changed to `none`, 2) the mode for all pins is set to `tri`
* RF_ANTENNA_SEL_DIV_CONF: RF_PORTS `TX1&2_RX1&2` enumerate value is renamed to `TX12_RX12`
* REG_MODE added in TEST_FEATURE_CFG section to configure Tx power upon regulations.
* PTA: now disabled by default

# Version 2.0
## FW compatibility
* PDS version 2.0 is the initial delivery, to work with FW 2.0.0

