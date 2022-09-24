# Module that provides an interface for loading / saving files that we interact with
#
# NOTE: this is meant purely for reading / writing files into base64 with
#   checksums. If you want readable text files for users, DO NOT USE THIS.
#
# NOTE: some clarifications:
#   - packed files are considered files encoding in base64, but particularly
#       encoded using the fae_packShipment() function. This function will
#       encode files into sized chunks that will work nicely with file io
#   - unpacked files are raw files, not encoded

init -900 python in fae_ics:
    import os
    # Image CheckSums

    

    #################################### RPY ##################################
    #game folder
    game_folder = os.path.normcase(
        renpy.config.basedir + "/game/"
    )
    ###########################################################################


init -45 python:
    import os # this thing is super crucial everywhere so we should just
        # keep it open

    class FAEDockingStation(object):
        """
        Docking station class designed to help with file reading / writing of
        certain files.
        """
        import hashlib  # sha256 signatures
        import base64   # "packing" shipments involve base64
        from io import BytesIO, StringIO

        import store.fae_utilities as fae_utilities # logging

        # The default docking station is the characters folder
        DEF_STATION = "/characters/"
        DEF_STATION_PATH = os.path.normcase(renpy.config.basedir + DEF_STATION)

        # default read size in bytes
        # NOTE: we use 4095 here since 3 divides evenly into 4095
        READ_SIZE = 4095
        B64_READ_SIZE = 5460

        ## docking station error format
        # 0 - message
        # 1 - docking station as str
        # 2 - exception (if applicable)
        ERR = "{0} | {1} | {2}"
        ERR_DEL = "Failure removing package '{0}'."
        ERR_GET = "Failure getting package '{0}'."
        ERR_OPEN = "Failure opening package '{0}'."
        ERR_READ = "Failure reading package '{0}'."
        ERR_SEND = "Failure sending package '{0}'."
        ERR_SIGN = "Failure to request signature for package '{0}'."
        ERR_SIGNP = "Package '{0}' does not match checksum."
        ERR_CREATE = "Failed to create directory '{0}'"

        ## constants returned from smartUnpack (status constants)
        ## these are bit-based
        # errored when we were tryingto red package
        PKG_E = 1

        # if we found the package
        PKG_F = 2

        # did not find package at all
        PKG_N = 4

        # package had bad checksum (corrupted)
        PKG_C = 8


        def __init__(self, station=None):
            """
            Constructor

            IN:
                station - the path to the folder this docking station interacts
                    with. (absolute path), will try to create the folder if it
                    doesn't exist. Exceptions will be logged.
                    NOTE: END WITH '/' please
                    (Default: DEF_STATION_PATH)
            """
            if station is None:
                station = self.DEF_STATION_PATH

#            if not station.endswith("/"):
#                station += "/"

            self.station = os.path.normcase(station)
            self.enabled = True

            if not os.path.isdir(self.station):
                try:
                    os.makedirs(self.station)

                except Exception as e:
                    store.fae_utilities.fae_log.error(
                        self.ERR.format(
                            self.ERR_CREATE.format(self.station),
                            str(self),
                            repr(e)
                        )
                    )
                    self.enabled = False

        def __str__(self):
            """
            toString
            """
            return "DS: [{0}]".format(self.station)

        def checkForPackage(self, package_name, check_read=True):
            """
            Checks if a package exists in the docking station

            NOTE: will log exceptions

            NOTE: no signature checking

            IN:
                package_name - the filename we are lookiung for
                check_read - If False, then only check for existence
                    (Default: True)

            RETURNS:
                True if the package exists
                    If check_read is true, then package must also be readable
                False otherwise
            """
            if not self.enabled:
                return False

            return self.__check_access(
                self._trackPackage(package_name),
                check_read
            )


        def createPackageSlip(self, package, bs=None):
            """
            Generates a checksum for a package (which is a file descriptor)

            NOTE: may throw exceptions

            NOTE: when checking packages, we read by B64_READ_SIZE always

            IN:
                package - file descriptor of the package we want
                    NOTE: is seek(0)'d after reading
                bs - blocksize to use. IF None, the default blocksize is ued
                    (Default: None)

            RETURNS:
                sha256 checksum (hexadec) of the given package, or None
                if error occured
            """
            if not self.enabled:
                return None

            pkg_slip = self._unpack(package, None, False, True, bs)

            # reset the package when done
            package.seek(0)

            return pkg_slip


        def destroyPackage(self, package_name):
            """
            Attempts to destroy the given package in the docking station.

            NOTE: exceptions are logged

            IN:
                package_name - name of the package to delete

            RETURNS:
                True if package no exist or was deleted. False otherwise
            """
            if not self.enabled:
                return False

            if not self.checkForPackage(package_name, False):
                return True

            # otherwise we have a package
            try:
                os.remove(self._trackPackage(package_name))
                return True

            except Exception as e:
                store.fae_utilities.fae_log.error(
                    self.ERR.format(
                        self.ERR_DEL.format(package_name),
                        str(self),
                        repr(e)
                    )
                )
                return False


        def getPackageList(self, ext_filter=""):
            """
            Gets a list of the packages in the docking station.
            We also ensure that the item retrieved is not a folder.

            IN:
                ext_filter - extension filter to use when getting list.
                    the '.' is added if not already given.
                    If not given, we get all the packages
                    (Default: "")

            RETURNS: list of packages
            """
            if not self.enabled:
                return []

            # correct filter if needed
            if len(ext_filter) > 0 and not ext_filter.startswith("."):
                ext_filter = "." + ext_filter

            return [
                package
                for package in os.listdir(self.station)
                if package.endswith(ext_filter)
                and not os.path.isdir(self._trackPackage(package))
            ]


        def getPackage(self, package_name, log=None):
            """
            Gets a package from the docking station

            NOTE: will log exceptions

            IN:
                package_name - The filename we are looking for
                log - log to write messages to, if needed
                    If None, we use fae_log
                    (Default: None)

            RETURNS:
                open file descriptor to the package (READ BYTES mode)
                    if package is readable and no errors occurred
                None otherwise
            """
            if not self.enabled:
                return None

            ### Check access
            if not self.checkForPackage(package_name):
                return None

            ### open the package
            package_path = self._trackPackage(package_name)
            package = None
            try:
                package = open(package_path, "rb")

            except Exception as e:
                msg = self.ERR.format(
                    self.ERR_OPEN.format(package_name),
                    str(self),
                    repr(e)
                )

                if log is None:
                    store.fae_utilities.fae_log.error(msg)
                else:
                    log.write(msg)

                if package is not None:
                    package.close()
                return None

            # otherwise, return the opened package
            return package


        def packPackage(self, contents, pkg_slip=False):
            """
            Packs a package so it can be sent
            (encodes a data buffer into base64)

            NOTE: may throw exceptions

            IN:
                contents - the bytes buffer we want to pack. Recommened to use
                    StringIO here, but any buffer that supports read(bytes)
                    will work fine.
                    NOTE: is CLOSED after reading
                pkg_slip - True will generate a checksum for the data buffer
                    and return that as well
                    (Default: False)

            RETURNS:
                tuple of the following format:
                [0] - base64 version of the given data, in a BytesIO buffer
                [1] - sha256 checksum if pkg_slip is True, None otherwise
            """
            box = None
            try:
                box = self.BytesIO()

                return (box, self._pack(contents, box, True, pkg_slip))

            except Exception as e:
                # if an error occured, close the box buffer and raise
                if box is not None:
                    box.close()
                raise e

            finally:
                # always close teh data buffer
                contents.close()


        def safeRandom(self, amount):
            """
            Generates a random amount of unicode-safe bytes.

            IN:
                amount - number of bytes to generate
            """
            return self.base64.b64encode(os.urandom(amount))[:amount]


        def sendPackage(self,
                package_name,
                package,
                unpacked=False,
                pkg_slip=False
            ):
            """
            Sends a package into the docking station
            (Writes a file in this stations' folder)

            NOTE: exceptions are logged

            IN:
                package_name - name of the file to write
                package - the data to write as bytes
                unpacked - True means that package is not in base64
                    False means that it is in base64
                    (Default: False)
                pkg_slip - True means we should generate a sha256 checksum for
                    the package and return that
                    (Default: False)

            RETURNS:
                sha256 checksum if pkg_slip is True
                True if package was sent successfully and pkg_slip is False
                False Otherwise
            """
            if not self.enabled:
                return False

            mailbox = None
            try:
                ### open the mailbox
                mailbox = open(self._trackPackage(package_name), "wb")

                ### now write to the mailbox
                _pkg_slip = self._pack(package, mailbox, unpacked, pkg_slip)

                ### return pkg slip if we want it
                if pkg_slip:
                    return _pkg_slip

                # otherwise we good
                return True

            except Exception as e:
                store.fae_utilities.fae_log.error(
                    self.ERR.format(
                        self.ERR_SEND.format(package_name),
                        str(self),
                        str(e)
                    )
                )
                return False

            finally:
                # always close the mailbox
                if mailbox is not None:
                    mailbox.close()

            return False


        def signForPackage(self,
                package_name,
                pkg_slip,
                keep_contents=False,
                bs=None
            ):
            """
            Gets a package, checks if all the contents are there, and then
            deletes the packaging.
            (Check if a file exists, is readable, has the checksum of the
            passed in pkg_slip, then deletes the file on disk)

            NOTE: Exceptions are logged

            IN:
                package_name - name of the file to check
                pkg_slip - sha256 checksum the file should match
                keep_contents - if True, then we copy the data into a StringIO
                    buffer and return it.
                    (Defualt: False)
                bs - blocksize to use when reading the package
                    IF None, the default blocksize is used
                    (Default: None)

            RETURNS:
                if the package matches signature:
                    - if keep_contents is True
                        StringIO buffer containing decoded data
                    - otherwise, 1 is returned
                if package found but no sig match
                    - NOTE: if this happens, we NEVER delete teh package
                    - return -2
                if package not found
                    - return -1
                0 otherwise (like if error occured)
            """
            if not self.enabled:
                return 0

            package = None
            contents = None
            try:
                ### get the package
                package = self.getPackage(package_name)
                if package is None:
                    return -1

                ### we have a package, lets unpack it
                if keep_contents:
                    # use StringIO since we dont know contents unpacked
                    contents = StringIO()

                # we always want a package slip in this case
                # we only want to unpack if we are keeping contents
                _pkg_slip = self._unpack(
                    package,
                    contents,
                    keep_contents,
                    True,
                    bs
                )

                ### check sigs
                if _pkg_slip != pkg_slip:
                    contents.close()
                    return -2

                ### otherwise we matched sigs, return result
                if keep_contents:
                    return contents

                ### or discard the results
                if contents is not None:
                    contents.close()

                package.close()
                os.remove(self._trackPackage(package_name))
                return 1

            except Exception as e:
                store.fae_utilities.fae_log.error(
                    self.ERR.format(
                        self.ERR_SIGNP.format(package_name),
                        str(self),
                        str(e)
                    ))
                if contents is not None:
                    contents.close()
                return 0

            finally:
                # always close the package
                if package is not None:
                    package.close()

            return 0


        def smartUnpack(self,
                    package_name,
                    pkg_slip,
                    contents=None,
                    lines=0,
                    b64=True,
                    bs=None,
                    log=None
            ):
            """
            Combines parts of signForPackage and _unpack in a way that is very
            useful for us

            NOTE: all exceptions are logged

            NOTE: if contents was passed in an error occurred (PKG_E will be in
                the return bits), then the contents of contents is undefined.

            IN:
                package_name - name of the package to read in
                pkg_slip - chksum to check package with (considerd PRE b64 decode)
                contents - buffer to save contents of package.
                    If None, we save contents to a StringIO object and return
                    that
                    (Default: None)
                lines - number of lines to retrieve when reading data.
                    If less than 0, then we scan the file itself to tell us
                    how many lines to read.
                    If "all", then we read ALL LINES
                    (Default: 0)
                b64 - True means the package is encoded in base64
                    (Default: True)
                bs - blocksize to use. By default, we use B64_READ_SIZE
                    (Default: None)
                log - log to write messages to, if needed.
                    If None, we use fae_log
                    (Default: None)

            RETURNS: tuple of the following format
                [0]: PKG_* bits constants highlighting success/failure status
                [1]: buffer containing the contents of the package.
                    If contents is not None, this is the same reference as
                    contents.
            """
            NUM_DELIM = "|num|"

            # First, lets try and get the package
            package = self.getPackage(package_name)

            # no package? this should already have been logged, so lets just
            # return appropriate stuff
            if package is None:
                return (self.PKG_N, None)

            # otherwise we have the package. Lets setup buffers and blocksizes
            if bs is None:
                bs = self.B64_READ_SIZE

            # internalize contents so we can do proper file closing
            if contents is None:
                _contents = self.BytesIO()
            else:
                _contents = contents

            # as well as the return bytes
            ret_val = self.PKG_F

            # and our pkgslip checker
            checklist = self.hashlib.sha256()

            # and attempt to decode package
            if lines == "all":
                # nothing we read should be 200 million lines of 4MB
                lines = 20000000

            try:
                # iterator for looping
                _box = FAEDockingStation._blockiter(package, bs)

                # no lines means we need to look for them instead
                if lines < 0:
                    first_item = next(_box, None)

                    if first_item is None:
                        raise Exception("EMPTY PACKAGE")

                    checklist.update(first_item)
                    first_unpacked = self.base64.b64decode(first_item)

                    # parse the line for the first NUM_DELIM
                    raw_num, sep, remain = first_unpacked.partition(NUM_DELIM)
                    if len(sep) == 0:
                        raise Exception(
                            "did not find sep. size of first {0}".format(
                                len(raw_num)
                            )
                        )

                    num = fae_utilities.tryparseint(raw_num, -1)

                    if num < 0:
                        # this is a problem. Raise an exception
                        raise Exception(
                            "did not find lines. found {0}".format(raw_num)
                        )

                    # otherwise, set lines to num
                    lines = num

                    if lines > 0:
                        # do we save the first line?
                        _contents.write(remain)
                        lines -= 1

                # and now to look at the rest.
                # only save what we need though
                for packed_item in _box:

                    checklist.update(packed_item)

                    if lines > 0:
                        # writing out contents to buffer
                        _contents.write(self.base64.b64decode(packed_item))
                        lines -= 1


            except Exception as e:
                msg = self.ERR.format(
                    self.ERR_READ.format(package_name),
                    str(self),
                    repr(e)
                )

                if log is None:
                    store.fae_utilities.fae_log.error(msg)
                else:
                    log.error(msg)

                if contents is None:
                    # only close our internal contents if we made it
                    _contents.close()

                return (ret_val | self.PKG_E, None)

            finally:
                # always close package after this
                package.close()

            # get checksum and log
            chk = checklist.hexdigest()
            msg = "chk: {0}".format(chk)
            if log is None:
                store.fae_utilities.fae_log.info(msg)
            else:
                log.info(msg)

            # now check checksum
            if chk != pkg_slip:
                # no match? uh oh, lets return stuff anyway
                return (ret_val | self.PKG_C, _contents)

            # otherwise, we got a match so
            return (ret_val, _contents)


        def unpackPackage(self, package, pkg_slip=None):
            """
            Unpacks a package
            (decodes a base64 file into a regular BytesIO buffer)

            NOTE: may throw exceptions

            IN:
                package - file descriptor of the file to decode / unpack
                    NOTE: is CLOSED after reading
                pkg_slip - sha256 hex checksum of what the package data should
                    be. If passed in, then we check this against the package
                    NOTE: generated checksum uses data BEFORE it is decoded
                    (Default: None)

            RETURNS:
                BytesIO buffer containing the package decoded
                Or None if pkg_slip checksum was passed in and the given
                    package failed the checksum
            """
            if not self.enabled:
                return None

            contents = None
            try:
                # NOTE: we use regular StringIO in case of unicode
                contents = self.BytesIO()

                _pkg_slip = self._unpack(
                    package,
                    contents,
                    True,
                    pkg_slip is not None
                )

                if pkg_slip is not None and _pkg_slip != pkg_slip:
                    # checksum checking
                    contents.close()
                    return None

                return contents

            except Exception as e:
                # if we get an exception, close the contents buffer and raise
                # the exception
                if contents is not None:
                    contents.close()
                raise e

            finally:
                # Always close the package when we're done
                package.close()


        @staticmethod
        def _blockiter(fd, blocksize):
            """
            Creates an itererator of a file using the given blocksize

            NOTE: May throw exceptions

            IN:
                fd - file descriptor
                    NOTE: seeks this to 0 before starting
                blocksize - size to use for blocks

            YIELDS:
                blocks until a block read attempt gave us nothing

            ASSUMES:
                given file descriptor is open
            """
            fd.seek(0)
            block = fd.read(blocksize)
            while len(block) > 0:
                yield block
                block = fd.read(blocksize)


        def _trackPackage(self, package_name):
            """
            Adds this docking station's path tot he package_name so we can
            access it and stuff

            IN:
                package_name - name of the package

            RETURNS:
                package_name in a valid package_path ready for checking
            """
            return os.path.normcase(self.station + package_name)


        def _pack(self, contents, box, pack=True, pkg_slip=True, bs=None):
            """
            Runs the packing algorithm for given file descriptors
            Supports:
                1. encoding and checksumming data
                    this will encode the input, checksum it, then write to
                    output
                2. encoding data
                    this will encode the input, then write to output
                3. checksumming data
                    this will checksum the input. DOES NOT WRITE to output

            NOTE: may throw exceptions
            NOTE: if both pack and pkg_slip are False, this does absoultely
                nothing

            IN:
                contents - file descriptor to read data from
                box - file descriptor to write data to
                pack - if True, encode the input data into base64 prior to
                    writing to output data
                    (Default: True)
                pkg_slip - if True, generate a checksum of the data.
                    NOTE: if pack is True, this is done using data AFTER
                        encoding
                    (Default: True)
                bs - blocksize to use. If None, we use READ_SIZE
                    (Default: None)

            RETURNS:
                generated sha256 checksum if pkg_slip is True
                Otherwise, None
            """
            if not self.enabled:
                return None

            if not (pkg_slip or pack):
                return None

            if bs is None:
                bs = self.READ_SIZE

            _contents = FAEDockingStation._blockiter(contents, bs)

            if pkg_slip and pack:
                # encode the data, then checksum the base64, then write to
                # output
                checklist = self.hashlib.sha256()

                for item in _contents:
                    packed_item = self.base64.b64encode(item)
                    checklist.update(packed_item)
                    box.write(packed_item)

                return checklist.hexdigest()

            elif pack:
                # encode the data, write to output
                for item in _contents:
                    box.write(self.base64.b64encode(item))

            else:
                # checksum the data
                checklist = self.hashlib.sha256()

                for item in _contents:
                    checklist.update(self.base64.b64encode(item))

                return checklist.hexdigest()

            return None


        def _unpack(self, box, contents, unpack=True, pkg_slip=True, bs=None):
            """
            Runs the unpacking algorithm for given file descriptors
            Supports:
                1. checksumming and decoding data
                    this will checksum input, decode it, then write to output
                2. decoding data
                    this will decode the input, then write to ouput
                3. checksumming data
                    this will checksum the input. DOES NOT WRITE to output

            NOTE: may throw exceptions
            NOTE: if both unpack and pkg_slip are False, this does absolutely
                nothing

            IN:
                box - file descriptor to read data from
                contents - file descriptor to write data to
                unpack - if True, decode input data from base64 prior to
                    writing output data
                    (Default: True)
                pkg_slip - if True, genereate a checksum of the data.
                    NOTE: if unpack is True, this is done using data BEFORE
                        decoding
                    (Default: True)
                bs - blocksize to use. If None, use B64_READ_SIZE
                    (Default: None)

            RETURNS:
                generated sha256 checksum if pkg_slip is True
                Otherwise, None
            """
            if not self.enabled:
                return None

            if not (pkg_slip or unpack):
                return None

            if bs is None:
                bs = self.B64_READ_SIZE

            _box = FAEDockingStation._blockiter(box, bs)

            if pkg_slip and unpack:
                # checksum data, decode it, write to output
                checklist = self.hashlib.sha256()

                for packed_item in _box:
                    checklist.update(packed_item)
                    contents.write(self.base64.b64decode(packed_item))

                return checklist.hexdigest()

            elif pkg_slip:
                # checksum data
                checklist = self.hashlib.sha256()

                for packed_item in _box:
                    checklist.update(packed_item)

                return checklist.hexdigest()

            else:
                # decode the data
                for packed_item in _box:
                    contents.write(self.base64.b64decode(packed_item))

            return None

        def __check_access(self, package_path, check_read):
            """
            Checks access of the file at package_path.
            Also ensures that the file is not actually is folder.

            NOTE:
                will log exceptions

            IN:
                package_path - path to the file we want to check access to
                check_read - If True, check for read access in addition to
                    file existence

            RETURNS:
                True if package exists / is readable.
                Otherwise:
                    if check_read is True, returns None
                    otherwise, returns False
            """
            if not self.enabled:
                return False

            try:
                file_ok = os.access(package_path, os.F_OK)
                read_ok = os.access(package_path, os.R_OK)
                not_dir = not os.path.isdir(package_path)

            except Exception as e:
                store.fae_utilities.fae_log.error(
                    self.ERR.format(
                        self.ERR_GET.format(package_path),
                        str(self),
                        repr(e)
                    )
                )

                # in error case, assume failure
                return self.__bad_check_read(check_read)

            if check_read:
                if not (file_ok and read_ok and not_dir):
                    return None

            return file_ok and not_dir

        def __bad_check_read(self, check_read):
            """
            Returns an appropriate failure value givne the check_read value

            IN:
                check_read - the value of check_read

            RETURNS:
                None if check_read is True, False otherwise
            """
            if check_read:
                return None

            return False

    fae_docking_station = FAEDockingStation()


default persistent._fae_moni_chksum = None

# these should have the same size during runtime (except for empty desk mode)
# NOTE: this is only for OUR monika. Rogue monikas are not added here.
# these should basically consist of tuples:
#   [0]: datetime of event
#   [1]: checksum of Monika during this event
default persistent._fae_dockstat_checkout_log = list()
default persistent._fae_dockstat_checkin_log = list()

# dict matching monika checksums to some monika state.
# basically, if a rogue monika appears, we save her checksum to this dict
# and store some additional data.
# NOTE: to prevent collisions, if a monika file generated by this FAE has the
#   same checksum as one in this dict, we pop that checksum off this dict.
#   Yes, we basically forget a monika, but there's no use in trying to make
#   this perfect. For the majority of people, checksums will never collide.
# key: checksum of the rogue monika
# value: TODO: not sure of this yet, probably giong to be a dict so we can
#   make the values malleable
default persistent._fae_dockstat_moni_log = dict()

# set this if we are on the path to leave.
default persistent._fae_dockstat_going_to_leave = False

# this value should be in bytes
# NOTE: do NOT set this directly. Use the helper functions
default persistent._fae_dockstat_moni_size = 0

default persistent._fae_bday_sbp_reacted = False
# True means we have reacted to the surprise birthday party.
# NOTE: we need to consider how we want to do this in future bdays. probably
# may do historical when we can


init -500 python in fae_dockstat:
    # blocksize is relatively constant
    blocksize = 4 * (1024**2)
    b64_blocksize = 5592408 # (above size converted to base64)

    ## package constants for the state of monika
    # bit-based
    # Monika not found
    FAE_PKG_NF = 1

    # Monika found
    FAE_PKG_F = 2

    # Not our monika was found
    FAE_PKG_FO = 4

    # Monika data is in list form
    FAE_PKG_DL = 8

    # Monika data is in persitent form
    FAE_PKG_DP = 16

    ## surprise party constants for the state of the surprise party
    # bit based

    FAE_SBP_NONE = 1
    # no surprise party files

    FAE_SBP_CAKE = 2
    # cake was found

    FAE_SBP_BANR = 4
    # banner was found

    FAE_SBP_BLON = 8
    # balloon was found

init -11 python in fae_dockstat:
    import store.fae_utilities as fae_utilities

    def decodeImages(dockstat, image_dict, selective=[]):
        """
        Attempts to decode the iamges

        IN:
            dockstat - docking station to use
            image_dict - image map to use
            selective - list of images keys to decode
                If not passed in, we decode EVERYTHINg
                (DEfault: [])

        Returns TRUE upon success, False otherwise
        """
        if len(selective) == 0:
            selective = list(image_dict.keys())

        for b64_name in selective:
            real_name, chksum = image_dict[b64_name]

            # read in the base64 versions, output an image
            b64_pkg = dockstat.getPackage(b64_name)

            if b64_pkg is None:
                # if we didnt find the image, we in big trouble
                return False

            # setup the outfile
            real_pkg = None
            real_chksum = None
            real_path = dockstat._trackPackage(real_name)

            # now try to decode image
            try:
                real_pkg = open(real_path, "wb")

                # unpack this package
                dockstat._unpack(
                    b64_pkg,
                    real_pkg,
                    True,
                    False,
                    bs=b64_blocksize
                )

                # close and reopen as read
                real_pkg.close()
                real_pkg = open(real_path, "rb")

                # check pkg slip
                real_chksum = dockstat.createPackageSlip(
                    real_pkg,
                    bs=blocksize
                )

            except Exception as e:
                store.fae_utilities.fae_log.error(
                    "Failed to decode '{0}' | {1}".format(
                        b64_name,
                        str(e)
                    )
                )
                return False

            finally:
                # always close the base64 package
                b64_pkg.close()

                if real_pkg is not None:
                    real_pkg.close()

            # now to check this image for chksum correctness
            if real_chksum is None:
                # bad shit happened here somehow
                fae_utilities.trydel(real_path)
                return False

            if real_chksum != chksum:
                # decoded was wrong somehow
                fae_utilities.trydel(real_path)
                return False

        # otherwise success somehow
        return True


    def removeImages(dockstat, image_dict, selective=[], log=False):
        """
        Removes the decoded images at the end of their lifecycle

        IN:
            dockstat - docking station
            image_dict - image map to use
            selective - list of image keys to delete
                If not passed in, we delete everything in the image dict
                (Default: [])
            log - should we log a delete failure?
                (Default: False)

        AKA quitting
        """
        if len(selective) == 0:
            selective = list(image_dict.keys())

        for b64_name in selective:
            real_name, chksum = image_dict[b64_name]
            fae_utilities.trydel(dockstat._trackPackage(real_name), log=log)



