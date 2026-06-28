<script>
	const labels = {
		curl: 'cURL',
		python: 'Python',
		js: 'JavaScript',
		php: 'PHP',
	};

	let { examples = {}, response = '' } = $props();
	let keys = $derived(Object.keys(examples));
	let lang = $state(keys.includes('curl') ? 'curl' : keys[0]);
	let copied = $state(false);

	function copyCode() {
		const code = examples[lang] || '';
		navigator.clipboard.writeText(code.replace(/&#123;/g, '{').replace(/&#125;/g, '}'));
		copied = true;
		setTimeout(() => copied = false, 2000);
	}
</script>

<div class="cb-group">
	<div class="cb-header">
		<div class="cb-tabs">
			{#each keys as key}
				<button
					class="cb-tab"
					class:active={lang === key}
					onclick={() => lang = key}
				>{labels[key] ?? key}</button>
			{/each}
		</div>
		<button class="cb-copy" onclick={copyCode}>
			{copied ? 'Copied' : 'Copy'}
		</button>
	</div>
	<pre class="cb-code"><code>{@html examples[lang]}</code></pre>
	{#if response}
	<div class="cb-response">
		<div class="cb-response-label">Response</div>
		<pre class="cb-code response"><code>{@html response}</code></pre>
	</div>
	{/if}
</div>

<style>
	.cb-group { margin: 0 0 28px; border-radius: 10px; overflow: hidden; border: 1px solid #1e293b; }
	.cb-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		background: #1e293b;
		padding: 8px 12px;
	}
	.cb-tabs { display: flex; gap: 2px; }
	.cb-tab {
		padding: 5px 14px;
		border: none;
		border-radius: 4px;
		background: transparent;
		color: #94a3b8;
		font-size: 12px;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.12s;
	}
	.cb-tab.active { background: #334155; color: #f1f5f9; }
	.cb-tab:hover:not(.active) { color: #e2e8f0; }
	.cb-copy {
		padding: 5px 12px;
		border: 1px solid #475569;
		border-radius: 4px;
		background: transparent;
		color: #94a3b8;
		font-size: 11px;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.12s;
	}
	.cb-copy:hover { background: #334155; color: #f1f5f9; border-color: #64748b; }
	.cb-code {
		margin: 0;
		padding: 20px 24px;
		background: #0f172a;
		color: #e2e8f0;
		font: 13px/1.7 ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
		overflow-x: auto;
		tab-size: 2;
		white-space: pre;
	}
	.cb-code.response {
		border-top: 1px solid #1e293b;
		background: #0a0f1a;
		color: #cbd5e1;
	}
	.cb-response { margin: 0; }
	.cb-response-label {
		font-size: 10px;
		font-weight: 700;
		color: #64748b;
		text-transform: uppercase;
		letter-spacing: 0.06em;
		padding: 8px 16px;
		background: #1e293b;
		border-top: 1px solid #334155;
	}
</style>
