const TOKEN_KEY = 'drizle_token';
const MERCHANT_KEY = 'drizle_merchant';

let t = $state(null);
let m = $state(null);

function load() {
	try {
		const saved = localStorage.getItem(TOKEN_KEY);
		if (saved) t = saved;
		const savedM = localStorage.getItem(MERCHANT_KEY);
		if (savedM) m = JSON.parse(savedM);
	} catch {}
}

load();

export const auth = {
    get token() { return t; },
    get merchant() { return m; },
    get isAuthenticated() { return t !== null; },
    get needsOnboarding() { return m !== null && !m.active; },
    get onboardingStatus() { return m?.onboarding_status || 'not_started'; },
    login(token, merchant) {
        t = token;
        m = merchant;
        localStorage.setItem(TOKEN_KEY, token);
        localStorage.setItem(MERCHANT_KEY, JSON.stringify(merchant));
    },
    logout() {
        t = null;
        m = null;
        localStorage.removeItem(TOKEN_KEY);
        localStorage.removeItem(MERCHANT_KEY);
    }
};
