import time
from locust import HttpUser, task, between
import random
from names import NAMES

class HelloWorldUser(HttpUser):
    wait_time = between(0.1, 0.5)
    @task(12)
    def checkhome(self):
        self.client.get("/")
        sleep_time = random.normalvariate(mu=0.2, sigma=0.04)
        if sleep_time < 0.02:
            sleep_time = 0.02
        time.sleep(sleep_time)

    @task(12)
    def checkhealth(self):
        self.client.get("/health")
        sleep_time = random.normalvariate(mu=0.2, sigma=0.04)
        if sleep_time < 0.02:
            sleep_time = 0.02
        time.sleep(sleep_time)

    @task(1)
    def test_error500(self):
        self.client.get("/error500")
        sleep_time = random.normalvariate(mu=0.2, sigma=0.04)
        if sleep_time < 0.02:
            sleep_time = 0.02
        time.sleep(sleep_time)
        

