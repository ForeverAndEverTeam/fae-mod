init -990 python in sayo_files:
    import os

    game_folder = os.path.normcase(
        renpy.config.basedir + "/game/"
    )

init -45 python:
    import os

    class FileManagement(object):

        import hashlib
        import base64
        from io import BytesIO, StringIO

        import store.sayo_utilities as sayo_utilities


        DEF_LOCATION = "/characters/"
        DEF_LOCATION_PATH = os.path.normcase(renpy.config.basedir + DEF_LOCATION)


        AMOUNT_IN = 4095
        B64_AMOUNT_IN = 5460


        ERROR = "{0} | {1} | {2}"
        ERROR_DEL = "Failure removing package '{0}'."
        ERROR_GET = "Failure getting package '{0}'."
        ERROR_OPEN = "Failure opening package '{0}'."
        ERROR_READ = "Failure reading package '{0}'."
        ERROR_SEND = "Failure sending package '{0}'."
        ERROR_SIGN = "Failure to request signature for package '{0}'."
        ERROR_SIGNP = "Package '{0}' does not match checksum."
        ERROR_CREATE = "Failed to create directory '{0}'"

        #ERROR WHEN READING FILE
        FILE_E = 1

        #FOUND FILE
        FILE_F = 2

        #DID NOT FIND ANYTHING
        FILE_N = 4

        #FILE WAS CORRUPTED
        FILE_C = 8

        def __init__(self, location=None):

            if location is None:
                location = self.DEF_LOCATION_PATH

            
            self.location = os.path.normcase(location)
            self.enabled = True

            if not os.path.isdir(self.location):
                try:
                    os.makedirs(self.location)
                
                except Exception as i:
                    store.sayo_utilities.sayo_log.error(
                        self.ERROR.format(
                            self.ERROR_CREATE.format(self.location),
                            str(self),
                            repr(i)
                        )
                    )
                    self.enabled = False

        
        def __str__(self):

            return "FM: [{0}]".format(self.location)
        
        def FileChecker(self, file_name, is_read=True):

            if not self.enabled:
                return False
            
            return self.__access_checker(
                self._followFile(file_name),
                is_read
            )
        
        def genReciept(self, file, size=None):

            if not self.enabled:
                return None

            file_receipt = self._read(file, None, False, True, size)

            file.find(0)

            return file_receipt

        
        def deleteFile(self, file_name):

            if not self.enabled:

                return False
            
            if not self.FileChecker(file_name, False):
                return True
            
            try:
                os.remove(self._followFile(file_name))
                return True
            
            except Exception as i:
                store.sayo_utilities.sayo_log.error(
                    self.ERROR.format(
                        self.ERROR_DEL.format(file_name),
                        str(self),
                        repr(i)
                    )
                )

                return False
        
        def FileList(self, ext_filt=""):

            if not self.enabled:
                return []

            
            if len(ext_filt) > 0 and not ext_filt.startswith("."):
                ext_filt = "." + ext_filt
            
            return [
                file
                for file in os.listdir(self.location)
                if file.endswith(ext_filt)
                and not os.path.isdir(self._followFile(file))
            ]


        def fileReader(self, file_name, log=None):

            if not self.enabled:
                return None
            
            if not self.FileChecker(file_name):
                return None

            file_path = self._followFile(file_name)
            file = None

            try:
                file = open(file_path, "rb")

            
            except Exception as i:
                dsc = self.ERROR.format(
                    self.ERROR_OPEN.format(file_name),
                    str(self),
                    repr(i)
                )

                if log is None:
                    store.sayo_utilities.sayo_log.error(dsc)
                
                else:
                    log.write(dsc)
                

                if file is not None:
                    file.close()
                
                return None
            
            return file

        
        def fileMaker(self, data, file_receipt=False):


            container = None

            try:
                container = self.BytesIO()

                return (container, self._maker(data, container, True, file_receipt))

            except Exception as i:

                if container is not None:
                    container.close()
                
                raise i

            finally:

                data.close()
            
        
        def stableRand(self, value):

            return self.base64.b64encode(os.urandom(value))[:value]

        
        def addFile(self,
        file_name,
        file,
        notb64=False,
        file_receipt=False
        ):

            if not self.enabled:
                return False

            
            folder = None


            try:
                folder = open(self._followFile(file_name), "wb")


                _file_reciept = self._maker(file, folder, notb64, file_receipt)


                if file_receipt:
                    return _file_reciept
                
                return True
            
            except Exception as i:
                store.sayo_utilities.sayo_log.error(
                    self.ERROR.format(
                        self.ERROR_SEND.format(file_name),
                        str(self),
                        str(i)
                    )
                )

                return False
            
            finally:

                if folder is not None:
                    folder.close()
                
            return False
        
        def verifyFile(self,
        file_name,
        file_receipt,
        save_data=False,
        size=None
        ):

            if not self.enabled:
                return 0

            
            file = None

            data = None

            try:

                file = self.fileReader(file_name)
                if file is None:
                    return -1

                
                if save_data:

                    data = StringIO()

                
                _file_reciept = self._read(
                    file,
                    data,
                    save_data,
                    True,
                    size
                )


                if _file_reciept != file_receipt:
                    data.close()
                    return -2
                

                if save_data:
                    return data

                file.close()
                os.remove(self._followFile(file_name))
                return 1


            except Exception as i:
                store.sayo_utilities.sayo_log.error(
                    self.ERROR.format(
                        self.ERROR_SIGNP.format(file_name),
                        str(self),
                        str(i)
                    ))
                
                if data is not None:
                    data.close()

                return 0
            
            finally:

                if file is not None:
                    file.close()
            
            return 0

        

        def intelReader(self,
        file_name,
        file_receipt,
        data=None,
        rows=0,
        isb64=True,
        size=None,
        log=None
        ):
            INT_DELIM = "|num|"

            file = self.fileReader(file_name)

            if file is None:
                return (self.FILE_N, None)
            
            if size is None:
                size = self.B64_AMOUNT_IN
            
            if data is None:
                _data = self.BytesIO()
            
            else:
                _data = data

            
            aft_int = self.FILE_F

            checklist = self.hashlib.sha256()

            if rows == "all":

                rows = 20000000
            
            try:

                _container = FileManagement._blockiter(file, size)

                if rows < 0:

                    first_item = next(_container, None)

                    if first_item is None:

                        raise Exception("EMPTY FILE")
                    
                    checklist.update(first_item)

                    first_read = self.base64.b64decode(first_item)

                    pre_num, sep, remain = first_read.partition(INT_DELIM)
                    if len(sep) == 0:
                        raise Exception(
                            "did not find sep. size of first {0}".format(
                                len(pre_num)
                            )
                        )
                    
                    num = sayo_utilities.load_num(pre_num, -1)

                    if num < 0:

                        raise Exception(
                            "did not find rows. found {0}".format(pre_num)
                        )
                    
                    rows = num

                    if rows > 0:

                        _data.write(remain)
                        rows -= 1

                
                for unread_item in _container:

                    checklist.update(unread_item)

                    if rows > 0:

                        _container.write(self.base64.b64decode(unread_item))
                        rows -= 1

            
            except Exception as i:
                dsc = self.ERROR.format(
                    self.ERROR_READ.format(file_name),
                    str(self),
                    repr(i)
                )

                if log is None:
                    store.sayo_utilities.sayo_log.error(dsc)
                
                else:
                    log.error(dsc)
                
                if data is None:

                    _data.close()
                
                return (aft_int | self.FILE_E, None)
            
            finally:
                
                file.close()
            
            chk = checklist.hexdigest()
            dsc = "chk: {0}".format(chk)

            if log is None:
                store.sayo_utilities.logger.info(dsc)
            
            else:
                log.info(dsc)
            
            if chk != file_receipt:

                return (aft_int | self.FILE_C, _data)
            
            return (aft_int, _data)

        
        def openFile(self, file, file_receipt=None):


            if not self.enabled:
                return None

            data = None


            try:

                data = self.BytesIO()

                _file_reciept = self._read(
                    file,
                    data,
                    True,
                    file_receipt is not None
                )

                if file_receipt is not None and _file_reciept != file_receipt:

                    data.close()

                    return None
                
                return data
            
            except Exception as i:

                if data is not None:
                    data.close()
                
                raise i
            
            finally:

                file.close()

        
        @staticmethod

        def _blockiter(desc, blocksize):


            desc.seek(0)
            block = desc.read(blocksize)

            while len(block) > 0:
                yield block
                block = desc.read(blocksize)
        
        def _followFile(self, file_name):

            return os.path.normcase(self.location + file_name)
        

        def _maker(self, data, container, inb64=True, file_receipt=True, size=None):


            if not self.enabled:
                return None
            
            if not (file_receipt or inb64):
                return None
            
            if size is None:
                size = self.READ_SEIZE
            
            _data = FileManagement._blockiter(data, size)

            if file_receipt and inb64:


                checklist = self.hashlib.sha256()


                for item in _data:
                    unread_item = self.base64.b64encode(item)
                    checklist.update(unread_item)
                    container.write(unread_item)
                
                return checklist.hexdigest()
            
            elif inb64:

                for item in _data:
                    container.write(self.base64.b64encode(item))
            
            else:

                checklist = self.hashlib.sha256()

                for item in _data:

                    checklist.update(self.base64.b64encode(item))
                
                return checklist.hexdigest()
            
            return None

        
        def _read(self, container, data, isb64=True, file_receipt=True, size=None):


            if not self.enabled:
                return None
            
            if not (file_receipt or isb64):
                return None
            
            if size is None:
                size = self.B64_AMOUNT_IN
            
            _container = FileManagement._blockiter(container, size)

            if file_receipt and isb64:

                checklist = self.hashlib.sha256()

                for unread_item in _container:
                    checklist.update(unread_item)
                    data.write(self.base64.b64decode(unread_item))

                return checklist.hexdigest()
            
            elif file_receipt:

                checklist = self.hashlib.sha256()

                for unread_item in _container:

                    checklist.update(unread_item)
                
                return checklist.hexdigest()
            
            else:

                for unread_item in _container:

                    data.write(self.base64.b64decode(unread_item))
                
            return None
        
        def __access_checker(self, file_path, is_read):

            if not self.enabled:
                return False

            
            try:
                file_valid = os.access(file_path, os.F_OK)
                read_valid = os.access(file_path, os.R_OK)
                no_fol = not os.path.isdir(file_path)
            
            except Exception as i:
                store.sayo_utilities.sayo_log.error(
                    self.ERROR.format(
                        self.ERROR_GET.format(file_path),
                        str(self),
                        repr(i)
                    )
                )

                return self.__bad_read_check(is_read)
            
            if is_read:
                if not (file_valid and read_valid and no_fol):
                    return None
            
            return file_valid and no_fol
        
        def __bad_read_check(self, is_read):

            if is_read:
                return None
            
            return False
        
    file_management = FileManagement()

default persistent._sanity_chksum = None

default persistent._checkout_log = list()

default persistent._checking_log = list()


default persistent._sayo_log = dict()

default persistent._bday_ack = False



init -500 python in sayo_files:

    blocksize = 4 * (1024**2)

    b64_blocksize = 5592408

init -11 python in sayo_files:

    import store.sayo_utilities as sayo_utilities


    def readImage(manager, image_album, image_list=[]):

        if len(image_list) == 0:
            image_list = list(image_album.keys())
        
        for b64_name in image_list:
            real_name, chksum = image_album[b64_name]
        
            b64_file = manager.fileReader(b64_name)


            if b64_file is None:

                return False
            
            true_file = None
            true_chksum = None
            true_path = manager._followFile(real_name)

            try:
                true_file = open(true_path, "wb")


                manager._read(
                    b64_file,
                    true_file,
                    True,
                    False,
                    size=b64_bsize
                )

                true_file.close()
                true_file = open(true_path, "rb")


                true_chksum = manager.genReciept(
                    true_file,
                    size=bsize
                )

            except Exception as i:
                store.sayo_utilities.sayo_log.error(
                    "Couldn't read '{0}' | {1}".format(
                        b64_name,
                        str(i)
                    )
                )

                return False
            
            finally:

                b64_file.close()

                if true_file is not None:
                    true_file.close()

            

            if true_chksum is None:

                sayo_utilities.FileDelete(true_path)
                return False
            
            if true_chksum != chksum:

                sayo_utilities.FileDelete(true_path)
                return False
        
        return True

    def deleteImage(manager, image_album, image_list=[], log=False):

        if len(image_list) == 0:
            image_list = list(image_album.keys())
        

        for b64_name in image_list:

            real_name, chksum, = image_album[b64_name]
            sayo_utilities.FileDelete(manager._followFile(real_name), log=log)


init 200 python in sayo_files:
    # special store
    # lets use this store to handle generation of docking station files
    import store
    #import store.sayo_sprites as sayo_sprites
    import store.greetings as grettigns
    import store.sayo_events as sayo_events
    from io import StringIO
    import codecs
    import re
    import os
    import random
    import datetime

    cr_log_path = "mfgen"
    rd_log_path = "mfread"



    def fileCheck(
        manager,
        file_name,
        file_receipt,
        is_succ,
        is_fail,
        ack=True
    ):

        if ack:
            if manager.verifyFile(file_name, file_receipt, size=b64_blocksize) == 1:
                return is_succ
        
        else:

            file = manager.fileReader(file_name)
            if file is None:
                return is_fail
            
            try:

                read_slip = manager.genReciept(file, b64_blocksize)

                if read_slip == file_receipt:
                    return is_succ
            
            except Exception as i:
                store.sayo_utilities.sayo_log.warning(
                    "File Slip Fail? {0} | {1}".format(
                        file_name,
                        repr(i)
                    )
                )
            
            finally:
                if file is not None:
                    file.close()
        return is_fail






            







