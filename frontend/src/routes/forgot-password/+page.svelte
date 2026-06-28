<script>
	let email = $state('');
	let error = $state('');
	let sent = $state(false);
	let loading = $state(false);

	async function submit(e) {
		e.preventDefault();
		error = '';
		loading = true;
		try {
			const { api } = await import('$lib/api');
			await api.forgotPassword(email);
			sent = true;
		} catch (err) {
			error = err.message;
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>Forgot Password | Drizle Pay</title>
</svelte:head>

<div class="page">
	<div class="card">
		<a href="/" class="brand">Drizle<span>Pay</span></a>
		{#if sent}
			<span class="icon success">✓</span>
			<h2>Check Your Email</h2>
			<p>If an account with that email exists, we've sent a password reset link.</p>
			<a class="btn primary" href="/login">Back to Login</a>
		{:else}
			<h2>Forgot Password</h2>
			<p class="subtitle">Enter your email and we'll send you a reset link.</p>
			<form onsubmit={submit}>
				{#if error}
					<div class="error">{error}</div>
				{/if}
				<label>
					<span>Email</span>
					<input type="email" bind:value={email} required placeholder="you@company.com" />
				</label>
				<button type="submit" class="btn primary" disabled={loading}>
					{loading ? 'Sending…' : 'Send Reset Link'}
				</button>
			</form>
			<p class="toggle"><a href="/login" class="link">Back to Sign In</a></p>
		{/if}
	</div>
</div>

<style>
	.page { min-height: 100vh; display: grid; place-items: center; background: #f8fafc; padding: 24px; }
	.card { width: 100%; max-width: 420px; padding: 40px 32px; background: #fff; border: 1px solid var(--line); border-radius: 8px; box-shadow: var(--shadow); }
	.brand { display: block; text-align: center; font-weight: 760; font-size: 23px; color: var(--hero-bg); margin-bottom: 28px; }
	.brand span { color: var(--primary); }
	h2 { font-size: 24px; font-weight: 700; color: var(--hero-bg); margin: 0 0 6px; text-align: center; }
	.subtitle { color: var(--muted); font-size: 14px; text-align: center; margin: 0 0 28px; }
	form { display: grid; gap: 16px; }
	label { display: grid; gap: 6px; }
	label span { font-size: 13px; font-weight: 600; color: var(--ink); }
	input { padding: 10px 14px; border: 1px solid var(--line); border-radius: 4px; font-size: 15px; color: var(--ink); background: #fff; outline: none; }
	input:focus { border-color: var(--primary); }
	.btn { display: flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 20px; border-radius: 4px; font-size: 15px; font-weight: 600; cursor: pointer; border: none; transition: all 0.15s; }
	.btn.primary { background: var(--primary); color: #fff; }
	.btn.primary:hover:not(:disabled) { background: var(--primary-dark); }
	.btn:disabled { opacity: 0.6; cursor: not-allowed; }
	.error { padding: 12px 14px; background: #fef2f2; color: #dc2626; border-radius: 4px; font-size: 14px; text-align: center; }
	.toggle { text-align: center; font-size: 14px; color: var(--muted); margin: 20px 0 0; }
	.link { color: var(--primary); font-weight: 600; text-decoration: none; }
	.link:hover { text-decoration: underline; }
	.icon { width: 48px; height: 48px; border-radius: 50%; display: grid; place-items: center; font-size: 24px; font-weight: 700; margin: 0 auto 16px; background: #e6fcf0; color: var(--primary-dark); }
</style>
