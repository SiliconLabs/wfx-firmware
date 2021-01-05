WFx Firmware Release Note
=========================

# Release 3.12.0
(release date 2021-01-04)

## New Features/Improvements
* [1486] - [LMAC] Limit aggregation packet retries according to the negotiated capacity
* [1697] - [UMAC] Increase the default packet retry attempt number
* [1700] - [LMAC] Optimize Fast-PS behavior when receiving multicast packets
* [1702] - [UMAC] Add an API to disable U-APSD power save mode
* [1703] - [UMAC] Add a power save error indication to notify the host of a mode changed

## Bug fixes
* [1701] - [LMAC] Fix keep-alive mechanism to allow de-authentication packet reception
* [1707] - [LMAC] Fix reordering buffer mechanism used in aggregation

# Release 3.11.1
(release date 2020-11-10)

## New Features/Improvements
* [1676] - [LMAC] Shorten aggregation maximum duration
* [1678] - [UMAC] Improve rate adaptation while using aggregation
* [1679] - [PTA] Fix background scan timeout while PTA is enabled

## Bug fixes
* [1689] - [UMAC] Fix WPA3 offloading feature

# Release 3.11.0
(release date 2020-10-07)

## New Features/Improvements
* [1669] - [LMAC] Update the API to allow CCMP/TKIP replay protection from the host
* [1474] - [LMAC] Implement CCMP/TKIP replay protection when using aggregation

## Bug fixes
* [1668] - [LMAC] Improve antenna diversity

# Release 3.10.0
(release date 2020-09-07)

## New Features/Improvements
* [1664] - [UMAC] Open the APIs required to allow the host to perform a WPA3 connection

## Bug fixes
* [1614] - [UMAC] Fix a firmware crash when the temperature reaches the WF200 operational limit
* [1663] - [LMAC] Improve the Management Frame Protection associated with the Block Ack mechanism in softAP mode

# Release 3.9.1
(release date 2020-08-19)

## Bug fixes
* [1666] - [API] Update the API version advertised in the startup indication

# Release 3.9.0
(release date 2020-08-04)

## New Features/Improvements
* [1599] - [LMAC] Abort pending frames when station go to sleep
* [1654] - [SLK] Sync the driver bitmap and firmware bitmap

## Bug fixes
* [1647] - [UMAC] Fix throughput issues in softAP TCP uplink traffic
* [1474] - [LMAC] Replayed TKIP/AES fragments are no longer accepted
* [1648] - [LMAC] Fix wrong starting sequence number when Ack and BlockAck interleave
* [1655] - [LMAC] Fix wrong probe response to probe request with hidden SSID
* [1658] - [LMAC] Fix a connection interoperability issue (AP Cisco WAP150)

## Known issues
* [1666] - [HIF] Wrong API version advertised in the startup indication

# Release 3.8.0
(release date 2020-07-09)

## New Features/Improvements
* [1652] - [SEC] Increment anti-rollback level
* [1598] - [LMAC] Improve scheduling when station uses fast-PS in combo AP/STA mode

## Bug fixes
* [1640] - [LMAC] Fix an issue with antenna diversity when using a dummy load

# Release 3.7.0
(release date 2020-06-10)

## New Features/Improvements
* [1601] - [LMAC] Include selected antenna information in RX_IND packets

## Bug fixes
* [1632] - [UMAC] Fix interoperability issue when using WPA2 security method (Orinoco AP-700)
* [1634] - [UMAC] Fix interoperability issue linked to the WMM-PS service period limitation (Netgear R8000)

# Release 3.6.1
(release date 2020-05-20)

## New Features/Improvements
* [1622] - [API] Add HIF message traces to error log

## Bug fixes
* [1615] - [UMAC] Fix a firmware exception when releasing a Tx buffer in softAP in specific conditions
* [1629] - [LMAC] Return an error when a wrong AC is set in a EDCA_QUEUE_PARAMS_REQ

# Release 3.6.0
(release date 2020-05-06)

## New Features/Improvements
* [1608] - [API] Further improve errors and exceptions reporting
* [1602] - [PTA] Update default PTA priority level

## Bug fixes
* [1572] - [UMAC] Fix a firmware exception triggered in specific conditions when stopping the softAP interface
* [1611] - [PDS] Fix FEM timings issue

# Release 3.5.0
(release date 2020-04-10)

## New Features/Improvements
* [1551] - [API] Improve errors and exceptions reporting
* [1563] - [API] Deprecate IBSS support
* [1554] - [SEC] Increment anti-rollback level to enforce Secure Link security update
* [1326] - [PHY] Improve channel 14 support
* [1536] - [PTA] Improve PTA behavior when handling long Coex requests
* [1555] - [PTA] Improve power consumption when PTA is enable
* [1426] - [LMAC] Improve scan by allowing the use of antenna diversity
* [1482] - [LMAC] Add a detection and correction for desynced beacons when in power save mode
* [1556] - [LMAC] Add an indication when PS-Poll power save mode is not working properly
* [1488] - [UMAC] Automatically switch to Fast-PS power save mode when PS-Poll is not working properly

## Bug fixes
* [1456] - [API] Fix WFM200 high temperature safety protection in RF test mode
* [1552] - [LMAC] Fix a firmware exception related to an unexpected message sequence after a PS-Poll

# Release 3.4.1
(release date 2020-03-06)

## New Features/Improvements
* [1409] - [LMAC] Include a mode adding CSI information to the receive frames
* [1435] - [LMAC] Add a fast beacon processing mode
* [1535] - [LMAC] Improve U-APSD mode behavior to improve power consumption
* [1446] - [UMAC] Add an API to select the CCA mode

## Bug fixes
* [1392] - [HIF] Communication issues in low-speed SDIO are fixed (around 400 KHz)

# Release 3.3.2
(release date 2019-12-20)

## New Features/Improvements
* [1484] - [LMAC] Enable CTS-to-self for A-MPDU when asked by the AP

## Bug fixes
* [1211] - [LMAC] Fix TCP throughput when competing with another device

## Known issues
* [1392] - [HIF] Communication issues in message mode using SDIO at low speed (around 400 KHz)

# Release 3.3.1
(release date 2019-12-06)

## New Features/Improvements
* [1451] - [UMAC] Improve station interface throughput in combo mode on different channels

## Bug fixes
* [1466] - [UMAC] Connection to a hidden AP is fixed

## Known issues
* [1392] - [HIF] Communication issues in message mode using SDIO at low speed (around 400 KHz)

# Release 3.3.0
(release date 2019-11-08)

## New Features/Improvements
* [1378] - [PTA] Improve PTA general behavior and stability
* [1077] - [LMAC] Estimate and compensate beacon reception deviation to improve power consumption
* [1043] - [UMAC] support channel 14
* [1383] - [UMAC] Improve behavior in combo mode when both interfaces are on the same channel
* [1396] - [UMAC] Add WPA3 and PMF information to the security mode bitmask in scan result indication
* [1402] - [UMAC] Add support for directed unicast scan

## Bug fixes
* [1395] - [PHY] Improve absolute CCA mode stability
* [1344] - [PTA] Fix dynamic control of PTA settings
* [1376] - [HIF] Fix communication issues using SPI low speed (around 1 MHz)
* [1404] - [TESTFEAT] Fix failing CW when in power save mode
* [1388] - [TESTFEAT] Fix RX RF test not working after a TX RF test
* [1410] - [UMAC] Fix failing WPA2 connection in combo mode on specific access points

## Known issues
* [1392] - [HIF] Communication issues in message mode using SDIO at low speed (around 400 KHz)
* [1466] - [UMAC] Connecting to a hidden AP is not working if not using fast connect

# Release 3.1.1
(release date 2019-10-14)

## Bug fixes
* [1399] - [PHY] Fix assertion on simultaneous received events

## Known issues
* [1344] - [PTA] Dynamic control of PTA settings does not work as expected
* [1376] - [HIF] Communication corruptions using SPI at low speed (around 1 MHz)
* [1388] - [TESTFEAT] an RX RF test does not work after a TX RF test
* [1466] - [UMAC] Connecting to a hidden AP is not working if not using fast connect

# Release 3.1.0
**WARNING: Use not recommended due to bug [1399]**

(release date 2019-09-13)

## New Features/Improvements
* [1154] - [SLK] Lighter alternative Secure Link Session Key Establishment protocol
* [1379] - [LMAC] Improve TX process to follow rate policy management
* [1271] - [LMAC] Limit the size of aggregated frames based on duration (max 10ms)
* [329] - [UMAC] Add more specific connection failure status codes

## Bug fixes
* [1366] - [PHY] Fix absolute CCA behavior
* [1358] - [TESTFEAT] Reduce temperature compensation gaps in CW tests
* [1361] - [TESTFEAT] Fix TX Packet transmission stops after temperature calibration
* [565] - [LMAC] Wrong RTS threshold check in aggregation
* [1381] - [UMAC] Fix 32-byte long SSIDs triggering invalid parameter status
* [1068] - [UMAC] Incorrect event on AP connection failure

## Known issues
* [1399] - [PHY] Assert causing instabilities in softAP and station mode
* [1344] - [PTA] Dynamic control of PTA settings does not work as expected
* [1376] - [HIF] Communication corruptions using SPI at low speed (< 1.5 MHz)
* [1388] - [TESTFEAT] an RX RF test does not work after a TX RF test
* [1466] - [UMAC] Connecting to a hidden AP is not working if not using fast connect

# Release 3.0.0
(release date 2019-07-26)

## New Features/Improvements
* General: API change on secure link and PTA (hence the major revision)
* [1317] - [API] PTA is now configured through an API (instead of PDS)
* [1250] - [API-SLK] API changes for Secure Link: key renegotiation, session key algorithm selection and session key protection disabling
* [1323] - [PHY] Updates TX shaping filters for channel 14
* [1337] - [UMAC] SoftAP allowed only 3 clients to connect at a time in WPA
* [1309] - [UMAC] Enable TX aggregation
* [1081] - [UMAC] Enable STA power save in combo mode
* [1162] - [UMAC-SLK] Implement Secure Link key renegotiation on UMAC

## Bug fixes
* [1265] - [TESTFEAT] Wrong backoffs set with a blank OTP (WFM200 only)
* [1338] - [TESTFEAT] CW test feature stopped transmission after temperature compensation

## Known issues
* [1344] - [PTA] Dynamic control of PTA settings does not work as expected
* [1388] - [TESTFEAT] An RX RF test does not work after a TX RF test
* [1466] - [UMAC] Connecting to a hidden AP is not working if not using fast connect

# Release 2.3.0
(release date 2019-06-24)

## New Features/Improvements
* [1166] - [PHY] Improve the TX power accuracy at low voltage
* [1195] - [API] Add a new indication message when the firmware is ready after a wake-up
* [168] - [UMAC] Implement an API to retrieve RSSI value of a connected station when in softAP mode

## Bug fixes
* [1188] - [PHY] Improve the robustness when RTS/CTS is used
* [1230] - [PHY] Assert when the RX RF test feature is launched twice
* [1254] - [UMAC] Security mode information reported in scan result indication is incorrect

## Known issues
* [1265] - [TESTFEAT] Test feature issue on WFM200 with blank OTP
* [1337] - [UMAC] SoftAP allows only 3 clients to connect at a time in WPA

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
* [1337] - [UMAC] SoftAP allows only 3 clients to connect at a time in WPA
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
* [942]  - [UMAC] The connection request is stuck if the softAP is started first
* [1044] - [UMAC] The WF200 softAP disconnects stations when configured to use mixed security mode

## Known issues
* [1230] - [PHY] Assert when the RX RF test feature is launched twice
* [1254] - [UMAC] Security mode information reported in scan result indication is incorrect
* [1337] - [UMAC] SoftAP allows only 3 clients to connect at a time in WPA
* [1338] - [TESTFEAT] CW test feature lost configuration after a temperature compensation

# Release 2.0.0
(release date 2019-01-09)
* Initial release
