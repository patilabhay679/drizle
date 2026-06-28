<script>
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	let tickets = $state([]);
	let loading = $state(true);
	let error = $state('');

	let showForm = $state(false);
	let subject = $state('');
	let category = $state('Account');
	let message = $state('');
	let priority = $state('normal');
	let submitting = $state(false);
	let formError = $state('');

	onMount(() => load());

	async function load() {
		loading = true;
		try {
			tickets = await api.getSupportTickets();
		} catch (e) { error = e.message || 'Something went wrong'; } finally {
			loading = false;
		}
	}

	function openForm() {
		showForm = true;
		subject = '';
		category = 'Account';
		message = '';
		priority = 'normal';
		formError = '';
	}

	async function submitTicket(e) {
		e.preventDefault();
		submitting = true;
		formError = '';
		try {
			await api.createSupportTicket({ subject, category, message, priority });
			showForm = false;
			await load();
		} catch (err) {
			formError = err.message;
		} finally {
			submitting = false;
		}
	}

	function statusClass(s) {
		return s === 'open' ? 'open' : s === 'resolved' ? 'resolved' : '';
	}

	function priorityClass(p) {
		return p === 'high' ? 'high' : p === 'low' ? 'low' : '';
	}

	function ago(dateStr) {
		const diff = Date.now() - new Date(dateStr).getTime();
		const mins = Math.floor(diff / 60000);
		if (mins < 60) return `${mins}m ago`;
		const hrs = Math.floor(mins / 60);
		if (hrs < 24) return `${hrs}h ago`;
		const days = Math.floor(hrs / 24);
		return `${days}d ago`;
	}
</script>

<svelte:head>
	<title>Support | DrizlePay</title>
</svelte:head>

<div class="page-header">
	<h2>Support</h2>
	<button class="btn primary" onclick={openForm}>New Ticket</button>
</div>

{#if error}
	<div class="error-banner">{error}</div>
{/if}

{#if showForm}
	<div class="card form-card">
		<h3>Create Support Ticket</h3>
		<form onsubmit={submitTicket}>
			{#if formError}
				<div class="form-error">{formError}</div>
			{/if}
			<label>
				<span>Subject</span>
				<input type="text" bind:value={subject} required placeholder="Brief summary of the issue" />
			</label>
			<label>
				<span>Category</span>
				<select bind:value={category}>
					<option value="Account">Account</option>
					<option value="Payments">Payments</option>
					<option value="API">API</option>
					<option value="Integrations">Integrations</option>
					<option value="Billing">Billing</option>
					<option value="Other">Other</option>
				</select>
			</label>
			<label>
				<span>Priority</span>
				<select bind:value={priority}>
					<option value="low">Low</option>
					<option value="normal">Normal</option>
					<option value="high">High</option>
				</select>
			</label>
			<label>
				<span>Message</span>
				<textarea bind:value={message} required rows="5" placeholder="Describe your issue in detail"></textarea>
			</label>
			<div class="form-actions">
				<button type="button" class="btn secondary" onclick={() => showForm = false}>Cancel</button>
				<button type="submit" class="btn primary" disabled={submitting}>
					{submitting ? 'Submitting…' : 'Submit Ticket'}
				</button>
			</div>
		</form>
	</div>
{/if}

{#if loading}
	<p class="loading-text">Loading tickets…</p>
{:else if tickets.length === 0}
	<p class="empty-text">No support tickets yet.</p>
{:else}
	<div class="ticket-list">
		{#each tickets as ticket}
			<div class="ticket-row">
				<div class="ticket-main">
					<strong class="ticket-subject">{ticket.subject}</strong>
					<span class="ticket-meta">{ticket.category} &middot; {ago(ticket.created_at)}</span>
				</div>
				<div class="ticket-badges">
					<span class="badge status {statusClass(ticket.status)}">{ticket.status}</span>
					<span class="badge priority {priorityClass(ticket.priority)}">{ticket.priority}</span>
				</div>
			</div>
		{/each}
	</div>
{/if}

<style>
	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 20px;
	}
	.page-header h2 { font-size: 20px; color: var(--hero-bg); margin: 0; }
	.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
	.loading-text, .empty-text { color: var(--muted); font-size: 14px; padding: 40px; text-align: center; }

	.card {
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 8px;
		padding: 20px;
		margin-bottom: 16px;
	}
	.form-card h3 { font-size: 16px; color: var(--hero-bg); margin: 0 0 16px; }
	.form-card form { display: grid; gap: 14px; max-width: 480px; }
	.form-card label { display: grid; gap: 4px; }
	.form-card label span { font-size: 13px; font-weight: 600; color: var(--ink); }
	.form-card input, .form-card select, .form-card textarea {
		padding: 8px 12px;
		border: 1px solid var(--line);
		border-radius: 4px;
		font-size: 14px;
		font-family: inherit;
		color: var(--ink);
		background: #fff;
		outline: none;
	}
	.form-card input:focus, .form-card select:focus, .form-card textarea:focus { border-color: var(--primary); }
	.form-card textarea { resize: vertical; }
	.form-error { padding: 8px 12px; background: #fef2f2; color: #dc2626; border-radius: 4px; font-size: 13px; }
	.form-actions { display: flex; gap: 8px; justify-content: flex-end; margin-top: 4px; }
	.btn {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-height: 36px;
		padding: 0 16px;
		border-radius: 4px;
		font-size: 13px;
		font-weight: 600;
		cursor: pointer;
		border: none;
		transition: all 0.15s;
	}
	.btn.primary { background: var(--primary); color: #fff; }
	.btn.primary:hover:not(:disabled) { background: var(--primary-dark); }
	.btn.secondary { background: #fff; color: var(--muted); border: 1px solid var(--line); }
	.btn.secondary:hover { border-color: var(--muted); color: var(--ink); }
	.btn:disabled { opacity: 0.6; cursor: not-allowed; }

	.ticket-list { display: flex; flex-direction: column; gap: 6px; }
	.ticket-row {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 14px 16px;
		background: #fff;
		border: 1px solid var(--line);
		border-radius: 6px;
		transition: border-color 0.15s;
	}
	.ticket-row:hover { border-color: #cbd5e1; }
	.ticket-main { display: flex; flex-direction: column; gap: 2px; }
	.ticket-subject { font-size: 14px; color: var(--hero-bg); }
	.ticket-meta { font-size: 12px; color: var(--muted); }
	.ticket-badges { display: flex; gap: 6px; align-items: center; }
	.badge {
		font-size: 11px;
		font-weight: 600;
		padding: 3px 10px;
		border-radius: 10px;
		text-transform: capitalize;
	}
	.badge.status.open { background: #fef3c7; color: #92400e; }
	.badge.status.resolved { background: #e6fcf0; color: var(--primary-dark); }
	.badge.priority { background: #f1f5f9; color: var(--muted); }
	.badge.priority.high { background: #fef2f2; color: #dc2626; }
	.badge.priority.low { background: #f1f5f9; color: #64748b; }
</style>
