<script>
	import { auth } from '$lib/stores/auth';
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { api } from '$lib/api';

	let { children } = $props();

	onMount(() => {
		if (!auth.isAuthenticated) goto('/login');
	});

	let pathname = $derived(page.url.pathname);
	let testMode = $state(auth.merchant?.test_mode ?? false);
	let toggling = $state(false);

	async function toggleTestMode() {
		toggling = true;
		try {
			await api.toggleTestMode();
			testMode = !testMode;
		} catch (e) {
			console.error(e);
		} finally {
			toggling = false;
		}
	}

	function logout() {
		auth.logout();
		goto('/login');
	}

	const steps = [
		{ href: '/onboarding/upload', label: 'Upload Documents' },
		{ href: '/onboarding/business', label: 'Verify Your Business' },
		{ href: '/onboarding/financial', label: 'Financial Setup' },
		{ href: '/onboarding/review', label: 'Review & Submit' },
	];

	function isActive(href) {
		return pathname === href;
	}
</script>

{#if !auth.isAuthenticated}
	<div class="loading">Redirecting…</div>
{:else}
	<div class="layout">
		<aside class="sidebar">
			<div class="sidebar-header">
				<a href="/" class="brand"><svg viewBox="0 0 120 130" width="24" height="26" fill="none" aria-hidden="true"><path d="M25,15 L50,15 L30,105 L5,105 Z" fill="#06162c"/><path d="M57,15 L82,15 L62,105 L37,105 Z" fill="#06162c" opacity="0.85"/><path d="M89,15 L120,55 L79,105 L65,105 L85,55 L64,15 Z" fill="#02c366"/></svg> Drizle<span>Pay</span></a>
				<span class="badge">Onboarding</span>
			</div>
			<nav>
				{#each steps as step, i}
					<a
						href={step.href}
						class="step-link"
						class:active={isActive(step.href)}
					>
						<span class="step-num">{i + 1}</span>
						{step.label}
					</a>
				{/each}
			</nav>
			<div class="sidebar-footer">
				<div class="test-mode-toggle">
					<button class="test-btn" class:active={testMode} onclick={toggleTestMode} disabled={toggling}>
						<span class="dot"></span>
						{testMode ? 'Test Mode ON' : 'Test Mode'}
					</button>
				</div>
				<div class="merchant-info">
					<strong>{auth.merchant?.name}</strong>
					<span>{auth.merchant?.email}</span>
				</div>
				<button class="logout-btn" onclick={logout}>Sign Out</button>
			</div>
		</aside>
		<main class="main">
			{@render children()}
		</main>
	</div>
{/if}

<style>
	.loading { min-height: 100vh; display: grid; place-items: center; color: var(--muted); font-size: 16px; }
	.layout { display: flex; min-height: 100vh; background: #f8fafc; }
	.sidebar {
		width: 240px; background: #fff; border-right: 1px solid var(--line);
		display: flex; flex-direction: column; position: fixed; top: 0; left: 0; bottom: 0; z-index: 30;
	}
	.sidebar-header { padding: 20px 20px 16px; border-bottom: 1px solid var(--line); display: flex; align-items: center; justify-content: space-between; }
	.brand { font-weight: 760; font-size: 18px; color: var(--hero-bg); text-decoration: none; display: flex; align-items: center; gap: 6px; }
	.brand span { color: var(--primary); }
	.badge { font-size: 10px; font-weight: 600; color: var(--primary); background: #e6fcf0; padding: 2px 8px; border-radius: 10px; }
	nav { flex: 1; padding: 16px 12px; display: flex; flex-direction: column; gap: 4px; }
	.step-link {
		display: flex; align-items: center; gap: 12px;
		padding: 10px 12px; border-radius: 8px;
		color: var(--muted); font-size: 14px; font-weight: 500;
		text-decoration: none; transition: all 0.15s;
	}
	.step-link:hover { background: #f1f5f9; color: var(--ink); }
	.step-link.active { background: #e6fcf0; color: var(--primary-dark); font-weight: 600; }
	.step-num {
		width: 26px; height: 26px; border-radius: 50%;
		display: grid; place-items: center;
		font-size: 13px; font-weight: 700;
		background: #f1f5f9; color: var(--muted); flex-shrink: 0;
	}
	.step-link.active .step-num { background: var(--primary); color: #fff; }
	.sidebar-footer { padding: 12px 20px 16px; border-top: 1px solid var(--line); }
	.test-mode-toggle { margin-bottom: 10px; }
	.test-btn {
		display: flex; align-items: center; gap: 8px; width: 100%;
		padding: 8px 12px; border: 1px solid var(--line); border-radius: 6px;
		background: none; font-size: 13px; font-weight: 600; color: var(--muted);
		cursor: pointer; transition: all 0.15s;
	}
	.test-btn:hover { border-color: var(--primary); color: var(--ink); }
	.test-btn:disabled { opacity: 0.5; cursor: not-allowed; }
	.test-btn.active { background: #fef3c7; border-color: #f59e0b; color: #92400e; }
	.dot { width: 8px; height: 8px; border-radius: 50%; background: var(--muted); }
	.test-btn.active .dot { background: #f59e0b; }
	.merchant-info strong { display: block; font-size: 12px; color: var(--ink); }
	.merchant-info span { font-size: 11px; color: var(--muted); }
	.logout-btn {
		width: 100%; margin-top: 8px; padding: 6px; border: 1px solid var(--line);
		border-radius: 4px; background: none; color: var(--muted); font-size: 12px;
		cursor: pointer; transition: all 0.15s;
	}
	.logout-btn:hover { border-color: #dc2626; color: #dc2626; }
	.main { flex: 1; margin-left: 240px; padding: 40px; max-width: 720px; }
</style>
