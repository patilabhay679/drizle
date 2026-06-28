<script>
	import './landing.css';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { page } from '$app/state';

	let { children } = $props();

	let isDocs = $derived(page.url.pathname.startsWith('/docs'));
	let isDashboard = $derived(page.url.pathname.startsWith('/dashboard'));
	let showMarketing = $derived(!isDocs && !isDashboard);
	let showFooter = $derived(!isDashboard);
</script>

{#if showMarketing}
	<Header />
{/if}

{@render children()}

{#if showFooter}
	<Footer />
{/if}
