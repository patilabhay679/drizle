<script>
	import { onMount } from 'svelte';
	import { api } from '$lib/api';

	let status = $state('verifying');
	let message = $state('');

	onMount(async () => {
		const params = new URLSearchParams(location.search);
		const token = params.get('token');
		if (!token) {
			status = 'error';
			message = 'No verification token provided.';
			return;
		}
		try {
			await api.verifyEmail(token);
			status = 'success';
			message = 'Your email has been verified. You can now log in.';
		} catch (err) {
			status = 'error';
			message = err.message;
		}
	});
</script>

<svelte:head>
	<title>Verify Email | DrizlePay</title>
</svelte:head>

<div class="page">
	<div class="card">
		<a href="/" class="brand"><svg viewBox="0 0 120 130" width="24" height="26" fill="none" aria-hidden="true"><path d="M25,15 L50,15 L30,105 L5,105 Z" fill="#06162c"/><path d="M57,15 L82,15 L62,105 L37,105 Z" fill="#06162c" opacity="0.85"/><path d="M89,15 L120,55 L79,105 L65,105 L85,55 L64,15 Z" fill="#02c366"/></svg> Drizle<span>Pay</span></a>
		{#if status === 'verifying'}
			<div class="spinner"></div>
			<p>Verifying your email…</p>
		{:else if status === 'success'}
			<span class="icon success">✓</span>
			<h2>Email Verified</h2>
			<p>{message}</p>
			<a class="btn primary" href="/login">Sign In</a>
		{:else}
			<span class="icon error">✗</span>
			<h2>Verification Failed</h2>
			<p>{message}</p>
			<a class="btn primary" href="/login">Back to Login</a>
		{/if}
	</div>
</div>

<style>
	.page { min-height: 100vh; display: grid; place-items: center; background: #f8fafc; padding: 24px; }
	.card { width: 100%; max-width: 420px; padding: 40px 32px; background: #fff; border: 1px solid var(--line); border-radius: 8px; box-shadow: var(--shadow); text-align: center; display: grid; gap: 16px; justify-items: center; }
	.brand { font-weight: 760; font-size: 23px; color: var(--hero-bg); margin-bottom: 12px; }
	.brand span { color: var(--primary); }
	h2 { margin: 0; font-size: 22px; font-weight: 700; color: var(--hero-bg); }
	p { color: var(--muted); font-size: 15px; margin: 0; line-height: 1.5; }
	.icon { width: 48px; height: 48px; border-radius: 50%; display: grid; place-items: center; font-size: 24px; font-weight: 700; }
	.icon.success { background: #e6fcf0; color: var(--primary-dark); }
	.icon.error { background: #fef2f2; color: #dc2626; }
	.spinner { width: 32px; height: 32px; border: 3px solid var(--line); border-top-color: var(--primary); border-radius: 50%; animation: spin 0.6s linear infinite; }
	@keyframes spin { to { transform: rotate(360deg); } }
	.btn { display: inline-flex; align-items: center; justify-content: center; min-height: 40px; padding: 0 24px; border-radius: 4px; font-size: 14px; font-weight: 600; cursor: pointer; text-decoration: none; }
	.btn.primary { background: var(--primary); color: #fff; border: none; }
	.btn.primary:hover { background: var(--primary-dark); }
</style>
