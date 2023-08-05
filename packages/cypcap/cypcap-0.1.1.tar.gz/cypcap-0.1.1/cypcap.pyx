# cython: language_level=3str, binding=True
"""
This module is a Cython based binding for modern libpcap.
"""

import os
import socket  # To make sure WinSock2 is initialized
import enum
import warnings
from typing import Optional, Union, List, Callable

cimport cython
from libc cimport stdio
from cpython cimport PyObject, PyErr_SetFromErrno

cimport cpcap
cimport csocket


__version__ = u"0.1.1"


include "npcap.pxi"


# TODO This is a really big enumeration, add more values as requested
class DatalinkType(enum.IntEnum):
    """Datalink types."""
    NULL_ = cpcap.DLT_NULL
    EN10MB = cpcap.DLT_EN10MB
    EN3MB = cpcap.DLT_EN3MB
    AX25 = cpcap.DLT_AX25
    PRONET = cpcap.DLT_PRONET
    CHAOS = cpcap.DLT_CHAOS
    IEEE802 = cpcap.DLT_IEEE802
    ARCNET = cpcap.DLT_ARCNET
    SLIP = cpcap.DLT_SLIP
    PPP = cpcap.DLT_PPP
    FDDI = cpcap.DLT_FDDI

    RAW = cpcap.DLT_RAW

    IEEE802_11_RADIO = cpcap.DLT_IEEE802_11_RADIO

    DOCSIS = cpcap.DLT_DOCSIS

    @property
    def description(self) -> str:
        return cpcap.pcap_datalink_val_to_description_or_dlt(self).decode()


class Error(Exception):
    """
    Raised when an error occurs in libpcap.

    .. attribute:: code
       :type: ErrorCode

       Error code.

    .. attribute:: msg
       :type: str

       Error message.
    """
    def __init__(self, code, msg):
        self.code = ErrorCode(code)
        self.msg = msg
        super().__init__(self.code, self.msg)


class Warning(Warning):
    """
    Warning category for libpcap warnings.

    .. attribute:: code
       :type: ErrorCode

       Error code.

    .. attribute:: msg
       :type: str

       Warning message.
    """
    def __init__(self, code, msg):
        self.code = ErrorCode(code)
        self.msg = msg
        super().__init__(self.code, self.msg)


# Initialize libpcap
cdef char init_errbuf[cpcap.PCAP_ERRBUF_SIZE]
if cpcap.pcap_init(cpcap.PCAP_CHAR_ENC_UTF_8, init_errbuf) < 0:
    raise Error(ErrorCode.ERROR, init_errbuf.decode())


class PcapIf:
    """
    A Pcap interface.

    You can either pass this object or its :attr:`name` to functions expecting an interface.

    .. attribute:: name
       :type: str

       Interface name.

    .. attribute:: description
       :type: Optional[str]

       Interface description.

    .. attribute:: addresses
       :type: PcapAddr

       List of interface addresses.

    .. attribute:: flags
       :type: PcapIfFlags

       Interface flags.
    """

    def __init__(self, name, description, addresses, flags):
        self.name = name
        self.description = description
        self.addresses = addresses
        self.flags = flags

    def __repr__(self):
        return f"<PcapIf(name={self.name!r}, description={self.description!r})>"


cdef object PcapIf_from_c(cpcap.pcap_if_t* dev):
    cdef cpcap.pcap_addr* addr

    addresses = []
    addr = dev.addresses
    while addr:
        addresses.append(PcapAddr_from_c(addr))
        addr = addr.next

    return PcapIf(
        dev.name.decode(),
        dev.description.decode() if dev.description is not NULL else None,
        addresses,
        PcapIfFlags(dev.flags),
    )


class PcapIfFlags(enum.IntFlag):
    """Pcap interface flags."""
    LOOPBACK = cpcap.PCAP_IF_LOOPBACK
    UP = cpcap.PCAP_IF_UP
    RUNNING = cpcap.PCAP_IF_RUNNING
    WIRELESS = cpcap.PCAP_IF_WIRELESS
    CONNECTION_STATUS_UNKNOWN = cpcap.PCAP_IF_CONNECTION_STATUS_UNKNOWN
    CONNECTION_STATUS_CONNECTED = cpcap.PCAP_IF_CONNECTION_STATUS_CONNECTED
    CONNECTION_STATUS_DISCONNECTED = cpcap.PCAP_IF_CONNECTION_STATUS_DISCONNECTED
    CONNECTION_STATUS_NOT_APPLICABLE = cpcap.PCAP_IF_CONNECTION_STATUS_NOT_APPLICABLE


class ErrorCode(enum.IntEnum):
    """Pcap error codes."""
    ERROR = cpcap.PCAP_ERROR
    BREAK = cpcap.PCAP_ERROR_BREAK
    NOT_ACTIVATED = cpcap.PCAP_ERROR_NOT_ACTIVATED
    ACTIVATED = cpcap.PCAP_ERROR_ACTIVATED
    NO_SUCH_DEVICE = cpcap.PCAP_ERROR_NO_SUCH_DEVICE
    RFMON_NOTSUP = cpcap.PCAP_ERROR_RFMON_NOTSUP
    NOT_RFMON = cpcap.PCAP_ERROR_NOT_RFMON
    PERM_DENIED = cpcap.PCAP_ERROR_PERM_DENIED
    IFACE_NOT_UP = cpcap.PCAP_ERROR_IFACE_NOT_UP
    CANTSET_TSTAMP_TYPE = cpcap.PCAP_ERROR_CANTSET_TSTAMP_TYPE
    PROMISC_PERM_DENIED = cpcap.PCAP_ERROR_PROMISC_PERM_DENIED
    TSTAMP_PRECISION_NOTSUP = cpcap.PCAP_ERROR_TSTAMP_PRECISION_NOTSUP

    WARNING = cpcap.PCAP_WARNING
    WARNING_PROMISC_NOTSUP = cpcap.PCAP_WARNING_PROMISC_NOTSUP
    WARNING_TSTAMP_TYPE_NOTSUP = cpcap.PCAP_WARNING_TSTAMP_TYPE_NOTSUP

    @property
    def description(self):
        """Error code description."""
        return cpcap.pcap_statustostr(self).decode()


class Direction(enum.IntEnum):
    """Direction for :meth:`Pcap.setdirection`."""
    INOUT = cpcap.PCAP_D_INOUT
    IN = cpcap.PCAP_D_IN
    OUT = cpcap.PCAP_D_OUT


NETMASK_UNKNOWN = <cpcap.bpf_u_int32>cpcap.PCAP_NETMASK_UNKNOWN


class TstampType(enum.IntEnum):
    """Timestamp types."""
    HOST = cpcap.PCAP_TSTAMP_HOST
    HOST_LOWPREC = cpcap.PCAP_TSTAMP_HOST_LOWPREC
    HOST_HIPREC = cpcap.PCAP_TSTAMP_HOST_HIPREC
    ADAPTER = cpcap.PCAP_TSTAMP_ADAPTER
    ADAPTER_UNSYNCED = cpcap.PCAP_TSTAMP_ADAPTER_UNSYNCED
    HOST_HIPREC_UNSYNCED = cpcap.PCAP_TSTAMP_HOST_HIPREC_UNSYNCED

    @property
    def name(self):
        return cpcap.pcap_tstamp_type_val_to_name(self).decode()

    @property
    def description(self):
        return cpcap.pcap_tstamp_type_val_to_description(self).decode()


class TstampPrecision(enum.IntEnum):
    """Timestamp precision."""
    MICRO = cpcap.PCAP_TSTAMP_PRECISION_MICRO
    NANO = cpcap.PCAP_TSTAMP_PRECISION_NANO


class PcapAddr:
    """
    Pcap interface address.

    .. attribute:: addr
       :type: str

       Address.

    .. attribute:: netmask
       :type: str

       Netmask for the address.

    .. attribute:: broadaddr
       :type: str

       Broadcast address for that address.

    .. attribute:: dstaddr
       :type: Optional[str]

       P2P destination address for that address.
    """

    def __init__(self, addr, netmask, broadaddr, dstaddr):
        self.addr = addr
        self.netmask = netmask
        self.broadaddr = broadaddr
        self.dstaddr = dstaddr

    def __repr__(self):
        return f"PcapAddr({self.addr!r}, {self.netmask!r}, {self.broadaddr!r}, {self.dstaddr!r})"


cdef object PcapAddr_from_c(cpcap.pcap_addr* addr):
    return PcapAddr(
        makesockaddr_addr(addr.addr),
        makesockaddr_addr(addr.netmask),
        makesockaddr_addr(addr.broadaddr),
        makesockaddr_addr(addr.dstaddr),
    )


cdef makesockaddr_addr(csocket.sockaddr* addr):
    cdef char inet_buf[csocket.INET_ADDRSTRLEN]
    cdef char inet6_buf[csocket.INET6_ADDRSTRLEN]

    if not addr:
        return None
    elif addr.sa_family == csocket.AF_INET:
        if not csocket.inet_ntop(csocket.AF_INET, &(<csocket.sockaddr_in*>addr).sin_addr, inet_buf, sizeof(inet_buf)):
            PyErr_SetFromErrno(OSError)
        return inet_buf.decode()
    elif addr.sa_family == csocket.AF_INET6:
        if not csocket.inet_ntop(csocket.AF_INET6, &(<csocket.sockaddr_in6*>addr).sin6_addr, inet6_buf, sizeof(inet6_buf)):
            PyErr_SetFromErrno(OSError)
        return inet6_buf.decode()
    else:
        # TODO What should we do for unknown sa_family? We don't even know the right size to copy it
        # raw...
        return (<unsigned char*>addr)[:sizeof(csocket.sockaddr)]


@cython.freelist(8)
cdef class Pkthdr:
    """
    Pcap packet header.
    """
    cdef cpcap.pcap_pkthdr pkthdr

    @staticmethod
    cdef from_ptr(const cpcap.pcap_pkthdr* pkthdr):
        cdef Pkthdr self = Pkthdr.__new__(Pkthdr)
        self.pkthdr = pkthdr[0]
        return self

    def __repr__(self):
        return f"<Pkthdr(ts={self.ts!r}, caplen={self.caplen!r}, len={self.len!r})>"

    @property
    def ts(self) -> int:
        """Timestamp."""
        return self.pkthdr.ts.tv_sec + self.pkthdr.ts.tv_usec / 1000000

    # TODO Consider a ts_datetime property that returns ts as a datetime (What about the timezone though...)

    @property
    def caplen(self) -> int:
        """Length of portion present."""
        return self.pkthdr.caplen

    @property
    def len(self) -> int:
        """Length of this packet (off wire)."""
        return self.pkthdr.len


@cython.freelist(8)
cdef class Stat:
    """Capture statistics."""
    cdef cpcap.pcap_stat stat

    def __repr__(self):
        return f"<Stat recv={self.recv!r} drop={self.drop!r} ifdrop={self.ifdrop!r}>"

    @property
    def recv(self):
        """Number of packets received."""
        return self.stat.ps_recv

    @property
    def drop(self):
        """Number of packets dropped."""
        return self.stat.ps_drop

    @property
    def ifdrop(self):
        """Drops by interface -- only supported on some platforms."""
        return self.stat.ps_ifdrop


def findalldevs() -> List[PcapIf]:
    """Get a list of capture devices."""
    cdef char errbuf[cpcap.PCAP_ERRBUF_SIZE]
    cdef cpcap.pcap_if_t* dev

    cdef cpcap.pcap_if_t* devs
    err = cpcap.pcap_findalldevs(&devs, errbuf)
    if err < 0:
        raise Error(err, errbuf.decode())

    try:
        result = []
        dev = devs
        while dev:
            result.append(PcapIf_from_c(dev))
            dev = dev.next

        return result
    finally:
        cpcap.pcap_freealldevs(devs)


def lookupnet(device: Union[str, PcapIf]) -> (int, int):
    """
    Find the IPv4 network number and netmask for a device.

    This is mostly used to pass the netmask to :meth:`Pcap.compile`.
    """
    if isinstance(device, PcapIf):
        device = device.name

    cdef char errbuf[cpcap.PCAP_ERRBUF_SIZE]
    cdef cpcap.bpf_u_int32 net
    cdef cpcap.bpf_u_int32 mask
    err = cpcap.pcap_lookupnet(device.encode(), &net, &mask, errbuf)
    if err < 0:
        raise Error(err, errbuf.decode())

    return net, mask


def create(source: Union[str, PcapIf]) -> Pcap:
    """
    Create a live capture.

    Set any additional configuration and call :meth:`Pcap.activate` to activate the capture.
    """
    if isinstance(source, PcapIf):
        source = source.name

    cdef char errbuf[cpcap.PCAP_ERRBUF_SIZE]
    cdef cpcap.pcap_t* pcap = cpcap.pcap_create(source.encode(), errbuf)
    if not pcap:
        raise Error(ErrorCode.ERROR, errbuf.decode())

    return Pcap.from_ptr(pcap)


def open_live(device: Union[str, PcapIf], snaplen: int, promisc: bool, to_ms: int) -> Pcap:
    """
    Open a device for capturing.

    .. deprecated:: libpcap-1.0
       Prefer :func:`create`
    """
    if isinstance(device, PcapIf):
        device = device.name

    cdef char errbuf[cpcap.PCAP_ERRBUF_SIZE]
    cdef cpcap.pcap_t* pcap = cpcap.pcap_open_live(device.encode(), snaplen, promisc, to_ms, errbuf)
    if not pcap:
        raise Error(ErrorCode.ERROR, errbuf.decode())

    return Pcap.from_ptr(pcap)


cpdef Pcap open_dead(linktype: DatalinkType, snaplen: int, precision: TstampPrecision=TstampPrecision.MICRO):
    """Open a fake Pcap for compiling filters or opening a capture for output."""
    cdef cpcap.pcap_t* pcap = cpcap.pcap_open_dead_with_tstamp_precision(linktype, snaplen, precision)
    return Pcap.from_ptr(pcap)


def open_offline(fname: os.PathLike, precision: TstampPrecision=TstampPrecision.MICRO) -> Pcap:
    """Open a saved capture file for reading."""
    cdef char errbuf[cpcap.PCAP_ERRBUF_SIZE]
    cdef cpcap.pcap_t* pcap = cpcap.pcap_open_offline_with_tstamp_precision(os.fsencode(fname), precision, errbuf)
    if not pcap:
        raise Error(ErrorCode.ERROR, errbuf.decode())

    return Pcap.from_ptr(pcap)


def compile(linktype: DatalinkType, snaplen: int, filter_: str, optimize: bool, netmask: int) -> BpfProgram:
    """
    Compile a filter expression.

    Shortcut for compiling a filter without an active Pcap. You might want to use
    :meth:`Pcap.compile` which will save you from passing some parameters.
    """
    with open_dead(linktype, snaplen) as pcap:
        return pcap.compile(filter_, optimize, netmask)


cdef struct _LoopCallbackContext:
    PyObject* pcap
    PyObject* func


# TODO Is the way we propogate exceptions here safe?
cdef void _loop_callback(unsigned char* user, const cpcap.pcap_pkthdr* pkt_header, const unsigned char* pkt_data) except * with gil:
    ctx = <_LoopCallbackContext*>user
    try:
        (<object>ctx.func)(Pkthdr.from_ptr(pkt_header), pkt_data[:pkt_header.caplen])
    except:
        cpcap.pcap_breakloop((<Pcap>ctx.pcap).pcap)
        raise


cdef class Pcap:
    """
    A packet capture.

    Created by one of :func:`create`, :func:`open_live`, :func:`open_dead`, or :func:`open_offline`.

    You need to explicitly :meth:`close` this when done or you will get a :exc:`ResourceWarning`.
    (You can use ``with``).

    To read packets, iterate this object. For example::

        for pkthdr, data in pcap:
            if pkthdr is None:
                continue

            print(pkthdr, data)

    .. warning:: Iteration will return ``(None, None)`` in case of packet buffer timeouts.

    Or use :meth:`loop` or :meth:`dispatch`.
    """
    cdef cpcap.pcap_t* pcap

    @staticmethod
    cdef from_ptr(cpcap.pcap_t* pcap):
        cdef Pcap self = Pcap.__new__(Pcap)
        self.pcap = pcap
        return self

    def __dealloc__(self):
        if self.pcap:
            warnings.warn(f"unclosed Pcap {self!r}", ResourceWarning, source=self)
            self.close()

    cpdef close(self):
        """Close the Pcap."""
        if self.pcap:
            cpcap.pcap_close(self.pcap)
            self.pcap = NULL

    cdef int _check_closed(self) except -1:
        if self.pcap is NULL:
            raise ValueError("Operation on closed Pcap")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def __iter__(self):
        return self

    def __next__(self):
        self._check_closed()

        cdef cpcap.pcap_pkthdr* pkt_header
        cdef const unsigned char* pkt_data

        with nogil:
            err = cpcap.pcap_next_ex(self.pcap, &pkt_header, &pkt_data)

        if err == cpcap.PCAP_ERROR_BREAK:
            raise StopIteration
        elif err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode())
        elif err == 0:
            return None, None

        # TODO I wonder if there is a way to use the Python buffer interface to possibly save the copy
        # ownership is a problem since the pointer is only valid until the next call
        return Pkthdr.from_ptr(pkt_header), pkt_data[:pkt_header.caplen]

    def loop(self, int cnt, callback: Callable[[Pkthdr, bytes], None]):
        """
        Process packets from a live capture or savefile.

        Unlike :meth:`dispatch` this does not return on live packet buffer timeouts.
        """
        self._check_closed()

        cdef _LoopCallbackContext ctx
        ctx.pcap = <PyObject*>self
        ctx.func = <PyObject*>callback

        with nogil:
            err = cpcap.pcap_loop(self.pcap, cnt, _loop_callback, <unsigned char*>&ctx)
        if err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode)

    def dispatch(self, int cnt, callback: Callable[[Pkthdr, bytes], None]):
        """Process packets from a live capture or savefile."""
        self._check_closed()

        cdef _LoopCallbackContext ctx
        ctx.pcap = <PyObject*>self
        ctx.func = <PyObject*>callback

        with nogil:
            err = cpcap.pcap_dispatch(self.pcap, cnt, _loop_callback, <unsigned char*>&ctx)
        if err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode())

    def breakloop(self):
        """Force a :meth:`dispatch` or :meth:`loop` call to return."""
        self._check_closed()

        cpcap.pcap_breakloop(self.pcap)

    def getnonblock(self) -> bool:
        """Get the state of non-blocking mode."""
        self._check_closed()

        cdef char errbuf[cpcap.PCAP_ERRBUF_SIZE]
        result = cpcap.pcap_getnonblock(self.pcap, errbuf)
        if result < 0:
            raise Error(result, errbuf.decode())

        return bool(result)

    def setnonblock(self, nonblock: bool):
        """Set the state of non-blocking mode."""
        self._check_closed()

        cdef char errbuf[cpcap.PCAP_ERRBUF_SIZE]
        result = cpcap.pcap_setnonblock(self.pcap, nonblock, errbuf)
        if result < 0:
            raise Error(result, errbuf.decode())

    def set_snaplen(self, snaplen: int):
        """Set the snapshot length for a not-yet-Pcap."""
        self._check_closed()

        err = cpcap.pcap_set_snaplen(self.pcap, snaplen)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def set_promisc(self, promisc: bool):
        """Set promiscuous mode for a not-yet-activated Pcap."""
        self._check_closed()

        err = cpcap.pcap_set_promisc(self.pcap, promisc)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def can_set_rfmon(self) -> bool:
        """Check whether monitor mode can be set for a not-yet-activated Pcap."""
        self._check_closed()

        result = cpcap.pcap_can_set_rfmon(self.pcap)
        if result < 0:
            if result == ErrorCode.ERROR:
                raise Error(result, cpcap.pcap_geterr(self.pcap).decode())

            raise Error(result, cpcap.pcap_statustostr(result).decode())

        return bool(result)

    def set_rfmon(self, rfmon: bool):
        """Set monitor mode for a not-yet-activated Pcap."""
        self._check_closed()

        err = cpcap.pcap_set_rfmon(self.pcap, rfmon)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def set_timeout(self, timeout: int):
        """Set the packet buffer timeout for a not-yet-activated Pcap."""
        self._check_closed()

        err = cpcap.pcap_set_timeout(self.pcap, timeout)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def set_tstamp_type(self, tstamp_type: TstampType):
        """Set the time stamp type to be used by a Pcap."""
        self._check_closed()

        err = cpcap.pcap_set_tstamp_type(self.pcap, tstamp_type)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def set_immediate_mode(self, immediate_mode: bool):
        """Set immediate mode for a not-yet-activated Pcap."""
        self._check_closed()

        err = cpcap.pcap_set_immediate_mode(self.pcap, immediate_mode)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def set_buffer_size(self, buffer_size: int):
        """Set the buffer size for a not-yet-activated Pcap."""
        self._check_closed()

        err = cpcap.pcap_set_buffer_size(self.pcap, buffer_size)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def set_tstamp_precision(self, tstamp_precision: TstampPrecision):
        """Set the time stamp precision returned in captures."""
        self._check_closed()

        err = cpcap.pcap_set_tstamp_precision(self.pcap, tstamp_precision)
        if err < 0:
            raise Error(err, cpcap.pcap_statustostr(err).decode())

    def get_tstamp_precision(self) -> TstampPrecision:
        """Get the time stamp precision returned in captures."""
        self._check_closed()

        return TstampPrecision(cpcap.pcap_get_tstamp_precision(self.pcap))

    def activate(self):
        """Activate a Pcap."""
        self._check_closed()

        err = cpcap.pcap_activate(self.pcap)
        if err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode())
        elif err > 0:
            warnings.warn(Warning(err, cpcap.pcap_geterr(self.pcap).decode()))

    def list_tstamp_types(self) -> List[TstampType]:
        """Get a list of time stamp types supported by a capture device."""
        self._check_closed()

        cdef int* tstamp_types
        cdef int num = cpcap.pcap_list_tstamp_types(self.pcap, &tstamp_types)
        if num < 0:
            raise Error(num, cpcap.pcap_geterr(self.pcap).decode())

        try:
            result = []
            for tstamp_type in tstamp_types[:num]:
                result.append(TstampType(tstamp_type))

            return result
        finally:
            cpcap.pcap_free_tstamp_types(tstamp_types)

    def datalink(self) -> DatalinkType:
        """Get the link-layer header type."""
        self._check_closed()

        result = cpcap.pcap_datalink(self.pcap)
        if result < 0:
            raise Error(result, cpcap.pcap_statustostr(result).decode())

        try:
            return DatalinkType(result)
        except ValueError:
            return result

    def list_datalinks(self) -> List[DatalinkType]:
        """Get a list of link-layer header types supported by a Pcap."""
        self._check_closed()

        cdef int* datalinks
        cdef int num = cpcap.pcap_list_datalinks(self.pcap, &datalinks)
        if num < 0:
            raise Error(num, cpcap.pcap_geterr(self.pcap).decode())

        try:
            result = []
            for datalink in datalinks[:num]:
                try:
                    result.append(DatalinkType(datalink))
                except ValueError:
                    result.append(datalink)

            return result
        finally:
            cpcap.pcap_free_datalinks(datalinks)

    def set_datalink(self, datalink: DatalinkType):
        """Set the link-layer header type to be used by a Pcap."""
        self._check_closed()

        result = cpcap.pcap_set_datalink(self.pcap, datalink)
        if result < 0:
            raise Error(result, cpcap.pcap_geterr(self.pcap).decode())

        return result

    def snapshot(self) -> int:
        """Get the snapshot length."""
        self._check_closed()

        result = cpcap.pcap_snapshot(self.pcap)
        if result < 0:
            raise Error(result, cpcap.pcap_statustostr(result).decode())

        return result

    def is_swapped(self):
        """Find out whether a savefile has the native byte order."""
        self._check_closed()

        result = cpcap.pcap_is_swapped(self.pcap)
        if result < 0:
            raise Error(result, cpcap.pcap_statustostr(result).decode())

        return result

    def compile(self, filter_: str, optimize: bool, netmask: int) -> BpfProgram:
        """Compile a filter expression."""
        # Note that if we add support for libpcap older than 1.8, we need to add a global lock here
        self._check_closed()

        cdef BpfProgram bpf_prog = BpfProgram.__new__(BpfProgram)
        err = cpcap.pcap_compile(self.pcap, &bpf_prog.bpf_prog, filter_.encode(), optimize, netmask)
        if err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode())

        return bpf_prog

    def setfilter(self, bpf_prog: BpfProgram):
        """Set the BPF filter."""
        self._check_closed()

        err = cpcap.pcap_setfilter(self.pcap, &bpf_prog.bpf_prog)
        if err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode())

    def setdirection(self, d: Direction):
        """Set the direction for which packets will be captured."""
        self._check_closed()

        err = cpcap.pcap_setdirection(self.pcap, d)
        if err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode())

    def stats(self) -> Stat:
        """Get capture statistics."""
        self._check_closed()

        cdef Stat stat = Stat.__new__(Stat)
        err = cpcap.pcap_stats(self.pcap, &stat.stat)
        if err < 0:
            raise Error(err, cpcap.pcap_geterr(self.pcap).decode())

        return stat

    def dump_open(self, fname: os.PathLike) -> Dumper:
        """Open a file to which to write packets."""
        self._check_closed()

        cdef Dumper dumper = Dumper.__new__(Dumper)
        dumper.dumper = cpcap.pcap_dump_open(self.pcap, os.fsencode(fname))
        if not dumper.dumper:
            raise Error(ErrorCode.ERROR, cpcap.pcap_geterr(self.pcap).decode())

        return dumper

    def dump_open_append(self, fname: os.PathLike) -> Dumper:
        """
        Open a file to which to write packets but, if the file already exists, and is a pcap file
        with the same byte order as the host opening the file, and has the same time stamp
        precision, link-layer header type, and snapshot length as p, it will write new packets at
        the end of the file.
        """
        self._check_closed()

        cdef Dumper dumper = Dumper.__new__(Dumper)
        dumper.dumper = cpcap.pcap_dump_open_append(self.pcap, os.fsencode(fname))
        if not dumper.dumper:
            raise Error(ErrorCode.ERROR, cpcap.pcap_geterr(self.pcap).decode())

        return dumper

    def inject(self, const unsigned char[::1] buf) -> int:
        """
        Transmit a packet. *buf* is a object supporting the buffer protocol, e.g. :class:`bytes`,
        :class:`bytearray`.

        .. note::

           :meth:`sendpacket` is like :meth:`inject`, but it returns 0 on success, rather than
           returning the number of bytes written. (pcap_inject() comes from OpenBSD;
           pcap_sendpacket() comes from WinPcap/Npcap. Both are provided for compatibility.)
        """
        self._check_closed()

        result = cpcap.pcap_inject(self.pcap, &buf[0], <size_t>buf.shape[0])
        if result < 0:
            raise Error(ErrorCode.ERROR, cpcap.pcap_geterr(self.pcap).decode())

        return result

    def sendpacket(self, const unsigned char[::1] buf):
        """
        Transmit a packet. *buf* is a object supporting the buffer protocol, e.g. :class:`bytes`,
        :class:`bytearray`.

        .. note::

           :meth:`sendpacket` is like :meth:`inject`, but it returns 0 on success, rather than
           returning the number of bytes written. (pcap_inject() comes from OpenBSD;
           pcap_sendpacket() comes from WinPcap/Npcap. Both are provided for compatibility.)
        """
        self._check_closed()

        result = cpcap.pcap_sendpacket(self.pcap, &buf[0], <int>buf.shape[0])
        if result < 0:
            raise Error(ErrorCode.ERROR, cpcap.pcap_geterr(self.pcap).decode())


# TODO Support dumping/loading bytecode, __getitem__?
cdef class BpfProgram:
    """
    A BPF filter program for :meth:`Pcap.setfilter`.

    Can be created via :meth:`Pcap.compile`.
    """
    cdef cpcap.bpf_program bpf_prog

    def __dealloc__(self):
        if self.bpf_prog.bf_insns:
            cpcap.pcap_freecode(&self.bpf_prog)

    def offline_filter(self, pkt_header: Pkthdr, pkt_data: bytes) -> bool:
        """Check whether a filter matches a packet."""
        return cpcap.pcap_offline_filter(&self.bpf_prog, &pkt_header.pkthdr, pkt_data)

    def dump(self, option=0):
        """
        Dump the filter to stdout.

        .. note:: Sadly the dumping function doesn't take an output stream...
        """
        cpcap.bpf_dump(&self.bpf_prog, option)
        stdio.fflush(stdio.stdout)


cdef class Dumper:
    """Dumper represents a capture savefile."""
    cdef cpcap.pcap_dumper_t* dumper

    def __dealloc__(self):
        if self.dumper:
            warnings.warn(f"unclosed Dumper {self!r}", ResourceWarning, source=self)
            self.close()

    cpdef close(self):
        """Close the Dumper."""
        if self.dumper:
            cpcap.pcap_dump_close(self.dumper)
            self.dumper = NULL

    cdef int _check_closed(self) except -1:
        if self.dumper is NULL:
            raise ValueError("Operation on closed Dumper")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def dump(self, Pkthdr pkt_header, pkt_data):
        """Write a packet to a capture file."""
        self._check_closed()

        cpcap.pcap_dump(<unsigned char*>self.dumper, &pkt_header.pkthdr, pkt_data)

    def ftell(self):
        """Get the current file offset for a savefile being written."""
        self._check_closed()

        result = cpcap.pcap_dump_ftell64(self.dumper)
        if result == cpcap.PCAP_ERROR:
            raise Error(result, cpcap.pcap_statustostr(<int>result).decode())

        return result


def lib_version():
    """Get the version information for libpcap."""
    return cpcap.pcap_lib_version().decode()
