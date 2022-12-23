default persistent._fae_version = "0.4.0.1"


python early in fae_data:

    from enum import Enum
    import re
    import store
    import store.fae_utilities as fae_utilities

    UPDATE_FUNCTIONS = dict()

    LATE_UPDATES = []

    VER_STR_PARSER = re.compile(r"^(?P<ver>\d+\.\d+\.\d+)(?P<suffix>.*)$")

    class MigrationRuntimes(Enum):

        INIT = 1
        RUNTIME = 2

    
    def transfer(from_versions, to_version, runtime=MigrationRuntimes.INIT):

        def wrap(_function):
            registerUpdateFunction(
                _callable=_function,
                from_versions=from_versions,
                to_version=to_version,
                runtime=runtime
            )
            return _function
        return wrap

    def registerUpdateFunction(_callable, from_versions, to_version, runtime=MigrationRuntimes.INIT):

        for from_version in from_versions:
            if from_version not in UPDATE_FUNCTIONS:
                UPDATE_FUNCTIONS[from_version] = dict()

            UPDATE_FUNCTIONS[from_version][runtime] = (_callable, to_version)
    

    def verStrToVerList(ver_str):

        match = VER_STR_PARSER.match(ver_str)
        if not match:
            raise ValueError("Invalid version string")
        
        ver_list = match.group("ver").split(".")
        return [int(x) for x in ver_list]

    def compareVersions(ver_str1, ver_str2):

        match1 = VER_STR_PARSER.match(ver_str1)
        match2 = VER_STR_PARSER.match(ver_str2)

        if not match1 or not match2:
            raise ValueError("Invalid version string")

        ver1 = verStrToVerList(match1.group("ver"))
        ver2 = verStrToVerList(match2.group("ver"))

        if len(ver1) > len(ver2):
            ver2 += [0] * (len(ver1) - len(ver2))
        elif len(ver1) < len(ver2):
            ver1 += [0] * (len(ver2) - len(ver1))

        #Now directly compare from left to right
        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1

        #If we got here, the versions are equal
        return 0

    def runInitTransfer():

        fae_utilities.log("Begin transfer")

        if store.persistent._fae_version not in UPDATE_FUNCTIONS:
            return

        from_version = store.persistent._fae_version

        while compareVersions(from_version, renpy.config.version) < 0:
            if MigrationRuntimes.RUNTIME in UPDATE_FUNCTIONS[store.persistent._fae_version]:
                LATE_UPDATES.append(UPDATE_FUNCTIONS[store.persistent._fae_version][MigrationRuntimes.RUNTIME])
            
            _callable, from_version = UPDATE_FUNCTIONS[from_version][MigrationRuntimes.INIT]

            _callable()
    
    def runRuntimeTransfer():

        fae_utilities.log("Begin Runtime Transfer")

        for _callable in LATE_UPDATES:
            _callable()
    
init 10 python:
    fae_data.runInitTransfer()


init python in fae_data:

    import store
    import store.fae_utilities as fae_utilities


    @transfer(["0.4.0.1"], "0.1.0", runtime=MigrationRuntimes.INIT)
    def to_0_1_0():

        fae_utilities.log("Begin transfer to 0.1.0")

        store.persistent._regret_db = dict()

        fae_utilities.log("Migrated regret dataabase")

        store.persistent._fae_version = "0.1.0"
        fae_utilities.save_game()
        fae_utilities.log("Transfer complete")
        return