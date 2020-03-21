import time
import os


def make_dir(name):
    if not os.path.isdir(name):
        os.mkdir(name)

dirname=time.strftime('%b%d', time.localtime())
make_dir(dirname)
