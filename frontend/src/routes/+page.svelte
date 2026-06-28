<svelte:head>
	<title>DrizlePay | Global Payments & Full-Stack Digital Commerce</title>
	<meta name="description" content="Increase your authorization rates with Drizle Pay. Our full-stack digital commerce platform handles payments, subscriptions, global compliance, and intelligent routing." />
	<link rel="canonical" href="https://drizlepay.com/" />
	<meta property="og:title" content="Drizle Pay | Global Payments & Full-Stack Digital Commerce" />
	<meta property="og:description" content="Increase your authorization rates with Drizle Pay. Our full-stack digital commerce platform handles payments, subscriptions, global compliance, and intelligent routing." />
	<meta property="og:url" content="https://drizlepay.com/" />
	<meta property="og:type" content="website" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content="Drizle Pay | Global Payments & Full-Stack Digital Commerce" />
	<meta name="twitter:description" content="Increase your authorization rates with Drizle Pay. Our full-stack digital commerce platform handles payments, subscriptions, global compliance, and intelligent routing." />
</svelte:head>

<script>
	import HeroSection from '$lib/components/HeroSection.svelte';
	import FeatureGrid from '$lib/components/FeatureGrid.svelte';
	import PaymentMethods from '$lib/components/PaymentMethods.svelte';
	import DevSection from '$lib/components/DevSection.svelte';
	import CTASection from '$lib/components/CTASection.svelte';
</script>

<main>
	<HeroSection />
	<FeatureGrid />
	<PaymentMethods />
	<section class="social-proof">
		<div class="container">
			<p class="sp-label">Trusted by businesses across the UAE and beyond</p>
			<div class="sp-logos">
				<span>Noor Markets</span>
				<span>Baraka</span>
				<span>YallaDeals</span>
				<span>Zbooni</span>
				<span>EduHive</span>
				<span>Washmen</span>
			</div>
		</div>
	</section>
	<DevSection />
	<CTASection />
</main>
