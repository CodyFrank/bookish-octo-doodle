import threading
import time
from typing import Dict, Any


class RateLimiter:
    def __init__(self, rate: float, capacity: float):
        if rate <= 0 or capacity <= 0:
            raise ValueError("Rate and Capacity must both be positive")

        self.rate = rate
        self.capacity = capacity
        self.clients: Dict[str, Dict[str, Any]] = {}
        self.lock = threading.Lock()

    def _get_or_create_client_state(self, client_id):
        if client_id not in self.clients:
            self.clients[client_id] = {
                "tokens": self.capacity,
                "last_updated": time.time(),
            }
        return self.clients[client_id]

    def is_allowed(self, client_id: str) -> bool:
        with self.lock:
            now = time.monotonic()
            client_state = self.clients.setdefault(
                client_id, {"tokens": self.capacity, "last_updated": now}
            )
            elapsed = now - client_state["last_updated"]
            client_state["tokens"] = min(
                self.capacity, client_state["tokens"] + elapsed * self.rate
            )
            client_state["last_updated"] = now

            if client_state["tokens"] >= 1.0 - 1e-9:
                client_state["tokens"] -= 1.0
                return True
            return False
