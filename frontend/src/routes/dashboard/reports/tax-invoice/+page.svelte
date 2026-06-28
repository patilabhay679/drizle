<script>
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	let invoices = $state([]);
	let loading = $state(true);
	let error = $state('');

	onMount(async () => {
		try {
			const res = await api.getTaxInvoices();
			invoices = res.data;
		} catch (e) { error = e.message || 'Something went wrong'; } finally {
			loading = false;
		}
	});
</script>

<svelte:head>
	<title>Tax Invoice | Drizle Pay</title>
</svelte:head>

<div class="page-header">
	<h2>Tax Invoice</h2>
</div>

<div class="card">
	{#if loading}
		<p class="loading-text">Loading…</p>
	{:else if invoices.length === 0}
		<p class="empty">No tax invoices available.</p>
	{:else}
		{#if error}
			<div class="error-banner">{error}</div>
		{/if}
		<div class="table-wrap">
			<table>
				<thead>
					<tr>
						<th>Period</th>
						<th>Invoice ID</th>
						<th>Amount</th>
						<th>Status</th>
						<th>Generated</th>
						<th>Action</th>
					</tr>
				</thead>
				<tbody>
					{#each invoices as inv}
						<tr>
							<td>{inv.label || inv.period}</td>
							<td class="mono">{inv.id}</td>
							<td class="mono">{inv.currency || 'AED'} {inv.amount?.toFixed(2)}</td>
							<td>
								<span class="badge" class:generated={inv.status === 'generated'} class:pending={inv.status === 'pending'}>
									{inv.status}
								</span>
							</td>
							<td class="mono">{inv.generated_at ? new Date(inv.generated_at).toLocaleDateString() : '—'}</td>
							<td>
								{#if inv.status === 'generated'}
									<button class="btn-download">Download</button>
								{:else}
									<button class="btn-download" disabled>Pending</button>
								{/if}
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{/if}
</div>

<style>
	.page-header { margin-bottom: 20px; }
	.page-header h2 { margin: 0; font-size: 20px; font-weight: 700; color: var(--hero-bg); }
	.loading-text, .empty { color: var(--muted); font-size: 15px; padding: 40px; text-align: center; }
	.card { background: #fff; border: 1px solid var(--line); border-radius: 8px; padding: 0; overflow: hidden; }
	.table-wrap { overflow-x: auto; }
	table { width: 100%; border-collapse: collapse; font-size: 13px; }
	th { text-align: left; padding: 10px 12px; color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid var(--line); white-space: nowrap; background: #fafafa; }
	td { padding: 10px 12px; color: var(--ink); border-bottom: 1px solid #f1f5f9; white-space: nowrap; }
	tr:last-child td { border-bottom: none; }
	.mono { font-family: ui-monospace, monospace; font-size: 12px; }
	.badge { display: inline-flex; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: #f1f5f9; color: var(--muted); }
	.badge.generated { background: #e6fcf0; color: var(--primary-dark); }
	.badge.pending { background: #fef3c7; color: #92400e; }
	.btn-download {
		padding: 4px 12px; border: 1px solid var(--line); border-radius: 4px;
		background: #fff; font-size: 12px; color: var(--ink); cursor: pointer;
	}
	.btn-download:hover:not(:disabled) { border-color: var(--primary); color: var(--primary); }
	.btn-download:disabled { opacity: 0.4; cursor: not-allowed; }
	.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
</style>
