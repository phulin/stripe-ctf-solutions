import os
import time
import string
import random
import pickle

TMPDIR = "/tmp/level05"

class Job(object):
    QUEUE_JOBS = os.path.join(TMPDIR, 'jobs')
    QUEUE_RESULTS = os.path.join(TMPDIR, 'results')

    def __init__(self):
        self.id = self.generate_id()
        self.created = time.time()
        self.started = None
        self.completed = None

    def generate_id(self):
                return ''.join([random.choice(string.ascii_letters) for i in range(20)])

    def job_file(self):
                return os.path.join(self.QUEUE_JOBS, self.id)

    def result_file(self):
                return os.path.join(self.QUEUE_RESULTS, self.id)

    def start(self):
                self.started = time.time()

    def complete(self):
                self.completed = time.time()

print pickle.dumps(Job())
