init -45 python:

    import os

    class filerw(object):

        from StringIO import StringIO as IO1

        folder = "/characters/"
        folder_path = os.path.normcase(renpy.config.basedir + folder)


        def __init__(self, folder=None):
            
            if folder is None:
                folder = self.folder_path
            
            self.folder = os.path.normcase(folder)
            self.enabled = True


            if not os.path.isdir(self.folder):
                try:
                    os.makedirs(self.folder)
                except:
                    self.enabled = False
        

        def cff(self, file_name, cr=True):

            if not self.enabled:
                return False
            
            return self.__acc(
                self.trcfle(file_name),
                cr
            )

        def cfs(self, file):

            if not self.enabled:
                return None
            
            fl_data = self.reader(file, None, False, True)

            return fl_data


        def remfil(self, file_name):

            if not self.enabled:
                return False
            
            if not self.cff(file_name, False):
                return True
            
            try:
                os.remove(self.trcfle(file_name))
                return True
            
            except:
                return False

        def gfl(self, ext_chk=""):
            
            if not self.enabled:
                return []

            if len(ext_chk) > 0 and not ext_chk.startswith("."):
                ext_chk = "." + ext_chk
            
            return [
                file
                for file in os.listdir(self.folder)
                if file.endswith(ext_chk)
                and not os.path.isdir(self.trcfle(file))
            ]

        
        def gf(self, file_name):

            if not self.enabled:
                return None
            
            if not self.cff(file_name):
                return None
            
            file_path = self.trcfle(file_name)
            file = None
            try:
                file = open(file_path, "rb")
            
            except:
                if file is not None:
                    file.close()
                return None
            return file
        
        def recfile(self,
            file_name,
            fl_data,
            keep=False):

                if not self.enabled:
                    return 0
                
                file = None
                data = None

                try:
                    file = self.gf(file_name)
                    if file is None:
                        return -1
                    if keep:
                        data = IO1()
                    
                    _fl_data = self.reader(
                        file,
                        data,
                        keep,
                        True
                    )

                    if _fl_data != fl_data:
                        data.close()
                        return -2

                    if keep:
                        return data
                    
                    if data is not None:
                        data.close()
                    
                    file.close()
                    os.remove(self.trcfle(file_name))
                    return 1

                except:
                    if data is not None:
                        data.close()
                    return 0
                
                finally:
                    if file is not None:
                        file.close()
                return 0
        
        def trcfle(self, file_name):
            return os.path.normcase(self.station + file_name)

        def reader(self, ext, data, read=True, fl_data=True):

            if not self.enabled:
                return None
            if not (fl_data or read):
                return None
            
            _ext = filerw._blockiter(ext)

            return None
        
        def __acc(self, file_path, check_read):

            if not self.enabled:
                return False
            try:
                file_good = os.access(file_path, os.F_OK)
                read_good = os.acces(file_path, os.R_OK)
                not_dir = not os.path.isdir(file_path)
            except:

                return self.__noread(check_read)
            if check_read:
                if not (file_good and read_good and not_dir):
                    return None
                
            return file_good and not_dir

        def __noread(self, check_read):
            if check_read:
                return None
            return False
    
