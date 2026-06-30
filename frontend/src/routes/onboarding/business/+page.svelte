<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import { data, loading, saving, error, load, saveSection } from '$lib/stores/onboarding.svelte';
	import { get } from 'svelte/store';

	let initialized = $state(false);

	let form = $state({
		business_type: { type: '', subtype: '' },
		business_details: { legal_name: '', trading_name: '', registration_number: '', tax_id: '', emirates_id: '', website: '', phone: '', address: '', city: '', country: 'UAE' },
		representative: { name: '', email: '', phone: '', job_title: '' },
		owners: [{ name: '', email: '', phone: '', nationality: '', ownership_pct: 0 }],
		executives: [{ name: '', email: '', job_title: '', nationality: '' }],
		products: { description: '', industry: '', avg_ticket_size: 0, expected_monthly_volume: 0, target_markets: [] },
		public: { public_name: '', support_email: '', support_phone: '', support_url: '', terms_url: '', privacy_url: '' },
	});

	const validTabs = ['business', 'representative', 'products', 'public'];
	let activeTab = $state('business');
	let tabParam = $derived(page.url.searchParams.get('tab'));

	onMount(async () => {
		await load();
		const d = get(data);
		if (d.business_type) form.business_type = { ...d.business_type };
		if (d.business_details) form.business_details = { ...d.business_details };
		if (d.representative) form.representative = { ...d.representative };
		if (d.owners?.length) form.owners = d.owners.map(o => ({ ...o }));
		if (d.executives?.length) form.executives = d.executives.map(e => ({ ...e }));
		if (d.products) form.products = { ...d.products, target_markets: [...(d.products.target_markets || [])] };
		if (d.public) form.public = { ...d.public };
		if (tabParam && validTabs.includes(tabParam)) activeTab = tabParam;
		initialized = true;
	});

	const tabs = [
		{ key: 'business', label: 'Business' },
		{ key: 'representative', label: 'Rep & Owners' },
		{ key: 'products', label: 'Products' },
		{ key: 'public', label: 'Public Info' },
	];

	async function saveAll() {
		saveSection('business_type', form.business_type);
		saveSection('business_details', form.business_details);
		saveSection('representative', form.representative);
		saveSection('owners', form.owners);
		saveSection('executives', form.executives);
		saveSection('products', form.products);
		saveSection('public', form.public);
	}

	async function handleSubmit(e) {
		e.preventDefault();
		await saveAll();
		goto('/onboarding/financial');
	}

	function toggleMarket(m) {
		if (form.products.target_markets.includes(m)) {
			form.products.target_markets = form.products.target_markets.filter(x => x !== m);
		} else {
			form.products.target_markets = [...form.products.target_markets, m];
		}
	}

	const markets = ['UAE', 'Saudi Arabia', 'Qatar', 'Kuwait', 'Oman', 'Bahrain', 'Egypt', 'India', 'UK', 'USA'];
</script>

{#if !initialized || $loading}
	<p class="loading-text">Loading…</p>
{:else}
	<div class="page">
		<div class="page-header">
			<h2>Verify Your Business</h2>
			<p>Review and correct the information extracted from your documents.</p>
		</div>

		<div class="tabs">
			{#each tabs as tab}
				<button class="tab" class:active={activeTab === tab.key} onclick={() => activeTab = tab.key}>
					{tab.label}
				</button>
			{/each}
		</div>

		<form onsubmit={handleSubmit}>
			<div class="card" class:hidden={activeTab !== 'business'}>
				<h3>Business Type</h3>
				<div class="grid">
					<label>Type
						<select bind:value={form.business_type.type}>
							<option value="">Select…</option>
							<option value="sole_proprietorship">Sole Proprietorship</option>
							<option value="llc">LLC</option>
							<option value="corporation">Corporation</option>
							<option value="partnership">Partnership</option>
							<option value="nonprofit">Nonprofit</option>
						</select>
					</label>
					<label>Subtype / Industry
						<select bind:value={form.business_type.subtype}>
							<option value="">Select…</option>
							<option value="ecommerce">Ecommerce</option>
							<option value="saas">SaaS</option>
							<option value="retail">Retail</option>
							<option value="fintech">Fintech</option>
							<option value="consulting">Consulting</option>
							<option value="hospitality">Hospitality</option>
						</select>
					</label>
				</div>

				<h3>Business Details</h3>
				<div class="grid">
					<label>Legal Name <input bind:value={form.business_details.legal_name} /></label>
					<label>Trading Name <input bind:value={form.business_details.trading_name} /></label>
					<label>Registration # <input bind:value={form.business_details.registration_number} /></label>
					<label>Tax ID <input bind:value={form.business_details.tax_id} /></label>
					<label>Emirates ID <input bind:value={form.business_details.emirates_id} /></label>
					<label>Website <input type="url" bind:value={form.business_details.website} placeholder="https://" /></label>
					<label>Phone <input type="tel" bind:value={form.business_details.phone} /></label>
					<label>City <input bind:value={form.business_details.city} /></label>
				</div>
				<label class="full">Address <textarea bind:value={form.business_details.address}></textarea></label>
				<label class="full">Country <input bind:value={form.business_details.country} /></label>
			</div>

			<div class="card" class:hidden={activeTab !== 'representative'}>
				<h3>Account Representative</h3>
				<div class="grid">
					<label>Name <input bind:value={form.representative.name} /></label>
					<label>Email <input type="email" bind:value={form.representative.email} /></label>
					<label>Phone <input type="tel" bind:value={form.representative.phone} /></label>
					<label>Job Title
						<select bind:value={form.representative.job_title}>
							<option value="">Select…</option>
							<option value="CEO">CEO</option>
							<option value="CFO">CFO</option>
							<option value="Founder">Founder</option>
							<option value="Managing Director">Managing Director</option>
							<option value="Owner">Owner</option>
						</select>
					</label>
				</div>

				<h3>Business Owners ({form.owners.length})</h3>
				{#each form.owners as owner, i}
					<div class="sub-card">
						<div class="card-header">
							<span>Owner {i + 1}</span>
							<button type="button" class="remove" onclick={() => { if (form.owners.length > 1) form.owners = form.owners.filter((_, idx) => idx !== i); }}>✕</button>
						</div>
						<div class="grid">
							<label>Name <input bind:value={owner.name} /></label>
							<label>Email <input type="email" bind:value={owner.email} /></label>
							<label>Phone <input type="tel" bind:value={owner.phone} /></label>
							<label>Nationality <input bind:value={owner.nationality} /></label>
							<label>Ownership % <input type="number" bind:value={owner.ownership_pct} /></label>
						</div>
					</div>
				{/each}
				<button type="button" class="add-btn" onclick={() => form.owners = [...form.owners, { name: '', email: '', phone: '', nationality: '', ownership_pct: 0 }]}>+ Add Owner</button>

				<h3>Business Executives ({form.executives.length})</h3>
				{#each form.executives as exec, i}
					<div class="sub-card">
						<div class="card-header">
							<span>Executive {i + 1}</span>
							<button type="button" class="remove" onclick={() => { if (form.executives.length > 1) form.executives = form.executives.filter((_, idx) => idx !== i); }}>✕</button>
						</div>
						<div class="grid">
							<label>Name <input bind:value={exec.name} /></label>
							<label>Email <input type="email" bind:value={exec.email} /></label>
							<label>Job Title
								<select bind:value={exec.job_title}>
									<option value="">Select…</option>
									<option value="CEO">CEO</option>
									<option value="CFO">CFO</option>
									<option value="CTO">CTO</option>
									<option value="COO">COO</option>
									<option value="CMO">CMO</option>
									<option value="Director">Director</option>
								</select>
							</label>
							<label>Nationality <input bind:value={exec.nationality} /></label>
						</div>
					</div>
				{/each}
				<button type="button" class="add-btn" onclick={() => form.executives = [...form.executives, { name: '', email: '', job_title: '', nationality: '' }]}>+ Add Executive</button>
			</div>

			<div class="card" class:hidden={activeTab !== 'products'}>
				<h3>Products & Services</h3>
				<label class="full">Description <textarea bind:value={form.products.description}></textarea></label>
				<div class="grid">
					<label>Industry
						<select bind:value={form.products.industry}>
							<option value="">Select…</option>
							<option value="ecommerce">Ecommerce</option>
							<option value="saas">SaaS</option>
							<option value="retail">Retail</option>
							<option value="fintech">Fintech</option>
							<option value="healthcare">Healthcare</option>
							<option value="education">Education</option>
						</select>
					</label>
					<label>Avg Ticket (AED) <input type="number" bind:value={form.products.avg_ticket_size} /></label>
					<label>Monthly Volume (AED) <input type="number" bind:value={form.products.expected_monthly_volume} /></label>
				</div>
				<label>Target Markets</label>
				<div class="chips">
					{#each markets as m}
						<button type="button" class="chip" class:selected={form.products.target_markets.includes(m)} onclick={() => toggleMarket(m)}>{m}</button>
					{/each}
				</div>
			</div>

			<div class="card" class:hidden={activeTab !== 'public'}>
				<h3>Public Details</h3>
				<div class="grid">
					<label>Public Name <input bind:value={form.public.public_name} /></label>
					<label>Support Email <input type="email" bind:value={form.public.support_email} /></label>
					<label>Support Phone <input type="tel" bind:value={form.public.support_phone} /></label>
					<label>Support URL <input type="url" bind:value={form.public.support_url} placeholder="https://" /></label>
					<label>Terms URL <input type="url" bind:value={form.public.terms_url} placeholder="https://" /></label>
					<label>Privacy URL <input type="url" bind:value={form.public.privacy_url} placeholder="https://" /></label>
				</div>
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
	.tabs { display: flex; gap: 4px; background: #fff; border-radius: 8px; border: 1px solid var(--line); padding: 4px; }
	.tab { flex: 1; padding: 8px; border: none; border-radius: 6px; background: none; font-size: 14px; font-weight: 500; color: var(--muted); cursor: pointer; transition: all 0.15s; }
	.tab.active { background: var(--primary); color: #fff; }
	.card { background: #fff; border-radius: 8px; border: 1px solid var(--line); padding: 24px; margin-bottom: 16px; }
	.card.hidden { display: none; }
	.card h3 { font-size: 16px; margin: 0 0 16px; color: var(--ink); }
	.card h3:not(:first-child) { margin-top: 24px; }
	.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
	.full { display: flex; flex-direction: column; gap: 4px; margin-top: 14px; }
	label { font-size: 13px; font-weight: 600; color: var(--ink); display: flex; flex-direction: column; gap: 4px; }
	input, select, textarea { padding: 8px 10px; border: 1px solid var(--line); border-radius: 6px; font-size: 14px; font-family: inherit; background: #fff; }
	input:focus, select:focus, textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(2,195,102,0.1); }
	textarea { resize: vertical; min-height: 60px; }
	.sub-card { border: 1px solid var(--line); border-radius: 6px; padding: 14px; margin-bottom: 10px; }
	.card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-weight: 600; font-size: 14px; color: var(--ink); }
	.remove { background: none; border: none; font-size: 16px; cursor: pointer; color: var(--muted); }
	.remove:hover { color: #dc2626; }
	.add-btn { padding: 8px 16px; border: 1px dashed var(--line); border-radius: 6px; background: none; font-size: 14px; color: var(--primary); cursor: pointer; font-weight: 500; margin-top: 8px; }
	.add-btn:hover { background: #f0fdf4; }
	.chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
	.chip { padding: 6px 14px; border: 1px solid var(--line); border-radius: 20px; background: #fff; font-size: 13px; cursor: pointer; }
	.chip.selected { background: var(--primary); color: #fff; border-color: var(--primary); }
	.error { background: #fef2f2; color: #dc2626; padding: 10px 14px; border-radius: 6px; font-size: 14px; margin-top: 8px; }
	.actions { display: flex; justify-content: flex-end; }
	.btn { padding: 10px 24px; border-radius: 6px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; }
	.btn:disabled { opacity: 0.5; cursor: not-allowed; }
	.btn-primary { background: var(--primary); color: #fff; }
	.btn-primary:hover:not(:disabled) { background: var(--primary-dark); }
</style>
