<script>
</script>

<svelte:head>
	<title>About Us | Drizle Pay</title>
	<meta name="description" content="Learn about Drizle Pay — the UAE's full-stack payment platform powering digital commerce for businesses across the Middle East." />
</svelte:head>

<div class="page">
	<section class="page-hero">
		<div class="container">
			<div class="eyebrow">About Drizle Pay</div>
			<h1>We power commerce by making payments simple, intelligent, and inclusive.</h1>
			<p class="lead">Headquartered in Dubai, Drizle Pay is a full-stack payment platform that helps businesses accept payments, manage subscriptions, handle global compliance, and grow revenue — all from a single integration.</p>
		</div>
	</section>

	<section>
		<div class="container">
			<h2 class="section-title">Our Mission</h2>
			<p class="section-copy">To democratise access to modern payment infrastructure across the Middle East and Africa. We believe every business — whether a Dubai startup or a Cairo retailer — deserves the same payment capabilities as the world's largest enterprises.</p>
		</div>
	</section>

	<section class="alt-bg">
		<div class="container">
			<h2 class="section-title">By the Numbers</h2>
			<div class="stats-grid">
				<div class="stat-card"><strong>2024</strong><span>Founded in Dubai, UAE</span></div>
				<div class="stat-card"><strong>15+</strong><span>Markets served across MENA</span></div>
				<div class="stat-card"><strong>99.95%</strong><span>Platform uptime</span></div>
				<div class="stat-card"><strong>30+</strong><span>Payment methods supported</span></div>
			</div>
		</div>
	</section>

	<section>
		<div class="container split">
			<div>
				<h2 class="section-title">What Sets Us Apart</h2>
				<p class="section-copy">Unlike traditional gateways that only route transactions, Drizle Pay is a unified platform. We handle payment orchestration, tax compliance, fraud screening, subscription billing, and reconciliation — so you can focus on your product, not your payments stack.</p>
			</div>
			<div class="values-list">
				<div class="value-item">
					<strong>Intelligent Routing</strong>
					<span>Transactions are dynamically routed to the acquiring bank most likely to authorise them, boosting success rates.</span>
				</div>
				<div class="value-item">
					<strong>Local Expertise</strong>
					<span>Built for the UAE market first — supporting Jaywan, Aani, Tabby, Tamara, and local acquiring banks natively.</span>
				</div>
				<div class="value-item">
					<strong>Merchant of Record</strong>
					<span>We take on the compliance burden — VAT/GST calculation, invoicing, and regulatory reporting across jurisdictions.</span>
				</div>
			</div>
		</div>
	</section>

	<section class="alt-bg">
		<div class="container cta">
			<div>
				<h2>Ready to simplify your payments?</h2>
				<p>Join businesses across the UAE that trust Drizle Pay to process, protect, and grow their revenue.</p>
			</div>
			<a class="btn primary" href="/login">Get Started</a>
		</div>
	</section>
</div>

<style>
	.page { background: var(--bg); }
	.page-hero {
		padding: clamp(64px, 8vw, 96px) 0;
		background: var(--hero-bg);
		color: var(--hero-text);
	}
	.page-hero h1 { max-width: 800px; }
	.page-hero .lead { color: var(--hero-muted); max-width: 700px; }
	.alt-bg { background: #f8fafc; }
	.stats-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 20px;
	}
	.stat-card {
		padding: 28px 24px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #fff;
		box-shadow: var(--shadow);
	}
	.stat-card strong {
		display: block;
		font-size: 32px;
		font-weight: 800;
		color: var(--primary);
		margin-bottom: 8px;
	}
	.stat-card span {
		color: var(--muted);
		font-size: 14px;
		line-height: 1.5;
	}
	.values-list { display: grid; gap: 16px; }
	.value-item {
		padding: 24px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #fff;
	}
	.value-item strong {
		display: block;
		font-size: 18px;
		font-weight: 700;
		color: var(--hero-bg);
		margin-bottom: 8px;
	}
	.value-item span {
		color: var(--muted);
		font-size: 15px;
		line-height: 1.6;
	}
	@media (max-width: 980px) {
		.stats-grid { grid-template-columns: repeat(2, 1fr); }
	}
	@media (max-width: 680px) {
		.stats-grid { grid-template-columns: 1fr; }
	}
</style>
