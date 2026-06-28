<script>
	let openDropdown = $state('');
	let closeTimeout;
	let pinned = $state('');

	function open(name) {
		clearTimeout(closeTimeout);
		if (!pinned) openDropdown = name;
	}

	function close() {
		if (pinned) return;
		closeTimeout = setTimeout(() => { openDropdown = ''; }, 150);
	}

	function clickToggle(name) {
		if (pinned === name) {
			pinned = '';
			openDropdown = '';
		} else {
			pinned = name;
			openDropdown = name;
			clearTimeout(closeTimeout);
		}
	}

	function onWindowClick(e) {
		if (e.target.closest('.nav-item') || e.target.closest('.dropdown')) return;
		pinned = '';
		openDropdown = '';
	}
</script>

<svelte:window onclick={onWindowClick} />

<header>
	<div class="container nav">
		<a class="brand" href="/" aria-label="Drizle Pay homepage"><svg viewBox="0 0 120 130" width="24" height="26" fill="none" aria-hidden="true"><path d="M25,15 L50,15 L30,105 L5,105 Z" fill="#06162c"/><path d="M57,15 L82,15 L62,105 L37,105 Z" fill="#06162c" opacity="0.85"/><path d="M89,15 L120,55 L79,105 L65,105 L85,55 L64,15 Z" fill="#02c366"/></svg> Drizle<span>Pay</span></a>
		<nav class="links" aria-label="Primary navigation">
			<div class="nav-item" onmouseenter={() => open('products')} onmouseleave={close}>
				<button class="nav-trigger" onclick={() => clickToggle('products')} aria-expanded={openDropdown === 'products'}>
					Products
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'products'} onmouseenter={() => open('products')} onmouseleave={close}>
					<div class="dd-grid">
						<section>
							<h4 class="dd-stitle">Payments</h4>
							<a href="/docs/payments" class="dd-link">
								<span class="dd-link-title">Payments<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Accept online payments</span>
							</a>
							<a href="/docs/recurring-payments" class="dd-link">
								<span class="dd-link-title">Subscriptions<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Recurring billing management</span>
							</a>
						</section>
						<section>
							<h4 class="dd-stitle">Money</h4>
							<a href="/docs/payouts" class="dd-link">
								<span class="dd-link-title">Payouts<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Send mass payouts</span>
							</a>
						</section>
					</div>
				</div>
			</div>
			<div class="nav-item" onmouseenter={() => open('solutions')} onmouseleave={close}>
				<button class="nav-trigger" onclick={() => clickToggle('solutions')} aria-expanded={openDropdown === 'solutions'}>
					Solutions
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'solutions'} onmouseenter={() => open('solutions')} onmouseleave={close}>
					<div class="dd-grid">
						<section>
							<h4 class="dd-stitle">Platforms</h4>
							<a href="/docs/platforms" class="dd-link">
								<span class="dd-link-title">Platforms &amp; Marketplaces<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Manage multiparty payments</span>
							</a>
						</section>
						<section>
							<h4 class="dd-stitle">Revenue</h4>
							<a href="/docs/recurring-payments" class="dd-link">
								<span class="dd-link-title">SaaS Subscriptions<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Automate recurring billing</span>
							</a>
							<a href="/docs" class="dd-link">
								<span class="dd-link-title">Payment Orchestration<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Optimize routing</span>
							</a>
						</section>
					</div>
				</div>
			</div>
			<div class="nav-item" onmouseenter={() => open('developers')} onmouseleave={close}>
				<button class="nav-trigger" onclick={() => clickToggle('developers')} aria-expanded={openDropdown === 'developers'}>
					Developers
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'developers'} onmouseenter={() => open('developers')} onmouseleave={close}>
					<div class="dd-grid">
						<section>
							<h4 class="dd-stitle">Build</h4>
							<a href="/docs/getting-started" class="dd-link">
								<span class="dd-link-title">Getting Started<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Quick integration guide</span>
							</a>
							<a href="/docs/api" class="dd-link">
								<span class="dd-link-title">API Reference<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Complete API documentation</span>
							</a>
						</section>
						<section>
							<h4 class="dd-stitle">Events</h4>
							<a href="/docs/webhooks" class="dd-link">
								<span class="dd-link-title">Webhooks<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Real-time notifications</span>
							</a>
						</section>
					</div>
				</div>
			</div>
			<div class="nav-item" onmouseenter={() => open('resources')} onmouseleave={close}>
				<button class="nav-trigger" onclick={() => clickToggle('resources')} aria-expanded={openDropdown === 'resources'}>
					Resources
					<svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
						<path d="M4.67 6l4.63 4.6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
						<path d="M12.67 6l-4 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
					</svg>
				</button>
				<div class="dropdown" class:open={openDropdown === 'resources'} onmouseenter={() => open('resources')} onmouseleave={close}>
					<div class="dd-grid">
						<section>
							<h4 class="dd-stitle">Learn</h4>
							<a href="/docs" class="dd-link">
								<span class="dd-link-title">Documentation<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Guides &amp; references</span>
							</a>
							<a href="/support" class="dd-link">
								<span class="dd-link-title">Support<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Get help</span>
							</a>
						</section>
						<section>
							<h4 class="dd-stitle">Legal</h4>
							<a href="/privacy" class="dd-link">
								<span class="dd-link-title">Privacy Policy<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Data protection</span>
							</a>
							<a href="/terms" class="dd-link">
								<span class="dd-link-title">Terms &amp; Conditions<svg class="dd-arrow" width="10" height="8" viewBox="0 0 10 8" fill="none" aria-hidden="true"><path fill="currentColor" d="M9.752 3.913 5.87 7.825l-.959-.951 2.27-2.287H0v-1.35h7.18L4.912.951 5.871 0z"/></svg></span>
								<span class="dd-link-desc">Terms of service</span>
							</a>
						</section>
					</div>
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
		display: inline-flex;
		align-items: center;
		font-weight: 760;
		font-size: 23px;
		letter-spacing: -.015em;
		line-height: 1;
		color: var(--hero-bg);
		text-decoration: none;
	}
	.brand svg { margin-right: 6px; margin-top: 4px; }
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
		transition: transform .25s cubic-bezier(0.16, 1, 0.3, 1);
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
		top: calc(100% + 10px);
		left: 0;
		transform: translateY(4px);
		width: 200px;
		background: #fff;
		border: 1px solid rgba(0,0,0,0.06);
		border-radius: 8px;
		box-shadow:
			0 0 0 1px rgba(0,0,0,0.02),
			0 6px 20px rgba(0,0,0,0.06),
			0 12px 40px rgba(0,0,0,0.04);
		padding: 1px;
		opacity: 0;
		pointer-events: none;
		transition: opacity .2s ease, transform .25s cubic-bezier(0.16, 1, 0.3, 1);
	}
	.dropdown.open {
		opacity: 1;
		transform: translateY(0);
		pointer-events: auto;
	}
	.dd-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 0;
	}
	.dd-grid section {
		display: flex;
		flex-direction: column;
		padding: 0;
	}
	.dd-stitle {
		font-size: 10px;
		line-height: 1.2;
		font-weight: 600;
		letter-spacing: .06em;
		text-transform: uppercase;
		color: var(--muted);
		margin: 0;
		padding: 0 14px 1px;
		display: none;
	}
	.dd-link {
		display: flex;
		flex-direction: column;
		padding: 6px 14px;
		border-radius: 10px;
		text-decoration: none;
		transition: background .15s ease;
	}
	.dd-link:hover { background: #f6f9fc; }
	.dd-link-title {
		font-size: 14px;
		font-weight: 600;
		line-height: 1.2;
		color: var(--ink);
		display: inline-flex;
		align-items: center;
		gap: 0;
		transition: color .15s ease;
	}
	.dd-link:hover .dd-link-title { color: var(--primary); }
	.dd-arrow {
		margin-left: 4px;
		flex-shrink: 0;
		opacity: 0;
		transition: opacity .2s ease, transform .2s ease;
	}
	.dd-link:hover .dd-arrow {
		opacity: 1;
		transform: translateX(3px);
	}
	.dd-link-desc {
		font-size: 12px;
		font-weight: 400;
		color: var(--muted);
		line-height: 1.1;
		margin-top: 0;
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
