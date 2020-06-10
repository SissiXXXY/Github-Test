from multiprocessing import process
import os


def run_proc(name):
    print('run child process %s (%s)...' % (name, os.getpid()))
