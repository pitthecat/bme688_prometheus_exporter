import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
import bme_get_data

class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        values = bme_get_data.get_data()
        print(values)
        t = GaugeMetricFamily("temperature", 'Help text', labels=['bme688'])
        t.add_metric(["temperature"], values[0])
        yield t

        p = CounterMetricFamily("pressure", 'Help text', labels=['bme688'])
        p.add_metric(["pressure"], values[1])
        yield p

        h = CounterMetricFamily("humidity", 'Help text', labels=['bme688'])
        h.add_metric(["humidity"], values[2])
        yield h
            
if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)