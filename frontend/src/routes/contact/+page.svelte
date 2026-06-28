<script>
	let name = $state('');
	let email = $state('');
	let company = $state('');
	let phone = $state('');
	let message = $state('');
	let submitted = $state(false);
	let loading = $state(false);
	let error = $state('');

	async function handleSubmit(e) {
		e.preventDefault();
		error = '';
		loading = true;
		try {
			const { api } = await import('$lib/api');
			await api.contact({ name, email, company, phone, message });
			submitted = true;
		} catch (err) {
			error = err.message;
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>Contact Sales | Drizle Pay</title>
	<meta name="description" content="Contact Drizle Pay's sales team. Get pricing, enterprise plans, and custom payment solutions for your business." />
</svelte:head>

<div class="page contact-page">
	<section class="page-hero">
		<div class="container">
			<div class="eyebrow">Contact Sales</div>
			<h1>Let's talk about your payment stack</h1>
			<p class="lead">Whether you're a startup looking for an API-first gateway or an enterprise needing a custom solution — we're here to help.</p>
		</div>
	</section>

	<section>
		<div class="container contact-grid">
			<div class="contact-info">
				<h2 class="section-title" style="margin-bottom:24px;">Get in touch</h2>

				<div class="info-item">
					<strong>Sales Inquiries</strong>
					<a href="mailto:sales@drizlepay.com">sales@drizlepay.com</a>
				</div>
				<div class="info-item">
					<strong>Developer Support</strong>
					<a href="mailto:dev@drizlepay.com">dev@drizlepay.com</a>
				</div>
				<div class="info-item">
					<strong>General</strong>
					<a href="mailto:hello@drizlepay.com">hello@drizlepay.com</a>
				</div>
				<div class="info-item">
					<strong>Address</strong>
					<span>Dubai, United Arab Emirates</span>
				</div>

				<div class="info-extra">
					<h3>Office Hours</h3>
					<p>Sunday – Thursday<br>9:00 AM – 6:00 PM (GST)</p>
					<p class="tiny">Urgent issues outside business hours?<br>Email us and we'll respond within 4 hours.</p>
				</div>
			</div>

			<div class="contact-form-card">
				{#if submitted}
					<div class="form-success">
						<div class="success-icon">
							<svg width="48" height="48" viewBox="0 0 48 48" fill="none">
								<rect width="48" height="48" rx="24" fill="#e6fcf0"/>
								<path d="M14 24l7 7 13-13" stroke="#02c366" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
							</svg>
						</div>
						<h3>Thanks for reaching out!</h3>
						<p>We'll get back to you within 24 hours.</p>
						<button class="btn primary" onclick={() => { submitted = false; name = ''; email = ''; company = ''; phone = ''; message = ''; }}>Send Another Message</button>
					</div>
				{:else}
					<h3>Send us a message</h3>
					<form onsubmit={handleSubmit}>
						{#if error}
							<div class="form-error">{error}</div>
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
						<div class="form-row">
							<label>
								<span>Company</span>
								<input type="text" bind:value={company} placeholder="Your company name" />
							</label>
							<label>
								<span>Phone</span>
								<input type="tel" bind:value={phone} placeholder="+971 XX XXX XXXX" />
							</label>
						</div>
						<label>
							<span>Message</span>
							<textarea bind:value={message} required rows="5" placeholder="Tell us about your business and what you're looking for…"></textarea>
						</label>
						<button type="submit" class="btn primary" disabled={loading}>
							{loading ? 'Sending…' : 'Send Message'}
						</button>
					</form>
				{/if}
			</div>
		</div>
	</section>

	<section class="alt-bg">
		<div class="container cta">
			<div>
				<h2>Prefer to try it first?</h2>
				<p>Create a free account and start accepting payments in minutes — no sales call required.</p>
			</div>
			<a class="btn primary" href="/login?register=true">Get Started</a>
		</div>
	</section>
</div>

<style>
	.contact-page { background: var(--bg); }
	.page-hero {
		padding: clamp(64px, 8vw, 96px) 0;
		background: var(--hero-bg);
		color: var(--hero-text);
	}
	.page-hero .lead { color: var(--hero-muted); max-width: 700px; }
	.contact-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: clamp(34px, 6vw, 64px);
		align-items: start;
	}
	.contact-info { padding-top: 8px; }
	.info-item {
		padding: 16px 0;
		border-bottom: 1px solid var(--line);
	}
	.info-item strong {
		display: block;
		font-size: 14px;
		color: var(--muted);
		font-weight: 600;
		margin-bottom: 4px;
	}
	.info-item a, .info-item span {
		font-size: 16px;
		color: var(--hero-bg);
		font-weight: 500;
	}
	.info-item a { color: var(--primary); }
	.info-item a:hover { text-decoration: underline; }
	.info-extra { margin-top: 28px; }
	.info-extra h3 {
		font-size: 16px;
		font-weight: 700;
		color: var(--hero-bg);
		margin: 0 0 10px;
	}
	.info-extra p {
		color: var(--muted);
		font-size: 15px;
		line-height: 1.6;
		margin: 0;
	}
	.info-extra .tiny { color: var(--muted); font-size: 13px; margin-top: 12px; }
	.contact-form-card {
		padding: 32px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #fff;
		box-shadow: var(--shadow);
	}
	.contact-form-card h3 {
		font-size: 20px;
		font-weight: 700;
		color: var(--hero-bg);
		margin: 0 0 24px;
	}
	form { display: grid; gap: 16px; }
	.form-row {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 16px;
	}
	label { display: grid; gap: 6px; }
	label span {
		font-size: 13px;
		font-weight: 600;
		color: var(--ink);
	}
	input, textarea {
		padding: 10px 14px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 15px;
		color: var(--ink);
		background: #fff;
		outline: none;
		font-family: inherit;
		transition: border-color 0.15s;
	}
	input:focus, textarea:focus { border-color: var(--primary); }
	textarea { resize: vertical; }
	.form-success {
		text-align: center;
		padding: 40px 20px;
		display: grid;
		gap: 16px;
		justify-items: center;
	}
	.form-success h3 {
		font-size: 22px;
		margin: 0;
	}
	.form-success p {
		color: var(--muted);
		font-size: 16px;
		margin: 0;
	}
	.form-error {
		padding: 12px 14px;
		background: #fef2f2;
		color: #dc2626;
		border-radius: 4px;
		font-size: 14px;
		text-align: center;
	}
	@media (max-width: 980px) {
		.contact-grid { grid-template-columns: 1fr; }
	}
	@media (max-width: 680px) {
		.form-row { grid-template-columns: 1fr; }
	}
</style>
