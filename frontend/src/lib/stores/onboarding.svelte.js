import { writable, derived } from 'svelte/store';
import { api } from '$lib/api';

export const data = writable({});
export const loading = writable(true);
export const saving = writable(false);
export const error = writable(null);
export const submitError = writable(null);
export const documents = writable([]);
export const onboardingStatus = writable('not_started');

let fetched = false;

export async function load(force = false) {
	if (fetched && !force) return;
	loading.set(true);
	error.set(null);
	data.set({});
	documents.set([]);
	try {
		const res = await api.getOnboardingData();
		data.set(res.data || {});
		documents.set(res.kyc_documents || []);
		onboardingStatus.set(res.onboarding_status || 'not_started');
		fetched = true;
	} catch (e) {
		error.set(e.message);
	} finally {
		loading.set(false);
	}
}

export async function saveSection(section, sectionData) {
	saving.set(true);
	error.set(null);
	try {
		const res = await api.saveOnboardingSection(section, sectionData);
		if (res.onboarding_status) onboardingStatus.set(res.onboarding_status);
		data.update(d => ({ ...d, [section]: sectionData }));
		return true;
	} catch (e) {
		error.set(e.message);
		return false;
	} finally {
		saving.set(false);
	}
}

export async function uploadDocument(file, docType) {
	error.set(null);
	try {
		const res = await api.uploadOnboardingDocument(file, docType);
		if (res.onboarding_status) onboardingStatus.set(res.onboarding_status);
		if (res.document) documents.update(d => [...d, res.document]);
		// Reload data from backend to pick up merged OCR
		const fresh = await api.getOnboardingData();
		data.set(fresh.data || {});
		return res;
	} catch (e) {
		error.set(e.message);
		return null;
	}
}

export async function submit() {
	submitError.set(null);
	try {
		const res = await api.submitOnboarding();
		if (res.onboarding_status) onboardingStatus.set(res.onboarding_status);
		return true;
	} catch (e) {
		submitError.set(e.message);
		return false;
	}
}

export function resetCache() {
	fetched = false;
}

export function clearErrors() {
	error.set(null);
	submitError.set(null);
}
