<script>
	let { label, type = 'text', bind:value, placeholder = '', required = false, options = [] } = $props();
</script>

<div class="field">
	<label>{label}{#if required}<span class="req">*</span>{/if}</label>
	{#if type === 'select'}
		<select {required} bind:value>
			<option value="">Select…</option>
			{#each options as opt}
				<option value={opt}>{opt}</option>
			{/each}
		</select>
	{:else if type === 'textarea'}
		<textarea {required} {placeholder} bind:value></textarea>
	{:else if type === 'number'}
		<input type="number" {required} {placeholder} bind:value />
	{:else if type === 'checkbox'}
		<div class="checkbox-wrap">
			<input type="checkbox" bind:checked={value} />
		</div>
	{:else}
		<input {type} {required} {placeholder} bind:value />
	{/if}
</div>

<style>
	.field { display: flex; flex-direction: column; gap: 4px; }
	label { font-size: 13px; font-weight: 600; color: var(--ink); }
	.req { color: #dc2626; margin-left: 2px; }
	input, select, textarea {
		padding: 9px 12px;
		border: 1px solid var(--line);
		border-radius: 6px;
		font-size: 14px;
		font-family: inherit;
		background: #fff;
		transition: border-color 0.15s;
	}
	input:focus, select:focus, textarea:focus {
		outline: none;
		border-color: var(--primary);
		box-shadow: 0 0 0 3px rgba(2, 195, 102, 0.1);
	}
	textarea { resize: vertical; min-height: 80px; }
	.checkbox-wrap { display: flex; align-items: center; padding: 4px 0; }
	.checkbox-wrap input { width: 18px; height: 18px; cursor: pointer; }
</style>
