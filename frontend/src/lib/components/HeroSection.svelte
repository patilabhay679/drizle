<script>
	import CheckoutPreview from './CheckoutPreview.svelte';
</script>

<section class="hero">
	<div class="container hero-grid">
		<div>
			<div class="eyebrow">More Than Just a Payment Gateway. We're Full-Stack.</div>
			<h1>Increase Authorization Rates with<br>DrizlePay</h1>
			<p class="lead">Payment gateways are just one piece of the puzzle. Our full-stack platform intelligently routes payments, manages global compliance, and automates recurring billing to maximize your successful transactions.</p>
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
