from prometheus_client import Gauge, Info, Counter

dawn_info = Info("dawn", "Info about dawn-validator node")
dawn_account_farming_gauge = Gauge('dawn_account_farming', 'Is account farming', ['account', 'error_log'])
mined_dawn_gauge = Gauge('mined_dawn', 'Number of mined dawn points', ['account'])
dawn_requests_total_counter = Counter('dawn_requests_total', 'API mining requests', ['account', 'status'])