<script>
	import CheckoutPreview from './CheckoutPreview.svelte';
</script>

<section class="hero">
	<div class="container hero-grid">
		<div>
			<div class="eyebrow">More Than Just a Payment Gateway. We're Full-Stack.</div>
			<h1>Start Accepting Payments<br>in Minutes</h1>
			<p class="lead">A unified platform that replaces your payment gateway, subscription engine, tax calculator, fraud screening, invoicing<br>and payout tool — all from a single integration.</p>
			<div class="hero-actions">
				<a class="btn primary" href="/login?register=true">Try Now</a>
				<a class="btn ghost" href="/contact">Schedule Demo</a>
			</div>
			<div class="cards" aria-label="Key benefits">
				<div class="stat"><strong>90%+</strong><span>Increase payment success rate up to 90% or more.</span></div>
				<div class="stat"><strong>17+</strong><span>Languages supported for localized checkout experiences.</span></div>
				<div class="stat"><strong>30+</strong><span>Global payment options available immediately.</span></div>
			</div>
		</div>
		<CheckoutPreview />
	</div>
</section>
