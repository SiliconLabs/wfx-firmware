WFx Firmware release note
=========================

# Release 2.3.0
(release date 2019-06-24)

## New Features/Improvements
* [1166] - [PHY] Improve the TX power accuracy at low voltage
* [1195] - [API] Add a new indication message when the firmware is ready after a wake-up
* [168] - [UMAC] implement an API to retrieve RSSI value of a connected station when in access point mode

## Bug fixes
* [1188] - [PHY] Improve the robustness when RTS/CTS is used
* [1230] - [PHY] Assert when the Rx RF test feature is launched twice
* [1254] - [UMAC] Security mode information reported in scan result indication is incorrect

# Release 2.2.2
(release date 2019-05-10)

## New Features/Improvements
* [919] - [PHY] RSSI compensation across temperature
* [1057] - [LMAC] Allow beacon interval to be updated
* [1034] - [UMAC] Speed up connection attempts
* [1116] - [UMAC] Enable short GI

## Bug fixes
* [1112] - [UMAC] WF200 stayed awaken after a successful roam

## Known issues
* [1230] - [PHY] Assert when the Rx RF test feature is launched twice
* [1254] - [UMAC] Security mode information reported in scan result indication is incorrect

# Release 2.2.1
(release date 2019-03-06)

## New Features/Improvements
* [883] - [PHY] Major improvement of the power consumption during the boot procedure
* [904] - [API] Use of 'FrameType' in HIF Control register to know the type of the frame available in the WF200
* [695] - [UMAC] Add API to change the scan parameters
* [961] - [UMAC] Support for TX power control
* [962] - [UMAC] Support for packet filtering based on client MAC address (whitelist / blacklist)
* [975] - [UMAC] Add AP bridging support
* [1028] - [UMAC] Add security mode parameter in scan result indication
* [1033] - [UMAC] Support for reading current PMK

## Bug fixes
* [1065] - [OTP] Support of new OTP table in WFM200
* [942]  - [UMAC] The connection request is stuck if the SoftAp is started first
* [1044] - [UMAC] The WF200 SoftAp disconnects stations when configured to use mixed security mode

## Known issues
* [1230] - [PHY] Assert when the Rx RF test feature is launched twice
* [1254] - [UMAC] Security mode information reported in scan result indication is incorrect

# Release 2.0.0
(release date 2019-01-09)
* Initial release
