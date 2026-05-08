class RateLimiter {
	private rate: number;
	private capacity: number;
	tokens: object;
	constructor(rate: number, capacity: number) {
		this.rate = rate;
		this.capacity = capacity;
		this.tokens = {}
	}

	_get_or_create_client_state(clinet_id: string, time: number): object {
		return {}
	}

	isAllowed(clinet_id: string): boolean {
		// need to lock threads
		// get current time
		// get client state
		// get elapesed time
		// calculate tokens based on smallest of capacity or state.tokens + elapsed + rate
		// store updated token value
		//
		//if tokens available 
		//	reduce token count
		//	return true
		//
		//if tokens unavailable
		//	return false
		return false

	};

}
