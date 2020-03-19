import datetime
import time
now = lambda: datetime.datetime.now().timestamp()
ts_start = now()
while True:
    print(now()-ts_start)
    time.sleep(1)
