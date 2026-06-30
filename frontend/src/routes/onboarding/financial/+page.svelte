<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { data, loading, saving, error, load, saveSection } from '$lib/stores/onboarding.svelte';
	import { get } from 'svelte/store';

	let initialized = $state(false);

	let bank = $state({ bank_name: '', account_name: '', account_number: '', iban: '', swift: '' });
	let security = $state({ two_factor_enabled: false });
	let extras = $state({ referral_source: '', notes: '' });

	onMount(async () => {
		await load();
		const d = get(data);
		if (d.bank) bank = { ...d.bank };
		if (d.security) security = { ...d.security };
		if (d.extras) extras = { ...d.extras };
		initialized = true;
	});

	async function handleSubmit(e) {
		e.preventDefault();
		await saveSection('bank', bank);
		await saveSection('security', security);
		await saveSection('extras', extras);
		goto('/onboarding/review');
	}
</script>

{#if !initialized || $loading}
	<p class="loading-text">Loading…</p>
{:else}
	<div class="page">
		<div class="page-header">
			<h2>Financial Setup</h2>
			<p>Set up your payout bank account and security preferences.</p>
		</div>

		<form onsubmit={handleSubmit}>
			<div class="card">
				<h3>Bank Account</h3>
				<div class="grid">
					<label>Bank Name
						<select bind:value={bank.bank_name}>
							<option value="">Select…</option>
							<option value="Emirates NBD">Emirates NBD</option>
							<option value="ADCB">ADCB</option>
							<option value="Mashreq">Mashreq</option>
							<option value="FAB">FAB</option>
							<option value="Dubai Islamic Bank">Dubai Islamic Bank</option>
							<option value="Other">Other</option>
						</select>
					</label>
					<label>Account Holder Name <input bind:value={bank.account_name} required /></label>
					<label>Account Number <input bind:value={bank.account_number} /></label>
					<label>IBAN <input bind:value={bank.iban} required placeholder="AEXXXXXXXXXXXXXXXXXXXXX" /></label>
					<label>SWIFT / BIC <input bind:value={bank.swift} /></label>
				</div>
			</div>

			<div class="card">
				<h3>Security</h3>
				<label class="checkbox">
					<input type="checkbox" bind:checked={security.two_factor_enabled} />
					Enable Two-Factor Authentication (2FA)
				</label>
				{#if security.two_factor_enabled}
					<p class="note">2FA will be required on next login. Configure TOTP in Settings after onboarding.</p>
				{/if}
			</div>

			<div class="card">
				<h3>Extras</h3>
				<div class="grid">
					<label>How did you hear about us?
						<select bind:value={extras.referral_source}>
							<option value="">Select…</option>
							<option value="Google">Google</option>
							<option value="LinkedIn">LinkedIn</option>
							<option value="Friend">Friend</option>
							<option value="Conference">Conference</option>
							<option value="Partner">Partner</option>
							<option value="Other">Other</option>
						</select>
					</label>
				</div>
				<label class="full">Notes <textarea bind:value={extras.notes} placeholder="Anything else?"></textarea></label>
			</div>

			{#if $error}
				<div class="error">{$error}</div>
			{/if}

			<div class="actions">
				<button type="submit" class="btn btn-primary" disabled={$saving}>
					{$saving ? 'Saving…' : 'Save & Continue →'}
				</button>
			</div>
		</form>
	</div>
{/if}

<style>
	.loading-text { color: var(--muted); font-size: 14px; }
	.page { display: flex; flex-direction: column; gap: 20px; }
	.page-header { margin-bottom: 4px; }
	.page-header h2 { font-size: 20px; color: var(--ink); margin: 0 0 4px; }
	.page-header p { font-size: 14px; color: var(--muted); margin: 0; }
	.card { background: #fff; border-radius: 8px; border: 1px solid var(--line); padding: 24px; margin-bottom: 16px; }
	.card h3 { font-size: 16px; margin: 0 0 16px; color: var(--ink); }
	.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
	.full { display: flex; flex-direction: column; gap: 4px; margin-top: 14px; }
	label { font-size: 13px; font-weight: 600; color: var(--ink); display: flex; flex-direction: column; gap: 4px; }
	input, select, textarea { padding: 8px 10px; border: 1px solid var(--line); border-radius: 6px; font-size: 14px; font-family: inherit; background: #fff; }
	input:focus, select:focus, textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(2,195,102,0.1); }
	textarea { resize: vertical; min-height: 60px; }
	.checkbox { flex-direction: row; align-items: center; gap: 10px; padding: 8px 0; }
	.checkbox input { width: 18px; height: 18px; }
	.note { font-size: 13px; color: var(--muted); padding: 8px 12px; background: #f8fafc; border-radius: 6px; margin: 8px 0 0; }
	.error { background: #fef2f2; color: #dc2626; padding: 10px 14px; border-radius: 6px; font-size: 14px; margin-top: 8px; }
	.actions { display: flex; justify-content: flex-end; }
	.btn { padding: 10px 24px; border-radius: 6px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; }
	.btn:disabled { opacity: 0.5; cursor: not-allowed; }
	.btn-primary { background: var(--primary); color: #fff; }
	.btn-primary:hover:not(:disabled) { background: var(--primary-dark); }
</style>
