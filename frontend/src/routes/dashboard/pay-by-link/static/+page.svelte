<script>
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	let links = $state([]);
	let loading = $state(true);
	let showForm = $state(false);
	let formAmount = $state('');
	let formDesc = $state('');
	let error = $state('');

	onMount(async () => {
		try {
			const res = await api.getPayLinks(1, 50, true);
			links = res.data;
		} catch (e) { error = e.message || 'Something went wrong'; } finally {
			loading = false;
		}
	});

	async function createStatic() {
		try {
			await api.createPayLink({ amount: formAmount ? parseFloat(formAmount) : null, description: formDesc, is_static: true });
			showForm = false; formAmount = ''; formDesc = '';
			const res = await api.getPayLinks(1, 50, true);
			links = res.data;
		} catch (e) { error = e.message || 'Something went wrong'; }
	}
</script>

<svelte:head>
	<title>Static Links | DrizlePay</title>
</svelte:head>

<div class="page-header">
	<h2>Static Links</h2>
	<button class="btn-primary" onclick={() => showForm = !showForm}>{showForm ? 'Cancel' : '+ New Static Link'}</button>
</div>

{#if showForm}
	<div class="card form-card">
		<h3>Create Static Link</h3>
		<div class="form-grid">
			<label><span>Amount (optional)</span><input type="number" step="0.01" bind:value={formAmount} placeholder="0.00" /></label>
			<label class="full-width"><span>Description</span><input type="text" bind:value={formDesc} placeholder="Label" /></label>
		</div>
		<button class="btn-primary" onclick={createStatic}>Generate Static Link</button>
	</div>
{/if}

<div class="card">
	{#if loading}
		<p class="loading-text">Loading…</p>
	{:else if links.length === 0}
		<p class="empty">No static links yet.</p>
	{:else}
		{#if error}
			<div class="error-banner">{error}</div>
		{/if}
		<div class="table-wrap">
			<table>
				<thead><tr><th>ID</th><th>URL</th><th>Amount</th><th>Description</th><th>Payments</th><th>Status</th><th>Created</th></tr></thead>
				<tbody>
					{#each links as link}
						<tr>
							<td class="mono">{link.id}</td>
							<td class="mono" style="max-width:200px;overflow:hidden;text-overflow:ellipsis;">{link.url}</td>
							<td class="mono">{link.amount ? `${link.currency} ${link.amount.toFixed(2)}` : 'Open'}</td>
							<td>{link.description || '—'}</td>
							<td>{link.payment_count || 0}</td>
							<td><span class="badge" class:active={link.status === 'active'}>{link.status}</span></td>
							<td class="mono">{new Date(link.created_at).toLocaleDateString()}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{/if}
</div>

<style>
	.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
	.page-header h2 { margin: 0; font-size: 20px; font-weight: 700; color: var(--hero-bg); }
	.btn-primary { padding: 8px 18px; background: var(--primary); color: #fff; border: none; border-radius: 4px; font-size: 13px; font-weight: 600; cursor: pointer; }
	.btn-primary:hover { background: var(--primary-dark); }
	.form-card { padding: 20px; background: #fff; border: 1px solid var(--line); border-radius: 8px; margin-bottom: 16px; }
	.form-card h3 { margin: 0 0 16px; font-size: 15px; font-weight: 600; color: var(--hero-bg); }
	.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px; }
	.form-grid label { display: grid; gap: 4px; }
	.form-grid label span { font-size: 12px; font-weight: 600; color: var(--ink); }
	.form-grid label input { padding: 8px 10px; border: 1px solid var(--line); border-radius: 4px; font-size: 13px; color: var(--ink); background: #fff; }
	.full-width { grid-column: 1 / -1; }
	.loading-text, .empty { color: var(--muted); font-size: 15px; padding: 40px; text-align: center; }
	.card { background: #fff; border: 1px solid var(--line); border-radius: 8px; padding: 0; overflow: hidden; }
	.table-wrap { overflow-x: auto; }
	table { width: 100%; border-collapse: collapse; font-size: 13px; }
	th { text-align: left; padding: 10px 12px; color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid var(--line); white-space: nowrap; background: #fafafa; }
	td { padding: 10px 12px; color: var(--ink); border-bottom: 1px solid #f1f5f9; white-space: nowrap; }
	tr:last-child td { border-bottom: none; }
	.mono { font-family: ui-monospace, monospace; font-size: 12px; }
	.badge { display: inline-flex; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: #f1f5f9; color: var(--muted); }
	.badge.active { background: #e6fcf0; color: var(--primary-dark); }
	.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
</style>
