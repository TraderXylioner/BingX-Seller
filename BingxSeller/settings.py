import environs

env = environs.Env()
env.read_env('.env')


class API:
    KEY = env('KEY')
    SECRET = env('SECRET')


SYMBOL = 'BTC-USDT'
