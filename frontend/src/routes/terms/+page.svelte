<script>
</script>

<svelte:head>
	<title>Terms & Conditions | DrizlePay</title>
	<meta name="description" content="Drizle Pay Terms and Conditions — the terms governing use of our payment platform and services." />
</svelte:head>

<div class="page legal-page">
	<section class="page-hero">
		<div class="container">
			<div class="eyebrow">Policies</div>
			<h1>Terms & Conditions</h1>
			<p class="lead">Last updated: 27 June 2026</p>
		</div>
	</section>

	<section>
		<div class="container legal-content">
			<h2>1. Introduction</h2>
			<p>These Terms and Conditions ("Terms") govern your access to and use of the Drizle Pay platform, website at drizlepay.com, API, mobile application, and related services (collectively, the "Platform"). By creating an account or using the Platform, you agree to be bound by these Terms.</p>
			<p>If you are entering into these Terms on behalf of a business or entity, you represent that you have the authority to bind that entity. If you do not agree to these Terms, you may not use the Platform.</p>

			<h2>2. Definitions</h2>
			<ul>
				<li><strong>"Account"</strong> — your registered Drizle Pay merchant account</li>
				<li><strong>"Merchant"</strong> — the business or individual using Drizle Pay to accept payments</li>
				<li><strong>"Buyer"</strong> — a customer purchasing goods or services from a Merchant</li>
				<li><strong>"Transaction"</strong> — a payment processed through the Platform</li>
				<li><strong>"Service"</strong> — payment processing, subscription management, fraud screening, and related services offered by Drizle Pay</li>
				<li><strong>"Agreement"</strong> — these Terms, together with any Merchant Service Agreement signed separately</li>
			</ul>

			<h2>3. Account Registration</h2>
			<p>To use the Platform, you must create an account and provide accurate, complete information. You are responsible for:</p>
			<ul>
				<li>Maintaining the confidentiality of your login credentials</li>
				<li>All activity occurring under your account</li>
				<li>Notifying us immediately of any unauthorized access or security breach</li>
				<li>Ensuring your business information (trade license, VAT certificate, etc.) remains current</li>
			</ul>
			<p>We reserve the right to reject or suspend any account at our discretion, particularly where KYC/AML requirements cannot be satisfied.</p>

			<h2>4. Payment Processing Services</h2>
			<h3>4.1 General</h3>
			<p>Drizle Pay acts as a payment facilitator and merchant of record. We process Transactions on your behalf through our network of acquiring banks and payment partners.</p>
			<h3>4.2 Settlement</h3>
			<p>Settlement of funds to your designated bank account occurs according to the schedule in your Merchant Service Agreement (typically T+1 to T+3 business days). Drizle Pay reserves the right to hold settlement funds pending fraud review or dispute resolution.</p>
			<h3>4.3 Fees</h3>
			<p>Processing fees are as set out in your Merchant Service Agreement or as displayed in your account dashboard. We may change fees with 30 days' notice. Continued use of the Platform after fee changes constitutes acceptance.</p>
			<h3>4.4 Chargebacks and Refunds</h3>
			<p>You are liable for all chargebacks, reversals, and refunds associated with your Transactions. Drizle Pay may deduct such amounts from your settlement balance or invoice you directly. Excessive chargebacks may result in account suspension or termination.</p>

			<h2>5. Compliance and Prohibited Activities</h2>
			<h3>5.1 Regulatory Compliance</h3>
			<p>You agree to comply with all applicable laws and regulations, including UAE Central Bank regulations, AML/CTF laws, PCI DSS requirements, data protection laws, and UAE VAT regulations.</p>
			<h3>5.2 Prohibited Businesses and Activities</h3>
			<p>Prohibited categories include illegal goods, adult content (unless approved), gambling, money services, cryptocurrency exchanges (without prior approval), MLM schemes, and any activity violating UAE law.</p>

			<h2>6. Intellectual Property</h2>
			<p>The Platform, including its design, code, trademarks, and content, is owned by Drizle Payments LLC. You may not copy, modify, distribute, reverse-engineer, or create derivative works without our prior written consent.</p>

			<h2>7. Limitation of Liability</h2>
			<p>To the maximum extent permitted by applicable law, Drizle Pay shall not be liable for indirect, incidental, special, or consequential damages. Our total liability for any claim shall not exceed the total fees paid by you in the 12 months preceding the claim.</p>

			<h2>8. Indemnification</h2>
			<p>You agree to indemnify and hold Drizle Pay harmless from any claims, losses, damages, and expenses arising from your breach of these Terms, violation of applicable law, or processing of prohibited transactions.</p>

			<h2>9. Termination</h2>
			<p>Either party may terminate this Agreement with 30 days' written notice. We may terminate immediately if you breach these Terms, your chargeback ratio exceeds acceptable thresholds, or we are required to do so by a regulatory authority.</p>

			<h2>10. Governing Law and Dispute Resolution</h2>
			<p>These Terms are governed by the laws of the United Arab Emirates and the Emirate of Dubai. Any disputes shall be subject to the exclusive jurisdiction of the Dubai courts.</p>

			<h2>11. Changes to Terms</h2>
			<p>We may modify these Terms at any time. Material changes will be communicated via email or through the Platform. Continued use after changes takes effect constitutes acceptance.</p>

			<h2>12. Contact</h2>
			<p><strong>Drizle Payments LLC</strong><br><strong>Email:</strong> <a href="mailto:legal@drizlepay.com">legal@drizlepay.com</a><br><strong>Address:</strong> Dubai, United Arab Emirates</p>
		</div>
	</section>
</div>

<style>
	.legal-page { background: var(--bg); }
	.page-hero {
		padding: clamp(48px, 6vw, 72px) 0;
		background: var(--hero-bg);
		color: var(--hero-text);
	}
	.page-hero .lead { color: var(--hero-muted); font-size: 16px; margin: 0; }
	.legal-content {
		max-width: 800px;
		margin: 0 auto;
		padding: clamp(48px, 6vw, 72px) 0;
	}
	.legal-content h2 {
		font-size: 24px;
		font-weight: 700;
		color: var(--hero-bg);
		margin: 40px 0 16px;
	}
	.legal-content h2:first-child { margin-top: 0; }
	.legal-content h3 {
		font-size: 18px;
		font-weight: 600;
		color: var(--hero-bg);
		margin: 24px 0 12px;
	}
	.legal-content p {
		color: var(--muted);
		font-size: 16px;
		line-height: 1.7;
		margin: 0 0 16px;
	}
	.legal-content ul { margin: 0 0 20px; padding-left: 24px; }
	.legal-content li {
		color: var(--muted);
		font-size: 16px;
		line-height: 1.7;
		margin-bottom: 8px;
	}
	.legal-content a { color: var(--primary); }
	.legal-content a:hover { text-decoration: underline; }
	.legal-content strong { color: var(--ink); }
</style>
