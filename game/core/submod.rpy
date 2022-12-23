init -999:
    default persistent._fae_submod_vers_data = dict()

init 10 python:
    store.fae_submod_utilities.Submod._checkUpdates()

init -989 python:

    if store.fae_submod_utilities.submod_def:
        fae_submod_utilities.submod_log.info(
            "\nINSTALLED SUBMODS:\n{0}".format(
                ",\n".join(
                    ["    '{0}' v{1}".format(submod.name, submod.version) for submod in store.fae_submod_utilities.submod_def.values()]
                )
            )
        )

    
    store.fae_submod_utilities.Submod._checkDependancies()

init -991 python in fae_submod_utilities:
    import re
    import store

    persistent = store.persistent

    submod_log = store.fae_logging.init_log("submod_log")

    submod_def = dict()

    class SubmodError(Exception):
        def __init__(self, _msg):
            self.msg = _msg
        def __str__(self):
            return self.msg
    
    class Submod(object):

        FB_VERS_STR = "0.0.0"
        AN_REGEXP = re.compile(r'^[ a-zA-Z_\u00a0-\ufffd][ 0-9a-zA-Z_\u00a0-\ufffd]*$')

        def __init__(
            self,
            author,
            name,
            version,
            description=None,
            dependencies={},
            settings_pane=None,
            version_updates={},
            coauthors=[]
        ):
            """
            FEED:
                author: name of author

                name: submod name

                version: submod version

                description: submod description

                dependencies: dict stating needed submod name and version

                settings_pane: string representing the screen for the submod settings

                version_updates: dict of {"old_version_update_label_name": "new_version_update_label_name"}

                coauthors: list/tuple of co-authors of the submod
            """

            if name in submod_def:
                raise SubmodError("A submod with name '{0}' has been installed twice. Please, uninstall the duplicate.".format(name))
            
            if not Submod.AN_REGEXP.match(author):
                raise SubmodError("Author '{0}' is invalid.".format(author))
            if not Submod.AN_REGEXP.match(name):
                raise SubmodError("Name '{0}' is invalid.".format(name))

            self.author = author
            self.name = name
            self.description = description if description is not None else ""
            self.version = version
            self.dependencies = dependencies
            self.settings_pane = settings_pane
            self.version_updates = version_updates
            self.coauthors = tuple(coauthors)

            submod_def[name] = self

            if name not in persistent._fae_submod_vers_data:
                persistent._fae_submod_vers_data[name] = version
            
        def __repr__(self):
            """
            Representation
            """
            return "<Submod: ({0} v{1} by {2})>".format(self.name, self.version, self.author)

        def getVersionNumberList(self):

            return list(map(int, self.version.split('.')))

        def hasUpdated(self):

            old_vers = persistent._fae_submod_vers_data.get(self.name)

            if not old_vers:
                return False

            try:
                old_vers = list(map(int, old_vers.split('.')))
            
            except:
                persistent._fae_submod_vers_data[self.name] = Submod.FB_VERS_STR
            
                return False
            return self.checkVersions(old_vers) > 0

        def updateFrom(self, version):

            while version in self.version_updates:
                updateTo = self.version_updates[version]
            
                if renpy.has_label(updateTo) and not renpy.seen_label(updateTo):
                    renpy.call_in_new_context(updateTo, updateTo)
                version = self.version_updates[version]
        
        def checkVersions(self, comparative_vers):

            return store.fae_utilities.compareVersionLists(
                self.getVersionNumberList(),
                comparative_vers
            )
            
        @staticmethod
        def _checkUpdates():

            for submod in submod_def.values():
            
                if submod.hasUpdated():
                    submod.updateFrom(
                        "{0}_{1}_v{2}".format(
                            submod.author,
                            submod.name,
                            persistent._fae_submod_vers_data.get(submod.name, Submod.FB_VERS_STR).replace('.', '_')
                        ).lower().replace(' ', '_')
                    )
            
                persistent._fae_submod_vers_data[submod.name] = submod.version
        
        @staticmethod
        def _checkDependancies():

            def parseVersions(version):
                
                return tuple(map(int, version.split('.')))

            for submod in submod_def.values():
                for dependency, minmax_version_tuple in submod.dependencies.items():
                    dependency_submod = Submod._getSubmod(dependency)

                    if dependency_submod is not None:
                        
                        minimum_version, maximum_version = minmax_version_tuple
                        
                        if (
                            minimum_version
                            and dependency_submod.checkVersions(parseVersions(minimum_version)) < 0
                        ):
                            raise SubmodError(
                                "Submod '{0}' is out of date. Version {1} required for {2}. Installed version is {3}".format(
                                    dependency_submod.name, minimum_version, submod.name, dependency_submod.version
                                )
                            )
                        
                        elif (
                            maximum_version
                            and dependency_submod.checkVersions(parseVersions(maximum_version)) > 0
                        ):
                            raise SubmodError(
                                "Version '{0}' of '{1}' is installed and is incompatible with {2}.\nVersion {3} is compatible.".format(
                                    dependency_submod.version, dependency_submod.name, submod.name, maximum_version
                                )
                            )

                    else:
                        raise SubmodError(
                            "Submod '{0}' is not installed and is required for {1}.".format(
                                dependency, submod.name
                            )
                        )
        
        @staticmethod
        def _getSubmod(name):

            return submod_def.get(name)

    def isSubmodInstalled(name, version=None):

        submod = Submod._getSubmod(name)

        if submod and version:
            return submod.checkVersions(version) >= 0
        return bool(submod)


init -980 python in fae_submod_utilities:

    import inspect
    import store

    current_label = None
    last_label = None

    function_plugins = dict()

    DEF_URGENCY = 0

    JUMP_CALL_URGENCY = 999

    URGENCY_SORT_KEY = lambda x: x[1][2]

    def functionplugin(_label, _args=[], auto_error_handling=True, urgency=0):

        def wrap(_function):
            registerFunction(
                _label,
                _function,
                _args,
                auto_error_handling,
                urgency
            )
            return _function
        return wrap
    

    def getAndRunFunctions(key=None):

        global function_plugins

        
        if not key:
            key = inspect.stack()[1][3]

        func_dict = function_plugins.get(key)

        if not func_dict:
            return

        
        sorted_plugins = __urgencySort(key)
        for _action, data_tuple in sorted_plugins:
            if data_tuple[1]:
                try:
                    store.__run(_action, getArgs(key, _action))
                except Exception as ex:
                    store.fae_utilities.fae_log.error("function {0} failed because {1}".format(_action.__name__, ex))

            else:
                store.__run(_action, getArgs(key, _action))

    def registerFunction(key, _function, args=[], auto_error_handling=True, urgency=DEF_URGENCY):

        global function_plugins

        if not callable(_function):
            store.fae_utilities.fae_log.error("{0} is not callable".format(_function.__name__))
            return False

        elif len(args) > len(inspect.getargspec(_function).args):
            store.fae_utilities.fae_log.error("Too many args provided for function {0}".format(_function.__name__))
            return False

        key = __getOverrideLabel(key)

        if key not in function_plugins:
            function_plugins[key] = dict()

        elif _function in function_plugins[key]:
            return False

        function_plugins[key][_function] = (args, auto_error_handling, urgency)
        return True

    def getArgs(key, _function):

        global function_plugins

        func_dict = function_plugins.get(key)

        if not func_dict:
            return

        return func_dict.get(_function)[0]

    def setArgs(key, _function, args=[]):

        global function_plugins

        func_dict = function_plugins.get(key)

        if not func_dict:
            return False

        elif _function not in func_dict:
            return False

        elif len(args) > len(inspect.getargspec(_function).args):
            store.fae_utilities.fae_log.error("Too many args provided for function {0}".format(_function.__name__))
            return False

        #Otherwise we can set
        old_values = func_dict[_function]
        func_dict[_function] = (args, old_values[1], old_values[2])
        return True

    def unregisterFunction(key, _function):

        global function_plugins

        func_dict = function_plugins.get(key)


        if not func_dict:
            return False


        elif _function not in func_dict:
            return False

  
        function_plugins[key].pop(_function)
        return True
    
    def __prioritySort(_label):
        
        global function_plugins

        
        func_list = [
            (_function, data_tuple)
            for _function, data_tuple in function_plugins[_label].items()
        ]

        return sorted(func_list, key=URGENCY_SORT_KEY)

    def __getOverrideLabel(_label):

        while renpy.config.label_overrides.get(_label) is not None:
            _label = renpy.config.label_overrides[_label]
        return _label

init -990 python:

    def __run(_function, args):

        return _function(*args)


