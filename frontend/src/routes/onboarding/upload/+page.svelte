<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { data, loading, documents, uploadDocument, load } from '$lib/stores/onboarding.svelte';
	import { get } from 'svelte/store';

	let initialized = $state(false);
	let uploading = $state(false);
	let error = $state(null);
	let docType = $state('');
	let uploadDone = $state(false);

	const docOptions = [
		{ value: '', label: 'Select document type…' },
		{ value: 'trade_license', label: 'Trade License' },
		{ value: 'passport_emirates_id', label: 'Passport / Emirates ID' },
		{ value: 'bank_letter', label: 'Bank Letter / IBAN Proof' },
		{ value: 'vat_certificate', label: 'VAT Certificate' },
		{ value: 'company_registration', label: 'Company Registration' },
	];

	onMount(async () => {
		await load();
		initialized = true;
	});

	async function handleUpload(e) {
		const file = e.target.files?.[0];
		if (!file || !docType) return;
		uploading = true;
		error = null;
		try {
			const res = await uploadDocument(file, docType);
			if (res) {
				uploadDone = true;
			}
		} catch (e) {
			error = e.message || 'Upload failed';
		} finally {
			uploading = false;
		}
	}
</script>

{#if !initialized || $loading}
	<p class="loading-text">Loading…</p>
{:else}
	<div class="page">
		<div class="page-header">
			<h2>Upload Documents</h2>
			<p>Upload your business documents and we'll auto-fill everything for you.</p>
		</div>

		{#if !uploadDone}
			<div class="card">
				<div class="field">
					<label>What document are you uploading?</label>
					<select bind:value={docType}>
						{#each docOptions as opt}
							<option value={opt.value}>{opt.label}</option>
						{/each}
					</select>
				</div>
				<div class="upload-area">
					<label class="upload-btn" class:disabled={uploading || !docType}>
						{uploading ? 'Processing…' : 'Choose File'}
						<input type="file" accept="image/png,image/jpeg,application/pdf" onchange={handleUpload} disabled={uploading || !docType} />
					</label>
					<span class="upload-hint">PNG, JPEG, PDF — max 10MB</span>
				</div>
				{#if error}
					<div class="error">{error}</div>
				{/if}
			</div>
		{:else}
			<div class="card success-card">
				<div class="success-icon">✓</div>
				<h3>Document Processed!</h3>
				<p>We extracted your information. Review each section below and make any corrections.</p>
				<div class="doc-chip">{docOptions.find(o => o.value === docType)?.label}</div>
			</div>
		{/if}

		{#if $documents.length > 0}
			<div class="card">
				<h3>Uploaded Documents ({$documents.length})</h3>
				<div class="doc-list">
					{#each $documents as doc}
						<div class="doc-item">
							<span class="doc-name">{doc.filename}</span>
							<span class="doc-type">{doc.doc_type?.replace(/_/g, ' ')}</span>
							<span class="doc-status">{doc.status}</span>
						</div>
					{/each}
				</div>
			</div>
		{/if}

		<div class="actions">
			{#if uploadDone}
				<button class="btn btn-outline" onclick={() => { docType = ''; uploadDone = false; }}>+ Upload Another</button>
			{/if}
			<button class="btn btn-primary" onclick={() => goto('/onboarding/business')}>
				{$documents.length > 0 ? 'Continue to Verify Business →' : 'Skip to Forms →'}
			</button>
		</div>
	</div>
{/if}

<style>
	.loading-text { color: var(--muted); font-size: 14px; }
	.page { display: flex; flex-direction: column; gap: 20px; }
	.page-header { margin-bottom: 4px; }
	.page-header h2 { font-size: 20px; color: var(--ink); margin: 0 0 4px; }
	.page-header p { font-size: 14px; color: var(--muted); margin: 0; }
	.card { background: #fff; border-radius: 8px; border: 1px solid var(--line); padding: 24px; }
	.card h3 { font-size: 16px; margin: 0 0 16px; color: var(--ink); }
	.field { display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; }
	.field label { font-size: 13px; font-weight: 600; color: var(--ink); }
	.field select { padding: 9px 12px; border: 1px solid var(--line); border-radius: 6px; font-size: 14px; font-family: inherit; background: #fff; }
	.field select:focus { outline: none; border-color: var(--primary); }
	.upload-area { display: flex; align-items: center; gap: 12px; }
	.upload-btn {
		display: inline-block; padding: 10px 20px; background: var(--primary); color: #fff;
		border-radius: 6px; font-size: 14px; font-weight: 600; cursor: pointer; transition: background 0.15s;
	}
	.upload-btn:hover { background: var(--primary-dark); }
	.upload-btn.disabled { opacity: 0.5; cursor: not-allowed; }
	.upload-btn input { display: none; }
	.upload-hint { font-size: 13px; color: var(--muted); }
	.error { background: #fef2f2; color: #dc2626; padding: 10px 14px; border-radius: 6px; font-size: 14px; margin-top: 12px; }
	.success-card { text-align: center; padding: 40px 24px; }
	.success-icon {
		width: 48px; height: 48px; border-radius: 50%; background: var(--primary);
		color: #fff; display: grid; place-items: center; font-size: 22px; font-weight: 700;
		margin: 0 auto 16px;
	}
	.success-card h3 { margin: 0 0 8px; }
	.success-card p { font-size: 14px; color: var(--muted); margin: 0 0 12px; }
	.doc-chip { display: inline-block; padding: 4px 12px; background: #e6fcf0; color: var(--primary-dark); border-radius: 12px; font-size: 13px; font-weight: 600; }
	.doc-list { display: flex; flex-direction: column; gap: 8px; }
	.doc-item { display: flex; align-items: center; gap: 12px; padding: 8px 0; border-bottom: 1px solid var(--line); font-size: 14px; }
	.doc-item:last-child { border-bottom: none; }
	.doc-name { flex: 1; font-weight: 500; }
	.doc-type { font-size: 12px; color: var(--muted); text-transform: capitalize; }
	.doc-status { font-size: 12px; color: var(--primary); background: #e6fcf0; padding: 2px 8px; border-radius: 10px; }
	.actions { display: flex; justify-content: flex-end; gap: 12px; }
	.btn { padding: 10px 24px; border-radius: 6px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; transition: all 0.15s; }
	.btn:disabled { opacity: 0.5; cursor: not-allowed; }
	.btn-primary { background: var(--primary); color: #fff; }
	.btn-primary:hover { background: var(--primary-dark); }
	.btn-outline { background: none; border: 1px solid var(--line); color: var(--muted); }
	.btn-outline:hover { border-color: var(--primary); color: var(--ink); }
</style>
