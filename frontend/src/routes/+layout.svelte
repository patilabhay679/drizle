<script>
	import './landing.css';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { page } from '$app/state';

	let { children } = $props();

	let isDocs = $derived(page.url.pathname.startsWith('/docs'));
	let isDashboard = $derived(page.url.pathname.startsWith('/dashboard'));
	let isOnboarding = $derived(page.url.pathname.startsWith('/onboarding'));
	let showMarketing = $derived(!isDocs && !isDashboard && !isOnboarding);
	let showFooter = $derived(!isDashboard && !isOnboarding);
</script>

{#if isDocs}
	{@render children()}
	{#if showFooter}
		<Footer />
	{/if}
{:else}
	<div class="layout">
		{#if showMarketing}
			<Header />
		{/if}

		<main>
			{@render children()}
		</main>

		{#if showFooter}
			<Footer />
		{/if}
	</div>
{/if}

<style>
	.layout {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}
	main { flex: 1; }
</style>
