<script>
	let openDropdown = $state('');

	function toggle(name) {
		openDropdown = openDropdown === name ? '' : name;
	}

	function onWindowClick(e) {
		if (e.target.closest('.nav-trigger')) return;
		openDropdown = '';
	}
</script>

<svelte:window onclick={onWindowClick} />

<header>
	<div class="container nav">
		<a class="brand" href="/" aria-label="Drizle Pay homepage">Drizle<span>Pay</span></a>
		<nav class="links" aria-label="Primary navigation">
			<div class="nav-item">
				<button
					class="nav-trigger"
					onclick={(e) => { toggle('products'); }}
					aria-expanded={openDropdown === 'products'}
				>
					Products
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'products'}>
					<a href="/docs/payments">Payments</a>
					<a href="/docs/recurring-payments">Subscriptions</a>
					<a href="/docs/payouts">Payouts</a>
				</div>
			</div>
			<div class="nav-item">
				<button
					class="nav-trigger"
					onclick={(e) => { toggle('solutions'); }}
					aria-expanded={openDropdown === 'solutions'}
				>
					Solutions
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'solutions'}>
					<a href="/docs/platforms">Platforms &amp; Marketplaces</a>
					<a href="/docs/recurring-payments">SaaS Subscriptions</a>
					<a href="/docs">Payment Orchestration</a>
				</div>
			</div>
			<div class="nav-item">
				<button
					class="nav-trigger"
					onclick={(e) => { toggle('developers'); }}
					aria-expanded={openDropdown === 'developers'}
				>
					Developers
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'developers'}>
					<a href="/docs/getting-started">Getting Started</a>
					<a href="/docs/api">API Reference</a>
					<a href="/docs/webhooks">Webhooks</a>
				</div>
			</div>
			<div class="nav-item">
				<button
					class="nav-trigger"
					onclick={(e) => { toggle('resources'); }}
					aria-expanded={openDropdown === 'resources'}
				>
					Resources
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'resources'}>
					<a href="/docs">Documentation</a>
					<a href="/support">Support</a>
					<a href="/privacy">Privacy</a>
					<a href="/terms">Terms</a>
				</div>
			</div>
			<a class="nav-link" href="/pricing">Pricing</a>
		</nav>
		<div class="actions">
			<a class="btn ghost" href="/login" style="color: var(--ink);">Sign In</a>
			<a class="btn primary" href="/login?register=true">Get Started<svg class="arrow" width="10" height="10" fill="none" stroke="currentColor" stroke-width="2"><path class="arrow-shaft" d="M0.5 5.5h7"/><path class="arrow-head" d="M1.5 1.5l4 4-4 4"/></svg></a>
			<a class="btn sales" href="/contact">Contact Sales</a>
		</div>
	</div>
</header>

<style>
	header {
		position: sticky;
		top: 0;
		z-index: 20;
		background: #ffffff;
		border-bottom: 1px solid var(--line);
	}
	.nav {
		min-height: 66px;
		display: grid;
		grid-template-columns: auto 1fr auto;
		align-items: center;
		gap: 28px;
	}
	.brand {
		font-weight: 760;
		font-size: 23px;
		letter-spacing: -.015em;
		line-height: 1;
		color: var(--hero-bg);
	}
	.brand span { color: var(--primary); }
	.links {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: clamp(22px, 3vw, 36px);
	}
	.nav-trigger {
		background: none;
		border: none;
		cursor: pointer;
		font-family: inherit;
		font-weight: 600;
		font-size: 14px;
		color: var(--muted);
		padding: 0;
		display: flex;
		align-items: center;
		gap: 4px;
		transition: color .18s ease;
	}
	.nav-trigger:hover,
	.nav-trigger[aria-expanded="true"] { color: var(--primary); }
	.chevron {
		transition: transform .18s ease;
	}
	.nav-trigger[aria-expanded="true"] .chevron {
		transform: rotate(180deg);
	}
	.nav-link {
		color: var(--muted);
		font-weight: 600;
		font-size: 14px;
		text-decoration: none;
		transition: color .18s ease;
	}
	.nav-link:hover { color: var(--primary); }
	.nav-item { position: relative; }
	.dropdown {
		position: absolute;
		top: calc(100% + 12px);
		left: 50%;
		transform: translateX(-50%);
		min-width: 200px;
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 12px;
		box-shadow: 0 8px 24px rgba(0,0,0,0.08);
		padding: 8px;
		opacity: 0;
		visibility: hidden;
		transition: opacity .15s ease, visibility .15s ease;
	}
	.dropdown:not(.open) { pointer-events: none; }
	.dropdown.open {
		opacity: 1;
		visibility: visible;
	}
	.dropdown a {
		display: block;
		padding: 8px 16px;
		border-radius: 8px;
		color: var(--ink);
		text-decoration: none;
		font-weight: 500;
		font-size: 14px;
		line-height: 1.4;
		white-space: nowrap;
		transition: background .12s ease, color .12s ease;
	}
	.dropdown a:hover {
		background: #f6f9fc;
		color: var(--primary);
	}
	.actions {
		display: flex;
		align-items: center;
		justify-content: flex-end;
		gap: 10px;
	}
	@media (max-width: 980px) {
		.nav { grid-template-columns: auto auto; }
		.links { display: none; }
	}
	.btn.sales {
		font-size: 13px;
		font-weight: 600;
		color: var(--muted);
		text-decoration: none;
		padding: 6px 12px;
		border-radius: 4px;
		transition: color .18s ease;
	}
	.btn.sales:hover { color: var(--primary); }
	.btn.primary .arrow-shaft {
		stroke-dasharray: 7;
		stroke-dashoffset: 7;
		transition: stroke-dashoffset .25s ease;
	}
	.btn.primary .arrow-head {
		transition: transform .25s ease;
	}
	.btn.primary:hover .arrow-shaft {
		stroke-dashoffset: 0;
	}
	.btn.primary:hover .arrow-head {
		transform: translateX(3px);
	}
	@media (max-width: 680px) {
		.nav { min-height: 62px; gap: 12px; }
		.actions :global(.btn.ghost) { display: none; }
		.actions :global(.btn.sales) { display: none; }
	}
</style>
