import { auth } from '$lib/stores/auth';

const BASE = '/api/v1';

async function request(path, options = {}) {
	const headers = { ...options.headers };
	if (!(options.body instanceof FormData)) {
		headers['Content-Type'] = 'application/json';
	}
	if (auth.token) {
		headers['Authorization'] = `Bearer ${auth.token}`;
	}
	const res = await fetch(`${BASE}${path}`, { ...options, headers });
	if (res.status === 401) {
		auth.logout();
		window.location.href = '/login';
		throw new Error('Unauthorized');
	}
	if (!res.ok) {
		const err = await res.json().catch(() => ({}));
		throw new Error(err.detail || 'Request failed');
	}
	return res.json();
}

export const api = {
	login: (email, password) =>
		request('/auth/login', { method: 'POST', body: JSON.stringify({ email, password }) }),

	register: (data) =>
		request('/auth/register', { method: 'POST', body: JSON.stringify(data) }),

	verifyEmail: (token) =>
		request(`/auth/verify-email?token=${encodeURIComponent(token)}`, { method: 'POST' }),

	forgotPassword: (email) =>
		request('/auth/forgot-password', { method: 'POST', body: JSON.stringify({ email }) }),

	resetPassword: (token, new_password) =>
		request('/auth/reset-password', { method: 'POST', body: JSON.stringify({ token, new_password }) }),

	getMe: () => request('/me'),

	updateMe: (data) =>
		request('/me', { method: 'PUT', body: JSON.stringify(data) }),

	changePassword: (current_password, new_password) =>
		request('/auth/change-password', { method: 'PUT', body: JSON.stringify({ current_password, new_password }) }),

	getApiKeys: () => request('/me/api-keys'),

	rotateApiKeys: () =>
		request('/auth/rotate-api-keys', { method: 'POST' }),

	// Dashboard
	getDashboardMetrics: (start_date, end_date) =>
		request(`/dashboard/metrics${start_date ? `?start_date=${start_date}&end_date=${end_date}` : ''}`),

	getDashboardCharts: (start_date, end_date) =>
		request(`/dashboard/charts${start_date ? `?start_date=${start_date}&end_date=${end_date}` : ''}`),

	getRecentPayouts: (limit = 5) =>
		request(`/payouts/recent?limit=${limit}`),

	// Transactions
	getTransactions: (page = 1, limit = 20, params = {}) => {
		const q = new URLSearchParams({ page, limit, ...params });
		return request(`/transactions?${q}`);
	},

	// Payouts
	getPayouts: (params = {}) => {
		const q = new URLSearchParams({ page: params.page || 1, limit: params.limit || 20 });
		if (params.status_filter) q.set('status_filter', params.status_filter);
		if (params.start_date) q.set('start_date', params.start_date);
		if (params.end_date) q.set('end_date', params.end_date);
		if (params.search) q.set('search', params.search);
		return request(`/payouts?${q}`);
	},

	// Pay by Link
	getPayLinks: (page = 1, limit = 20, is_static, is_recurring) => {
		const q = new URLSearchParams({ page, limit });
		if (is_static) q.set('is_static', 'true');
		if (is_recurring) q.set('is_recurring', 'true');
		return request(`/pay-links?${q}`);
	},

	createPayLink: (data) =>
		request('/pay-links', { method: 'POST', body: JSON.stringify(data) }),

	getPayLinkStats: () => request('/pay-links/stats'),

	// Team / User Management
	getTeam: () => request('/team'),

	inviteTeamMember: (email, role = 'member') =>
		request('/team/invite', { method: 'POST', body: JSON.stringify({ email, role }) }),

	removeTeamMember: (memberId) =>
		request(`/team/${memberId}`, { method: 'DELETE' }),

	// Reports
	getTaxInvoices: (page = 1, limit = 20) =>
		request(`/reports/tax-invoices?page=${page}&limit=${limit}`),

	getMonthlyStatements: (page = 1, limit = 20) =>
		request(`/reports/monthly-statements?page=${page}&limit=${limit}`),

	// Contact
	contact: (data) =>
		request('/contact', { method: 'POST', body: JSON.stringify(data) }),

	// Support
	getSupportTickets: () => request('/support/tickets'),

	createSupportTicket: (data) =>
		request('/support/tickets', { method: 'POST', body: JSON.stringify(data) }),

	submitPublicTicket: (data) =>
		request('/support/tickets/public', { method: 'POST', body: JSON.stringify(data) }),

	// Onboarding
	getOnboardingData: () => request('/onboarding/data'),

	saveOnboardingSection: (section, data) =>
		request('/onboarding/data', { method: 'PUT', body: JSON.stringify({ section, data }) }),

	uploadOnboardingDocument: (file, docType) => {
		const formData = new FormData();
		formData.append('file', file);
		formData.append('doc_type', docType);
		return request('/onboarding/upload-document', { method: 'POST', body: formData });
	},

	submitOnboarding: () =>
		request('/onboarding/submit', { method: 'POST' }),

	toggleTestMode: () =>
		request('/onboarding/test-mode', { method: 'POST' }),
};
