import threading
import time


class RateLimiter:
    def __init__(self, rate, capacity):
        if rate <= 0 or capacity <= 0:
            raise ValueError("Rate and Capacity must both be positive")

        self.rate = rate
        self.capacity = capacity
        self.clients = {}
        self.lock = threading.Lock()
