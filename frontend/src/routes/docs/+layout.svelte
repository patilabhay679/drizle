<script>
	import { page } from '$app/state';

	let { children } = $props();

	let sidebarOpen = $state(false);

	const groups = [
		{
			name: 'Getting Started',
			items: [
				{ href: '/docs', label: 'Overview' },
				{ href: '/docs/getting-started', label: 'Quickstart' },
				{ href: '/docs/authentication', label: 'Authentication' },
				{ href: '/docs/errors', label: 'Error Codes' },
				{ href: '/docs/versioning', label: 'Versioning' },
			]
		},
		{
			name: 'Core Resources',
			items: [
				{ href: '/docs/balance', label: 'Balance' },
				{ href: '/docs/charges', label: 'Charges' },
				{ href: '/docs/customers', label: 'Customers' },
				{ href: '/docs/disputes', label: 'Disputes' },
				{ href: '/docs/events', label: 'Events' },
				{ href: '/docs/files', label: 'Files' },
				{ href: '/docs/payment-intents', label: 'Payment Intents' },
				{ href: '/docs/payments', label: 'Payments' },
				{ href: '/docs/payouts', label: 'Payouts' },
				{ href: '/docs/refunds', label: 'Refunds' },
				{ href: '/docs/setup-intents', label: 'Setup Intents' },
				{ href: '/docs/tokens', label: 'Tokens' },
				{ href: '/docs/transfers', label: 'Transfers' },
			]
		},
		{
			name: 'Payment Methods',
			items: [
				{ href: '/docs/payment-methods', label: 'Payment Methods' },
				{ href: '/docs/cards', label: 'Cards' },
				{ href: '/docs/sources', label: 'Sources' },
			]
		},
		{
			name: 'Products & Pricing',
			items: [
				{ href: '/docs/products', label: 'Products' },
				{ href: '/docs/prices', label: 'Prices' },
				{ href: '/docs/coupons', label: 'Coupons' },
				{ href: '/docs/promotion-codes', label: 'Promotion Codes' },
				{ href: '/docs/shipping-rates', label: 'Shipping Rates' },
				{ href: '/docs/tax-codes', label: 'Tax Codes' },
				{ href: '/docs/tax-rates', label: 'Tax Rates' },
			]
		},
		{
			name: 'Subscriptions & Invoicing',
			items: [
				{ href: '/docs/subscriptions', label: 'Subscriptions' },
				{ href: '/docs/subscription-items', label: 'Subscription Items' },
				{ href: '/docs/subscription-schedules', label: 'Subscription Schedules' },
				{ href: '/docs/invoices', label: 'Invoices' },
				{ href: '/docs/invoice-items', label: 'Invoice Items' },
				{ href: '/docs/credit-notes', label: 'Credit Notes' },
				{ href: '/docs/quotes', label: 'Quotes' },
				{ href: '/docs/billing-portal', label: 'Billing Portal' },
			]
		},
		{
			name: 'Connect',
			items: [
				{ href: '/docs/accounts', label: 'Accounts' },
				{ href: '/docs/account-links', label: 'Account Links' },
				{ href: '/docs/application-fees', label: 'Application Fees' },
				{ href: '/docs/capabilities', label: 'Capabilities' },
				{ href: '/docs/country-specs', label: 'Country Specs' },
				{ href: '/docs/persons', label: 'Persons' },
				{ href: '/docs/external-accounts', label: 'External Accounts' },
				{ href: '/docs/platforms', label: 'Platforms' },
			]
		},
		{
			name: 'Fraud & Risk',
			items: [
				{ href: '/docs/reviews', label: 'Reviews' },
				{ href: '/docs/radar-value-lists', label: 'Value Lists' },
				{ href: '/docs/radar-early-fraud-warnings', label: 'Early Fraud Warnings' },
			]
		},
		{
			name: 'Additional APIs',
			items: [
				{ href: '/docs/tax', label: 'Tax' },
				{ href: '/docs/identity', label: 'Identity' },
				{ href: '/docs/financial-connections', label: 'Financial Connections' },
				{ href: '/docs/reporting', label: 'Reporting' },
				{ href: '/docs/forwarding', label: 'Forwarding API' },
				{ href: '/docs/climate', label: 'Climate' },
				{ href: '/docs/terminal', label: 'Terminal' },
			]
		},
		{
			name: 'Guides',
			items: [
				{ href: '/docs/webhooks', label: 'Webhooks' },
				{ href: '/docs/webhook-endpoints', label: 'Webhook Endpoints' },
				{ href: '/docs/idempotency', label: 'Idempotency' },
			]
		}
	];

	let pathname = $derived(page.url.pathname);
</script>

<div class="dl">
	<aside class="ds" class:open={sidebarOpen}>
		<div class="ds-hd">
			<a href="/" class="ds-brand">Drizle<span>Pay</span> <span class="ds-suffix">Docs</span></a>
			<button class="ds-close" onclick={() => sidebarOpen = false}>✕</button>
		</div>
		<nav>
			{#each groups as group}
				<div class="ng">
					<div class="ng-t">{group.name}</div>
					{#each group.items as item}
						<a
							href={item.href}
							class="nl"
							class:active={pathname === item.href}
							onclick={() => sidebarOpen = false}
						>
							<span class="nl-dot" class:active={pathname === item.href}></span>
							{item.label}
						</a>
					{/each}
				</div>
			{/each}
		</nav>
		<div class="ds-ft">
			<a href="/" class="ds-ft-link">← Back to site</a>
		</div>
	</aside>

	<div class="ov" class:visible={sidebarOpen} onclick={() => sidebarOpen = false}></div>

	<main class="dc">
		<header class="tb">
			<button class="tb-menu" onclick={() => sidebarOpen = true}>☰</button>
			<div class="bc">
				<a href="/docs">API Reference</a>
				{#if pathname !== '/docs'}
					{@const parts = pathname.replace('/docs/', '').split('/')}
					{#each parts as part}
						<span class="bc-sep">/</span>
						<span class="bc-crumb">{part.replace(/-/g, ' ')}</span>
					{/each}
				{/if}
			</div>
			<div class="sp"></div>
		</header>
		<div class="ct">
			{@render children()}
		</div>
	</main>
</div>

<style>
	.dl { display: flex; min-height: 100vh; background: #fff; }

	/* ─── Sidebar ─── */
	.ds {
		width: 270px;
		background: #fafbfc;
		border-right: 1px solid #edf2f7;
		display: flex;
		flex-direction: column;
		position: fixed;
		top: 0;
		left: 0;
		bottom: 0;
		z-index: 30;
		overflow-y: auto;
		transition: transform 0.2s;
	}
	.ds-hd {
		padding: 20px 20px 16px;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.ds-brand { font-weight: 800; font-size: 17px; color: #0f172a; text-decoration: none; letter-spacing: -0.02em; }
	.ds-brand span { color: var(--primary); }
	.ds-brand .ds-suffix { font-size: 13px; font-weight: 500; color: #94a3b8; }
	.ds-close { display: none; background: none; border: none; font-size: 18px; cursor: pointer; color: #94a3b8; }
	nav { flex: 1; padding: 12px 10px 20px; }
	.ng { margin-bottom: 24px; }
	.ng:last-child { margin-bottom: 0; }
	.ng-t {
		font-size: 10px;
		font-weight: 700;
		color: #94a3b8;
		text-transform: uppercase;
		letter-spacing: 0.08em;
		padding: 0 12px;
		margin-bottom: 6px;
	}
	.nl {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 7px 12px;
		border-radius: 5px;
		color: #475569;
		font-size: 14px;
		font-weight: 500;
		text-decoration: none;
		transition: all 0.12s;
	}
	.nl:hover { background: #edf2f7; color: #0f172a; }
	.nl.active { background: #f0fdf4; color: #059669; font-weight: 600; }
	.nl-dot {
		width: 5px;
		height: 5px;
		border-radius: 50%;
		background: #cbd5e1;
		flex-shrink: 0;
	}
	.nl-dot.active { background: var(--primary); }
	.nl.active .nl-dot { background: var(--primary); box-shadow: 0 0 0 2px #d1fae5; }

	.ds-ft {
		padding: 12px 16px;
		border-top: 1px solid #edf2f7;
	}
	.ds-ft-link {
		font-size: 13px;
		font-weight: 500;
		color: #94a3b8;
		text-decoration: none;
	}
	.ds-ft-link:hover { color: #059669; }

	.ov { display: none; }

	/* ─── Main Content ─── */
	.dc {
		flex: 1;
		margin-left: 270px;
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}
	.tb {
		height: 52px;
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 0 32px;
		border-bottom: 1px solid #edf2f7;
		background: #fff;
		position: sticky;
		top: 0;
		z-index: 10;
	}
	.tb-menu { display: none; background: none; border: none; font-size: 20px; cursor: pointer; color: #475569; padding: 4px; }
	.bc {
		display: flex;
		align-items: center;
		gap: 6px;
		font-size: 13px;
		color: #94a3b8;
	}
	.bc a { color: #94a3b8; text-decoration: none; font-weight: 500; }
	.bc a:hover { color: #059669; }
	.bc-sep { color: #cbd5e1; font-weight: 300; }
	.bc-crumb { color: #334155; font-weight: 500; text-transform: capitalize; }
	.sp { flex: 1; }
	.ct {
		flex: 1;
		padding: 48px 56px;
		max-width: 920px;
	}

	/* ─── Mobile ─── */
	@media (max-width: 900px) {
		.ds { transform: translateX(-100%); }
		.ds.open { transform: translateX(0); }
		.ds-close { display: block; }
		.ov {
			display: block;
			position: fixed;
			inset: 0;
			background: rgba(15,23,42,0.4);
			z-index: 29;
			opacity: 0;
			pointer-events: none;
			transition: opacity 0.2s;
		}
		.ov.visible { opacity: 1; pointer-events: auto; }
		.dc { margin-left: 0; }
		.tb-menu { display: block; }
		.ct { padding: 32px 24px; }
		.tb { padding: 0 16px; }
	}
</style>
