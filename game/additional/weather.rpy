
# Dimming effects
image dim light = "mod_assets/images/atmosphere/dim/dim_light.png"
image dim medium = "mod_assets/images/atmosphere/dim/dim_medium.png"
image dim heavy = "mod_assets/images/atmosphere/dim/dim_heavy.png"

image space 1:
    "images/cg/monika/mask.png"
    sky_scroll
image space 2:
    "images/cg/monika/mask_2.png"
    sky_scroll
image space 3:
    "images/cg/monika/mask_3.png"
    sky_scroll

#SKY FILES

image sky day sunny:
    "mod_assets/masks/sky_day.png"
    sky_scroll

image sky evening sunny:
    "mod_assets/masks/sky_sunset.png"
    sky_scroll

image sky night sunny:
    "mod_assets/masks/sky_night.png"
    sky_scroll

# Transform
transform sky_scroll:
    # Clouds shift from left to right
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 30 xoffset -1280
        repeat

init 0 python in fae_sky:
    from Enum import Enum
    import os
    import random
    import re
    import requests
    import store
    import store.fae_utilities as fae_utilities

    # Zorder indexes
    # Complete order is:
    # V PROPS
    # V SAYORI
    # V BACKGROUND
    _DIM_Z_ORDER = 2
    _CLOUDS_Z_ORDER = -1
    _SKY_Z_ORDER = -2



    class FAEWeather():
        def __init__(
            self,
            day_sky_image,
            evening_sky_image,
            night_sky_image,
            dim_image=None,
        ):

            self.day_sky_image = day_sky_image
            self.evening_sky_image = evening_sky_image
            self.night_sky_image = night_sky_image
            self.dim_image = dim_image


    
    WEATHER_SUNNY = FAEWeather(
        day_sky_image="sky day sunny",
        evening_sky_image="sky evening sunny",
        night_sky_image="sky night sunny",
        dim_image="dim medium",
    )

    WEATHER_GLITCH = FAEWeather(
        day_sky_image="space 2",
        evening_sky_image="space 2",
        night_sky_image="space 2"
    )

    current_weather = None

    def reload_sky(with_transition=True):

        form_sky(WEATHER_SUNNY, with_transition=with_transition)
    

    def form_sky(weather, with_transition=True):

        if store.fae_is_day():
            sky_to_show = weather.day_sky_image
        elif store.fae_is_evening():
            sky_to_show = weather.evening_sky_image
        
        else:
            sky_to_show = weather.night_sky_image
        
        renpy.show(name=sky_to_show, zorder=_SKY_Z_ORDER)
        if with_transition:
            renpy.with_statement(trans=store.weather_change_transition)
        
        if weather.dim_image:
            renpy.show(name=weather.dim_image, zorder=_DIM_Z_ORDER)
            if with_transition:
                renpy.with_statement(trans=store.dim_change_transition)
        
        else:
            renpy.hide("dim")
        

        #sky_to_show = weather.day_sky_image if store.fae_is_day() elif store.fae_is_evening() else weather.night_sky_image
define weather_change_transition = Dissolve(0.75)
define dim_change_transition = Dissolve(0.25)
