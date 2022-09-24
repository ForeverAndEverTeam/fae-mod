init python:

    def removeTopicID(topicID):

        if renpy.seen_label(topicID):
            persistent._seen_ever.pop(topicID)
    

    def fae_eraseTopic(topicID, per_eventDB=persistent._chat_db):

        if topicID in per_eventDB:
            per_eventDB.pop(topicID)
    
    def fae_transferTopicSeen(old_topicID, new_topicID):

        if old_topicID in persistent._seen_ever:
            persistent._seen_ever.pop(old_topicID)
            persistent._seen_ever[new_topicID] = True

        
    def adjustTopicIDs(changedIDs, updating_persistent=persistent):

        for oldTopic in changedIDs:
            if updating_persistent._seen_ever.pop(oldTopic,False):
                updating_persistent._seen_ever[changedIDs[oldTopic]] = True
        
        return updating_persistent

    def updateTopicIDs(version_number, updating_persistent=persistent):

        if version_number in updates.topics:
            changedIDs = updates.topic[version_number]

            if changedIDs is not None:
                adjustTopicIDs(changedIDs, updating_persistent)
        
        return updating_persistent

    def updateGameFrom(startVers):
        """
        Updates the game, starting at the given start version

        IN:
            startVers - the version number in the parsed format ('v#####')

        ASSUMES:
            updates.version_updates
        """

        while startVers in updates.version_updates:

            updateTo = updates.version_updates[startVers]

            # we should only call update labels that we have
            if renpy.has_label(updateTo) and not renpy.seen_label(updateTo):
                renpy.call_in_new_context(updateTo, updateTo)
            startVers = updates.version_updates[startVers]

    def safeDel(varname):
        """
        Safely deletes variables from persistent

        IN:
            varname - name of the variable to delete from persistent as string

        NOTE: THIS SHOULD BE USED IN PLACE OF THE DEFAULT `del` KEYWORD WHEN DELETING VARIABLES FROM THE PERSISTENT
        """
        if varname in persistent.__dict__:
            persistent.__dict__.pop(varname)




init 10 python:

    if persistent.version_number is None:

        persistent.version_number = config.version

        fae_versions.clear()
    
    elif persistent.version_number != config.version:

        t_version = persistent.version_number
        if "-" in t_version:
            t_version = t_version[:t_version.index("-")]
        vvvv_version = "v"+"_".join(t_version.split("."))

        updateGameFrom(vvvv_version)

        persistent.version_number = config.version

        fae_versions.clear()

    
    def _fae_resetVersionUpdates():

        late_updates = [
            "v0_0_1"
        ]

        store.fae_versions.init()
        ver_list = list(store.updates.version_updates.keys())

        if "-" in config.version:
            working_version = config.version[:config.version.index("-")]
        else:
            working_version = config.version
        
        ver_list.extend(["fae_lupd_" + x for x in late_updates])
        ver_list.append("v" + "_".join(
            working_version.split(".")
        ))

        for _version in ver_list:
            if _version in persistent._seen_ever:
                persistent._seen_ever.pop(_version)
    

label vgenericupdate(version="v0_0_1"):
label v0_0_2(version=version):
label v0_0_3(version=version):
label v0_0_4(version=version):
label v0_0_5(version=version):
label v0_0_6(version=version):
    python:
        updateTopicIDs(version)
    return

label v0_1_0(version="v0_1_0"):
    python hide:
        pass
    return



label fae_lupd_v0_1_0:
    python:

        pass
    return

