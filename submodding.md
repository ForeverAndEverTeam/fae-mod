# WORKING WITH THE SUBMOD MATRIX

When v0.1: New Beginnings released, it contained the inclusion of a submod system.

Submods are ways for players to add their own content to the mod, without dev review/approval.

Players of MAS will find this system easy to understand, since I've made it as similar as possible for ease of use.

# USING THE SUBMOD SYSTEM

The `submod` system is basically a way to let the game know you're adding extra content.

It **must** be done in an `init -990 python in fae_submod_utilities` block.

If run at another runlevel, dependancies will not be checked.

An example of the beginning of a submod would be the following

```renpy
init -990 python in fae_submod_utilities:
    Submod(
        author="Forever And Ever Team",
        name="Submod example",
        description="An example submod.",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )
```


The above code will import a submod with this information:

- Author: `Forever And Ever Team`
- Name: `Submod example`
- Description: `An example submod.`
- Version: `1.0.0`
- Dependencies: None
- Settings: No settings
- Version Updates: No update scripts

When creating dialogue submods, please try and adhere to the [Coding Style](https://github.com/ForeverAndEverTeam/fae-mod/blob/master/STYLE.md)
