
init -991 python in fae_extras:

    import store

    persistent = store.persistent

    dictionary_submods = dict()

    class Extras(object):

        def __init__(
            self,
            name,
            creator,
            description
        ):

            self.name = name
            self.creator = creator
            self.description = description

            dictionary_submods[name] = self

    
        def __repr__(self):

            return str(self.name, self.creator)

        @staticmethod
        def _findSubmod(name):

            return dictionary_submods.get(name)

    def isInstalled(name):

        extramod = Extras._findSubmod(name)

        return bool(extramod)
    


    





