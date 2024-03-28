#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import local


def do_clean(number=0):
    """Delete out-of-date archives.
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    tot_archives = sorted(os.listdir('versions'))
    [tot_archives.pop() for i in range(number)]
    [local("rm versions/{}".format(a)) for a in tot_archives]
