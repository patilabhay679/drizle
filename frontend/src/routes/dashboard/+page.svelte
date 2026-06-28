<script>
	import { api } from '$lib/api';
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	let metrics = $state(null);
	let charts = $state(null);
	let recentPayouts = $state([]);
	let loading = $state(true);
	let activeTab = $state('transactions');
	let startDate = $state('');
	let endDate = $state('');
	let error = $state('');

	onMount(async () => {
		try {
			const [m, c, r] = await Promise.all([
				api.getDashboardMetrics(),
				api.getDashboardCharts(),
				api.getRecentPayouts(5),
			]);
			metrics = m;
			charts = c;
			recentPayouts = r;
		} catch (e) { error = e.message || 'Something went wrong'; } finally {
			loading = false;
		}
	});

	function formatChange(change) {
		const prefix = change >= 0 ? '+' : '';
		const cls = change >= 0 ? 'positive' : 'negative';
		return { text: `${prefix}${change}% vs last period`, cls };
	}

	// SVG line chart
	function linePath(points, width, height) {
		if (!points || points.length < 2) return '';
		const max = Math.max(...points, 1);
		const min = Math.min(...points, 0);
		const range = max - min || 1;
		const stepX = width / (points.length - 1);
		return points.map((v, i) => {
			const x = i * stepX;
			const y = height - ((v - min) / range) * (height - 20) - 10;
			return `${i === 0 ? 'M' : 'L'} ${x} ${y}`;
		}).join(' ');
	}

	function barWidth(total) {
		if (!total) return 0;
		return 100;
	}

	function barHeight(val, maxVal) {
		if (!maxVal) return 0;
		return (val / maxVal) * 100;
	}

	// Pie chart with conic gradient
	function conicGradient(data) {
		if (!data || data.length === 0) return '';
		const total = data.reduce((s, d) => s + d.volume, 0);
		if (total === 0) return '';
		let degrees = 0;
		const colors = ['#10b981', '#3b82f6', '#f59e0b', '#ef4444', '#8b5cf6'];
		const stops = data.map((d, i) => {
			const pct = (d.volume / total) * 100;
			const start = degrees;
			degrees += pct;
			return `${colors[i % colors.length]} ${start}% ${degrees}%`;
		});
		return stops.join(', ');
	}
</script>

<svelte:head>
	<title>Dashboard | DrizlePay</title>
</svelte:head>

{#if loading}
	<p class="loading-text">Loading…</p>
{:else}
	{#if error}
		<div class="error-banner">{error}</div>
	{/if}
	<div class="welcome">
		Welcome back, <strong>{metrics?.merchant_name || auth.merchant?.name || 'Merchant'}</strong>
	</div>

	<div class="tabs">
		<button
			class="tab"
			class:active={activeTab === 'transactions'}
			onclick={() => activeTab = 'transactions'}
		>Transactions</button>
		<button
			class="tab"
			class:active={activeTab === 'pay-by-link'}
			onclick={() => goto('/dashboard/pay-by-link')}
		>Pay by link</button>
	</div>

	<div class="filters-row">
		<div class="date-range">
			<input type="date" bind:value={startDate} class="date-input" />
			<span class="date-sep">—</span>
			<input type="date" bind:value={endDate} class="date-input" />
		</div>
		<button class="btn-filter" onclick={async () => {
			loading = true;
			try {
				const [m, c] = await Promise.all([
					api.getDashboardMetrics(startDate || undefined, endDate || undefined),
					api.getDashboardCharts(startDate || undefined, endDate || undefined),
				]);
				metrics = m;
				charts = c;
			} catch (e) { error = e.message || 'Something went wrong'; } finally {
				loading = false;
			}
		}}>Filters</button>
	</div>

	<div class="metrics-grid">
		<div class="metric-card">
			<span class="metric-label">Transaction amount</span>
			<strong class="metric-value">{metrics?.transaction_amount?.value?.toFixed(2) || '0.00'} {metrics?.transaction_amount?.currency || 'AED'}</strong>
			<span class="metric-change {formatChange(metrics?.transaction_amount?.change || 0).cls}">{formatChange(metrics?.transaction_amount?.change || 0).text}</span>
		</div>
		<div class="metric-card">
			<span class="metric-label">Number of transactions</span>
			<strong class="metric-value">{metrics?.transaction_count?.value || 0}</strong>
			<span class="metric-change {formatChange(metrics?.transaction_count?.change || 0).cls}">{formatChange(metrics?.transaction_count?.change || 0).text}</span>
		</div>
		<div class="metric-card">
			<span class="metric-label">Average transactions</span>
			<strong class="metric-value">{metrics?.average_transaction?.value?.toFixed(2) || '0.00'} {metrics?.average_transaction?.currency || 'AED'}</strong>
			<span class="metric-change {formatChange(metrics?.average_transaction?.change || 0).cls}">{formatChange(metrics?.average_transaction?.change || 0).text}</span>
		</div>
	</div>

	<div class="charts-grid">
		<div class="chart-card wide">
			<h3 class="chart-title">Transaction Volume Over Time</h3>
			{#if charts?.volume_over_time?.length}
				<svg class="line-chart" viewBox="0 0 600 200" preserveAspectRatio="none">
					<path d={linePath(charts.volume_over_time.map(d => d.volume), 600, 200)}
						fill="none" stroke="#10b981" stroke-width="2" />
					<defs>
						<linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
							<stop offset="0%" stop-color="#10b981" stop-opacity="0.15" />
							<stop offset="100%" stop-color="#10b981" stop-opacity="0.01" />
						</linearGradient>
					</defs>
					<path d={linePath(charts.volume_over_time.map(d => d.volume), 600, 200) + ` L 600 200 L 0 200 Z`}
						fill="url(#areaGrad)" />
				</svg>
				<div class="chart-labels">
					<span>{charts.volume_over_time[0]?.date?.slice(5) || ''}</span>
					<span>{charts.volume_over_time[charts.volume_over_time.length - 1]?.date?.slice(5) || ''}</span>
				</div>
			{:else}
				<p class="no-data">No volume data</p>
			{/if}
		</div>

		<div class="chart-card">
			<h3 class="chart-title">Top stores</h3>
			{#if charts?.top_schemes?.length}
				<div class="pie-container">
					<div class="pie" style="background: conic-gradient({conicGradient(charts.top_schemes)});"></div>
					<div class="pie-total">
						<strong>{charts.top_schemes.reduce((s, d) => s + d.volume, 0).toFixed(2)}</strong>
						<span>AED</span>
					</div>
				</div>
				<div class="pie-legend">
					{#each charts.top_schemes as scheme, i}
						<div class="legend-item">
							<span class="legend-dot" style="background: {['#10b981', '#3b82f6', '#f59e0b', '#ef4444', '#8b5cf6'][i % 5]}"></span>
							<span class="legend-label">{scheme.name}</span>
						</div>
					{/each}
				</div>
			{:else}
				<p class="no-data">No scheme data</p>
			{/if}
			<p class="chart-subtitle">Chart displays data for up to five selected stores</p>
		</div>

		<div class="chart-card">
			<h3 class="chart-title">Top schemes</h3>
			{#if charts?.top_schemes?.length}
				<div class="bar-chart">
					{#each charts.top_schemes as scheme}
						<div class="bar-item">
							<div class="bar-track">
								<div class="bar-fill" style="height: {barHeight(scheme.volume, Math.max(...charts.top_schemes.map(s => s.volume)))}%"></div>
							</div>
							<span class="bar-label">{scheme.name}</span>
						</div>
					{/each}
				</div>
			{:else}
				<p class="no-data">No scheme data</p>
			{/if}
			<p class="chart-subtitle">Chart displays data for up to five selected schemes</p>
		</div>
	</div>

	<div class="bottom-grid">
		<div class="card recent-payouts">
			<h3>Recent payouts</h3>
			{#if recentPayouts.length}
				<div class="payout-list">
					{#each recentPayouts as po}
						<div class="payout-item">
							<div class="payout-info">
								<span class="payout-value">{po.currency} {po.amount?.toFixed(2) || '0.00'}</span>
								<span class="payout-date">{po.date ? new Date(po.date).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }) : ''}</span>
							</div>
							<span class="payout-status" class:completed={po.status === 'completed'} class:pending={po.status === 'pending'}>{po.status}</span>
						</div>
					{/each}
				</div>
				<a href="/dashboard/payouts" class="see-more">See more</a>
			{:else}
				<p class="no-data">No recent payouts</p>
			{/if}
		</div>
	</div>
{/if}

<style>
	.loading-text { color: var(--muted); font-size: 15px; padding: 40px; text-align: center; }
	.welcome { font-size: 22px; font-weight: 500; color: var(--ink); margin-bottom: 20px; }
	.welcome strong { color: var(--hero-bg); }
	.tabs { display: flex; gap: 0; margin-bottom: 20px; border-bottom: 1px solid var(--line); }
	.tab {
		padding: 10px 20px;
		border: none;
		background: none;
		font-size: 14px;
		font-weight: 500;
		color: var(--muted);
		cursor: pointer;
		border-bottom: 2px solid transparent;
		margin-bottom: -1px;
		transition: all 0.15s;
	}
	.tab.active { color: var(--primary); border-bottom-color: var(--primary); font-weight: 600; }
	.tab:hover { color: var(--ink); }
	.filters-row {
		display: flex;
		align-items: center;
		gap: 12px;
		margin-bottom: 20px;
	}
	.date-range { display: flex; align-items: center; gap: 8px; }
	.date-input {
		padding: 6px 10px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 13px;
		color: var(--ink);
		background: #fff;
	}
	.date-sep { color: var(--muted); font-size: 13px; }
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
	.metrics-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 16px;
		margin-bottom: 24px;
	}
	.metric-card {
		padding: 20px;
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
	}
	.metric-label { display: block; font-size: 13px; color: var(--muted); margin-bottom: 6px; }
	.metric-value { font-size: 24px; font-weight: 700; color: var(--hero-bg); display: block; margin-bottom: 4px; }
	.metric-change { font-size: 12px; font-weight: 500; }
	.metric-change.positive { color: var(--primary-dark); }
	.metric-change.negative { color: #dc2626; }
	.charts-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 16px;
		margin-bottom: 24px;
	}
	.chart-card.wide { grid-column: 1 / -1; }
	.chart-card {
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		padding: 20px;
	}
	.chart-title { font-size: 14px; font-weight: 600; color: var(--hero-bg); margin: 0 0 16px; }
	.chart-subtitle { font-size: 11px; color: var(--muted); margin: 12px 0 0; }
	.no-data { color: var(--muted); font-size: 13px; text-align: center; padding: 30px 0; }
	.line-chart { width: 100%; height: 160px; }
	.chart-labels { display: flex; justify-content: space-between; font-size: 11px; color: var(--muted); margin-top: 4px; }
	.pie-container {
		display: flex;
		justify-content: center;
		position: relative;
		margin-bottom: 12px;
	}
	.pie {
		width: 120px;
		height: 120px;
		border-radius: 50%;
	}
	.pie-total {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		text-align: center;
	}
	.pie-total strong { display: block; font-size: 16px; color: var(--hero-bg); }
	.pie-total span { font-size: 11px; color: var(--muted); }
	.pie-legend { display: flex; flex-direction: column; gap: 6px; }
	.legend-item { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--ink); }
	.legend-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
	.legend-label { color: var(--muted); }
	.bar-chart {
		display: flex;
		justify-content: center;
		align-items: flex-end;
		gap: 24px;
		height: 100px;
		padding-top: 10px;
	}
	.bar-item { display: flex; flex-direction: column; align-items: center; gap: 6px; }
	.bar-track {
		width: 40px;
		height: 80px;
		background: #f1f5f9;
		border-radius: 4px;
		position: relative;
		display: flex;
		align-items: flex-end;
	}
	.bar-fill {
		width: 100%;
		background: #10b981;
		border-radius: 4px;
		transition: height 0.3s;
		min-height: 4px;
	}
	.bar-label { font-size: 11px; color: var(--muted); white-space: nowrap; }
	.bottom-grid { margin-bottom: 24px; }
	.card {
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		padding: 20px;
	}
	.card h3 { font-size: 14px; font-weight: 600; color: var(--hero-bg); margin: 0 0 16px; }
	.payout-list { display: flex; flex-direction: column; gap: 0; }
	.payout-item {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 10px 0;
		border-bottom: 1px solid #f1f5f9;
	}
	.payout-item:last-child { border-bottom: none; }
	.payout-info { display: flex; flex-direction: column; gap: 2px; }
	.payout-value { font-size: 14px; font-weight: 600; color: var(--ink); }
	.payout-date { font-size: 12px; color: var(--muted); }
	.payout-status {
		font-size: 12px;
		font-weight: 600;
		padding: 2px 10px;
		border-radius: 12px;
		background: #f1f5f9;
		color: var(--muted);
	}
	.payout-status.completed { background: #e6fcf0; color: var(--primary-dark); }
	.payout-status.pending { background: #fef3c7; color: #92400e; }
	.see-more {
		display: block;
		text-align: center;
		padding: 10px;
		font-size: 13px;
		color: var(--primary);
		font-weight: 600;
		text-decoration: none;
		margin-top: 4px;
		border-top: 1px solid var(--line);
	}
	.see-more:hover { text-decoration: underline; }
		.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
	@media (max-width: 768px) {
		.metrics-grid { grid-template-columns: 1fr; }
		.charts-grid { grid-template-columns: 1fr; }
		.chart-card.wide { grid-column: 1; }
	}
</style>
