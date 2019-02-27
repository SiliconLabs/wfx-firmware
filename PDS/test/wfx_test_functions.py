"""wfx_test_functions.py

These functions adapt the test API to the underlying FW API
For this reason, they are closely related to the FW version
Keeping these tied to the FW maintain a usable set of test functions
 despite possible API changes (such as attribute renaming)
"""
#!/usr/bin/python3

from wfx_test_core import *
from distutils.version import StrictVersion
from time import sleep


def channel(ch=None):
    if ch is None:
        return "TEST_CHANNEL" + " " + set_pds_param("TEST_CHANNEL")
    else:
        if ch >= 14:
            set_pds_param("TEST_CHANNEL", 14)
        else:
            set_pds_param("TEST_CHANNEL", ch)
    apply_pds()


def tx_power(dbm=None):
    if dbm is None:
        power = int(set_pds_param("MAX_OUTPUT_POWER_QDBM"))
        return "MAX_OUTPUT_POWER_QDBM" + " " + str(power) + \
            "tx_power " + str(int(power/4)) + " dBm"
    else:
        set_pds_param("MAX_OUTPUT_POWER_QDBM", int(4*dbm))
    apply_pds()


def tx_backoff(mode_802_11=None, backoff_level=0):
    if backoff_level == "":
        backoff_level = 0
    if mode_802_11 == "RSVD":
        return
    if mode_802_11 is None:
        backoff_val= set_pds_param("BACKOFF_VAL")
        (backoff_data, nb) = re.subn('\[|\]| ','',backoff_val)
        backoff_max = max(backoff_data.split(','))
        backoff_dbm = str(int(int(backoff_max)/4))
        return "BACKOFF_VAL " + backoff_max + "  tx_backoff " + \
        backoff_dbm + " dB"
    else:
        if "DSSS" in mode_802_11:
            index = 0
        elif "6Mbps" in mode_802_11 or "MCS0" in mode_802_11:
            index = 1
        elif "9Mbps" in mode_802_11:
            index = 1
        elif "12Mbps" in mode_802_11 or "MCS1" in mode_802_11:
            index = 1
        elif "18Mbps" in mode_802_11 or "MCS2" in mode_802_11:
            index = 2
        elif "24Mbps" in mode_802_11 or "MCS3" in mode_802_11:
            index = 2
        elif "36Mbps" in mode_802_11 or "MCS4" in mode_802_11:
            index = 3
        elif "48Mbps" in mode_802_11 or "MCS5" in mode_802_11:
            index = 3
        elif "54Mbps" in mode_802_11 or "MCS6" in mode_802_11:
            index = 4
        elif "MCS7" in mode_802_11:
            index = 5
        else:
            return "Unknown 802.11 mode"    
        value = [0, 0, 0, 0, 0, 0]
        value[index] = int(4 * backoff_level)
        set_pds_param("BACKOFF_VAL", str(value))
    apply_pds() 


def tx_rx_select(tx_ant=None, rx_ant=None):
    if tx_ant is None:
        return "RF_PORTS" + " " + set_pds_param("RF_PORTS")
    else:
        set_pds_param("RF_PORTS", "TX" + str(tx_ant) + \
                                 "_RX" + str(rx_ant))
    apply_pds() 


def tx_stop():
    set_pds_param("NB_FRAME", 100)
    apply_pds() 


def tx_framing(packet_length_bytes=None, delay_between_us=100):
    if packet_length_bytes is None:
        return "FRAME_SIZE_BYTE " + set_pds_param("FRAME_SIZE_BYTE") + \
             "  " + "IFS_US " + set_pds_param("IFS_US")
    else:
        set_pds_param("FRAME_SIZE_BYTE", packet_length_bytes)
        set_pds_param("IFS_US", delay_between_us)


def tx_mode(mode_802_11=None):
    if mode_802_11 is None:
        return "HT_PARAM " + set_pds_param("HT_PARAM") + "  " + \
               "RATE " + set_pds_param("RATE")
    else:
        res = re.findall("([^_]*)_(.*)", mode_802_11)
        prefix = res[0][0]
        suffix = res[0][1]
        ht_param = "MM"
        if "GF_" in mode_802_11:
            rate = "N_" + suffix
            ht_param = "GF"
        elif "MM_" in mode_802_11:
            rate = "N_" + suffix
        elif "LEG_" in mode_802_11:
            rate = "G_" + suffix
        elif "DSSS_" in mode_802_11:
            rate = "B_" + suffix + "Mbps"
        elif "CCK_" in mode_802_11:
            rate = "B_" + suffix + "Mbps"
        else:
            return "Unknown 802.11 mode"
        set_pds_param("HT_PARAM", ht_param)
        set_pds_param("RATE", rate)


def tx_start(nb_frames=None):
    if nb_frames is None:
        return "TEST_MODE " + set_pds_param("TEST_MODE") + "  " + \
               "NB_FRAME "  + set_pds_param("NB_FRAME")
    else:
        set_pds_param("TEST_MODE", "tx_packet")
        if str(nb_frames) is "continuous":
            set_pds_param("NB_FRAME", "0")
        else:
            set_pds_param("NB_FRAME", nb_frames)
    apply_pds()


def tone(cmd=None, freq=0):
    # CW Mode: generate CW @ (freq+1)*312.5Khz
    if cmd is None:
        return set_pds_param("TEST_MODE")
    else:
        if cmd == "start":
            set_pds_param("CW_MODE", "single")
            set_pds_param("TEST_MODE", "tx_cw")
            set_pds_param("FREQ1", freq)
        elif cmd == "stop":
            set_pds_param("TEST_MODE", "tx_packet")
            set_pds_param("NB_FRAME", 100)
    apply_pds()


def tone_power(dbm=None):
    if dbm is None:
        power = int(set_pds_param("MAX_OUTPUT_POWER"))
        return "MAX_OUTPUT_POWER " + str(power) + "  " + \
                "  tone_power " + str(int(power/4)) + " dBm"
    else:
        set_pds_param("MAX_OUTPUT_POWER", int(4*dbm))
    apply_pds() 
