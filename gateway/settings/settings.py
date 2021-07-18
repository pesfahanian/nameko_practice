VERSION = '1'

BASE_ENDPOINT = f'/api/v{VERSION}'

TITLE = 'Microservice'

RABBIT_USER: str = 'guest'
RABBIT_PASSWORD: str = 'guest'
RABBIT_HOST: str = 'localhost'
RABBIT_PORT: int = 5672

AMQP_URI = f'amqp://{RABBIT_USER}:{RABBIT_PASSWORD}@{RABBIT_HOST}:{RABBIT_PORT}/'

CLUSTER_RPC = {'AMQP_URI': AMQP_URI}
