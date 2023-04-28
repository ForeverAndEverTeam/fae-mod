# This determines if the game should use realtime weather
default persistent._fae_weather_setting = int(fae_preferences.weather.FAEWeatherSettings.disabled)

init -1 python in fae_preferences.weather:
    from Enum import Enum
    import store

    class FAEWeatherSettings(Enum):

        disabled = 1
        random = 2

        def __int__(self):
            return self.value