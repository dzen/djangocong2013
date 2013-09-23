import json
import time
import factory
import redis
import random


class DataFactory(factory.DictFactory):
    state = factory.Iterator([0, 1])
    module = factory.Sequence(lambda _: round(random.uniform(6, 8), 2))
    heater1 = factory.Sequence(lambda _: round(random.uniform(6, 8), 2))
    heater2 = factory.Sequence(lambda _: round(random.uniform(6, 8), 2))
    tcrimp1 = factory.Sequence(lambda _: round(random.uniform(6, 8), 2))
    tcrimp2 = factory.Sequence(lambda _: round(random.uniform(6, 8), 2))


client = redis.StrictRedis()

while True:
    client.publish('channel', json.dumps(DataFactory()))
    time.sleep(2)
