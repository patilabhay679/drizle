<script>
	let name = $state('');
	let email = $state('');
	let subj = $state('');
	let cat = $state('Account');
	let msg = $state('');
	let loading = $state(false);
	let done = $state(false);
	let err = $state('');

	async function submitTicket(e) {
		e.preventDefault();
		loading = true;
		err = '';
		try {
			const { api } = await import('$lib/api');
			await api.submitPublicTicket({ name, email, subject: subj, category: cat, message: msg });
			done = true;
		} catch (e) {
			err = e.message;
		} finally {
			loading = false;
		}
	}

	const faq = [
		{
			q: 'How do I reset my password?',
			a: 'On the login page, click "Forgot password?" and enter your registered email. You\'ll receive a password reset link within a few minutes. If you don\'t see it, check your spam folder.',
		},
		{
			q: 'What payment methods are supported?',
			a: 'We support cards (Visa, Mastercard, Amex), Apple Pay, Google Pay, local UAE schemes (Jaywan), BNPL providers (Tabby, Tamara), and bank transfers. New methods are added regularly.',
		},
		{
			q: 'How long do payouts take?',
			a: 'Standard payouts to UAE bank accounts are processed within 24–48 hours on business days. International payouts may take 3–5 business days depending on the destination.',
		},
		{
			q: 'How do I get my API keys?',
			a: 'Sign in to your dashboard, go to Settings, and you\'ll find your publishable and secret API keys. Never share your secret key publicly.',
		},
		{
			q: 'Can I test payments before going live?',
			a: 'Yes. Use our test mode with test card numbers (available in the docs) to simulate successful and failed payments without processing real transactions.',
		},
		{
			q: 'What are the transaction fees?',
			a: 'Fees depend on your pricing plan and payment method. Standard card transactions are 2.9% + AED 1.00. Local UAE schemes and BNPL may have different rates. See our pricing page for details.',
		},
	];

	const quickLinks = [
		{ title: 'Getting Started', desc: 'Integrate Drizle Pay in minutes', href: '/docs/payments' },
		{ title: 'API Reference', desc: 'Explore our REST API endpoints', href: '/docs/api' },
		{ title: 'Payouts Guide', desc: 'Understand settlement schedules', href: '/docs/payouts' },
		{ title: 'Webhooks', desc: 'Set up real-time notifications', href: '/docs/webhook-endpoints' },
	];
</script>

<svelte:head>
	<title>Support | Drizle Pay</title>
	<meta name="description" content="Get help with Drizle Pay. Browse FAQs, explore documentation, or reach out to our support team." />
</svelte:head>

<div class="page">
	<section class="page-hero">
		<div class="container">
			<div class="eyebrow">Help & Support</div>
			<h1>How can we help you?</h1>
			<p class="lead">Find answers in our documentation, browse common questions, or get in touch with our team.</p>
		</div>
	</section>

	<section>
		<div class="container">
			<h2 class="section-title">Quick Links</h2>
			<div class="links-grid">
				{#each quickLinks as link}
					<a href={link.href} class="link-card">
						<strong>{link.title}</strong>
						<span>{link.desc}</span>
					</a>
				{/each}
			</div>
		</div>
	</section>

	<section class="alt-bg">
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
		<div class="container">
			<h2 class="section-title">Submit a Ticket</h2>
			<p class="section-copy">Our support team is available Sunday through Thursday, 9 AM to 6 PM GST. We typically respond within 2–4 hours during business hours.</p>
			{#if done}
				<div class="success-card">
					<strong>Ticket submitted</strong>
					<p>We've received your request and will get back to you soon. You'll hear from us at <strong>{email}</strong>.</p>
					<button class="btn secondary" onclick={() => { done = false; name = ''; email = ''; subj = ''; msg = ''; }}>Submit another</button>
				</div>
			{:else}
				<form onsubmit={submitTicket} class="ticket-form">
					{#if err}
						<div class="form-error">{err}</div>
					{/if}
					<div class="form-row">
						<label>
							<span>Name</span>
							<input type="text" bind:value={name} required placeholder="Your full name" />
						</label>
						<label>
							<span>Email</span>
							<input type="email" bind:value={email} required placeholder="you@company.com" />
						</label>
					</div>
					<label>
						<span>Subject</span>
						<input type="text" bind:value={subj} required placeholder="Brief summary of the issue" />
					</label>
					<label>
						<span>Category</span>
						<select bind:value={cat}>
							<option value="Account">Account</option>
							<option value="Payments">Payments</option>
							<option value="API">API</option>
							<option value="Integrations">Integrations</option>
							<option value="Billing">Billing</option>
							<option value="Other">Other</option>
						</select>
					</label>
					<label>
						<span>Message</span>
						<textarea bind:value={msg} required rows="5" placeholder="Describe your issue in detail"></textarea>
					</label>
					<button type="submit" class="btn primary" disabled={loading}>
						{loading ? 'Submitting…' : 'Submit Ticket'}
					</button>
				</form>
			{/if}
		</div>
	</section>

	<section class="alt-bg">
		<div class="container cta">
			<div>
				<h2>Ready to get started?</h2>
				<p>Create an account and start accepting payments in minutes.</p>
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
	.page-hero h1 { max-width: 700px; }
	.page-hero .lead { color: var(--hero-muted); max-width: 600px; }
	.alt-bg { background: #f8fafc; }
	.section-title { font-size: 24px; font-weight: 700; color: var(--hero-bg); margin: 0 0 24px; }
	.section-copy { color: var(--muted); font-size: 15px; line-height: 1.6; max-width: 700px; margin: 0 0 24px; }

	.links-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 16px;
	}
	.link-card {
		display: grid;
		gap: 6px;
		padding: 24px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #fff;
		text-decoration: none;
		transition: border-color 0.15s, box-shadow 0.15s;
	}
	.link-card:hover { border-color: var(--primary); box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
	.link-card strong { font-size: 15px; font-weight: 700; color: var(--hero-bg); }
	.link-card span { font-size: 13px; color: var(--muted); line-height: 1.5; }

	.faq-list { max-width: 720px; display: grid; gap: 8px; }
	.faq-item {
		border: 1px solid var(--line);
		border-radius: 6px;
		background: #fff;
		padding: 0 16px;
	}
	.faq-item summary {
		padding: 14px 0;
		font-weight: 600;
		font-size: 15px;
		color: var(--hero-bg);
		cursor: pointer;
	}
	.faq-item[open] summary { margin-bottom: 12px; }
	.faq-item p {
		margin: 0 0 14px;
		font-size: 14px;
		color: var(--muted);
		line-height: 1.6;
	}

	.ticket-form { max-width: 600px; display: grid; gap: 14px; }
	.ticket-form label { display: grid; gap: 4px; }
	.ticket-form label span { font-size: 13px; font-weight: 600; color: var(--ink); }
	.ticket-form input, .ticket-form select, .ticket-form textarea {
		padding: 10px 14px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 14px;
		font-family: inherit;
		color: var(--ink);
		background: #fff;
		outline: none;
	}
	.ticket-form input:focus, .ticket-form select:focus, .ticket-form textarea:focus { border-color: var(--primary); }
	.ticket-form textarea { resize: vertical; }
	.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
	.form-error { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 4px; font-size: 13px; }
	.success-card {
		max-width: 600px;
		padding: 28px;
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
	}
	.success-card strong { display: block; font-size: 17px; color: var(--primary-dark); margin-bottom: 8px; }
	.success-card p { font-size: 14px; color: var(--muted); line-height: 1.6; margin: 0 0 16px; }
	.success-card p strong { display: inline; font-size: inherit; color: var(--ink); }

	@media (max-width: 980px) {
		.links-grid { grid-template-columns: repeat(2, 1fr); }
		.form-row { grid-template-columns: 1fr; }
	}
	@media (max-width: 680px) {
		.links-grid { grid-template-columns: 1fr; }
	}
</style>
