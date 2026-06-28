<script>
	import { auth } from '$lib/stores/auth';
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	let { children } = $props();
	let sidebarOpen = $state(false);

	onMount(() => {
		if (!auth.isAuthenticated) goto('/login');
	});

	function logout() {
		auth.logout();
		goto('/login');
	}

	let pathname = $derived(page.url.pathname);

	function isActive(href) {
		return pathname === href;
	}

	function isSubActive(parent) {
		return pathname.startsWith(parent);
	}

	let sections = [
		{
			label: '',
			items: [
				{ href: '/dashboard', label: 'Dashboard', icon: '⌂' },
				{ href: '/dashboard/transactions', label: 'Transactions', icon: '⇄' },
				{ href: '/dashboard/payouts', label: 'Payouts', icon: '↑' },
			],
		},
		{
			label: 'Reports',
			items: [
				{ href: '/dashboard/reports/tax-invoice', label: 'Tax Invoice', icon: '☐' },
				{ href: '/dashboard/reports/monthly-statement', label: 'Monthly Statement', icon: '☰' },
			],
		},
		{
			label: 'Pay by Link',
			items: [
				{ href: '/dashboard/pay-by-link', label: 'Payment Links', icon: '⊡' },
				{ href: '/dashboard/pay-by-link/static', label: 'Static Links', icon: '⊡' },
				{ href: '/dashboard/pay-by-link/recurring', label: 'Recurring Payments', icon: '↻' },
				{ href: '/dashboard/pay-by-link/bulk', label: 'Bulk Uploads', icon: '⇧' },
			],
		},
		{
			label: 'Management',
			items: [
				{ href: '/dashboard/users', label: 'User Management', icon: '⊞' },
				{ href: '/dashboard/support', label: 'Support', icon: '?' },
				{ href: '/dashboard/settings', label: 'Settings', icon: '⚙' },
			],
		},
	];
</script>

{#if !auth.isAuthenticated}
	<div class="loading">Redirecting…</div>
{:else}
	<div class="dashboard">
		<aside class="sidebar" class:open={sidebarOpen}>
			<div class="sidebar-header">
				<a href="/" class="brand">Drizle<span>Pay</span></a>
				<button class="close-btn" onclick={() => sidebarOpen = false}>✕</button>
			</div>
			<nav>
				{#each sections as section}
					{#if section.label}
						<div class="section-label">{section.label}</div>
					{/if}
					{#each section.items as item}
						<a
							href={item.href}
							class="nav-item"
							class:active={isActive(item.href)}
							class:sub-active={!isActive(item.href) && isSubActive(item.href)}
							onclick={() => sidebarOpen = false}
						>
							<span class="icon">{item.icon}</span>
							{item.label}
						</a>
					{/each}
				{/each}
			</nav>
			<div class="sidebar-footer">
				<div class="merchant-info">
					<strong>{auth.merchant?.name}</strong>
					<span>{auth.merchant?.email}</span>
				</div>
				<button class="logout-btn" onclick={logout}>Sign Out</button>
			</div>
		</aside>

		<div class="overlay" class:visible={sidebarOpen} onclick={() => sidebarOpen = false}></div>

		<main class="main">
			<header class="topbar">
				<button class="menu-btn" onclick={() => sidebarOpen = true}>☰</button>
				<h2>Dashboard</h2>
				<div class="spacer"></div>
				<div class="topbar-merchant">{auth.merchant?.name}</div>
			</header>
			{#if auth.merchant?.email_verified === false}
				<div class="verify-banner">
					Please verify your email address to access all features.
					<a href="/verify-email">Resend verification</a>
				</div>
			{/if}
			<div class="content">
				{@render children()}
			</div>
		</main>
	</div>
{/if}

<style>
	.loading {
		min-height: 100vh;
		display: grid;
		place-items: center;
		color: var(--muted);
		font-size: 16px;
	}
	.dashboard {
		display: flex;
		min-height: 100vh;
		background: #f8fafc;
	}
	.sidebar {
		width: 260px;
		background: #fff;
		border-right: 1px solid var(--line);
		display: flex;
		flex-direction: column;
		position: fixed;
		top: 0;
		left: 0;
		bottom: 0;
		z-index: 30;
		transition: transform 0.2s;
	}
	.sidebar-header {
		padding: 20px 20px 16px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		border-bottom: 1px solid var(--line);
	}
	.brand { font-weight: 760; font-size: 20px; color: var(--hero-bg); text-decoration: none; }
	.brand span { color: var(--primary); }
	.close-btn { display: none; background: none; border: none; font-size: 20px; cursor: pointer; color: var(--muted); }
	nav { flex: 1; padding: 12px; overflow-y: auto; }
	.section-label {
		font-size: 11px;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.08em;
		color: var(--muted);
		padding: 16px 14px 6px;
	}
	.nav-item {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 9px 14px;
		border-radius: 6px;
		color: var(--muted);
		font-size: 14px;
		font-weight: 500;
		text-decoration: none;
		transition: all 0.15s;
		margin-bottom: 1px;
	}
	.nav-item:hover { background: #f1f5f9; color: var(--ink); }
	.nav-item.active { background: #e6fcf0; color: var(--primary-dark); font-weight: 600; }
	.nav-item.sub-active { background: #f1f5f9; color: var(--ink); font-weight: 500; }
	.icon { font-size: 16px; width: 20px; text-align: center; flex-shrink: 0; }
	.sidebar-footer {
		padding: 16px 20px;
		border-top: 1px solid var(--line);
	}
	.merchant-info { margin-bottom: 12px; }
	.merchant-info strong { display: block; font-size: 13px; color: var(--ink); }
	.merchant-info span { font-size: 12px; color: var(--muted); }
	.logout-btn {
		width: 100%;
		padding: 8px;
		border: 1px solid var(--line);
		border-radius: 4px;
		background: none;
		color: var(--muted);
		font-size: 13px;
		cursor: pointer;
		transition: all 0.15s;
	}
	.logout-btn:hover { border-color: #dc2626; color: #dc2626; }
	.overlay { display: none; }
	.main {
		flex: 1;
		margin-left: 260px;
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}
	.topbar {
		height: 60px;
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 0 24px;
		background: #fff;
		border-bottom: 1px solid var(--line);
		flex-shrink: 0;
	}
	.menu-btn { display: none; background: none; border: none; font-size: 22px; cursor: pointer; color: var(--ink); padding: 4px; }
	.spacer { flex: 1; }
	.topbar-merchant { font-size: 14px; font-weight: 500; color: var(--muted); }
	.content { flex: 1; padding: 24px; overflow-y: auto; }
	.verify-banner { padding: 10px 24px; background: #fef3c7; color: #92400e; font-size: 14px; display: flex; gap: 8px; align-items: center; }
	.verify-banner a { color: var(--primary); font-weight: 600; white-space: nowrap; }
	.verify-banner a:hover { text-decoration: underline; }
	@media (max-width: 768px) {
		.sidebar { transform: translateX(-100%); }
		.sidebar.open { transform: translateX(0); }
		.close-btn { display: block; }
		.overlay {
			display: block;
			position: fixed;
			inset: 0;
			background: rgba(0,0,0,0.3);
			z-index: 29;
			opacity: 0;
			pointer-events: none;
			transition: opacity 0.2s;
		}
		.overlay.visible { opacity: 1; pointer-events: auto; }
		.main { margin-left: 0; }
		.menu-btn { display: block; }
	}
</style>
