<script>
	const features = [
		'Payment processing (cards, wallets, BNPL)',
		'Subscription & recurring billing',
		'Fraud screening & chargeback protection',
		'VAT/GST calculation & invoicing',
		'Dashboard & real-time analytics',
		'API & webhook access',
		'Email & chat support',
		'PCI DSS Level 1 compliance'
	];

	const enterpriseFeatures = [
		'Dedicated account manager',
		'Custom acquiring bank integration',
		'Volume-based pricing',
		'SLA guarantees (99.99% uptime)',
		'Priority support (phone + Slack)',
		'On-site onboarding & migration',
		'Custom webhooks & reporting',
		'Multi-entity consolidation'
	];

	const faq = [
		{
			q: 'Are there any setup or monthly fees?',
			a: 'No setup fees, no monthly minimums, and no hidden charges. You only pay when you process payments.'
		},
		{
			q: 'When do I get paid out?',
			a: 'Settlement occurs on T+1 for most transactions. Instant settlement is available for eligible merchants.'
		},
		{
			q: 'Do you support multiple currencies?',
			a: 'Yes. You can accept payments in AED, USD, EUR, GBP, SAR, and 100+ currencies. Settlement in AED is standard.'
		},
		{
			q: 'What is the contract duration?',
			a: 'No lock-in contracts. You can cancel anytime. Enterprise plans may have minimum terms.'
		},
		{
			q: 'Is there a discount for high-volume merchants?',
			a: 'Yes. Process over AED 500K/month and you qualify for volume-based pricing. Contact our sales team.'
		}
	];
</script>

<svelte:head>
	<title>Pricing | DrizlePay</title>
	<meta name="description" content="Transparent pricing for Drizle Pay. No setup fees, no hidden charges. Accept payments in AED and 100+ currencies." />
</svelte:head>

<div class="page pricing-page">
	<section class="page-hero">
		<div class="container">
			<div class="eyebrow">Pricing</div>
			<h1>Simple, transparent pricing</h1>
			<p class="lead">No setup fees, no monthly minimums, no hidden charges. You only pay when you process.</p>
		</div>
	</section>

	<section>
		<div class="container plans">
			<div class="plan-card">
				<div class="plan-name">Standard</div>
				<div class="plan-price">
					<strong>2.9% + AED 1</strong>
					<span>per successful transaction</span>
				</div>
				<ul class="plan-features">
					{#each features as f}
						<li>{f}</li>
					{/each}
				</ul>
				<a class="btn primary" href="/login?register=true">Get Started</a>
			</div>
			<div class="plan-card featured">
				<div class="plan-badge">Best for Scale</div>
				<div class="plan-name">Enterprise</div>
				<div class="plan-price">
					<strong>From 1.5% + AED 0.50</strong>
					<span>volume-based pricing</span>
				</div>
				<ul class="plan-features">
					{#each enterpriseFeatures as f}
						<li>{f}</li>
					{/each}
				</ul>
				<a class="btn primary" href="/contact">Contact Sales</a>
			</div>
		</div>
	</section>

	<section class="alt-bg">
		<div class="container">
			<h2 class="section-title">Additional Services</h2>
			<div class="addon-grid">
				<div class="addon-card">
					<strong>International Cards</strong>
					<span>+0.5% per transaction</span>
				</div>
				<div class="addon-card">
					<strong>BNPL (Tabby / Tamara)</strong>
					<span>From 3.5% + AED 2</span>
				</div>
				<div class="addon-card">
					<strong>Instant Settlement</strong>
					<span>1% of settlement amount</span>
				</div>
				<div class="addon-card">
					<strong>API Only Plan</strong>
					<span>From 2.5% + AED 0.50</span>
				</div>
			</div>
		</div>
	</section>

	<section>
		<div class="container">
			<h2 class="section-title">Frequently Asked Questions</h2>
			<div class="faq-list">
				{#each faq as { q, a }}
					<details class="faq-item">
						<summary>{q}</summary>
						<p>{a}</p>
					</details>
				{/each}
			</div>
		</div>
	</section>

	<section class="alt-bg">
		<div class="container cta">
			<div>
				<h2>Ready to start accepting payments?</h2>
				<p>Create your account in minutes. No commitment, no credit card required.</p>
			</div>
			<a class="btn primary" href="/login?register=true">Get Started</a>
		</div>
	</section>
</div>

<style>
	.pricing-page { background: var(--bg); }
	.page-hero {
		padding: clamp(64px, 8vw, 96px) 0;
		background: var(--hero-bg);
		color: var(--hero-text);
	}
	.page-hero h1 { max-width: 700px; }
	.page-hero .lead { color: var(--hero-muted); max-width: 600px; }
	.plans {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 28px;
		align-items: start;
	}
	.plan-card {
		padding: 40px 32px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #fff;
		box-shadow: var(--shadow);
		display: grid;
		gap: 24px;
		position: relative;
	}
	.plan-card.featured {
		border-color: var(--primary);
		border-width: 2px;
		box-shadow: 0 10px 30px rgba(2, 195, 102, 0.1);
	}
	.plan-badge {
		position: absolute;
		top: -13px;
		left: 50%;
		transform: translateX(-50%);
		padding: 4px 16px;
		border-radius: 4px;
		background: var(--primary);
		color: var(--hero-bg);
		font-size: 12px;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: .04em;
	}
	.plan-name {
		font-size: 22px;
		font-weight: 700;
		color: var(--hero-bg);
	}
	.plan-price strong {
		display: block;
		font-size: 36px;
		font-weight: 800;
		color: var(--hero-bg);
		letter-spacing: -.02em;
		line-height: 1.1;
		margin-bottom: 6px;
	}
	.plan-price span {
		color: var(--muted);
		font-size: 14px;
	}
	.plan-features {
		list-style: none;
		padding: 0;
		margin: 0;
		display: grid;
		gap: 12px;
	}
	.plan-features li {
		padding-left: 24px;
		position: relative;
		color: var(--ink);
		font-size: 14.5px;
		line-height: 1.5;
	}
	.plan-features li::before {
		content: '';
		position: absolute;
		left: 0;
		top: 7px;
		width: 14px;
		height: 10px;
		border-left: 2px solid var(--primary);
		border-bottom: 2px solid var(--primary);
		transform: rotate(-45deg);
	}
	.addon-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 20px;
	}
	.addon-card {
		padding: 28px 24px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #fff;
	}
	.addon-card strong {
		display: block;
		font-size: 17px;
		font-weight: 700;
		color: var(--hero-bg);
		margin-bottom: 8px;
	}
	.addon-card span {
		color: var(--primary);
		font-size: 15px;
		font-weight: 600;
	}
	.faq-list {
		max-width: 780px;
		display: grid;
		gap: 2px;
	}
	.faq-item {
		padding: 20px 24px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #fff;
	}
	.faq-item summary {
		font-size: 16px;
		font-weight: 600;
		color: var(--hero-bg);
		cursor: pointer;
		user-select: none;
	}
	.faq-item[open] summary { margin-bottom: 12px; }
	.faq-item p {
		color: var(--muted);
		font-size: 15px;
		line-height: 1.6;
		margin: 0;
	}
	@media (max-width: 980px) {
		.plans { grid-template-columns: 1fr; }
		.addon-grid { grid-template-columns: repeat(2, 1fr); }
	}
	@media (max-width: 680px) {
		.addon-grid { grid-template-columns: 1fr; }
	}
</style>
