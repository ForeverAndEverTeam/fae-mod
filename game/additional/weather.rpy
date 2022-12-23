# Images courtesy of JN Team

# Sky types
image sky day overcast = "mod_assets/backgrounds/atmosphere/sky/sky_day_overcast.png"
image sky day rain = "mod_assets/backgrounds/atmosphere/sky/sky_day_rain.png"
image sky day sunny = "mod_assets/backgrounds/atmosphere/sky/sky_day_sunny.png"
image sky day thunder = "mod_assets/backgrounds/atmosphere/sky/sky_day_thunder.png"
image sky day snow = "mod_assets/backgrounds/atmosphere/sky/sky_day_snow.png"

image sky night overcast = "mod_assets/backgrounds/atmosphere/sky/sky_night_overcast.png"
image sky night rain = "mod_assets/backgrounds/atmosphere/sky/sky_night_rain.png"
image sky night sunny = "mod_assets/backgrounds/atmosphere/sky/sky_night_sunny.png"
image sky night thunder = "mod_assets/backgrounds/atmosphere/sky/sky_night_thunder.png"

# Dimming effects; used with various weather conditions
image dim light = "mod_assets/backgrounds/atmosphere/dim/dim_light.png"
image dim medium = "mod_assets/backgrounds/atmosphere/dim/dim_medium.png"
image dim heavy = "mod_assets/backgrounds/atmosphere/dim/dim_heavy.png"

# Glitch effects
image glitch_garbled_a = "mod_assets/backgrounds/etc/glitch_garbled_a.png"
image glitch_garbled_b = "mod_assets/backgrounds/etc/glitch_garbled_b.png"
image glitch_garbled_c = "mod_assets/backgrounds/etc/glitch_garbled_c.png"
image glitch_garbled_n = "mod_assets/backgrounds/etc/youdidthis.png"
image glitch_garbled_red = "mod_assets/backgrounds/etc/glitch_garbled_red.png"

image sky glitch_fuzzy:
    "mod_assets/backgrounds/etc/glitch_fuzzy_a.png"
    pause 0.25
    "mod_assets/backgrounds/etc/glitch_fuzzy_b.png"
    pause 0.25
    "mod_assets/backgrounds/etc/glitch_fuzzy_c.png"
    pause 0.25
    repeat

# Clouds
image clouds day light:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_day_light.png"
    cloud_scroll

image clouds day heavy:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_day_heavy.png"
    cloud_scroll

image clouds day thunder:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_day_thunder.png"
    cloud_scroll

image clouds night light:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_night_light.png"
    cloud_scroll

image clouds night heavy:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_night_heavy.png"
    cloud_scroll

# Particles
# Credit for rain, snow graphics goes to Monika After Story @ https://github.com/Monika-After-Story/MonikaModDev
# Thanks for allowing us to use these!
image particles rain:
    "mod_assets/backgrounds/atmosphere/particles/rain.png"
    rain_scroll

image particles snow:
    "mod_assets/backgrounds/atmosphere/particles/snow.png"
    snow_scroll

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

image particles snow:
    "mod_assets/images/atmosphere/particles/snow.png"
    snow_scroll

image particles rain:
    "mod_assets/images/atmosphere/particles/rain.png"
    rain_scroll

transform snow_scroll:
    subpixel True
    right
    parallel:
        xoffset 0 yoffset 0
        linear 60 xoffset 220  yoffset 1280
        repeat

transform rain_scroll:
    subpixel True
    right
    parallel:
        xoffset 0 yoffset 0
        linear 2 xoffset 220  yoffset 1280
        repeat

transform cloud_scroll:
    # Clouds shift from left to right
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 30 xoffset -1280
        repeat

transform sky_scroll:
    # Clouds shift from left to right
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 60 xoffset -1280
        repeat

init 0 python in fae_sky:
    from Enum import Enum
    import os
    import random
    import store
    import store.fae_utilities as fae_utilities
    import store.fae_preferences as fae_preferences

    # Zorder indexes
    # Complete order is:
    # V PROPS
    # V SAYORI
    # V BACKGROUND
    # V DIM
    # SKY
    _DIM_Z_ORDER = 2
    _CLOUDS_Z_ORDER = -1
    _SKY_Z_ORDER = -2

    class FAEWeatherTypes(Enum):

        overcast = 1
        rain = 2
        sunny = 3
        thunder = 4
        glitch = 5
        snow = 6


    class FAEWeather():
        def __init__(
            self,
            weather_type,
            day_sky_image,
            night_sky_image,
            evening_sky_image,
            dim_image=None,
            #day_clouds_image=None,
            #night_clouds_image=None,
            #day_particles_image=None,
            #night_particles_image=None,
            #weather_sfx=None
        ):
            """
            Initializes a new instance of weather.

            FEED:
                day_sky_image = name of image to show for the weather event
                evening_sky_image = name of image to show for evening
                night_sky_image = name of the image to show for evening
                dim_image = name of dimming effect to use
            """

            self.weather_type = weather_type
            self.day_sky_image = day_sky_image
            self.evening_sky_image = evening_sky_image
            self.night_sky_image = night_sky_image
            self.dim_image = dim_image
            #self.day_particles_image = day_particles_image
            #self.night_particles_image = night_particles_image
            #self.weather_sfx = weather_sfx
    """
    WEATHER_OVERCAST = FAEWeather(
        weather_type=FAEWeatherTypes.overcast,
        day_sky_image="sky day overcast",
        night_sky_image="sky night overcast",
        dim_image="dim light",
        #day_clouds_image="clouds day heavy",
        #night_clouds_image="clouds night heavy",
    )

    WEATHER_RAIN = FAEWeather(
        weather_type=FAEWeatherTypes.rain,
        day_sky_image="sky day rain",
        night_sky_image="sky night rain",
        dim_image="dim medium",
        day_clouds_image="clouds day heavy",
        night_clouds_image="clouds night heavy",
        day_particles_image="particles rain",
        night_particles_image="particles rain",
        #weather_sfx="mod_assets/sfx/rain_muffled.ogg"
    )

    WEATHER_THUNDER = FAEWeather(
        weather_type=FAEWeatherTypes.thunder,
        day_sky_image="sky day thunder",
        night_sky_image="sky night thunder",
        dim_image="dim heavy",
        day_clouds_image="clouds day thunder",
        night_clouds_image="clouds night heavy",
        day_particles_image="particles rain",
        night_particles_image="particles rain",
        #weather_sfx="mod_assets/sfx/rain_muffled.ogg"
    )

    WEATHER_SNOW = FAEWeather(
        weather_type=FAEWeatherTypes.snow,
        day_sky_image="sky day snow",
        night_sky_image="sky night overcast",
        dim_image="dim light",
        day_clouds_image="clouds day light",
        night_clouds_image="clouds night light",
        day_particles_image="particles snow",
        night_particles_image="particles snow",
    )

    WEATHER_SUNNY = FAEWeather(
        weather_type=FAEWeatherTypes.sunny,
        day_sky_image="sky day sunny",
        night_sky_image="sky night sunny",
        day_clouds_image="clouds day light",
        night_clouds_image="clouds night light"
    )
    WEATHER_SUNNY1 = FAEWeather(
        weather_type=FAEWeatherTypes.sunny,
        day_sky_image="sky day sunny",
        night_sky_image="sky night sunny",
        day_clouds_image="clouds day light",
        night_clouds_image="clouds night light"
    )

    """
    
    WEATHER_SUNNY = FAEWeather(
        weather_type=FAEWeatherTypes.sunny,
        day_sky_image="sky day sunny",
        evening_sky_image="sky evening sunny",
        night_sky_image="sky night sunny",
        dim_image="dim medium",
    )

    WEATHER_GLITCH = FAEWeather(
        weather_type=FAEWeatherTypes.glitch,
        day_sky_image="space 2",
        evening_sky_image="space 2",
        night_sky_image="space 2",
        
    )

    
  
    current_weather = None

    def reload_sky(with_transition=True):

        """
        Shows the sky based on sunrise/sunset times specified in persistent.
        
        FEED:
            with_transition = If True, will visually fade in the new weather
        """

        form_sky(WEATHER_SUNNY, with_transition=with_transition)

        """

        if store.persistent._fae_weather_setting == int(fae_preferences.weather.FAEWeatherSettings.random):


            form_sky(random.choice([
                WEATHER_OVERCAST,
                WEATHER_RAIN,
                WEATHER_THUNDER,
                WEATHER_SUNNY,
                WEATHER_SUNNY,
                WEATHER_SUNNY,
                WEATHER_SNOW,
                WEATHER_SNOW
            ]),
            with_transition = with_transition)
        
        else:
            form_sky(WEATHER_SUNNY, with_transition=with_transition)
        """

    def form_sky(weather, with_transition=True):

        """
        Shows the specified sky with clouds/dimming effect
        FEED:
            weather = Weather to set
            with_transition = If True, will visually fade in new weather
        """

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