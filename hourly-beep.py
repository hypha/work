import time
import os
import time
import sys


def countdown(t):
    for i in range(t, 0, -1):
        print 'Next alarm will be in %d seconds\r' % i,
        sys.stdout.flush()
        time.sleep(1)


def beep(t):
    while True:
        countdown(t)
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.5, 2000))


beep(3600)

