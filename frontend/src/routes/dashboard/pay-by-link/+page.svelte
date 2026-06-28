<script>
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	let links = $state([]);
	let stats = $state(null);
	let loading = $state(true);
	let showForm = $state(false);

	let formAmount = $state('');
	let formCurrency = $state('AED');
	let formDesc = $state('');
	let error = $state('');

	onMount(async () => {
		try {
			const [res, st] = await Promise.all([
				api.getPayLinks(1, 20),
				api.getPayLinkStats(),
			]);
			links = res.data;
			stats = st;
		} catch (e) { error = e.message || 'Something went wrong'; } finally {
			loading = false;
		}
	});

	async function createLink() {
		try {
			const data = {
				amount: formAmount ? parseFloat(formAmount) : null,
				currency: formCurrency,
				description: formDesc,
			};
			await api.createPayLink(data);
			showForm = false;
			formAmount = '';
			formDesc = '';
			const res = await api.getPayLinks(1, 20);
			links = res.data;
		} catch (e) { error = e.message || 'Something went wrong'; }
	}
</script>

<svelte:head>
	<title>Payment Links | DrizlePay</title>
</svelte:head>

<div class="page-header">
	<h2>Payment Links</h2>
	<button class="btn-primary" onclick={() => showForm = !showForm}>
		{showForm ? 'Cancel' : '+ New Link'}
	</button>
</div>

{#if stats}
	<div class="stats-mini">
		<div class="stat-mini">
			<span class="stat-mini-label">Total Links</span>
			<strong>{stats.total_links}</strong>
		</div>
		<div class="stat-mini">
			<span class="stat-mini-label">Active</span>
			<strong>{stats.active_links}</strong>
		</div>
		<div class="stat-mini">
			<span class="stat-mini-label">Collected</span>
			<strong>AED {stats.total_collected?.toFixed(2)}</strong>
		</div>
		<div class="stat-mini">
			<span class="stat-mini-label">Payments</span>
			<strong>{stats.total_payments}</strong>
		</div>
	</div>
{/if}

{#if showForm}
	<div class="card form-card">
		<h3>Create Payment Link</h3>
		<div class="form-grid">
			<label>
				<span>Amount (optional)</span>
				<input type="number" step="0.01" bind:value={formAmount} placeholder="0.00" />
			</label>
			<label>
				<span>Currency</span>
				<select bind:value={formCurrency}>
					<option value="AED">AED</option>
					<option value="USD">USD</option>
				</select>
			</label>
			<label class="full-width">
				<span>Description</span>
				<input type="text" bind:value={formDesc} placeholder="What is this for?" />
			</label>
		</div>
		<button class="btn-primary" onclick={createLink}>Generate Link</button>
	</div>
{/if}

<div class="card">
	{#if loading}
		<p class="loading-text">Loading…</p>
	{:else if links.length === 0}
		<p class="empty">No payment links yet. Create one above.</p>
	{:else}
		{#if error}
			<div class="error-banner">{error}</div>
		{/if}
		<div class="table-wrap">
			<table>
				<thead>
					<tr>
						<th>Link ID</th>
						<th>Amount</th>
						<th>Description</th>
						<th>Payments</th>
						<th>Collected</th>
						<th>Status</th>
						<th>Created</th>
					</tr>
				</thead>
				<tbody>
					{#each links as link}
						<tr>
							<td class="mono">{link.id}</td>
							<td class="mono">{link.amount ? `${link.currency} ${link.amount.toFixed(2)}` : 'Open amount'}</td>
							<td>{link.description || '—'}</td>
							<td>{link.payment_count || 0}</td>
							<td class="mono">{link.currency} {(link.total_collected || 0).toFixed(2)}</td>
							<td>
								<span class="badge" class:active={link.status === 'active'} class:disabled={link.status === 'disabled'}>
									{link.status}
								</span>
							</td>
							<td class="mono">{new Date(link.created_at).toLocaleDateString()}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{/if}
</div>

<style>
	.page-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20px;
	}
	.page-header h2 { margin: 0; font-size: 20px; font-weight: 700; color: var(--hero-bg); }
	.btn-primary {
		padding: 8px 18px;
		background: var(--primary);
		color: #fff;
		border: none;
		border-radius: 4px;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
		transition: background 0.15s;
	}
	.btn-primary:hover { background: var(--primary-dark); }
	.stats-mini {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 12px;
		margin-bottom: 20px;
	}
	.stat-mini {
		padding: 14px;
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 6px;
	}
	.stat-mini-label { display: block; font-size: 11px; color: var(--muted); margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.05em; }
	.stat-mini strong { font-size: 18px; color: var(--hero-bg); }
	.form-card {
		padding: 20px;
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		margin-bottom: 16px;
	}
	.form-card h3 { margin: 0 0 16px; font-size: 15px; font-weight: 600; color: var(--hero-bg); }
	.form-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 12px;
		margin-bottom: 16px;
	}
	.form-grid label { display: grid; gap: 4px; }
	.form-grid label span { font-size: 12px; font-weight: 600; color: var(--ink); }
	.form-grid label input,
	.form-grid label select {
		padding: 8px 10px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 13px;
		color: var(--ink);
		background: #fff;
	}
	.full-width { grid-column: 1 / -1; }
	.loading-text, .empty { color: var(--muted); font-size: 15px; padding: 40px; text-align: center; }
	.card {
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		padding: 0;
		overflow: hidden;
	}
	.table-wrap { overflow-x: auto; }
	table { width: 100%; border-collapse: collapse; font-size: 13px; }
	th {
		text-align: left; padding: 10px 12px; color: var(--muted); font-weight: 600;
		font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em;
		border-bottom: 1px solid var(--line); white-space: nowrap; background: #fafafa;
	}
	td { padding: 10px 12px; color: var(--ink); border-bottom: 1px solid #f1f5f9; white-space: nowrap; }
	tr:last-child td { border-bottom: none; }
	.mono { font-family: ui-monospace, monospace; font-size: 12px; }
	.badge {
		display: inline-flex; padding: 2px 8px; border-radius: 12px;
		font-size: 11px; font-weight: 600; background: #f1f5f9; color: var(--muted);
	}
	.badge.active { background: #e6fcf0; color: var(--primary-dark); }
	.badge.disabled { background: #f1f5f9; color: var(--muted); }
		.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
	@media (max-width: 768px) { .stats-mini { grid-template-columns: repeat(2, 1fr); } }
</style>
