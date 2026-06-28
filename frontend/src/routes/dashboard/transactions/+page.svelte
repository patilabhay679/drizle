<script>
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	let txns = $state([]);
	let total = $state(0);
	let page = $state(1);
	let loading = $state(true);
	const limit = 10;

	let search = $state('');
	let schemeFilter = $state('');
	let typeFilter = $state('');
	let startDate = $state('');
	let endDate = $state('');
	let error = $state('');

	onMount(() => load());

	async function load() {
		loading = true;
		try {
			const params = {};
			if (search) params.search = search;
			if (schemeFilter) params.scheme = schemeFilter;
			if (typeFilter) params.txn_type = typeFilter;
			const res = await api.getTransactions(page, limit, params);
			txns = res.data;
			total = res.total;
		} catch (e) { error = e.message || 'Something went wrong'; } finally {
			loading = false;
		}
	}

	const totalPages = $derived(Math.ceil(total / limit));

	function go(p) { page = p; load(); }

	function applyFilters() { page = 1; load(); }

	function clearFilters() {
		search = '';
		schemeFilter = '';
		typeFilter = '';
		startDate = '';
		endDate = '';
		page = 1;
		load();
	}

	function pageRange() {
		const pages = [];
		const maxVisible = 7;
		let start = Math.max(1, page - 3);
		let end = Math.min(totalPages, page + 3);
		if (end - start < maxVisible - 1) {
			if (start === 1) end = Math.min(totalPages, start + maxVisible - 1);
			else start = Math.max(1, end - maxVisible + 1);
		}
		for (let i = start; i <= end; i++) pages.push(i);
		return pages;
	}
</script>

<svelte:head>
	<title>Transactions | DrizlePay</title>
</svelte:head>

<div class="page-header">
	<h2>Transactions</h2>
	<span class="count">{total} total</span>
</div>

<div class="filters-bar">
	<input type="date" bind:value={startDate} class="filter-input" placeholder="Start date" />
	<span class="sep">—</span>
	<input type="date" bind:value={endDate} class="filter-input" placeholder="End date" />
	<select bind:value={schemeFilter} class="filter-input">
		<option value="">All schemes</option>
		<option value="Visa">Visa</option>
		<option value="Mastercard">Mastercard</option>
		<option value="Meeza/Jaywan">Meeza/Jaywan</option>
		<option value="Amex">Amex</option>
	</select>
	<select bind:value={typeFilter} class="filter-input">
		<option value="">All types</option>
		<option value="Purchase">Purchase</option>
		<option value="Refund">Refund</option>
	</select>
	<input type="text" bind:value={search} placeholder="Search" class="filter-input search-input" />
	<button class="btn-filter" onclick={applyFilters}>Filters</button>
	<button class="btn-filter btn-clear" onclick={clearFilters}>Clear</button>
</div>

<div class="card">
	{#if loading}
		<p class="loading-text">Loading…</p>
	{:else if txns.length === 0}
		<p class="empty">No transactions found.</p>
	{:else}
		{#if error}
			<div class="error-banner">{error}</div>
		{/if}
		<div class="table-wrap">
			<table>
				<thead>
					<tr>
						<th>Reference / Order ID</th>
						<th>Date and time</th>
						<th>Terminal ID</th>
						<th>Scheme</th>
						<th>Amount</th>
						<th>Tags</th>
						<th>Type</th>
						<th>Card Class</th>
						<th>Card Segment</th>
						<th>Card Origin</th>
						<th>Actions</th>
					</tr>
				</thead>
				<tbody>
					{#each txns as txn}
						<tr>
							<td class="mono">{txn.reference || txn.id}</td>
							<td class="mono">{new Date(txn.created_at).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })}</td>
							<td class="mono">{txn.terminal_id || '—'}</td>
							<td>{txn.scheme || '—'}</td>
							<td class="mono">{txn.currency || 'AED'} {txn.amount?.toFixed(2)}</td>
							<td>{txn.tags?.length ? txn.tags.join(', ') : ''}</td>
							<td>
								<span class="badge" class:purchase={txn.type === 'Purchase'} class:refund={txn.type === 'Refund'}>
									{txn.type || '—'}
								</span>
							</td>
							<td>{txn.card_class || 'N/A'}</td>
							<td>{txn.card_segment || 'N/A'}</td>
							<td>{txn.card_origin || 'N/A'}</td>
							<td><button class="btn-action" title="View details">⋯</button></td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
		<div class="pagination">
			<span class="pagination-summary">Show {Math.min(limit, total)} of {total} transactions</span>
			<div class="pagination-pages">
				<button class="page-btn" disabled={page <= 1} onclick={() => go(page - 1)}>‹</button>
				{#each pageRange() as p}
					<button class="page-btn" class:current={p === page} onclick={() => go(p)}>{p}</button>
				{/each}
				{#if totalPages > 7 && page < totalPages - 3}
					<span class="page-ellipsis">…</span>
					<button class="page-btn" onclick={() => go(totalPages)}>{totalPages}</button>
				{/if}
				<button class="page-btn" disabled={page >= totalPages} onclick={() => go(page + 1)}>›</button>
			</div>
		</div>
	{/if}
</div>

<style>
	.page-header {
		display: flex;
		align-items: baseline;
		gap: 12px;
		margin-bottom: 16px;
	}
	.page-header h2 { margin: 0; font-size: 20px; font-weight: 700; color: var(--hero-bg); }
	.count { font-size: 14px; color: var(--muted); }
	.filters-bar {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 16px;
		flex-wrap: wrap;
	}
	.filter-input {
		padding: 6px 10px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 13px;
		color: var(--ink);
		background: #fff;
	}
	.search-input { min-width: 140px; }
	.sep { color: var(--muted); font-size: 13px; }
	.btn-filter {
		padding: 6px 14px;
		border: 1px solid var(--line);
		border-radius: 4px;
		background: #fff;
		font-size: 13px;
		color: var(--ink);
		cursor: pointer;
		transition: all 0.15s;
	}
	.btn-filter:hover { border-color: var(--primary); color: var(--primary); }
	.btn-clear { color: var(--muted); }
	.btn-clear:hover { border-color: #dc2626; color: #dc2626; }
	.loading-text, .empty { color: var(--muted); font-size: 15px; padding: 40px; text-align: center; }
	.card {
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		padding: 0;
		overflow: hidden;
	}
	.table-wrap { overflow-x: auto; }
	table {
		width: 100%;
		border-collapse: collapse;
		font-size: 13px;
	}
	th {
		text-align: left;
		padding: 10px 12px;
		color: var(--muted);
		font-weight: 600;
		font-size: 11px;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		border-bottom: 1px solid var(--line);
		white-space: nowrap;
		background: #fafafa;
	}
	td {
		padding: 10px 12px;
		color: var(--ink);
		border-bottom: 1px solid #f1f5f9;
		white-space: nowrap;
	}
	tr:last-child td { border-bottom: none; }
	.mono { font-family: ui-monospace, monospace; font-size: 12px; }
	.badge {
		display: inline-flex;
		padding: 2px 8px;
		border-radius: 12px;
		font-size: 11px;
		font-weight: 600;
		background: #f1f5f9;
		color: var(--muted);
	}
	.badge.purchase { background: #e6fcf0; color: var(--primary-dark); }
	.badge.refund { background: #fef3c7; color: #92400e; }
	.btn-action {
		background: none;
		border: 1px solid var(--line);
		border-radius: 4px;
		padding: 2px 8px;
		cursor: pointer;
		font-size: 15px;
		color: var(--muted);
		line-height: 1;
	}
	.btn-action:hover { border-color: var(--primary); color: var(--primary); }
	.pagination {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 12px 16px;
		border-top: 1px solid var(--line);
	}
	.pagination-summary { font-size: 12px; color: var(--muted); }
	.pagination-pages { display: flex; align-items: center; gap: 2px; }
	.page-btn {
		min-width: 30px;
		height: 30px;
		padding: 0 6px;
		border: 1px solid transparent;
		border-radius: 4px;
		background: none;
		font-size: 13px;
		color: var(--ink);
		cursor: pointer;
		transition: all 0.15s;
	}
	.page-btn:hover:not(:disabled) { border-color: var(--line); background: #f1f5f9; }
	.page-btn.current { background: var(--primary); color: #fff; font-weight: 600; }
	.page-btn:disabled { opacity: 0.3; cursor: not-allowed; }
	.page-ellipsis { padding: 0 4px; color: var(--muted); font-size: 13px; }
		.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
	@media (max-width: 768px) {
		.pagination { flex-direction: column; gap: 8px; }
	}
</style>
