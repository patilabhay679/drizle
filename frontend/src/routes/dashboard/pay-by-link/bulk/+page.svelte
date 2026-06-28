<script>
	let file = $state(null);
	let uploading = $state(false);
	let result = $state(null);

	function handleFile(e) {
		file = e.target.files[0] || null;
		result = null;
	}

	async function upload() {
		if (!file) return;
		uploading = true;
		result = null;
		// Simulate upload — backend endpoint would exist in production
		await new Promise(r => setTimeout(r, 1500));
		result = { success: 12, failed: 2, total: 14 };
		uploading = false;
	}
</script>

<svelte:head>
	<title>Bulk Uploads | DrizlePay</title>
</svelte:head>

<div class="page-header">
	<h2>Bulk Uploads</h2>
</div>

<div class="card upload-card">
	<h3>Upload CSV / Excel File</h3>
	<p class="upload-desc">Upload a file with columns: amount, currency, description, email. Each row generates a payment link.</p>

	<div class="drop-zone" class:has-file={file !== null}>
		<input type="file" accept=".csv,.xlsx,.xls" onchange={handleFile} id="file-input" />
		<label for="file-input">
			{#if file}
				<strong>{file.name}</strong> ({(file.size / 1024).toFixed(1)} KB)
			{:else}
				<span>Drop a file here or click to browse</span>
			{/if}
		</label>
	</div>

	<button class="btn-primary" disabled={!file || uploading} onclick={upload}>
		{uploading ? 'Uploading…' : 'Upload & Generate Links'}
	</button>

	{#if result}
		<div class="result-box">
			<strong>Upload complete</strong>
			<span>{result.success} succeeded, {result.failed} failed</span>
		</div>
	{/if}
</div>

<div class="card">
	<h3 style="padding: 20px 20px 0; margin: 0; font-size: 15px;">Upload History</h3>
	<div class="table-wrap">
		<table>
			<thead><tr><th>File</th><th>Date</th><th>Rows</th><th>Success</th><th>Failed</th></tr></thead>
			<tbody>
				<tr><td class="mono">bulk_links_2026_06.xlsx</td><td>15 Jun 2026</td><td>14</td><td><span class="badge success">12</span></td><td><span class="badge failed">2</span></td></tr>
				<tr><td class="mono">subscribers_may.xlsx</td><td>01 May 2026</td><td>25</td><td><span class="badge success">25</span></td><td><span class="badge failed">0</span></td></tr>
			</tbody>
		</table>
	</div>
</div>

<style>
	.page-header { margin-bottom: 20px; }
	.page-header h2 { margin: 0; font-size: 20px; font-weight: 700; color: var(--hero-bg); }
	.upload-card { padding: 24px; background: #fff; border: 1px solid var(--line); border-radius: 8px; margin-bottom: 16px; }
	.upload-card h3 { margin: 0 0 8px; font-size: 15px; font-weight: 600; color: var(--hero-bg); }
	.upload-desc { font-size: 13px; color: var(--muted); margin: 0 0 16px; }
	.drop-zone {
		border: 2px dashed var(--line);
		border-radius: 8px;
		padding: 40px 20px;
		text-align: center;
		margin-bottom: 16px;
		transition: border-color 0.15s;
		position: relative;
	}
	.drop-zone.has-file { border-color: var(--primary); background: #f0fdf4; }
	.drop-zone input { position: absolute; inset: 0; opacity: 0; cursor: pointer; }
	.drop-zone label { display: block; cursor: pointer; color: var(--muted); font-size: 14px; }
	.drop-zone label strong { color: var(--ink); }
	.btn-primary {
		padding: 8px 18px; background: var(--primary); color: #fff; border: none; border-radius: 4px;
		font-size: 13px; font-weight: 600; cursor: pointer;
	}
	.btn-primary:hover:not(:disabled) { background: var(--primary-dark); }
	.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
	.result-box {
		margin-top: 16px; padding: 12px 14px; background: #e6fcf0; border-radius: 6px;
		display: flex; flex-direction: column; gap: 2px;
	}
	.result-box strong { font-size: 14px; color: var(--primary-dark); }
	.result-box span { font-size: 13px; color: var(--ink); }
	.card { background: #fff; border: 1px solid var(--line); border-radius: 8px; padding: 0 0 0; overflow: hidden; }
	.table-wrap { overflow-x: auto; }
	table { width: 100%; border-collapse: collapse; font-size: 13px; }
	th { text-align: left; padding: 10px 12px; color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid var(--line); white-space: nowrap; background: #fafafa; }
	td { padding: 10px 12px; color: var(--ink); border-bottom: 1px solid #f1f5f9; white-space: nowrap; }
	tr:last-child td { border-bottom: none; }
	.mono { font-family: ui-monospace, monospace; font-size: 12px; }
	.badge { display: inline-flex; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; }
	.badge.success { background: #e6fcf0; color: var(--primary-dark); }
	.badge.failed { background: #fef2f2; color: #dc2626; }
</style>
