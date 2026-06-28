<script>
	import { onMount } from 'svelte';

	let token = $state('');
	let password = $state('');
	let confirm = $state('');
	let error = $state('');
	let done = $state(false);
	let loading = $state(false);

	onMount(() => {
		const params = new URLSearchParams(location.search);
		token = params.get('token') || '';
	});

	async function submit(e) {
		e.preventDefault();
		error = '';
		if (password !== confirm) {
			error = 'Passwords do not match.';
			return;
		}
		if (password.length < 6) {
			error = 'Password must be at least 6 characters.';
			return;
		}
		loading = true;
		try {
			const { api } = await import('$lib/api');
			await api.resetPassword(token, password);
			done = true;
		} catch (err) {
			error = err.message;
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>Reset Password | DrizlePay</title>
</svelte:head>

<div class="page">
	<div class="card">
		<a href="/" class="brand"><svg viewBox="0 0 120 130" width="24" height="26" fill="none" aria-hidden="true"><path d="M25,15 L50,15 L30,105 L5,105 Z" fill="#06162c"/><path d="M57,15 L82,15 L62,105 L37,105 Z" fill="#06162c" opacity="0.85"/><path d="M89,15 L120,55 L79,105 L65,105 L85,55 L64,15 Z" fill="#02c366"/></svg> Drizle<span>Pay</span></a>
		{#if done}
			<span class="icon success">✓</span>
			<h2>Password Changed</h2>
			<p>Your password has been reset successfully.</p>
			<a class="btn primary" href="/login">Sign In</a>
		{:else if !token}
			<span class="icon error">✗</span>
			<h2>Invalid Link</h2>
			<p>No reset token provided. Check your email for the full reset link.</p>
			<a class="btn primary" href="/forgot-password">Request New Link</a>
		{:else}
			<h2>Reset Password</h2>
			<p class="subtitle">Enter your new password.</p>
			<form onsubmit={submit}>
				{#if error}
					<div class="error">{error}</div>
				{/if}
				<label>
					<span>New Password</span>
					<input type="password" bind:value={password} required minlength={6} placeholder="••••••••" />
				</label>
				<label>
					<span>Confirm Password</span>
					<input type="password" bind:value={confirm} required placeholder="••••••••" />
				</label>
				<button type="submit" class="btn primary" disabled={loading}>
					{loading ? 'Resetting…' : 'Reset Password'}
				</button>
			</form>
		{/if}
	</div>
</div>

<style>
	.page { min-height: 100vh; display: grid; place-items: center; background: #f8fafc; padding: 24px; }
	.card { width: 100%; max-width: 420px; padding: 40px 32px; background: #fff; border: 1px solid var(--line); border-radius: 8px; box-shadow: var(--shadow); text-align: center; }
	.brand { display: block; text-align: center; font-weight: 760; font-size: 23px; color: var(--hero-bg); margin-bottom: 28px; }
	.brand span { color: var(--primary); }
	h2 { font-size: 24px; font-weight: 700; color: var(--hero-bg); margin: 0 0 6px; }
	.subtitle { color: var(--muted); font-size: 14px; margin: 0 0 28px; }
	form { display: grid; gap: 16px; text-align: left; }
	label { display: grid; gap: 6px; }
	label span { font-size: 13px; font-weight: 600; color: var(--ink); }
	input { padding: 10px 14px; border: 1px solid var(--line); border-radius: 4px; font-size: 15px; color: var(--ink); background: #fff; outline: none; }
	input:focus { border-color: var(--primary); }
	.btn { display: flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 20px; border-radius: 4px; font-size: 15px; font-weight: 600; cursor: pointer; border: none; transition: all 0.15s; width: 100%; }
	.btn.primary { background: var(--primary); color: #fff; }
	.btn.primary:hover:not(:disabled) { background: var(--primary-dark); }
	.btn:disabled { opacity: 0.6; cursor: not-allowed; }
	.error { padding: 12px 14px; background: #fef2f2; color: #dc2626; border-radius: 4px; font-size: 14px; text-align: center; }
	.icon { width: 48px; height: 48px; border-radius: 50%; display: grid; place-items: center; font-size: 24px; font-weight: 700; margin: 0 auto 16px; }
	.icon.success { background: #e6fcf0; color: var(--primary-dark); }
	.icon.error { background: #fef2f2; color: #dc2626; }
</style>
