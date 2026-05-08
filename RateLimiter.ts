interface ClientState {
	tokens: number;
	lastUpdated: number;
};
interface Tokens {
	clientId: ClientState;
};

class RateLimiter {
	private readonly rate: number;
	private readonly capacity: number;
	private tokens: Tokens;
	constructor(rate: number, capacity: number) {
		this.rate = rate;
		this.capacity = capacity;
		this.tokens = {}
	};

	private _getOrCreateClientState(clientId: string, time: number): ClientState {
		let value = this.tokens.get()
		if (this.tokens.clientId) {
			k
		}

		if (this.tokens[clientId])
			return clientState
	};

	isAllowed(clinet_id: string): boolean {
		// need to lock threads
		// get current time
		const now = Date.now();
		// get client state
		let clientState = this._getOrCreateClientState(clinet_id, now);
		// get elapesed time
		const elapsed = now - clientState.last_updated;
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
