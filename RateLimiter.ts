class RateLimiter {
	private rate: number;
	private capacity: number;
	tokens: object;
	constructor(rate: number, capacity: number) {
		this.rate = rate;
		this.capacity = capacity;
		this.tokens = {}
	}

	function isAllowed(clinet_id: str) -> boolean {
	// need to lock threads
	// fill token bucket based on rate
	// check if there are available tokens
	// if yes remove token and return true
	// else return false

};

}
