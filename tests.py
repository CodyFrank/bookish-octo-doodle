def simulate_client(client_id, limiter, requests_to_make):
    """Helper function to simulate a client making requests"""
    print(f"Client {client_id} attempting {requests_to_make} requests...")

    for i in range(requests_to_make):
        allowed = limiter.is_allowed(client_id)
        status = "✅ ALLOWED" if allowed else "❌ BLOCKED"

        # Optional: Print quota info for insight
        # info = limiter.get_quota_info(client_id)
        # print(f"Req {i+1}: {status} | Remaining: {info['remaining']}")

        print(f"Req {i + 1}: {status}")
        time.sleep(0.2)  # Small delay to see the pattern clearly


if __name__ == "__main__":
    # CONFIGURATION:
    # Allow bursts of up to 5 requests (capacity)
    # Refill 1 token every 1 second (rate)
    rate_limiter = SmartRateLimiter(rate=1.0, capacity=5)

    print("--- SCENARIO 1: Burst Traffic ---")
    # Client A tries to make 7 requests quickly
    simulate_client("Client_A", rate_limiter, 7)

    print("\n--- SCENARIO 2: Waiting (Refill) ---")
    # Wait 3 seconds to let the bucket refill
    print("Waiting 3 seconds for tokens to refill...")
    time.sleep(3)

    print("Attempting 3 more requests after waiting:")
    simulate_client("Client_A", rate_limiter, 3)

    print("\n--- SCENARIO 3: Concurrent Access (Threading) ---")
    # Create a new limiter for this test
    busy_limiter = SmartRateLimiter(rate=0.5, capacity=2)  # Slow refill, small capacity

    def concurrent_request():
        result = (
            "ALLOWED" if busy_limiter.is_allowed("Concurrent_Client") else "BLOCKED"
        )
        print(f"Thread Request: {result}")

    # Create 4 threads trying to access the limit simultaneously
    threads = []
    for _ in range(4):
        t = threading.Thread(target=concurrent_request)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n(Expected: Only 2 ALLOWED, 2 BLOCKED due to capacity=2)")
