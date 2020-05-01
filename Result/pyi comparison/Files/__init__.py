import os, sys, time, logging

from random import choice
from functools import wraps

import pyric
import pyric.pyw as pyw

from pyric.lib import libnl as nl

from scapy.all import *
from scapy.contrib.wpa_eapol import WPA_key

MGMT_ASSOC_REQ    = (0, 0)
MGMT_ASSOC_RESP   = (0, 1)
MGMT_REASSOC_REQ  = (0, 2)
MGMT_REASSOC_RESP = (0, 3)
MGMT_PROBE_REQ    = (0, 4)
MGMT_PROBE_RESP   = (0, 5)
MGMT_BEACON       = (0, 8)
MGMT_ATIM         = (0, 9)
MGMT_DISASSOC     = (0, 10)
MGMT_AUTH         = (0, 11)
MGMT_DEAUTH       = (0, 12)

CTRL_POLL         = (1, 10)
CTRL_RTS          = (1, 11)
CTRL_CTS          = (1, 12)
CTRL_ACK          = (1, 13)
CTRL_CFEND        = (1, 14)
CTRL_CFECFA       = (1, 15)

DATA_ANY          = (2, (0,1,2,3,4,5,6,7,8,9,10,11))

BAD_MAC = [
    "ff:ff:ff:ff:ff:ff",
    "00:00:00:00:00:00",                    # Multicast
    "01:80:c2:00:00:00",                    # Multicast
    "01:00:5e",                             # Multicast
    "01:80:c2",                             # Multicast
    "33:33"                                 # Multicast
]

FIVEHERTZ = [
    36, 40, 44, 48, 52,
    56, 60, 64, 100, 104,
    108, 112, 116, 132, 136,
    140, 149, 153, 157, 161, 165
]

MACFILTER = "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"

def gchan(card):
    try:
        return pyw.chget(card)
    except pyric.error:
        return 0

def root():
    return True if os.geteuid() == 0 else False

class BoopSniff:

    def __init__(self, interface : str, hopper = None, target : str = None):

        if not root():
            raise OSError(f"User must be root to use this functionality")

        if interface not in [x for x in pyw.winterfaces() if pyw.modeget(x) == "monitor"]:
            raise ValueError(f"Invalid interface: {interface}")

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.ERROR,
            format='%(name)-12s:%(levelname)-8s | %(funcName)-12s:%(lineno)-4d | %(message)s')

        self.interface = pyw.getcard(interface)
        self.handler_map = {0:{}, 1:{}, 2:{}}

        self.filter = f"ether host {target}" if target else None
        self.hopper = hopper

        self.logger.info(f"App created on interface: {self.interface.dev}")

    def __str__(self):
        return f"BoopSniff({self.interface.dev})"

    def __repr__(self):
        return self.__str__()

    def handler(self, ptype):
        def __handle(f):
            self.handler_map[ptype[0]][ptype[1]] = f
            self.logger.info(f"Handler set for: {ptype[0]}:{ptype[1]}")
            return f
        return __handle

    def printer(self):
        def __printer(f):

            if not hasattr(self, 'pthread'):
                self.logger.info(f"Printer Thread Given")

                self.pthread = Thread(target=f, args=(self,))
                self.pthread.daemon = True
                self.pthread.start()
                return f

            return None
        return __printer

    # @timeit
    def pkt_router(self, pkt):
        try:
            return self.handler_map[pkt.type][pkt.subtype](self, pkt)
        # except:
            # return
        except KeyError:
            pass
        except Exception as e:
            print(type(e), e)
            sys.exit(0)

    def run(self, f=None, timeout=None):
        if self.hopper:
            self.pthread = Thread(target=self.hopper.run)
            self.pthread.daemon = True
            self.pthread.start()

        sniff(
            iface=self.interface.dev, filter=self.filter,
            prn=f or self.pkt_router, timeout=timeout, store=0)

    def channel(self):
        return gchan(self.interface)


class Hopper:

    def __init__(
        self,
        interface : str,
        frequencies : list = [2],
        channels : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] + FIVEHERTZ
    ):

        if not root():
            raise OSError(f"User must be root to use this functionality")

        if interface not in [x for x in pyw.winterfaces() if pyw.modeget(x) == "monitor"]:
            raise ValueError(f"Invalid interface: {interface}")

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.ERROR,
            format='%(name)-12s:%(levelname)-8s | %(funcName)-12s:%(lineno)-4d | %(message)s')

        self.interface = pyw.getcard(interface)
        self.channels  = []

        if 2 in frequencies:
            [self.channels.append(x) for x in channels if x in range(12)]

        if 5 in frequencies:
            [self.channels.append(x) for x in channels if x in FIVEHERTZ]

    def __str__(self):
        return f"Hopper({self.channels})"

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        self.run()

    def channel(self, chan=None):
        if chan:
            try:
                pyw.chset(self.interface, chan, self.nlsock)
            except:
                self.logger.warn(f"Failed to change channel: {self.interface.dev}: {chan}")
                return False
            return True
        return gchan(self.interface)

    def run(self):
        while True:
            channel = choice(self.channels)

            try:
                pyw.chset(self.interface, channel, None)

            except:
                self.logger.warn(f"Failed to change channel: {self.interface.dev}: {channel}")

            time.sleep(5)
