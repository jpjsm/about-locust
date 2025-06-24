import time
from locust import HttpUser, task, between
import random
from names import NAMES

class HelloWorldUser(HttpUser):
    wait_time = between(0.2, 0.8)
    @task(10)
    def checkhome(self):
        self.client.get("/")
        self.client.get("/health")
        time.sleep(0.25)

    @task(1)
    def icecreams(self):
        self.client.get("/icecream")
        sleep_time = random.normalvariate(mu=0.5, sigma=0.08)
        if sleep_time < 0.02:
            sleep_time = 0.02
        time.sleep(sleep_time)

    @task(89)
    def selected_icecreams(self):
        ids = []
        for _ in range(random.randint(1,10)):
            ids.append(random.randint(1,2500))

        names = random.choices(NAMES, k=random.randint(1,10))
        args=""
        for _id in ids:
            args += f"&id={_id}"
        
        for _name in names:
            args += f"&name={_name}"

        self.client.get(f"/icecream?{args}", name='selected_icecreams')
        sleep_time = random.normalvariate(mu=0.5, sigma=0.08)
        if sleep_time < 0.02:
            sleep_time = 0.02
        time.sleep(sleep_time)
        

