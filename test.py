#!/usr/bin/python
import time
import random
import statsd
counter_name = 'my.test.1'
wait_s = 1
while 1:
    c = statsd.StatsClient('localhost', 8125)
    random_count = random.randrange(1, 100)
    print 'Count=(%d)' % random_count
    while random_count > 0:
        c.incr(counter_name, 5)
        random_count -= 1
    time.sleep(wait_s)
