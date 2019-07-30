WFx Firmware release note
=========================

# Release 3.0.0
(release date 2019-07-26)

## New Features/Improvements
* General: API change on secure link and PTA (hence the major revision)
* [1317] - [API] PTA is now configured through an API (instead of PDS)
* [1250] - [API-SLK] API changes for Secure Link: key renegotiation, session key algorithm selection and session key protection disabling
* [1323] - [PHY] Updates TX shaping filters for channel 14
* [1337] - [UMAC] softAP allowed only 3 clients to connect at a time in WPA
* [1309] - [UMAC] Enable TX aggregation
* [1081] - [UMAC] Enable STA power save in combo mode
* [1162] - [UMAC-SLK] Implement Secure Link key renegotiation on UMAC

## Bug fixes
* [1265] - [TESTFEAT] Wrong backoffs set with a blank OTP (WFM200 only)
* [1338] - [TESTFEAT] CW test feature stopped transmission after temperature compensation

## Known issues
* [1344] - [PTA] Dynamic control of PTA settings does not work as expected


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

## Known issues
* [1265] - [TESTFEAT] Test feature issue on WFM200 with blank OTP
* [1337] - [UMAC] softAP allows only 3 clients to connect at a time in WPA


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
* [1337] - [UMAC] softAP allows only 3 clients to connect at a time in WPA
* [1265] - [TESTFEAT] Test feature issue on WFM200 with blank OTP
* [1338] - [TESTFEAT] CW test feature lost configuration after a temperature compensation


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
* [1337] - [UMAC] softAP allows only 3 clients to connect at a time in WPA
* [1338] - [TESTFEAT] CW test feature lost configuration after a temperature compensation

# Release 2.0.0
(release date 2019-01-09)
* Initial release
