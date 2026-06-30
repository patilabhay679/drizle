<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { data, loading, documents, submit, submitError, onboardingStatus, load, resetCache } from '$lib/stores/onboarding.svelte';
	import { auth } from '$lib/stores/auth';
	import { api } from '$lib/api';
	import { get } from 'svelte/store';

	let initialized = $state(false);
	let submitting = $state(false);
	let submitted = $state(false);

	onMount(async () => {
		resetCache();
		await load(true);
		initialized = true;
	});

	const d = $derived(get(data));
	const docs = $derived(get(documents));

	const overview = $derived({
		legal_name: d.business_details?.legal_name || '',
		trading_name: d.business_details?.trading_name || '',
		business_type: d.business_type?.type || '',
		industry: d.business_type?.subtype || '',
		registration: d.business_details?.registration_number || '',
		city: d.business_details?.city || '',
		country: d.business_details?.country || 'UAE',
	});

	const rep = $derived({
		name: d.representative?.name || '',
		email: d.representative?.email || '',
		phone: d.representative?.phone || '',
		job_title: d.representative?.job_title || '',
		owners_count: d.owners?.length || 0,
		execs_count: d.executives?.length || 0,
	});

	const products = $derived({
		description: d.products?.description || '',
		industry: d.products?.industry || '',
		avg_ticket: d.products?.avg_ticket_size || 0,
		monthly_volume: d.products?.expected_monthly_volume || 0,
		markets: d.products?.target_markets || [],
	});

	const publicInfo = $derived({
		public_name: d.public?.public_name || '',
		support_email: d.public?.support_email || '',
		support_phone: d.public?.support_phone || '',
		support_url: d.public?.support_url || '',
		terms_url: d.public?.terms_url || '',
		privacy_url: d.public?.privacy_url || '',
	});

	const bank = $derived({
		name: d.bank?.bank_name || '',
		holder: d.bank?.account_name || '',
		number: d.bank?.account_number || '',
		iban: d.bank?.iban || '',
		swift: d.bank?.swift || '',
	});

	const security = $derived({
		two_factor: d.security?.two_factor_enabled || false,
	});

	const sections = $derived([
		{
			key: 'business',
			label: 'Business Information',
			edit: '/onboarding/business?tab=business',
			items: [
				{ label: 'Legal Name', value: overview.legal_name },
				{ label: 'Trading Name', value: overview.trading_name },
				{ label: 'Business Type', value: overview.business_type ? overview.business_type.replace(/_/g, ' ') + (overview.industry ? ' / ' + overview.industry.replace(/_/g, ' ') : '') : '' },
				{ label: 'Registration #', value: overview.registration },
				{ label: 'Location', value: overview.city ? overview.city + (overview.country ? ', ' + overview.country : '') : '' },
			],
			empty: !overview.legal_name && !overview.registration,
		},
		{
			key: 'contacts',
			label: 'Contacts & Ownership',
			edit: '/onboarding/business?tab=representative',
			items: [
				{ label: 'Representative', value: rep.name ? rep.name + (rep.email ? ' — ' + rep.email : '') : '' },
				{ label: 'Job Title', value: rep.job_title },
				{ label: 'Phone', value: rep.phone },
				{ label: 'Business Owners', value: rep.owners_count > 0 ? rep.owners_count + ' listed' : 'None' },
				{ label: 'Executives', value: rep.execs_count > 0 ? rep.execs_count + ' listed' : 'None' },
			],
			empty: !rep.name,
		},
		{
			key: 'products',
			label: 'Products & Services',
			edit: '/onboarding/business?tab=products',
			items: [
				{ label: 'Description', value: products.description },
				{ label: 'Industry', value: products.industry || '—' },
				{ label: 'Avg Ticket', value: products.avg_ticket ? 'AED ' + Number(products.avg_ticket).toLocaleString() : '—' },
				{ label: 'Monthly Volume', value: products.monthly_volume ? 'AED ' + Number(products.monthly_volume).toLocaleString() : '—' },
				{ label: 'Target Markets', value: products.markets.length > 0 ? products.markets.join(', ') : '—' },
			],
			empty: !products.description,
		},
		{
			key: 'public',
			label: 'Public Details',
			edit: '/onboarding/business?tab=public',
			items: [
				{ label: 'Business Name (public)', value: publicInfo.public_name },
				{ label: 'Support Email', value: publicInfo.support_email || '—' },
				{ label: 'Support Phone', value: publicInfo.support_phone || '—' },
				{ label: 'Support URL', value: publicInfo.support_url || '—' },
				{ label: 'Terms URL', value: publicInfo.terms_url || '—' },
				{ label: 'Privacy URL', value: publicInfo.privacy_url || '—' },
			],
			empty: !publicInfo.public_name && !publicInfo.support_email,
		},
		{
			key: 'bank',
			label: 'Bank Account',
			edit: '/onboarding/financial',
			items: [
				{ label: 'Bank', value: bank.name || '—' },
				{ label: 'Account Holder', value: bank.holder },
				{ label: 'Account Number', value: bank.number || '—' },
				{ label: 'IBAN', value: bank.iban || '—' },
				{ label: 'SWIFT / BIC', value: bank.swift || '—' },
			],
			empty: !bank.holder && !bank.iban,
		},
		{
			key: 'documents',
			label: 'Uploaded Documents',
			edit: '/onboarding/upload',
			items: docs.map(doc => ({
				label: doc.doc_type?.replace(/_/g, ' ') || 'Document',
				value: doc.filename,
			})),
			empty: docs.length === 0,
		},
	]);

	let doneCount = $derived(sections.filter(s => !s.empty).length);
	let totalCount = $derived(sections.length);
	let allDone = $derived(doneCount === totalCount);

	function formatDocType(raw) {
		if (!raw) return 'Document';
		return raw.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
	}

	async function handleSubmit() {
		if (!allDone) return;
		submitting = true;
		try {
			const ok = await submit();
			if (ok) {
				submitted = true;
				const res = await api.getMe();
				auth.login(auth.token, res);
			}
		} finally {
			submitting = false;
		}
	}
</script>

{#if !initialized || $loading}
	<p class="loading-text">Loading…</p>
{:else if submitted}
	<div class="page">
		<div class="card success-card">
			<div class="success-icon">✓</div>
			<h2>Application Submitted!</h2>
			<p>Thank you. We've received your onboarding application and it's now under review.</p>
			<div class="timeline">
				<div class="tl-item active">
					<span class="tl-dot"></span>
					<div>
						<strong>Application Received</strong>
						<span>Just now</span>
					</div>
				</div>
				<div class="tl-item">
					<span class="tl-dot"></span>
					<div>
						<strong>Document Verification</strong>
						<span>Typically within 24 hours</span>
					</div>
				</div>
				<div class="tl-item">
					<span class="tl-dot"></span>
					<div>
						<strong>Compliance Review</strong>
						<span>1–2 business days</span>
					</div>
				</div>
				<div class="tl-item">
					<span class="tl-dot"></span>
					<div>
						<strong>Account Activated</strong>
						<span>You'll receive an email</span>
					</div>
				</div>
			</div>
			<button class="btn btn-primary" onclick={() => goto('/dashboard')}>Go to Dashboard</button>
		</div>
	</div>
{:else}
	<div class="page">
		<div class="page-header">
			<h2>Review & Submit</h2>
			<p>Please review your information carefully before submitting. Everything will be verified by our compliance team.</p>
		</div>

		<div class="card progress-card">
			<div class="progress-bar">
				<div class="progress-fill" style="width: {doneCount / totalCount * 100}%"></div>
			</div>
			<div class="progress-status">
				<span class="progress-text">{doneCount} of {totalCount} sections complete</span>
				{#if allDone}
					<span class="ready-badge">Ready to Submit</span>
				{:else}
					<span class="missing-badge">{totalCount - doneCount} section{totalCount - doneCount > 1 ? 's' : ''} incomplete</span>
				{/if}
			</div>
		</div>

		{#each sections as section}
			<div class="section-card" class:empty={section.empty}>
				<div class="section-header">
					<div class="section-left">
						<span class="section-icon" class:done={!section.empty}>
							{section.empty ? '○' : '✓'}
						</span>
						<div>
							<strong>{section.label}</strong>
							<span class="section-summary">{section.items.find(i => i.value)?.value || 'Not provided'}</span>
						</div>
					</div>
					<div class="section-right">
						<a href={section.edit} class="edit-link">Edit</a>
					</div>
				</div>
				<div class="section-body">
					{#each section.items as item}
						<div class="field-row">
							<span class="field-label">{item.label}</span>
							<span class="field-value" class:empty-value={!item.value}>{item.value || '—'}</span>
						</div>
					{/each}
				</div>
			</div>
		{/each}

		<div class="card next-steps">
			<h3>What Happens After You Submit?</h3>
			<div class="tl-list">
				<div class="tl-row">
					<span class="tl-num">1</span>
					<div>
						<strong>Application Received</strong>
						<span>You'll get a confirmation email immediately.</span>
					</div>
				</div>
				<div class="tl-row">
					<span class="tl-num">2</span>
					<div>
						<strong>Document Review</strong>
						<span>Our team verifies your documents — typically within 24 hours.</span>
					</div>
				</div>
				<div class="tl-row">
					<span class="tl-num">3</span>
					<div>
						<strong>Compliance Check</strong>
						<span>Standard compliance review takes 1–2 business days.</span>
					</div>
				</div>
				<div class="tl-row">
					<span class="tl-num">4</span>
					<div>
						<strong>Account Activated</strong>
						<span>You'll receive an email once your account is ready. You can then start accepting payments.</span>
					</div>
				</div>
			</div>
			<p class="next-note">We'll notify you at <strong>{rep.email || auth.merchant?.email}</strong> with updates.</p>
		</div>

		{#if $submitError}
			<div class="error">{$submitError}</div>
		{/if}

		<div class="actions-bar">
			<div class="actions-info">
				{#if allDone}
					<span>✓ All sections complete</span>
				{:else}
					<span>{totalCount - doneCount} section{totalCount - doneCount > 1 ? 's' : ''} incomplete</span>
				{/if}
			</div>
			<button class="btn btn-primary btn-large" disabled={!allDone || submitting} onclick={handleSubmit}>
				{submitting ? 'Submitting…' : 'Submit Application'}
			</button>
		</div>
	</div>
{/if}

<style>
	.loading-text { color: var(--muted); font-size: 14px; }
	.page { display: flex; flex-direction: column; gap: 16px; padding-bottom: 40px; }

	.page-header { margin-bottom: 4px; }
	.page-header h2 { font-size: 22px; color: var(--ink); margin: 0 0 6px; }
	.page-header p { font-size: 14px; color: var(--muted); margin: 0; max-width: 500px; }

	/* ── Progress ── */
	.progress-card { background: #fff; border-radius: 8px; border: 1px solid var(--line); padding: 20px 24px; }
	.progress-bar { height: 6px; background: #e2e8f0; border-radius: 3px; overflow: hidden; }
	.progress-fill { height: 100%; background: var(--primary); border-radius: 3px; transition: width 0.4s; }
	.progress-status { display: flex; align-items: center; justify-content: space-between; margin-top: 10px; }
	.progress-text { font-size: 14px; color: var(--muted); }
	.ready-badge { font-size: 13px; font-weight: 600; color: var(--primary); background: #e6fcf0; padding: 3px 10px; border-radius: 10px; }
	.missing-badge { font-size: 13px; font-weight: 600; color: #92400e; background: #fef3c7; padding: 3px 10px; border-radius: 10px; }

	/* ── Section Cards ── */
	.section-card { background: #fff; border-radius: 8px; border: 1px solid var(--line); overflow: hidden; }
	.section-card.empty { border-color: #fde68a; background: #fffbeb; }
	.section-header {
		display: flex; align-items: center; justify-content: space-between;
		padding: 16px 20px; border: none; background: none;
		cursor: default; font-family: inherit; font-size: inherit;
		text-align: left;
	}
	.section-left { display: flex; align-items: center; gap: 12px; }
	.section-left div { display: flex; flex-direction: column; gap: 2px; }
	.section-left strong { font-size: 15px; color: var(--ink); }
	.section-summary { font-size: 12px; color: var(--muted); max-width: 340px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
	.section-icon { width: 22px; height: 22px; border-radius: 50%; display: grid; place-items: center; font-size: 12px; font-weight: 700; border: 2px solid var(--line); color: var(--muted); flex-shrink: 0; }
	.section-icon.done { background: var(--primary); border-color: var(--primary); color: #fff; }
	.section-right { display: flex; align-items: center; gap: 12px; }
	.edit-link { font-size: 13px; color: var(--primary); font-weight: 600; text-decoration: none; }
	.edit-link:hover { text-decoration: underline; }
	.section-body { padding: 4px 20px 16px 54px; display: flex; flex-direction: column; gap: 8px; }
	.field-row { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 6px 0; border-bottom: 1px solid #f1f5f9; }
	.field-row:last-child { border-bottom: none; }
	.field-label { font-size: 13px; color: var(--muted); white-space: nowrap; }
	.field-value { font-size: 14px; color: var(--ink); text-align: right; word-break: break-all; max-width: 60%; }
	.field-value.empty-value { color: var(--muted); font-style: italic; }

	/* ── What's Next ── */
	.next-steps { background: #fff; border-radius: 8px; border: 1px solid var(--line); padding: 24px; }
	.next-steps h3 { font-size: 16px; margin: 0 0 16px; color: var(--ink); }
	.tl-list { display: flex; flex-direction: column; gap: 14px; }
	.tl-row { display: flex; gap: 14px; align-items: flex-start; }
	.tl-num {
		width: 26px; height: 26px; border-radius: 50%; background: var(--primary);
		color: #fff; display: grid; place-items: center;
		font-size: 13px; font-weight: 700; flex-shrink: 0; margin-top: 1px;
	}
	.tl-row div { display: flex; flex-direction: column; gap: 2px; }
	.tl-row strong { font-size: 14px; color: var(--ink); }
	.tl-row span { font-size: 13px; color: var(--muted); line-height: 1.4; }
	.next-note { font-size: 13px; color: var(--muted); margin: 16px 0 0; padding-top: 14px; border-top: 1px solid var(--line); }

	/* ── Error ── */
	.error { background: #fef2f2; color: #dc2626; padding: 12px 16px; border-radius: 6px; font-size: 14px; }

	/* ── Actions Bar ── */
	.actions-bar { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 16px 20px; background: #fff; border-radius: 8px; border: 1px solid var(--line); }
	.actions-info { font-size: 14px; color: var(--muted); }

	/* ── Buttons ── */
	.btn { padding: 10px 24px; border-radius: 6px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; transition: all 0.15s; }
	.btn:disabled { opacity: 0.5; cursor: not-allowed; }
	.btn-primary { background: var(--primary); color: #fff; }
	.btn-primary:hover:not(:disabled) { background: var(--primary-dark); }
	.btn-large { padding: 14px 36px; font-size: 16px; }

	/* ── Success State ── */
	.success-card { text-align: center; padding: 48px 32px; margin-top: 20px; }
	.success-card h2 { font-size: 24px; color: var(--ink); margin: 0 0 8px; }
	.success-card p { font-size: 15px; color: var(--muted); margin: 0 0 28px; }
	.success-icon { width: 56px; height: 56px; border-radius: 50%; background: var(--primary); color: #fff; display: grid; place-items: center; font-size: 26px; font-weight: 700; margin: 0 auto 20px; }
	.timeline { display: flex; flex-direction: column; gap: 0; margin: 0 auto 28px; max-width: 360px; text-align: left; }
	.tl-item { display: flex; gap: 14px; padding-bottom: 20px; position: relative; }
	.tl-item:not(:last-child)::before { content: ''; position: absolute; left: 11px; top: 24px; bottom: 0; width: 2px; background: #e2e8f0; }
	.tl-item.active .tl-dot { background: var(--primary); border-color: var(--primary); }
	.tl-dot { width: 24px; height: 24px; border-radius: 50%; border: 2px solid var(--line); background: #fff; flex-shrink: 0; position: relative; z-index: 1; }
	.tl-item div { display: flex; flex-direction: column; gap: 2px; padding-top: 2px; }
	.tl-item strong { font-size: 14px; color: var(--ink); }
	.tl-item span { font-size: 13px; color: var(--muted); }
</style>
