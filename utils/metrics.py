from prometheus_client import Gauge, Info, Counter

dawn_info = Info("dawn", "Info about dawn-validator node")
dawn_account_farming_gauge = Gauge('dawn_account_farming', 'Account farming status', ['account', 'status'])
mined_dawn_gauge = Gauge('mined_dawn', 'Number of mined dawn points', ['account'])
dawn_requests_total_counter = Counter('dawn_requests_total', 'API mining requests', ['account', 'status'])

DAWN_ACCOUNT_SUCCESS = "success"
DAWN_ACCOUNT_UNVERIFIED = "unverified"
DAWN_ACCOUNT_BANNED = "banned"
DAWN_ACCOUNT_UNREGISTERED = "unregistered"
DAWN_ACCOUNT_UNLOGGED = "unlogged"
DAWN_ACCOUNT_STARTED = "started"

def set_dawn_account_farming(account: str, status: str):
    reset_dawn_account_farming(account)
    dawn_account_farming_gauge.labels(account=account, status=status).set(1)

def reset_dawn_account_farming(account: str):
    dawn_account_farming_gauge.labels(account=account, status=DAWN_ACCOUNT_SUCCESS).set(0)
    dawn_account_farming_gauge.labels(account=account, status=DAWN_ACCOUNT_UNVERIFIED).set(0)
    dawn_account_farming_gauge.labels(account=account, status=DAWN_ACCOUNT_BANNED).set(0)
    dawn_account_farming_gauge.labels(account=account, status=DAWN_ACCOUNT_UNREGISTERED).set(0)
    dawn_account_farming_gauge.labels(account=account, status=DAWN_ACCOUNT_UNLOGGED).set(0)
    dawn_account_farming_gauge.labels(account=account, status=DAWN_ACCOUNT_STARTED).set(0)