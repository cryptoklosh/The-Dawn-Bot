from prometheus_client import Gauge, Info, Counter

dawn_info = Info("dawn", "Info about dawn-validator node")
mined_coins_gauge = Gauge('mined_coins', 'Number of mined coins', ['account'])
dawn_requests_total_counter = Counter('dawn_requests_total', 'Succeeded API mining requests', ['account', 'status'])