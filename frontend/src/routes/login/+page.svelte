<script>
	import { auth } from '$lib/stores/auth';
	import { api } from '$lib/api';
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	let email = $state('');
	let password = $state('');
	let error = $state('');
	let loading = $state(false);
	let name = $state('');
	let company = $state('');
	let showPassword = $state(false);

	let isRegister = $derived(page.url.searchParams.get('register') === 'true');

	onMount(() => {
		if (auth.isAuthenticated) goto('/dashboard');
	});

	function toggleMode() {
		error = '';
		goto(isRegister ? '/login' : '/login?register=true');
	}

	async function submit(e) {
		e.preventDefault();
		error = '';
		loading = true;
		try {
			const res = isRegister
				? await api.register({ email, password, name, company })
				: await api.login(email, password);
			auth.login(res.access_token, res.merchant);
			goto('/dashboard');
		} catch (err) {
			error = err.message;
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>{isRegister ? 'Register' : 'Sign In'} | Drizle Pay</title>
</svelte:head>

<div class="login-page">
	<div class="login-card">
		<a href="/" class="brand">Drizle<span>Pay</span></a>
		<h1>{isRegister ? 'Create Account' : 'Sign In'}</h1>
		<p class="subtitle">
			{isRegister ? 'Start accepting payments in minutes' : 'Access your merchant dashboard'}
		</p>

		<form onsubmit={submit} autocomplete="on">
			{#if error}
				<div class="error">{error}</div>
			{/if}

			{#if isRegister}
				<label>
					<span>Name</span>
					<input type="text" bind:value={name} required placeholder="Your full name" autocomplete="name" />
				</label>
				<label>
					<span>Company (optional)</span>
					<input type="text" bind:value={company} placeholder="Your company name" autocomplete="organization" />
				</label>
			{/if}

			<label>
				<span>Email</span>
				<input type="email" bind:value={email} required placeholder="you@company.com" autocomplete="email" />
			</label>

			<label>
				<span>Password</span>
				<input type={showPassword ? 'text' : 'password'} bind:value={password} required placeholder="••••••••" autocomplete={isRegister ? 'new-password' : 'current-password'} />
			</label>
			<label class="show-pw">
				<input type="checkbox" bind:checked={showPassword} />
				Show password
			</label>
			{#if !isRegister}
				<a href="/forgot-password" class="forgot">Forgot password?</a>
			{/if}

			<button type="submit" class="btn primary" disabled={loading}>
				{loading ? 'Please wait…' : isRegister ? 'Create Account' : 'Sign In'}
			</button>
		</form>

		<p class="toggle">
			{isRegister ? 'Already have an account?' : "Don't have an account?"}
			<button class="link" onclick={toggleMode}>
				{isRegister ? 'Sign In' : 'Register'}
			</button>
		</p>

	</div>
</div>

<style>
	.login-page {
		min-height: 100vh;
		display: grid;
		place-items: center;
		background: #f8fafc;
		padding: 24px;
	}
	.login-card {
		width: 100%;
		max-width: 420px;
		padding: 40px 32px;
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		box-shadow: var(--shadow);
	}
	.brand {
		display: block;
		text-align: center;
		font-weight: 760;
		font-size: 23px;
		color: var(--hero-bg);
		margin-bottom: 28px;
	}
	.brand span { color: var(--primary); }
	h1 {
		font-size: 24px;
		font-weight: 700;
		color: var(--hero-bg);
		margin: 0 0 6px;
		text-align: center;
	}
	.subtitle {
		color: var(--muted);
		font-size: 14px;
		text-align: center;
		margin: 0 0 28px;
	}
	form { display: grid; gap: 16px; }
	label {
		display: grid;
		gap: 6px;
	}
	label span {
		font-size: 13px;
		font-weight: 600;
		color: var(--ink);
	}
	input {
		padding: 10px 14px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 15px;
		color: var(--ink);
		background: #fff;
		outline: none;
		transition: border-color 0.15s;
	}
	input:focus { border-color: var(--primary); }
	.show-pw input[type="checkbox"] {
		width: 16px;
		height: 16px;
		padding: 0;
		border: 1.5px solid var(--line);
		border-radius: 3px;
		accent-color: var(--primary);
		cursor: pointer;
	}
	.show-pw {
		display: flex;
		align-items: center;
		gap: 8px;
		font-size: 13px;
		color: var(--muted);
		cursor: pointer;
		margin-top: -6px;
	}
	.show-pw input { width: auto; }
	.btn {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 44px;
		padding: 0 20px;
		border-radius: 4px;
		border: none;
		font-size: 15px;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.15s;
	}
	.btn.primary { background: var(--primary); color: #fff; }
	.btn.primary:hover:not(:disabled) { background: var(--primary-dark); }
	.btn:disabled { opacity: 0.6; cursor: not-allowed; }
	.error {
		padding: 12px 14px;
		background: #fef2f2;
		color: #dc2626;
		border-radius: 4px;
		font-size: 14px;
		text-align: center;
	}
	.toggle {
		text-align: center;
		font-size: 14px;
		color: var(--muted);
		margin: 20px 0 0;
	}
	.link {
		background: none;
		border: none;
		color: var(--primary);
		font-weight: 600;
		cursor: pointer;
		font-size: 14px;
		padding: 0;
	}
	.link:hover { text-decoration: underline; }
	.forgot { font-size: 13px; color: var(--primary); font-weight: 600; text-align: right; margin-top: -8px; }
	.forgot:hover { text-decoration: underline; }

</style>
