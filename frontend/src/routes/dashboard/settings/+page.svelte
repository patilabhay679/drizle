<script>
	import { auth } from '$lib/stores/auth';
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	let name = $state('');
	let company = $state('');
	let profileSaved = $state(false);
	let profileError = $state('');
	let profileLoading = $state(false);

	let currentPassword = $state('');
	let newPassword = $state('');
	let confirmPassword = $state('');
	let passwordChanged = $state(false);
	let passwordError = $state('');
	let passwordLoading = $state(false);

	let apiKeys = $state(null);
	let keyError = $state('');
	let keyLoading = $state(false);
	let error = $state('');

	let testMode = $state(auth.merchant?.test_mode ?? false);
	let toggling = $state(false);

	onMount(async () => {
		name = auth.merchant?.name || '';
		company = auth.merchant?.company || '';
		try {
			apiKeys = await api.getApiKeys();
		} catch (e) { error = e.message || 'Something went wrong'; }
	});

	async function toggleTestMode() {
		toggling = true;
		try {
			const updated = await api.toggleTestMode();
			auth.updateMerchant(updated);
			testMode = updated.test_mode;
		} catch (e) {
			console.error(e);
		} finally {
			toggling = false;
		}
	}

	async function saveProfile(e) {
		e.preventDefault();
		profileError = '';
		profileLoading = true;
		try {
			const res = await api.updateMe({ name, company });
			auth.login(auth.token, res);
			profileSaved = true;
			setTimeout(() => profileSaved = false, 3000);
		} catch (err) {
			profileError = err.message;
		} finally {
			profileLoading = false;
		}
	}

	async function changePassword(e) {
		e.preventDefault();
		passwordError = '';
		if (newPassword !== confirmPassword) {
			passwordError = 'Passwords do not match.';
			return;
		}
		if (newPassword.length < 6) {
			passwordError = 'Password must be at least 6 characters.';
			return;
		}
		passwordLoading = true;
		try {
			await api.changePassword(currentPassword, newPassword);
			passwordChanged = true;
			currentPassword = '';
			newPassword = '';
			confirmPassword = '';
			setTimeout(() => passwordChanged = false, 3000);
		} catch (err) {
			passwordError = err.message;
		} finally {
			passwordLoading = false;
		}
	}

	async function rotateKeys() {
		if (!confirm('Rotate API keys? Existing keys will stop working immediately.')) return;
		keyError = '';
		keyLoading = true;
		try {
			apiKeys = await api.rotateApiKeys();
		} catch (err) {
			keyError = err.message;
		} finally {
			keyLoading = false;
		}
	}
</script>

<svelte:head>
	<title>Settings | DrizlePay</title>
</svelte:head>

<div class="page-header">
	<h2>Settings</h2>
</div>

{#if error}
	<div class="error-banner">{error}</div>
{/if}

<div class="card">
	<h3>Profile</h3>
	<form onsubmit={saveProfile}>
		{#if profileError}
			<div class="msg error">{profileError}</div>
		{/if}
		{#if profileSaved}
			<div class="msg success">Profile updated.</div>
		{/if}
		<label>
			<span>Name</span>
			<input type="text" bind:value={name} required />
		</label>
		<label>
			<span>Email</span>
			<input type="email" value={auth.merchant?.email || ''} disabled />
		</label>
		<label>
			<span>Company</span>
			<input type="text" bind:value={company} placeholder="Your company name" />
		</label>
		<button type="submit" class="btn primary" disabled={profileLoading}>
			{profileLoading ? 'Saving…' : 'Save Changes'}
		</button>
	</form>
</div>

<div class="card">
	<h3>Change Password</h3>
	<form onsubmit={changePassword}>
		{#if passwordError}
			<div class="msg error">{passwordError}</div>
		{/if}
		{#if passwordChanged}
			<div class="msg success">Password changed.</div>
		{/if}
		<label>
			<span>Current Password</span>
			<input type="password" bind:value={currentPassword} required placeholder="••••••••" />
		</label>
		<label>
			<span>New Password</span>
			<input type="password" bind:value={newPassword} required minlength={6} placeholder="••••••••" />
		</label>
		<label>
			<span>Confirm New Password</span>
			<input type="password" bind:value={confirmPassword} required placeholder="••••••••" />
		</label>
		<button type="submit" class="btn primary" disabled={passwordLoading}>
			{passwordLoading ? 'Changing…' : 'Update Password'}
		</button>
	</form>
</div>

<div class="card">
	<h3>API Keys</h3>
	<p class="hint">Your API keys are used to authenticate requests to the Drizle Pay API. Keep them secure.</p>
	{#if keyError}
		<div class="msg error">{keyError}</div>
	{/if}
	{#if apiKeys}
		<div class="field-row">
			<span class="field-label">Publishable Key</span>
			<code>{apiKeys.publishable}</code>
		</div>
		<div class="field-row">
			<span class="field-label">Secret Key</span>
			<code>{apiKeys.secret.slice(0, 12)}••••••••••••••••••••••</code>
		</div>
	{/if}
	<button class="btn secondary" onclick={rotateKeys} disabled={keyLoading}>
		{keyLoading ? 'Rotating…' : 'Rotate Keys'}
	</button>
</div>

<div class="card">
	<h3>Test Mode</h3>
	<p class="hint">When test mode is on, the dashboard shows a banner and all API interactions use test endpoints. Toggle it here or from the sidebar.</p>
	<div class="test-toggle-row">
		<span class="test-toggle-label">{testMode ? 'Test Mode is ON' : 'Test Mode is OFF'}</span>
		<button class="test-btn" class:active={testMode} onclick={toggleTestMode} disabled={toggling}>
			<span class="dot"></span>
			{toggling ? 'Toggling…' : testMode ? 'Disable Test Mode' : 'Enable Test Mode'}
		</button>
	</div>
</div>

<div class="card">
	<h3>Account</h3>
	<p class="hint">Sign out of your account.</p>
	<button class="btn secondary" onclick={() => auth.logout()}>Sign Out</button>
</div>

<style>
	.page-header { margin-bottom: 20px; }
	.page-header h2 { margin: 0; font-size: 20px; font-weight: 700; color: var(--hero-bg); }
	.card {
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		padding: 20px;
		margin-bottom: 16px;
	}
	.card h3 {
		font-size: 16px;
		font-weight: 600;
		color: var(--hero-bg);
		margin: 0 0 16px;
	}
	.hint {
		color: var(--muted);
		font-size: 14px;
		margin: -8px 0 16px;
		line-height: 1.5;
	}
	form { display: grid; gap: 14px; max-width: 400px; }
	label { display: grid; gap: 6px; }
	label span { font-size: 13px; font-weight: 600; color: var(--ink); }
	input {
		padding: 10px 14px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 14px;
		color: var(--ink);
		background: #fff;
		outline: none;
	}
	input:focus { border-color: var(--primary); }
	input:disabled { background: #f8fafc; color: var(--muted); }
	.msg {
		padding: 10px 14px;
		border-radius: 4px;
		font-size: 14px;
	}
	.msg.success { background: #e6fcf0; color: var(--primary-dark); }
	.msg.error { background: #fef2f2; color: #dc2626; }
	.btn {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-height: 40px;
		padding: 0 20px;
		border-radius: 4px;
		font-size: 14px;
		font-weight: 600;
		cursor: pointer;
		border: none;
		transition: all 0.15s;
		width: fit-content;
	}
	.btn.primary { background: var(--primary); color: #fff; }
	.btn.primary:hover:not(:disabled) { background: var(--primary-dark); }
	.btn:disabled { opacity: 0.6; cursor: not-allowed; }
	.btn.secondary {
		background: #fff;
		color: var(--ink);
		border: 1px solid var(--line);
	}
	.btn.secondary:hover:not(:disabled) { border-color: var(--muted); }
	.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
	.test-toggle-row { display: flex; align-items: center; justify-content: space-between; gap: 16px; }
	.test-toggle-label { font-size: 14px; font-weight: 500; color: var(--ink); }
	.test-btn {
		display: flex; align-items: center; gap: 8px;
		padding: 8px 16px; border: 1px solid var(--line); border-radius: 6px;
		background: #fff; font-size: 13px; font-weight: 600; color: var(--muted);
		cursor: pointer; transition: all 0.15s;
	}
	.test-btn:hover { border-color: var(--primary); color: var(--ink); }
	.test-btn:disabled { opacity: 0.5; cursor: not-allowed; }
	.test-btn.active { background: #fef3c7; border-color: #f59e0b; color: #92400e; }
	.dot { width: 8px; height: 8px; border-radius: 50%; background: var(--muted); }
	.test-btn.active .dot { background: #f59e0b; }
	.field-row {
		display: flex;
		align-items: center;
		gap: 16px;
		padding: 10px 0;
		border-bottom: 1px solid #f1f5f9;
	}
	.field-row:last-child { border-bottom: none; }
	.field-label {
		width: 140px;
		font-size: 13px;
		font-weight: 600;
		color: var(--muted);
		flex-shrink: 0;
	}
	.field-row code {
		font-family: ui-monospace, monospace;
		font-size: 13px;
		background: #f8fafc;
		padding: 4px 8px;
		border-radius: 4px;
		border: 1px solid var(--line);
	}
</style>
