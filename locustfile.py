import json
from locust import HttpUser, task, between, constant, tag

#A user class for a steady workload
class PeriodicUser(HttpUser):
    #wait_time sets a delay between requests for each user.
    #Setting a constant time to simulate a predictable workload
    wait_time = constant(1)

    @task
    @tag('periodic')
    def my_periodic_task(self):
        payload = {"number": 10}
        self.client.post("/hello", json=payload)


#A user class for a bursty (sudden spike) workload
class BurstyUser(HttpUser):
    #Setting a very short wait_time to simulate a rapid-fire burst of requests
    wait_time = between(0.01, 0.1)

    @task
    @tag('bursty')
    def my_burst_task(self):
        payload = {"number": 10}
        self.client.post("/hello", json=payload)


#A user class that combines both periodic and bursty behavior
class MixedWorkloadUser(HttpUser):
    #Using a combination of different wait times to simulate irregular patterns
    wait_time = between(0.5, 3.0)
    
    #weight controls how often each task runs
    @task(weight=9)
    def periodic_task(self):
        payload = {"number": 10}
        self.client.post("/hello", json=payload)

    @task(weight=1)
    def burst_task(self):
        payload = {"number": 10}
        self.client.post("/hello", json=payload)