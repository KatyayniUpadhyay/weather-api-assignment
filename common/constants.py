class Constants:
    WEATHER_API_URL = ''
    WEATHER_API_KEY = ''

    @staticmethod
    def readEnv(config):
        Constants.WEATHER_API_URL = config['WEATHER']['API_URL']
        Constants.WEATHER_API_KEY = config['WEATHER']['API_KEY']