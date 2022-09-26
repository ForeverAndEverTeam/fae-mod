from __future__ import absolute_import
import errno
import logging
from ..codes import errorcodes
from ..util.utils import is_windows, range, get_temp_path, to_bytes, bytes, to_unicode, is_python3, is_callable
import struct
import sys
if is_windows():
    # we're going to have to do some ugly things, because Windows sucks
    import ctypes
    GENERIC_READ = 0x80000000
    GENERIC_WRITE = 0x40000000
    OPEN_EXISTING = 0x3
    INVALID_HANDLE_VALUE = -1
    PIPE_READMODE_MESSAGE = 0x2
    ERROR_FILE_NOT_FOUND = 0x2
    ERROR_PIPE_BUSY = 0xE7
    ERROR_MORE_DATA = 0xEA
    BUFSIZE = 512
else:
    try:
        from socket import MSG_NOSIGNAL
        _msg_flags = MSG_NOSIGNAL
    except ImportError:
        _msg_flags = 0
    try:
        from socket import SO_NOSIGPIPE
        _do_sock_opt = True
    except ImportError:
        _do_sock_opt = False
    import socket
    import fcntl
    from os import O_NONBLOCK


class BaseConnection(object):
    """Generate IPC Connection handler."""
    # *nix specific
    __sock = None
    # Windows specific
    __pipe = None

    __open = False
    __logger = None
    __is_logging = False

    def __init__(self, log=True, logger=None, log_file=None, log_level=logging.INFO):
        if not isinstance(log, bool):
            raise TypeError('log must be of bool type!')
        if log:
            if logger is not None:
                # Panda3D notifies are similar, so we simply check if we can make the same calls as logger
                if not hasattr(logger, 'debug'):
                    raise TypeError('logger must be of type logging!')
                self.__logger = logger
            else:
                self.__logger = logging.getLogger(__name__)
                log_fmt = logging.Formatter('[%(asctime)s][%(levelname)s] ' + '%(name)s - %(message)s')
                if log_file is not None and hasattr(log_file, 'strip'):
                    fhandle = logging.FileHandler(log_file)
                    fhandle.setLevel(log_level)
                    fhandle.setFormatter(log_fmt)
                    self.__logger.addHandler(fhandle)
                shandle = logging.StreamHandler(sys.stdout)
                shandle.setLevel(log_level)
                shandle.setFormatter(log_fmt)
                self.__logger.addHandler(shandle)
                self.__is_logging = True

    def log(self, callback_name, *args):
        if self.__logger is not None:
            if hasattr(self.__logger, callback_name) and is_callable(self.__logger.__getattribute__(callback_name)):
                self.__logger.__getattribute__(callback_name)(*args)

    def __open_pipe(self, pipe_name, log_type='warning'):
        """
        :param pipe_name:   the named pipe string
        :param log_type:    the log type to use (default 'warning')
        :return:    opened(bool), try_again(bool)
        """
        if not is_windows():
            self.log('error', 'Attempted to call a Windows call on a non-Windows OS.')
            return
        pipe = ctypes.windll.kernel32.CreateFileW(pipe_name, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0,
                                                  None)
        if pipe != INVALID_HANDLE_VALUE:
            self.__pipe = pipe
            return True, False
        err = ctypes.windll.kernel32.GetLastError()
        if err == ERROR_FILE_NOT_FOUND:
            self.log(log_type, 'File not found.')
            self.log(log_type, 'Pipe name: {}'.format(pipe_name))
            return False, False
        elif err == ERROR_PIPE_BUSY:
            if ctypes.windll.kernel32.WaitNamedPipeW(pipe_name, 10000) == 0:
                self.log(log_type, 'Pipe busy.')
                return False, False
            else:
                # try again, should be free now
                self.log('debug', 'Pipe was busy, but should be free now. Try again.')
                return False, True
        # some other error we don't care about
        self.log('debug', 'Unknown error: {}'.format(err))
        return False, False

    def open(self, pipe_no=None):
        if pipe_no is not None:
            if not isinstance(pipe_no, int):
                raise TypeError('pipe_no must be of type int!')
            if pipe_no not in range(0, 10):
                raise ValueError('pipe_no must be within range (0 <= pipe number < 10)!')
        if is_windows():
            # NOTE: don't forget to use a number after ipc-
            pipe_name = u'\\\\.\\pipe\\discord-ipc-{}'
            if pipe_no is not None:
                # we only care about the first value if pipe_no isn't None
                opened, try_again = self.__open_pipe(pipe_name.format(pipe_no))
                if opened:
                    self.__open = True
                    self.log('info', 'Connected to pipe {}, as user requested.'.format(pipe_no))
                    return
                elif try_again:
                    self.open(pipe_no=pipe_no)
                    return
            else:
                num = 0
                while True:
                    if num >= 10:
                        break
                    opened, try_again = self.__open_pipe(pipe_name.format(num), log_type='debug')
                    if opened:
                        self.__open = True
                        self.log('debug', 'Automatically connected to pipe {}.'.format(num))
                        return
                    if try_again:
                        continue
                    num += 1
            # we failed to get a pipe
            self.__pipe = None
            self.log('warning', 'Could not open a connection.')
        else:
            self.__sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            if self.__sock is None or self.__sock == -1:
                self.log('warning', 'Could not open socket.')
                self.close()
                return
            try:
                fcntl.fcntl(self.__sock, fcntl.F_SETFL, O_NONBLOCK)
            except Exception as e:
                self.log('warning', e)
                self.close()
                return
            if _do_sock_opt:
                try:
                    socket.setsockopt(socket.SOL_SOCKET, SO_NOSIGPIPE)
                except Exception as e:
                    self.log('warning', e)
                    self.log('debug', 'Attempting to use sock as is. Notify a developer if an error occurs.')
            sock_addr = get_temp_path()
            if sock_addr.endswith('/'):
                sock_addr = sock_addr[:-1]
            sock_addr += '/discord-ipc-{}'
            if pipe_no is not None:
                ret_val = self.__sock.connect_ex(sock_addr.format(pipe_no))
                if ret_val == 0:
                    self.__open = True
                    self.log('info', 'Connected to socket {}, as user requested.'.format(pipe_no))
                    return
                else:
                    self.log('warning', 'Could not open socket {}.'.format(pipe_no))
                    self.close()
            else:
                for num in range(0, 10):
                    ret_val = self.__sock.connect_ex(sock_addr.format(num))
                    if ret_val == 0:
                        self.__open = True
                        self.log('debug', 'Automatically connected to socket {}.'.format(num))
                        return
                self.log('warning', 'Could not open socket.')
                self.close()

    def write(self, data, opcode):
        if not self.connected():
            self.log('warning', 'Cannot write if we aren\'t connected yet!')
            return False
        if not isinstance(opcode, int):
            raise TypeError('Opcode must be of int type!')
        if data is None:
            data = ''
        try:
            data = to_bytes(data)
        except Exception as e:
            self.log('warning', e)
            return False
        data_len = len(data)
        # the following data must be little endian unsigned ints
        # see: https://github.com/discordapp/discord-rpc/blob/master/documentation/hard-mode.md#notes
        header = struct.pack('<II', opcode, data_len)
        # append header to data
        data = header + data
        # get new data size
        data_len = len(data)
        if self.__pipe is not None:
            written = ctypes.c_ulong(0)
            success = ctypes.windll.kernel32.WriteFile(self.__pipe, ctypes.c_char_p(data), data_len,
                                                       ctypes.byref(written), None)
            if (not success) or (data_len != written.value):
                self.log('warning', 'Failed to write data onto pipe.')
                return False
            return True
        elif self.__sock is not None:
            data_sent = 0
            while data_sent < data_len:
                try:
                    sent = self.__sock.send(data[data_sent:], _msg_flags)
                except Exception as e:
                    self.log('warning', e)
                    return False
                if sent == 0:
                    self.log('warning', 'Socket connection broken!')
                    if data_sent == 0:
                        self.log('warning', 'No data sent; closing connection.')
                        self.close()
                    return False
                data_sent += sent
            return True
        self.log('warning', 'write() executed code that shouldn\'t have run.')
        return False

    def read(self):
        ret_val = [False, None, None]
        if not self.connected():
            self.log('warning', 'Cannot read if we haven\'t opened a connection!')
            return ret_val
        data = bytes()
        header_size = struct.calcsize('<II')
        # (is_successful_read, OpCode, data)
        if self.__pipe is not None:
            available = ctypes.c_ulong(0)
            if not ctypes.windll.kernel32.PeekNamedPipe(self.__pipe, None, 0, None, ctypes.byref(available), None):
                self.log('warning', 'Peek on pipe for header failed.')
                self.close()
                ret_val[2] = [errorcodes.PipeClosed, 'Pipe closed']
                return ret_val
            if available.value < header_size:
                self.log('debug', 'Pipe doesn\'t have enough data to read in header.')
                # assume this is like errno.EAGAIN
                ret_val[2] = [errorcodes.PipeClosed, 'Pipe closed']
                return ret_val
            cb_read = ctypes.c_ulong(0)
            buff = ctypes.create_string_buffer(header_size)
            success = 0
            while not success:
                success = ctypes.windll.kernel32.ReadFile(self.__pipe, buff, header_size, ctypes.byref(cb_read), None)
                if success == 1:
                    # we successfully read the HEADER :O
                    # Note: we use RAW here, otherwise it'll be a 1 byte kinda weird thing
                    header = buff.raw
                    break
                elif ctypes.windll.kernel32.GetLastError() != ERROR_MORE_DATA:
                    # we don't have more data; close pipe
                    self.log('warning', 'Failed to read in header from pipe.')
                    self.close()
                    ret_val[2] = [errorcodes.PipeClosed, 'Pipe closed']
                    return ret_val
            opcode, data_len = struct.unpack('<II', header)
            cb_read = ctypes.c_ulong(0)
            buff = ctypes.create_string_buffer(data_len)
            success = 0
            available = ctypes.c_ulong(0)
            if not ctypes.windll.kernel32.PeekNamedPipe(self.__pipe, None, 0, None, ctypes.byref(available), None):
                self.log('warning', 'Peek on pipe for data failed.')
                self.close()
                ret_val[2] = [errorcodes.ReadCorrupt, 'Partial data in frame']
                return ret_val
            if available.value < data_len:
                self.log('warning', 'Pipe doesn\'t have enough data to read in data.')
                # assume this is like errno.EAGAIN
                ret_val[2] = [errorcodes.ReadCorrupt, 'Partial data in frame']
                return ret_val
            while not success:
                success = ctypes.windll.kernel32.ReadFile(self.__pipe, buff, data_len, ctypes.byref(cb_read), None)
                if success == 1:
                    # we successfully read the DATA :O
                    ret_val[0] = True
                    ret_val[1] = opcode
                    # value here actually works okay, so use that
                    # Note: raw also seems to work, but meh
                    data = buff.value
                    break
                elif ctypes.windll.kernel32.GetLastError() != ERROR_MORE_DATA:
                    # we don't have more data; close pipe
                    self.log('warning', 'Failed to read in data from pipe.')
                    self.close()
                    ret_val[2] = [errorcodes.ReadCorrupt, 'Partial data in frame']
                    return ret_val
        elif self.__sock is not None:
            packets = list()
            while len(bytes().join(packets)) < header_size:
                try:
                    packet = self.__sock.recv(header_size - len(bytes().join(packets)))
                except Exception as e:
                    ret_val[2] = [errorcodes.PipeClosed, 'Pipe closed']
                    if hasattr(e, 'errno'):
                        if e.errno == errno.EAGAIN:
                            self.log('debug', e)
                            self.log('debug', 'errno == EAGAIN')
                            return ret_val
                        self.log('warning', 'Failed to read in header!')
                        self.log('warning', e)
                        self.close()
                if packet is None or len(packet) == 0:
                    self.log('warning', 'Socket connection broken!')
                    if len(bytes().join(packets)) == 0:
                        self.log('warning', 'No data sent; closing connection.')
                        self.close()
                    ret_val[2] = [errorcodes.PipeClosed, 'Pipe closed']
                    return ret_val
                packets.append(packet)
            header = bytes().join(packets)
            packets = list()
            opcode, data_len = struct.unpack('<II', header)
            self.log('debug', 'Opcode: {}, data length: {}'.format(opcode, data_len))
            while len(bytes().join(packets)) < data_len:
                try:
                    packet = self.__sock.recv(data_len - len(bytes().join(packets)))
                except Exception as e:
                    ret_val[2] = [errorcodes.ReadCorrupt, 'Partial data in frame']
                    if hasattr(e, 'errno'):
                        if e.errno == errno.EAGAIN:
                            self.log('debug', e)
                            self.log('debug', 'errno == EAGAIN')
                            return ret_val
                        self.log('warning', 'Failed to read in data!')
                        self.log('warning', e)
                if packet is None or len(packet) == 0:
                    self.log('warning', 'Socket connection broken!')
                    if len(bytes().join(packets)) == 0:
                        self.log('warning', 'No data sent; closing connection.')
                        self.close()
                    ret_val[2] = [errorcodes.ReadCorrupt, 'Partial data in frame']
                    return ret_val
                packets.append(packet)
            data = bytes().join(packets)
            ret_val[0] = True
            ret_val[1] = opcode
        if ret_val[0]:
            if is_python3():
                data = to_unicode(data)
            ret_val[2] = data
        self.log('debug', 'Return values: {}'.format(ret_val))
        return ret_val

    def close(self):
        # ensure we're using Windows before trying to close a pipe
        # Note: This should **never** execute on a non-Windows machine!
        if self.__pipe is not None and is_windows():
            ctypes.windll.kernel32.CloseHandle(self.__pipe)
            self.__pipe = None
        if self.__sock is not None:
            try:
                self.__sock.shutdown(socket.SHUT_RDWR)
                self.__sock.close()
            except Exception as e:
                self.log('warning', e)
            finally:
                self.__sock = None
        if self.__open:
            self.__open = False
            self.log('debug', 'Closed IPC connection.')

    def destroy(self):
        # make sure we close everything
        self.close()
        # if we automatically set our own logger, clean it up
        if self.__is_logging:
            for handle in self.__logger.handlers[:]:
                handle.close()
                self.__logger.removeHandler(handle)
        self.__logger = None

    @property
    def is_open(self):
        return self.__open

    def connected(self):
        return self.is_open
