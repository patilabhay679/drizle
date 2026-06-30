<script>
	let { title, description, saving, error, onsubmit, children } = $props();
</script>

<form onsubmit={onsubmit}>
	<div class="form-header">
		<h2>{title}</h2>
		{#if description}
			<p>{description}</p>
		{/if}
	</div>
	<div class="form-body">
		{@render children()}
	</div>
	{#if error}
		<div class="form-error">{error}</div>
	{/if}
	<div class="form-actions">
		<button type="submit" class="btn btn-primary" disabled={saving}>
			{saving ? 'Saving…' : 'Save & Continue'}
		</button>
	</div>
</form>

<style>
	form { background: #fff; border-radius: 8px; border: 1px solid var(--line); padding: 32px; }
	.form-header { margin-bottom: 24px; }
	.form-header h2 { font-size: 20px; color: var(--ink); margin: 0 0 4px; }
	.form-header p { font-size: 14px; color: var(--muted); margin: 0; }
	.form-body { display: flex; flex-direction: column; gap: 16px; }
	.form-error { background: #fef2f2; color: #dc2626; padding: 10px 14px; border-radius: 6px; font-size: 14px; margin-top: 8px; }
	.form-actions { margin-top: 24px; display: flex; justify-content: flex-end; }
	.btn { padding: 10px 24px; border-radius: 6px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; transition: all 0.15s; }
	.btn:disabled { opacity: 0.6; cursor: not-allowed; }
	.btn-primary { background: var(--primary); color: #fff; }
	.btn-primary:hover:not(:disabled) { background: var(--primary-dark); }
</style>
