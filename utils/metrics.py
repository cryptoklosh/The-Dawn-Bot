from prometheus_client import Gauge, Info, Counter

dawn_info = Info("dawn", "Info about dawn-validator node")
mined_dawn_gauge = Gauge('mined_dawn', 'Number of mined dawn points', ['account'])
dawn_requests_total_counter = Counter('dawn_requests_total', 'API mining requests', ['account', 'status'])