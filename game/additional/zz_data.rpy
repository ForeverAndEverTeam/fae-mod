python early in fae_data:
    from enum import Enum
    import re
    import store

    UPD_FUN = dict()

    AFT_UPD = []

    STR_VER_PAR = re.compile(r"^(?P<ver>\d+\.\d+\.\d+)(?P<suffix>.*)$")

    class TransRun(Enum):
        """
        TTR transfer scripts
        """
        INIT = 1
        RUNTIME = 2
    
    def transfer(from_versions, to_version, transfer=TransRun.INIT):
        """
        Transfer register

        FEED:
            from_versoins = version list to transfer from

            to_version = target to transfer to

            transfer = whether it's run during runtime. False = init 10

        RESULT:
            function
        """

        def wrap(_function):
            regUpdFunc(
                _callable=_function,
                from_versions=from_versions,
                to_version=to_version,
                transfer=transfer
            )
            return _function
        return wrap

    def regUpdFunc(_callable, from_versions, to_version, transfer=TransRun.INIT):
        """
        Add a function to run on update

        FEED:
            _callable = function that is run
            from_versions = version list to transfer from
            to_version = target to transfer to
            transfer = whether it's run during runtime. False = init 10
        
        """

        for from_version in from_versions:
            if from_version not in UPD_FUN:
                UPD_FUN[from_version] = dict()
            
            UPD_FUN[from_version][transfer] = (_callable, to_version)
    
    def verStrLst(ver_str):
        """
        Converter from string to list.
        """
        match = STR_VER_PAR.match(ver_str)
        if not match:
            raise ValueError("Invalid version string")
        
        ver_list = match.group("ver").split(".")
        return [int(x) for x in ver_list]

    def verComp(ver_str1, ver_str2):
        """
        Version comparitor
        """
        match1 = STR_VER_PAR.match(ver_str1)
        match2 = STR_VER_PAR.match(ver_str2)

        if not match1 or not match2:
            raise ValueError("Invalid version string")
        
        ver1 = verStrLst(match1.group("ver"))
        ver2 = verStrLst(match2.group("ver"))

        if len(ver1) > len(ver2):
            ver2 += [0] * (len(ver1) - len(ver2))
        elif len(ver1) < len(ver2):
            ver1 += [0] * (len(ver2) - len(ver1))
        

        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1
        return 0

    def runInitTransfer():
        """
        Runs init time transfer funcs. Must be after 0
        """
        if store.persistent._fae_version not in UPD_FUN:
            return

        from_version = store.persistent._fae_version

        while verComp(from_version, renpy.config.version) < 0:

            if TransRun.RUNTIME in UPD_FUN[store.persistent._fae_version]:
                AFT_UPD.append(UPD_FUN[store.persistent._fae_version][TransRun.RUNTIME])
            
            _callable, from_version = UPD_FUN[from_version][TransRun.INIT]


            _callable()
    
    def runRuntimeTransfer():
        """
        Runs runtime tranfer funcs
        """
        for _callable in AFT_UPD:
            _callable()

init 10 python:
    fae_data.runInitTransfer()

init python in fae_data:
    DID_DO_UPD = False

    @transfer(["0.0.0"], "0.0.1", transfer=TransRun.INIT)
    def to_0_0_1():
        pass