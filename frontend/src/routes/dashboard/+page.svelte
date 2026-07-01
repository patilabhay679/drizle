<script>
	import { api } from '$lib/api';
	import { auth } from '$lib/stores/auth';
	import { onMount } from 'svelte';

	let metrics = $state(null);
	let charts = $state(null);
	let loading = $state(true);
	let error = $state('');
	let activeRange = $state('30d');
	let startDate = $state('');
	let endDate = $state('');
	let showCustom = $state(false);
	let barGranularity = $state('day');

	const ranges = [
		{ key: 'today', label: 'Today', days: 0 },
		{ key: '7d', label: '7D', days: 7 },
		{ key: '30d', label: '30D', days: 30 },
		{ key: '90d', label: '90D', days: 90 },
		{ key: 'custom', label: 'Custom', days: null },
	];

	const granularities = [
		{ key: 'day', label: 'Day' },
		{ key: 'week', label: 'Week' },
		{ key: 'month', label: 'Month' },
	];

	const availableGranularities = $derived.by(() => {
		if (activeRange === 'today' || activeRange === '7d') return ['day'];
		if (activeRange === '30d') return ['day', 'week'];
		return ['day', 'week', 'month'];
	});

	const resolvedGranularity = $derived(
		availableGranularities.includes(barGranularity) ? barGranularity : availableGranularities[0]
	);

	function rangeStart(days) {
		const d = new Date();
		d.setDate(d.getDate() - days);
		const y = d.getFullYear();
		const m = String(d.getMonth() + 1).padStart(2, '0');
		const day = String(d.getDate()).padStart(2, '0');
		return `${y}-${m}-${day}`;
	}

	function todayStr() {
		const d = new Date();
		const y = d.getFullYear();
		const m = String(d.getMonth() + 1).padStart(2, '0');
		const day = String(d.getDate()).padStart(2, '0');
		return `${y}-${m}-${day}`;
	}

	function selectRange(key) {
		activeRange = key;
		if (key === 'custom') {
			showCustom = true;
			return;
		}
		showCustom = false;
		const r = ranges.find((r) => r.key === key);
		if (r.days === 0) {
			startDate = todayStr();
			endDate = todayStr();
		} else {
			startDate = rangeStart(r.days);
			endDate = '';
		}
		refresh();
	}

	function selectGranularity(key) {
		barGranularity = key;
	}

	onMount(async () => {
		await refresh();
	});

	function fmt(n) {
		return (n ?? 0).toLocaleString('en-AE', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
	}

	function fmtInt(n) {
		return (n ?? 0).toLocaleString('en-AE');
	}

	function trendCls(change) {
		if (change > 0) return 'trend-up';
		if (change < 0) return 'trend-down';
		return 'trend-neutral';
	}

	function trendIcon(change) {
		if (change > 0) return '↑';
		if (change < 0) return '↓';
		return '—';
	}

	// Stacked area chart helpers
	let chartWidth = $state(620);
	let chartHeight = 180;
	let hoverIdx = $state(-1);
	let barWidth = $state(900);
	let barHeight = 200;
	let barHoverIdx = $state(-1);
	let cumulativeMode = $state('year');
	let selectedMonth = $state('');
	let yearData = $state(null);

	function getYearStart() {
		const now = new Date();
		return `${now.getFullYear()}-01-01`;
	}

	async function refresh() {
		loading = true;
		error = '';
		try {
			const [sd, ed] = startDate ? [startDate, endDate || undefined] : [undefined, undefined];
			const ys = getYearStart();
			const [m, c, y] = await Promise.all([
				api.getDashboardMetrics(sd, ed),
				api.getDashboardCharts(sd, ed, 'day'),
				api.getDashboardCharts(ys, ed || undefined, 'day'),
			]);
			metrics = m;
			charts = c;
			yearData = y;
			if (!selectedMonth && yearData?.volume_over_time?.length) {
				const months = [...new Set(yearData.volume_over_time.map(d => d.date.slice(0, 7)))];
				selectedMonth = months[months.length - 1];
			}
		} catch (e) {
			error = e.message || 'Something went wrong';
		} finally {
			loading = false;
		}
	}

	function setCumulativeMode(mode) {
		cumulativeMode = mode;
		if (mode === 'month' && yearData?.volume_over_time?.length) {
			const months = [...new Set(yearData.volume_over_time.map(d => d.date.slice(0, 7)))];
			if (!selectedMonth || !months.includes(selectedMonth)) {
				selectedMonth = months[months.length - 1];
			}
		}
	}

	let monthOptions = $derived(
		[...new Set((yearData?.volume_over_time ?? []).map(d => d.date.slice(0, 7)))].sort()
	);

	let cumulativeVolume = $derived.by(() => {
		const raw = yearData?.volume_over_time ?? [];
		let data = raw;
		if (cumulativeMode === 'month' && selectedMonth) {
			data = raw.filter(d => d.date.startsWith(selectedMonth));
		}
		let cumSuc = 0, cumRef = 0;
		return data.map(d => {
			cumSuc += d.successful;
			cumRef += d.refunded;
			return { date: d.date, successful: cumSuc, refunded: cumRef, total: cumSuc + cumRef };
		});
	});

	let maxVolume = $derived(
		cumulativeVolume.length
			? Math.max(...cumulativeVolume.map((d) => d.total), 1)
			: 1
	);

	let cumLabels = $derived.by(() => {
		const total = cumulativeVolume.length;
		if (!total) return [];
		if (cumulativeMode === 'year') {
			const months = new Map();
			for (let i = 0; i < total; i++) {
				const m = cumulativeVolume[i].date.slice(0, 7);
				if (!months.has(m)) months.set(m, i);
			}
			const shortMonths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
			return [...months].map(([m, i]) => ({
				label: shortMonths[+m.slice(5, 7) - 1] || m,
				left: (areaPadL + i / Math.max(total - 1, 1) * (chartWidth - areaPadL)) / chartWidth * 100,
			}));
		} else {
			const step = Math.max(1, Math.floor(total / 5));
			const labels = [];
			for (let i = 0; i < total; i += step) {
				labels.push({
					label: formatLabel(cumulativeVolume[i].date, 'day'),
					left: (areaPadL + i / Math.max(total - 1, 1) * (chartWidth - areaPadL)) / chartWidth * 100,
				});
			}
			if (labels.length && labels[labels.length - 1].left < 99) {
				labels.push({
					label: formatLabel(cumulativeVolume[total - 1].date, 'day'),
					left: 100,
				});
			}
			return labels;
		}
	});

	// Shared Y-axis tick helper
	function niceTicks(max) {
		if (max <= 0) return [];
		const roughStep = max / 5;
		const mag = Math.pow(10, Math.floor(Math.log10(roughStep)));
		const nice = [1, 2, 2.5, 5, 10].find(n => n * mag >= roughStep) * mag;
		const ticks = [];
		const top = Math.ceil(max / nice) * nice;
		for (let v = 0; v <= top + 0.01; v += nice) {
			ticks.push(Math.round(v * 100) / 100);
		}
		return ticks;
	}

	// Area chart Y-axis
	let areaPadL = 42;
	let areaPlotW = $derived(chartWidth - areaPadL);
	let areaTicks = $derived(niceTicks(maxVolume));

	function scaleX(i, total) {
		if (total <= 1) return areaPadL;
		return areaPadL + (i / (total - 1)) * (chartWidth - areaPadL);
	}

	function scaleY(val) {
		return Math.max(2, chartHeight - 10 - (val / maxVolume) * (chartHeight - 30));
	}

	function areaPath(data, key) {
		if (!data?.length) return '';
		const top = data.map((d, i) => `${i === 0 ? 'M' : 'L'} ${scaleX(i, data.length)} ${scaleY(d[key])}`);
		const bottom = data.map((d, i) => `L ${scaleX(data.length - 1 - i, data.length)} ${scaleY(0)}`);
		return `${top.join(' ')} ${bottom.join(' ')} Z`;
	}

	function linePath(data, key) {
		if (!data?.length) return '';
		return data.map((d, i) => `${i === 0 ? 'M' : 'L'} ${scaleX(i, data.length)} ${scaleY(d[key])}`).join(' ');
	}

	// Vertical bar chart helpers
	let barMaxVol = $derived(barData.length ? Math.max(...barData.map(d => d.total), 1) : 1);
	let barPadL = 26;
	let barPadR = 12;
	let barPadT = 16;
	let barPadB = 24;
	let barPlotW = $derived(barWidth - barPadL - barPadR);
	let barPlotH = $derived(barHeight - barPadT - barPadB);
	let barTicks = $derived(niceTicks(barMaxVol));
	function barX(i, total) {
		if (total <= 1) return barPadL;
		return barPadL + (i / total) * barPlotW;
	}
	function barWidthPx(total) {
		if (total <= 1) return barPlotW;
		return Math.max((barPlotW / total) * 0.55, 4);
	}
	function barY(val) {
		return Math.max(2, barPadT + barPlotH - (val / barMaxVol) * barPlotH);
	}
	function barH(val) {
		return (val / barMaxVol) * barPlotH;
	}

	// Payment methods — colors and helpers
	const methodColors = {
		card: '#1a1f71',
		apple_pay: '#000',
		google_pay: '#4285f4',
		taby: '#6f2dbd',
		aani: '#d41139',
	};
	function methodColor(name) { return methodColors[name] ?? '#64748b'; }

	// Card schemes — brand-tinted initials + coloring
	const schemeMeta = {
		'Visa': { color: '#1a1f71', short: 'V' },
		'Mastercard': { color: '#eb001b', short: 'MC' },
		'Amex': { color: '#2e77bc', short: 'AX' },
		'Meeza/Jaywan': { color: '#0b7f4f', short: 'MJ' },
	};
	function schemeMetaFor(name) { return schemeMeta[name] ?? { color: '#475569', short: name?.charAt(0) ?? '?' }; }

	function authRateClass(rate) {
		if (rate >= 95) return 'auth-good';
		if (rate >= 85) return 'auth-warn';
		return 'auth-bad';
	}
	function authRateLabel(rate) {
		if (rate >= 95) return 'Excellent';
		if (rate >= 85) return 'Below benchmark';
		return 'Needs attention';
	}

	// Format labels per granularity
	function formatLabel(dateStr, grain) {
		if (!dateStr) return '';
		if (grain === 'day') {
			const m = dateStr.slice(5, 7);
			const d = dateStr.slice(8, 10);
			const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
			return `${+d} ${months[+m - 1]}`;
		}
		if (grain === 'week') {
			const [, y, w] = dateStr.match(/^(\d{4})-W(\d{2})$/);
			return `W${+w} ${y}`;
		}
		if (grain === 'month') {
			const m = dateStr.slice(5, 7);
			const y = dateStr.slice(0, 4);
			const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
			return `${months[+m - 1]} ${y}`;
		}
		return dateStr;
	}

	// Aggregation helpers for bar chart
	function getISOWeek(dateStr) {
		const dt = new Date(dateStr + 'T00:00:00');
		const dayNum = dt.getUTCDay() || 7;
		dt.setUTCDate(dt.getUTCDate() + 4 - dayNum);
		const y = dt.getUTCFullYear();
		const start = new Date(Date.UTC(y, 0, 1));
		const week = Math.ceil((((dt - start) / 86400000) + 1) / 7);
		return `${y}-W${String(week).padStart(2, '0')}`;
	}

	function aggregateVolume(data, grain) {
		if (!data?.length) return [];
		const groups = {};
		for (const d of data) {
			const key = grain === 'day' ? d.date : grain === 'week' ? getISOWeek(d.date) : d.date.slice(0, 7);
			if (!groups[key]) groups[key] = { date: key, successful: 0, refunded: 0, total: 0 };
			groups[key].successful += d.successful;
			groups[key].refunded += d.refunded;
			groups[key].total += d.total;
		}
		return Object.values(groups).sort((a, b) => a.date.localeCompare(b.date));
	}

	let barData = $derived(aggregateVolume(charts?.volume_over_time, resolvedGranularity));

	// Period comparison: split volume data in half, compare totals
	let periodComparison = $derived.by(() => {
		const vd = charts?.volume_over_time ?? [];
		if (vd.length < 2) return null;
		const mid = Math.floor(vd.length / 2);
		const current = vd.slice(mid).reduce((s, d) => s + d.total, 0);
		const prior = vd.slice(0, mid).reduce((s, d) => s + d.total, 0);
		if (prior === 0) return null;
		return {
			current,
			prior,
			change: Math.round(((current - prior) / prior) * 100),
		};
	});

	let totalMethodVolume = $derived(charts?.payment_methods?.reduce((s, m) => s + m.volume, 0) ?? 1);

	// Smart Insights — computed client-side from data we already fetch
	let volumeData = $derived(charts?.volume_over_time ?? []);

	let bestDay = $derived.by(() => {
		if (!volumeData.length) return null;
		return volumeData.reduce((best, d) => (d.successful > (best?.successful ?? -1) ? d : best), volumeData[0]);
	});

	let slowestDay = $derived.by(() => {
		if (!volumeData.length) return null;
		return volumeData.reduce((worst, d) => (d.successful < (worst?.successful ?? Infinity) && d.successful > 0 ? d : worst), volumeData[0]);
	});

	let weekOverWeek = $derived.by(() => {
		if (volumeData.length < 14) return null;
		const last7 = volumeData.slice(-7).reduce((s, d) => s + d.successful, 0);
		const prev7 = volumeData.slice(-14, -7).reduce((s, d) => s + d.successful, 0);
		if (prev7 === 0) return null;
		return Math.round(((last7 - prev7) / prev7) * 100);
	});

	let revenueAtRisk = $derived.by(() => {
		const ar = metrics?.authorization_rate?.value ?? 100;
		const gross = metrics?.gross_volume?.value ?? 0;
		if (ar >= 95) return null;
		const lossPct = (95 - ar) / 100;
		return { value: Math.round(gross * lossPct * 10) / 10, currency: metrics?.gross_volume?.currency || 'AED' };
	});

	let topMethod = $derived(charts?.payment_methods?.[0] ?? null);
</script>

<svelte:head>
	<title>Dashboard | DrizlePay</title>
</svelte:head>

{#if loading && !metrics}
	<div class="dash-header">
		<div class="skeleton" style="width: 340px; height: 20px; border-radius: 6px;"></div>
		<div class="skeleton" style="width: 200px; height: 34px; border-radius: 8px;"></div>
	</div>
	<div class="kpi-row">
		{#each { length: 5 } as _}
			<div class="kpi-card">
				<div class="skeleton" style="width: 80px; height: 12px; border-radius: 4px; margin-bottom: 8px;"></div>
				<div class="skeleton" style="width: 140px; height: 24px; border-radius: 6px;"></div>
			</div>
		{/each}
	</div>
	<div class="panel" style="margin-bottom: 20px; padding: 18px;">
		<div class="panel-head">
			<div class="skeleton" style="width: 160px; height: 16px; border-radius: 6px;"></div>
			<div class="skeleton" style="width: 120px; height: 28px; border-radius: 6px;"></div>
		</div>
		<div class="skeleton" style="width: 100%; height: 200px; border-radius: 8px;"></div>
	</div>
	<div class="chart-row">
		<div class="vol-col">
			<div class="panel" style="padding: 18px;">
				<div class="panel-head">
					<div class="skeleton" style="width: 200px; height: 16px; border-radius: 6px;"></div>
				</div>
				<div class="skeleton" style="width: 100%; height: 180px; border-radius: 8px;"></div>
			</div>
		</div>
		<div class="panel" style="padding: 18px;">
			<div class="panel-head">
				<div class="skeleton" style="width: 140px; height: 16px; border-radius: 6px;"></div>
			</div>
			{#each { length: 3 } as _}
				<div class="pm-item">
					<div class="skeleton" style="width: 100%; height: 32px; border-radius: 4px; margin-bottom: 6px;"></div>
				</div>
			{/each}
		</div>
		<div class="panel" style="padding: 18px;">
			<div class="panel-head">
				<div class="skeleton" style="width: 140px; height: 16px; border-radius: 6px;"></div>
			</div>
			{#each { length: 3 } as _}
				<div class="scheme-card">
					<div class="skeleton" style="width: 100%; height: 60px; border-radius: 4px;"></div>
				</div>
			{/each}
		</div>
	</div>
	<div class="bottom-row">
		<div class="panel" style="padding: 18px;">
			<div class="panel-head">
				<div class="skeleton" style="width: 160px; height: 16px; border-radius: 6px;"></div>
			</div>
			<div class="skeleton" style="width: 100%; height: 120px; border-radius: 8px;"></div>
		</div>
		<div class="panel" style="padding: 18px;">
			<div class="panel-head">
				<div class="skeleton" style="width: 120px; height: 16px; border-radius: 6px;"></div>
			</div>
			{#each { length: 3 } as _}
				<div class="insight-card">
					<div class="skeleton" style="flex: 1; height: 40px; border-radius: 4px;"></div>
				</div>
			{/each}
		</div>
	</div>
{:else if error}
	<div class="error-banner">{error}</div>
{:else}
	<!-- Header -->
	<div class="dash-header">
		<p class="sub">Welcome back, <strong>{auth.merchant?.name || 'Merchant'}</strong> — here's your business at a glance.</p>
		<div class="range-bar">
			{#each ranges as r}
				<button
					class="range-btn"
					class:active={activeRange === r.key}
					onclick={() => selectRange(r.key)}
				>{r.label}</button>
			{/each}
		</div>
	</div>

	{#if showCustom}
		<div class="custom-bar">
			<input type="date" bind:value={startDate} class="date-input" />
			<span>to</span>
			<input type="date" bind:value={endDate} class="date-input" />
			<button class="apply-btn" onclick={refresh}>Apply</button>
		</div>
	{/if}

	<!-- KPI Row -->
	<div class="kpi-row">
		<div class="kpi-card highlight">
			<div class="kpi-top">
				<span class="kpi-label">Gross Volume</span>
				<span class="kpi-trend {trendCls(metrics?.gross_volume?.change)}">
					{trendIcon(metrics?.gross_volume?.change)} {Math.abs(metrics?.gross_volume?.change || 0)}%
				</span>
			</div>
			<div class="kpi-value">{metrics?.gross_volume?.currency || 'AED'} {fmt(metrics?.gross_volume?.value)}</div>
		</div>
		<div class="kpi-card">
			<div class="kpi-top">
				<span class="kpi-label">Net Volume</span>
				<span class="kpi-trend {trendCls(metrics?.net_volume?.change)}">
					{trendIcon(metrics?.net_volume?.change)} {Math.abs(metrics?.net_volume?.change || 0)}%
				</span>
			</div>
			<div class="kpi-value">{metrics?.net_volume?.currency || 'AED'} {fmt(metrics?.net_volume?.value)}</div>
		</div>
		<div class="kpi-card">
			<div class="kpi-top">
				<span class="kpi-label">Auth Rate</span>
				<span class="kpi-trend {trendCls(metrics?.authorization_rate?.change)}">
					{trendIcon(metrics?.authorization_rate?.change)} {Math.abs(metrics?.authorization_rate?.change || 0)}pp
				</span>
			</div>
			<div class="kpi-value">{metrics?.authorization_rate?.value || 0}%</div>
		</div>
		<div class="kpi-card">
			<div class="kpi-top">
				<span class="kpi-label">Avg Order Value</span>
				<span class="kpi-trend {trendCls(metrics?.average_order_value?.change)}">
					{trendIcon(metrics?.average_order_value?.change)} {Math.abs(metrics?.average_order_value?.change || 0)}%
				</span>
			</div>
			<div class="kpi-value">{metrics?.average_order_value?.currency || 'AED'} {fmt(metrics?.average_order_value?.value)}</div>
		</div>
		<div class="kpi-card">
			<div class="kpi-top">
				<span class="kpi-label">Highest Order Value</span>
			</div>
			<div class="kpi-value">{metrics?.highest_order_value?.currency || 'AED'} {fmt(metrics?.highest_order_value?.value)}</div>
		</div>
	</div>

	<!-- Volume Breakdown (bar chart with granularity toggle) — full width -->
	<div class="panel bar-panel bar-panel-full">
		<div class="panel-head">
			<h3>Volume Breakdown</h3>
			<div class="chart-head-right">
				<div class="legend-inline">
					<span class="legend-swatch green"></span> Successful
					<span class="legend-swatch" style="background:#c02666"></span> Refunded
				</div>
				<div class="granularity-bar">
					{#each granularities as g}
						{#if availableGranularities.includes(g.key)}
							<button
								class="gran-btn"
								class:active={resolvedGranularity === g.key}
								onclick={() => selectGranularity(g.key)}
							>{g.label}</button>
						{/if}
					{/each}
				</div>
			</div>
		</div>
	{#if barData.length}
		<div class="bar-chart-wrap" bind:clientWidth={barWidth}>
			<svg viewBox="0 0 {barWidth} {barHeight}" class="bar-chart-svg" preserveAspectRatio="none" role="img" aria-label="Volume breakdown bar chart showing successful and refunded transactions per {resolvedGranularity}">
				<!-- Y-axis grid lines and labels -->
				<g aria-hidden="true">
				{#each barTicks as tick}
					{@const ty = barY(tick)}
					<line x1={barPadL} y1={ty} x2={barWidth} y2={ty} stroke="#e2e8f0" stroke-width="1" />
				{/each}
				</g>
				<!-- Y-axis line -->
				<line x1={barPadL} y1={barTicks.length > 1 ? barY(barTicks[barTicks.length - 1]) : barPadT} x2={barPadL} y2={barPadT + barPlotH} stroke="#cbd5e1" stroke-width="1" aria-hidden="true" />
				<!-- X-axis baseline -->
				<line x1={barPadL} y1={barPadT + barPlotH} x2={barWidth} y2={barPadT + barPlotH} stroke="#cbd5e1" stroke-width="1" aria-hidden="true" />
				<!-- Bars -->
				{#each barData as b, i}
					{@const bx = barX(i, barData.length)}
					{@const bw = barWidthPx(barData.length)}
					{@const halfW = Math.max(bw * 0.5, 2)}
					{@const sucX = bx}
					{@const refX = bx + halfW}
					{@const sucH = barH(b.successful)}
					{@const refH = barH(b.refunded)}
					{@const sucY = barY(b.successful)}
					{@const refY = barY(b.refunded)}
					<rect x={sucX} y={sucY} width={halfW} height={Math.max(sucH, 1)} fill="#10b981" opacity={barHoverIdx === i ? 1 : 0.85} aria-hidden="true" />
					<rect x={refX} y={refY} width={halfW} height={Math.max(refH, 1)} fill="#c02666" opacity={barHoverIdx === i ? 1 : 0.85} aria-hidden="true" />
				{/each}
			</svg>
			<div class="bar-yaxis" aria-hidden="true">
				{#each barTicks as tick}
					{@const ty = barY(tick)}
					<span style="top: {ty / barHeight * 100}%">{fmtInt(tick)}</span>
				{/each}
			</div>
			<div class="bar-hover-overlay" style="left: {barPadL}px; width: {barPlotW}px; height: {barHeight}px;">
				{#each barData as _, i}
					{@const leftPct = barData.length <= 1 ? 50 : (i / barData.length) * 100}
					<div
						class="bar-zone"
						style="left: {leftPct}%;"
						onmouseenter={() => barHoverIdx = i}
						onmouseleave={() => barHoverIdx = -1}
					></div>
				{/each}
			{#if barHoverIdx >= 0 && barData[barHoverIdx]}
				{@const ttLeft = barX(barHoverIdx, barData.length) + barWidthPx(barData.length) * 0.5}
				<div class="tooltip" style="position: absolute; left: {ttLeft}px; top: 100%; transform: translateX(-50%); margin-top: 4px;" role="status" aria-live="polite" aria-atomic="true">
					<span class="tt-date">{formatLabel(barData[barHoverIdx].date, resolvedGranularity)}</span>
					<span class="tt-row"><span class="tt-dot green"></span> Successful: AED {fmt(barData[barHoverIdx].successful)}</span>
					<span class="tt-row"><span class="tt-dot red"></span> Refunded: AED {fmt(barData[barHoverIdx].refunded)}</span>
					<span class="tt-row"><strong>Total: AED {fmt(barData[barHoverIdx].total)}</strong></span>
				</div>
			{/if}
		</div>
		</div>
		<div class="bar-xaxis">
			{#each barData as b, i}
				{@const barCx = (barPadL + (i / barData.length) * barPlotW + Math.max(barPlotW / barData.length - 4, 4) / 2) / barWidth * 100}
				<span style="left: {barCx}%">{formatLabel(b.date, resolvedGranularity)}</span>
			{/each}
		</div>
	{:else}
		<p class="no-data">No data for this granularity</p>
	{/if}
	</div>

	<!-- Charts Row -->
	<div class="chart-row">
		<div class="vol-col">
			<!-- Volume Chart (cumulative area chart) -->
			<div class="panel chart-panel">
				<div class="panel-head">
					<h3>Cumulative Volume Over Time</h3>
					<div class="chart-head-right">
						<div class="legend-inline">
							<span class="legend-swatch green"></span> Successful
							<span class="legend-swatch red"></span> Refunded
						</div>
						<div class="cum-mode-bar">
							<button class="cum-mode-btn" class:active={cumulativeMode === 'year'} onclick={() => setCumulativeMode('year')}>Year</button>
							<button class="cum-mode-btn" class:active={cumulativeMode === 'month'} onclick={() => setCumulativeMode('month')}>Month</button>
						</div>
						{#if cumulativeMode === 'month'}
							<select class="cum-month-select" bind:value={selectedMonth}>
								{#each monthOptions as m}
									<option value={m}>{m}</option>
								{/each}
							</select>
						{/if}
					</div>
				</div>
				{#if cumulativeVolume.length}
					<div class="chart-wrap" bind:clientWidth={chartWidth}>
						<svg viewBox="0 0 {chartWidth} {chartHeight}" class="vol-chart" preserveAspectRatio="none" role="img" aria-label="Cumulative volume over time chart showing successful and refunded transactions">
							<defs>
								<linearGradient id="successGrad" x1="0" y1="0" x2="0" y2="1">
									<stop offset="0%" stop-color="#10b981" stop-opacity="0.3" />
									<stop offset="100%" stop-color="#10b981" stop-opacity="0.02" />
								</linearGradient>
								<linearGradient id="refundGrad" x1="0" y1="0" x2="0" y2="1">
									<stop offset="0%" stop-color="#ef4444" stop-opacity="0.2" />
									<stop offset="100%" stop-color="#ef4444" stop-opacity="0.02" />
								</linearGradient>
							</defs>
							<!-- Y-axis grid lines and labels -->
							<g aria-hidden="true">
							{#each areaTicks as tick}
								{@const ty = scaleY(tick)}
								<line x1={areaPadL} y1={ty} x2={chartWidth} y2={ty} stroke="#e2e8f0" stroke-width="1" />
								<text x={areaPadL - 6} y={ty + 4} text-anchor="end" fill="#64748b" font-size="11" font-weight="600" font-family="Urbanist, system-ui, sans-serif">{fmtInt(tick)}</text>
							{/each}
							</g>
							<!-- Y-axis line -->
							<line x1={areaPadL} y1={areaTicks.length > 1 ? scaleY(areaTicks[areaTicks.length - 1]) : scaleY(maxVolume)} x2={areaPadL} y2={scaleY(0)} stroke="#cbd5e1" stroke-width="1" aria-hidden="true" />
							<!-- X-axis baseline -->
							<line x1={areaPadL} y1={scaleY(0)} x2={chartWidth} y2={scaleY(0)} stroke="#cbd5e1" stroke-width="1" aria-hidden="true" />
							<!-- Area paths -->
							<path d={areaPath(cumulativeVolume, 'successful')} fill="url(#successGrad)" aria-hidden="true" />
							<path d={linePath(cumulativeVolume, 'successful')} fill="none" stroke="#10b981" stroke-width="2" aria-hidden="true" />
							<path d={areaPath(cumulativeVolume, 'refunded')} fill="url(#refundGrad)" aria-hidden="true" />
							<path d={linePath(cumulativeVolume, 'refunded')} fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4 3" aria-hidden="true" />
							{#if hoverIdx >= 0 && cumulativeVolume[hoverIdx]}
								<g aria-hidden="true">
								<line x1={scaleX(hoverIdx, cumulativeVolume.length)} y1={scaleY(maxVolume)} x2={scaleX(hoverIdx, cumulativeVolume.length)} y2={scaleY(0)} stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3" />
								<circle cx={scaleX(hoverIdx, cumulativeVolume.length)} cy={scaleY(cumulativeVolume[hoverIdx].successful)} r="4" fill="#10b981" stroke="#fff" stroke-width="2" />
								</g>
							{/if}
					</svg>
					<div class="hover-overlay" style="left: {areaPadL}px; width: {chartWidth - areaPadL}px; height: {chartHeight}px;">
						{#each cumulativeVolume as _, i}
							<div
								class="hover-zone"
								style="left: {(i / Math.max(cumulativeVolume.length - 1, 1)) * 100}%;"
								onmouseenter={() => hoverIdx = i}
								onmouseleave={() => hoverIdx = -1}
							></div>
						{/each}
					{#if hoverIdx >= 0 && cumulativeVolume[hoverIdx]}
						{@const ttLeft = scaleX(hoverIdx, cumulativeVolume.length)}
						<div class="tooltip" style="position: absolute; left: {ttLeft}px; top: 100%; transform: translateX(-50%); margin-top: 4px;" role="status" aria-live="polite" aria-atomic="true">
							<span class="tt-date">Cumulative to {cumulativeVolume[hoverIdx].date}</span>
							<span class="tt-row"><span class="tt-dot green"></span> Successful: AED {fmt(cumulativeVolume[hoverIdx].successful)}</span>
							<span class="tt-row"><span class="tt-dot red"></span> Refunded: AED {fmt(cumulativeVolume[hoverIdx].refunded)}</span>
						</div>
					{/if}
				</div>
				</div>
				<div class="chart-xaxis">
					{#each cumLabels as cl}
						<span style="left: {cl.left}%">{cl.label}</span>
					{/each}
				</div>
				{#if periodComparison}
					<div class="comparison-row">
							<span class="comp-label">vs prior period</span>
							<span class="comp-value">
								{periodComparison.change >= 0 ? '+' : ''}{periodComparison.change}%
							</span>
							<span class="comp-bar-wrap">
								<span class="comp-bar {periodComparison.change >= 0 ? 'up' : 'down'}" style="width: {Math.min(Math.abs(periodComparison.change), 100)}%"></span>
							</span>
							<span class="comp-detail">
								AED {fmt(periodComparison.current)} vs AED {fmt(periodComparison.prior)}
							</span>
						</div>
					{/if}
				{:else}
					<p class="no-data">No volume data for this period</p>
				{/if}
			</div>
		</div>

		<!-- Payment Methods -->
		<div class="panel">
			<div class="panel-head">
				<h3>Payment Methods</h3>
				<span class="panel-sub">Share of volume by method</span>
			</div>
			{#if charts?.payment_methods?.length}
				<div class="pm-list">
					{#each charts.payment_methods as m, i}
						{@const share = Math.round((m.volume / Math.max(totalMethodVolume, 1)) * 100)}
						<div class="pm-item">
							<div class="pm-head">
								<span class="pm-brand" style="background: {methodColor(m.name)}">{m.name?.charAt(0)?.toUpperCase()}</span>
								<span class="pm-name">{m.name?.replace('_', ' ')}</span>
								<span class="pm-share">{share}%</span>
							</div>
							<div class="pm-bar-wrap">
								<div class="pm-bar" style="width: {share}%; background: {methodColor(m.name)}"></div>
							</div>
							<div class="pm-meta">
								<span>AED {fmt(m.volume)} · {m.count} txns</span>
								<span class="pm-aov">AOV AED {fmt(m.aov)}</span>
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<p class="no-data">No data</p>
			{/if}
		</div>

		<!-- Card Schemes Performance -->
		<div class="panel">
			<div class="panel-head">
				<h3>Card Scheme Performance</h3>
				<span class="panel-sub">Auth rate per scheme</span>
			</div>
			{#if charts?.top_schemes?.length}
				<div class="scheme-cards">
					{#each charts.top_schemes as s}
						{@const meta = schemeMetaFor(s.name)}
						<div class="scheme-card">
							<div class="sc-top">
								<span class="sc-badge" style="background: {meta.color}">{meta.short}</span>
								<span class="sc-name">{s.name}</span>
							</div>
							<div class="sc-auth">
								<div class="sc-auth-bar">
									<div class="sc-auth-fill {authRateClass(s.auth_rate)}" style="width: {s.auth_rate}%"></div>
								</div>
								<strong class="sc-auth-val {authRateClass(s.auth_rate)}">{s.auth_rate}%</strong>
							</div>
							<span class="sc-auth-label {authRateClass(s.auth_rate)}">{authRateLabel(s.auth_rate)}</span>
							<div class="sc-stats">
								<div><strong>AED {fmt(s.volume)}</strong><span>Volume</span></div>
								<div><strong>{s.count}</strong><span>Attempts</span></div>
								<div><strong>{s.success_count}</strong><span>Approved</span></div>
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<p class="no-data">No scheme data</p>
			{/if}
		</div>
	</div>

	<!-- Balance & Smart Insights -->
	<div class="bottom-row">
		<!-- Balance -->
		<div class="panel balance-panel">
			<div class="panel-head">
				<h3>Balance & Settlement</h3>
				<a href="/dashboard/payouts" class="link-more">View payouts →</a>
			</div>
			{#if metrics?.balance}
				<div class="balance-stack">
					<div class="balance-item highlight">
						<span class="bal-label">Available for Payout</span>
						<strong class="bal-value">{metrics.balance.available.currency} {fmt(metrics.balance.available.value)}</strong>
					</div>
					<div class="balance-row">
						<div class="balance-item sm">
							<span class="bal-label">Pending Payouts</span>
							<strong class="bal-value-sm">{metrics.balance.pending_payouts.currency} {fmt(metrics.balance.pending_payouts.value)}</strong>
						</div>
						<div class="balance-item sm">
							<span class="bal-label">Next Payout</span>
							<strong class="bal-value-date">{metrics.balance.next_payout_date}</strong>
						</div>
					</div>
				</div>
			{/if}
		</div>

		<!-- Smart Insights -->
		<div class="panel insights-panel">
			<div class="panel-head">
				<h3>Smart Insights</h3>
			</div>
			<div class="insights-list">
				{#if weekOverWeek !== null}
					<div class="insight-card {weekOverWeek >= 0 ? 'positive' : 'negative'}">
						<span class="insight-icon">{weekOverWeek >= 0 ? '📈' : '📉'}</span>
						<div class="insight-body">
							<strong class="insight-headline">
								{weekOverWeek >= 0 ? 'Volume is trending up' : 'Volume is trending down'}
								{weekOverWeek >= 0 ? '+' : ''}{weekOverWeek}% this week
							</strong>
							<span class="insight-sub">Comparing last 7 days vs the prior 7 days</span>
						</div>
					</div>
				{/if}

				{#if bestDay}
					<div class="insight-card neutral">
						<span class="insight-icon">🏆</span>
						<div class="insight-body">
							<strong class="insight-headline">Best day: {bestDay.date?.slice(5)}</strong>
							<span class="insight-sub">AED {fmt(bestDay.successful)} across {bestDay.count} successful payments — schedule promotions on similar days</span>
						</div>
					</div>
				{/if}

				{#if revenueAtRisk}
					<div class="insight-card warning">
						<span class="insight-icon">⚠️</span>
						<div class="insight-body">
							<strong class="insight-headline">{revenueAtRisk.currency} {fmt(revenueAtRisk.value)} at risk from declined cards</strong>
							<span class="insight-sub">Auth rate of {metrics?.authorization_rate?.value ?? 0}% is below 95% benchmark — recovering declines could unlock this revenue</span>
						</div>
					</div>
				{/if}

				{#if (metrics?.refund_rate?.value ?? 0) > 10}
					<div class="insight-card warning">
						<span class="insight-icon">↩️</span>
						<div class="insight-body">
							<strong class="insight-headline">Refund rate ({metrics.refund_rate.value}%) is high</strong>
							<span class="insight-sub">Industry norm is 3–5%. Investigate driving causes — item, dispute, fraud?</span>
						</div>
					</div>
				{/if}

				{#if (metrics?.refund_rate?.value ?? 0) <= 10 && !revenueAtRisk}
					<div class="insight-card positive">
						<span class="insight-icon">✅</span>
						<div class="insight-body">
							<strong class="insight-headline">All systems healthy</strong>
							<span class="insight-sub">Auth rate above 95% and refund rate within industry norm — keep up the good work</span>
						</div>
					</div>
				{/if}

				{#if topMethod}
					<div class="insight-card neutral">
						<span class="insight-icon">💳</span>
						<div class="insight-body">
							<strong class="insight-headline">{topMethod.name} drives {topMethod.count} of your payments</strong>
							<span class="insight-sub">AED {fmt(topMethod.volume)} processed — your customers favour this method</span>
						</div>
					</div>
				{/if}
			</div>
		</div>
	</div>
{/if}

<style>
	.skeleton {
		background: linear-gradient(90deg, #e2e8f0 25%, #f1f5f9 50%, #e2e8f0 75%);
		background-size: 200% 100%;
		animation: skeleton-shimmer 1.5s ease-in-out infinite;
	}
	@keyframes skeleton-shimmer {
		0% { background-position: 200% 0; }
		100% { background-position: -200% 0; }
	}
	.loading-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 300px;
		gap: 12px;
	}
	.spinner {
		width: 28px;
		height: 28px;
		border: 3px solid var(--line, #e2e8f0);
		border-top-color: #10b981;
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}
	@keyframes spin { to { transform: rotate(360deg); } }
	.loading-state p { color: var(--muted, #94a3b8); font-size: 14px; margin: 0; }

	.dash-header {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
		margin-bottom: 24px;
		flex-wrap: wrap;
		gap: 16px;
	}
	.dash-header .sub { font-size: 15px; font-weight: 500; color: var(--muted, #94a3b8); margin: 0; }
	.dash-header .sub strong { color: var(--ink, #1e293b); }

	.range-bar { display: flex; gap: 4px; background: #fff; border: 1px solid var(--line, #e2e8f0); border-radius: 8px; padding: 4px; }
	.range-btn {
		padding: 6px 14px;
		border: none;
		background: none;
		font-size: 13px;
		font-weight: 600;
		color: var(--muted, #94a3b8);
		cursor: pointer;
		border-radius: 5px;
		transition: all 0.15s;
	}
	.range-btn.active { background: #06162c; color: #fff; }
	.range-btn:hover:not(.active) { background: #f1f5f9; }

	.custom-bar { display: flex; align-items: center; gap: 8px; margin-bottom: 16px; }
	.date-input { padding: 6px 10px; border: 1px solid var(--line, #e2e8f0); border-radius: 6px; font-size: 13px; color: var(--ink, #1e293b); }
	.apply-btn { padding: 6px 16px; border: none; background: #10b981; color: #fff; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer; }

	.error-banner { padding: 12px 16px; background: #fef2f2; color: #dc2626; border-radius: 8px; font-size: 14px; }

	/* KPI Cards */
	.kpi-row {
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		gap: 14px;
		margin-bottom: 20px;
	}
	.kpi-card {
		background: #fff;
		border: 1px solid var(--line, #e2e8f0);
		border-radius: 10px;
		padding: 16px 14px;
		transition: box-shadow 0.15s;
	}
	.kpi-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
	.kpi-card.highlight { border-color: #10b981; background: linear-gradient(135deg, #fff, #f0fdf4); }
	.kpi-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; }
	.kpi-label { font-size: 11px; font-weight: 600; color: var(--muted, #94a3b8); text-transform: uppercase; letter-spacing: 0.05em; }
	.kpi-trend { font-size: 11px; font-weight: 600; padding: 2px 6px; border-radius: 4px; white-space: nowrap; }
	.trend-up { color: #10b981; background: #f0fdf4; }
	.trend-down { color: #dc2626; background: #fef2f2; }
	.trend-neutral { color: var(--muted, #94a3b8); background: #f8fafc; }
	.kpi-value { font-size: 20px; font-weight: 700; color: var(--hero-bg, #06162c); line-height: 1.3; }
	.kpi-sub { font-size: 11px; color: var(--muted, #94a3b8); margin-top: 2px; }

	/* Chart Panels */
	.chart-row {
		display: grid;
		grid-template-columns: 2fr 1fr 1.3fr;
		gap: 16px;
		margin-bottom: 20px;
	}
	.vol-col { display: flex; flex-direction: column; gap: 16px; }
	.bar-panel-full { margin-bottom: 20px; }
	.panel {
		background: #fff;
		border: 1px solid var(--line, #e2e8f0);
		border-radius: 10px;
		padding: 18px;
	}
	.panel-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px; }
	.panel-head h3 { font-size: 14px; font-weight: 600; color: var(--hero-bg, #06162c); margin: 0; }
	.chart-head-right { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
	.granularity-bar { display: flex; gap: 2px; background: #f1f5f9; border-radius: 6px; padding: 2px; }
	.cum-mode-bar { display: flex; gap: 2px; background: #f1f5f9; border-radius: 6px; padding: 2px; }
	.cum-mode-btn { border: none; background: transparent; padding: 4px 10px; font-size: 11px; font-weight: 600; color: #94a3b8; border-radius: 4px; cursor: pointer; transition: all 0.15s; }
	.cum-mode-btn.active { background: #fff; color: #06162c; box-shadow: 0 1px 2px rgba(0,0,0,0.08); }
	.cum-month-select { border: 1px solid #e2e8f0; border-radius: 6px; padding: 4px 8px; font-size: 11px; font-weight: 600; color: #06162c; background: #fff; cursor: pointer; }
	.gran-btn {
		padding: 3px 10px; border: none; background: none; font-size: 11px; font-weight: 600;
		color: var(--muted, #94a3b8); cursor: pointer; border-radius: 4px; transition: all 0.15s;
	}
	.gran-btn.active { background: #fff; color: var(--hero-bg, #06162c); box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
	.gran-btn:hover:not(.active) { color: var(--ink, #1e293b); }
	.panel-sub { font-size: 11px; color: var(--muted, #94a3b8); font-weight: 500; }
	.legend-inline { display: flex; gap: 12px; font-size: 11px; color: var(--muted, #94a3b8); font-weight: 500; }
	.legend-swatch { width: 10px; height: 10px; border-radius: 2px; display: inline-block; margin-right: 4px; vertical-align: middle; }
	.legend-swatch.green { background: #10b981; }
	.legend-swatch.red { background: #ef4444; }
	.chart-panel .chart-wrap { position: relative; }
	.vol-chart { width: 100%; height: 180px; }
	.hover-overlay { position: absolute; top: 0; left: 0; display: flex; justify-content: space-between; pointer-events: none; }
	.hover-zone { width: 30px; height: 100%; margin-left: -15px; pointer-events: auto; }
	.tooltip {
		background: #06162c; color: #fff; border-radius: 8px; padding: 10px 14px;
		font-size: 12px; display: inline-flex; flex-direction: column; gap: 4px;
		margin-top: 8px;
	}
	.tt-date { font-weight: 600; margin-bottom: 2px; }
	.tt-row { display: flex; align-items: center; gap: 6px; }
	.tt-dot { width: 6px; height: 6px; border-radius: 50%; }
	.tt-dot.green { background: #10b981; }
	.tt-dot.red { background: #ef4444; }
	.chart-xaxis { position: relative; height: 18px; margin-top: 6px; border-top: 1px solid #e2e8f0; }
	.chart-xaxis span { position: absolute; transform: translateX(-50%); font-size: 11px; font-weight: 500; color: var(--muted, #94a3b8); white-space: nowrap; }
	.no-data { color: var(--muted, #94a3b8); font-size: 13px; text-align: center; padding: 40px 0; }
	.comparison-row {
		display: flex; align-items: center; gap: 10px; margin-top: 10px;
		padding: 8px 12px; background: #f8fafc; border-radius: 6px;
		font-size: 12px;
	}
	.comp-label { color: var(--muted, #94a3b8); font-weight: 500; white-space: nowrap; }
	.comp-value { font-weight: 700; color: var(--hero-bg, #06162c); white-space: nowrap; }
	.comp-bar-wrap { flex: 1; height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden; max-width: 80px; }
	.comp-bar { height: 100%; border-radius: 3px; transition: width 0.4s; }
	.comp-bar.up { background: #10b981; }
	.comp-bar.down { background: #ef4444; }
	.comp-detail { color: var(--muted, #94a3b8); font-size: 11px; white-space: nowrap; }

	/* Payment Methods (horizontal bar list with brand colors) */
	.pm-list { display: flex; flex-direction: column; gap: 14px; }
	.pm-item { display: flex; flex-direction: column; gap: 4px; }
	.pm-head { display: flex; align-items: center; gap: 8px; }
	.pm-brand {
		width: 22px; height: 22px; border-radius: 5px; flex-shrink: 0;
		color: #fff; font-size: 11px; font-weight: 700;
		display: flex; align-items: center; justify-content: center;
	}
	.pm-name { font-size: 13px; font-weight: 600; color: var(--ink, #1e293b); text-transform: capitalize; flex: 1; }
	.pm-share { font-size: 12px; font-weight: 600; color: var(--muted, #94a3b8); }
	.pm-bar-wrap { height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
	.pm-bar { height: 100%; border-radius: 3px; transition: width 0.4s; }
	.pm-meta { display: flex; justify-content: space-between; font-size: 11px; color: var(--muted, #94a3b8); margin-top: 2px; }
	.pm-aov { font-weight: 600; }

	/* Card Scheme Performance cards */
	.scheme-cards { display: flex; flex-direction: column; gap: 10px; }
	.scheme-card {
		padding: 12px;
		border: 1px solid var(--line, #e2e8f0);
		border-radius: 8px;
		background: #fafbfc;
		display: flex;
		flex-direction: column;
		gap: 6px;
	}
	.sc-top { display: flex; align-items: center; gap: 8px; }
	.sc-badge {
		width: 28px; height: 28px; border-radius: 6px;
		color: #fff; font-size: 11px; font-weight: 700;
		display: flex; align-items: center; justify-content: center;
		flex-shrink: 0;
	}
	.sc-name { font-size: 13px; font-weight: 600; color: var(--ink, #1e293b); }
	.sc-auth { display: flex; align-items: center; gap: 8px; }
	.sc-auth-bar { flex: 1; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; }
	.sc-auth-fill { height: 100%; border-radius: 3px; transition: width 0.4s; }
	.sc-auth-fill.auth-good { background: linear-gradient(90deg, #10b981, #34d399); }
	.sc-auth-fill.auth-warn { background: linear-gradient(90deg, #f59e0b, #fbbf24); }
	.sc-auth-fill.auth-bad { background: linear-gradient(90deg, #ef4444, #f87171); }
	.sc-auth-val { font-size: 13px; font-weight: 700; width: 42px; text-align: right; }
	.sc-auth-val.auth-good { color: #10b981; }
	.sc-auth-val.auth-warn { color: #f59e0b; }
	.sc-auth-val.auth-bad { color: #ef4444; }
	.sc-auth-label { font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
	.sc-auth-label.auth-good { color: #10b981; }
	.sc-auth-label.auth-warn { color: #f59e0b; }
	.sc-auth-label.auth-bad { color: #ef4444; }
	.sc-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; padding-top: 8px; border-top: 1px solid var(--line, #e2e8f0); }
	.sc-stats div { display: flex; flex-direction: column; gap: 1px; }
	.sc-stats strong { font-size: 12px; color: var(--ink, #1e293b); }
	.sc-stats span { font-size: 10px; color: var(--muted, #94a3b8); text-transform: capitalize; }

	/* Volume Breakdown vertical bar chart */
	.bar-chart-wrap { position: relative; }
	.bar-chart-svg { width: 100%; height: 200px; }
	.bar-yaxis { position: absolute; top: 0; left: 0; width: 26px; height: 100%; pointer-events: none; }
	.bar-yaxis span { position: absolute; right: 4px; transform: translateY(-50%); font-size: 11px; font-weight: 600; font-family: Urbanist, system-ui, sans-serif; color: #64748b; }
	.bar-hover-overlay { position: absolute; top: 0; left: 0; display: flex; justify-content: space-between; pointer-events: none; }
	.bar-zone { width: 30px; height: 100%; margin-left: -15px; pointer-events: auto; }
	.bar-xaxis { position: relative; height: 18px; margin-top: 6px; border-top: 1px solid #e2e8f0; }
	.bar-xaxis span { position: absolute; transform: translateX(-50%); font-size: 11px; font-weight: 500; color: var(--muted, #94a3b8); white-space: nowrap; }

	/* Balance + Insights */
	.bottom-row {
		display: grid;
		grid-template-columns: 1fr 2fr;
		gap: 16px;
		margin-bottom: 20px;
	}
	.balance-panel .panel-head .link-more { font-size: 13px; color: #10b981; font-weight: 600; text-decoration: none; }
	.balance-panel .panel-head .link-more:hover { text-decoration: underline; }
	.balance-stack { display: flex; flex-direction: column; gap: 12px; }
	.balance-item {
		padding: 16px;
		border: 1px solid var(--line, #e2e8f0);
		border-radius: 8px;
		background: #fafbfc;
	}
	.balance-item.highlight {
		background: linear-gradient(135deg, #f0fdf4, #dcfce7);
		border-color: #86efac;
	}
	.balance-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
	.balance-item.sm { padding: 12px; }
	.bal-label { display: block; font-size: 11px; font-weight: 600; color: var(--muted, #94a3b8); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; }
	.bal-value { font-size: 22px; font-weight: 700; color: var(--hero-bg, #06162c); }
	.bal-value-sm { font-size: 16px; font-weight: 700; color: var(--hero-bg, #06162c); }
	.bal-value-date { font-size: 15px; font-weight: 700; color: #f59e0b; }

	/* Smart Insights */
	.insights-list { display: flex; flex-direction: column; gap: 10px; }
	.insight-card {
		display: flex;
		align-items: flex-start;
		gap: 12px;
		padding: 12px 14px;
		border-radius: 8px;
		border: 1px solid var(--line, #e2e8f0);
		background: #fff;
		transition: border-color 0.15s;
	}
	.insight-card.positive { background: #f0fdf4; border-color: #86efac; }
	.insight-card.negative { background: #fef2f2; border-color: #fca5a5; }
	.insight-card.warning { background: #fffbeb; border-color: #fcd34d; }
	.insight-card.neutral { background: #f8fafc; }
	.insight-icon { font-size: 18px; line-height: 1.4; flex-shrink: 0; }
	.insight-body { display: flex; flex-direction: column; gap: 2px; }
	.insight-headline { font-size: 13px; font-weight: 600; color: var(--ink, #1e293b); }
	.insight-sub { font-size: 12px; color: var(--muted, #94a3b8); line-height: 1.4; }

	@media (max-width: 1200px) {
		.kpi-row { grid-template-columns: repeat(2, 1fr); }
		.chart-row { grid-template-columns: 1fr; }
		.bottom-row { grid-template-columns: 1fr; }
	}
	@media (max-width: 768px) {
		.kpi-row { grid-template-columns: 1fr; }
		.dash-header { flex-direction: column; }
		.balance-row { grid-template-columns: 1fr; }
	}
</style>