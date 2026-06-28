<script>
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	let members = $state([]);
	let loading = $state(true);
	let showInvite = $state(false);
	let inviteEmail = $state('');
	let inviteRole = $state('member');
	let inviteError = $state('');
	let error = $state('');

	onMount(async () => {
		try {
			members = await api.getTeam();
		} catch (e) { error = e.message || 'Something went wrong'; } finally {
			loading = false;
		}
	});

	async function invite() {
		if (!inviteEmail) return;
		inviteError = '';
		try {
			await api.inviteTeamMember(inviteEmail, inviteRole);
			showInvite = false;
			inviteEmail = '';
			members = await api.getTeam();
		} catch (err) {
			inviteError = err.message;
		}
	}

	async function remove(id) {
		try {
			await api.removeTeamMember(id);
			members = await api.getTeam();
		} catch (e) { error = e.message || 'Something went wrong'; }
	}

	function roleBadge(role) {
		const colors = { admin: '#e6fcf0', developer: '#dbeafe', analyst: '#fef3c7', member: '#f1f5f9' };
		return colors[role] || '#f1f5f9';
	}
</script>

<svelte:head>
	<title>User Management | Drizle Pay</title>
</svelte:head>

<div class="page-header">
	<h2>User Management</h2>
	<button class="btn-primary" onclick={() => showInvite = !showInvite}>
		{showInvite ? 'Cancel' : '+ Invite User'}
	</button>
</div>

{#if showInvite}
	<div class="card invite-card">
		<h3>Invite Team Member</h3>
		<div class="invite-form">
			<label>
				<span>Email</span>
				<input type="email" bind:value={inviteEmail} placeholder="colleague@company.com" />
			</label>
			<label>
				<span>Role</span>
				<select bind:value={inviteRole}>
					<option value="admin">Admin</option>
					<option value="developer">Developer</option>
					<option value="analyst">Analyst</option>
					<option value="member">Member</option>
				</select>
			</label>
			<button class="btn-primary" onclick={invite}>Send Invite</button>
		</div>
		{#if inviteError}
			<p class="error-msg">{inviteError}</p>
		{/if}
	</div>
{/if}

<div class="card">
	{#if loading}
		<p class="loading-text">Loading…</p>
	{:else if members.length === 0}
		<p class="empty">No team members yet.</p>
	{:else}
		{#if error}
			<div class="error-banner">{error}</div>
		{/if}
		<div class="table-wrap">
			<table>
				<thead>
					<tr>
						<th>Name</th>
						<th>Email</th>
						<th>Role</th>
						<th>Status</th>
						<th>Joined</th>
						<th>Actions</th>
					</tr>
				</thead>
				<tbody>
					{#each members as m}
						<tr>
							<td>{m.name || '—'}</td>
							<td class="mono">{m.email}</td>
							<td>
								<span class="role-badge" style="background: {roleBadge(m.role)}">{m.role}</span>
							</td>
							<td>
								<span class="badge" class:active={m.status === 'active'} class:invited={m.status === 'invited'}>
									{m.status}
								</span>
							</td>
							<td class="mono">{new Date(m.created_at).toLocaleDateString()}</td>
							<td>
								<button class="btn-remove" onclick={() => remove(m.id)}>Remove</button>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{/if}
</div>

<style>
	.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
	.page-header h2 { margin: 0; font-size: 20px; font-weight: 700; color: var(--hero-bg); }
	.btn-primary { padding: 8px 18px; background: var(--primary); color: #fff; border: none; border-radius: 4px; font-size: 13px; font-weight: 600; cursor: pointer; transition: background 0.15s; }
	.btn-primary:hover { background: var(--primary-dark); }
	.invite-card { padding: 20px; background: #fff; border: 1px solid var(--line); border-radius: 8px; margin-bottom: 16px; }
	.invite-card h3 { margin: 0 0 16px; font-size: 15px; font-weight: 600; color: var(--hero-bg); }
	.invite-form { display: flex; gap: 12px; align-items: flex-end; flex-wrap: wrap; }
	.invite-form label { display: grid; gap: 4px; flex: 1; min-width: 160px; }
	.invite-form label span { font-size: 12px; font-weight: 600; color: var(--ink); }
	.invite-form label input, .invite-form label select { padding: 8px 10px; border: 1px solid var(--line); border-radius: 4px; font-size: 13px; color: var(--ink); background: #fff; }
	.error-msg { margin-top: 12px; padding: 8px 12px; background: #fef2f2; color: #dc2626; border-radius: 4px; font-size: 13px; }
	.loading-text, .empty { color: var(--muted); font-size: 15px; padding: 40px; text-align: center; }
	.card { background: #fff; border: 1px solid var(--line); border-radius: 8px; padding: 0; overflow: hidden; }
	.table-wrap { overflow-x: auto; }
	table { width: 100%; border-collapse: collapse; font-size: 13px; }
	th { text-align: left; padding: 10px 12px; color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid var(--line); white-space: nowrap; background: #fafafa; }
	td { padding: 10px 12px; color: var(--ink); border-bottom: 1px solid #f1f5f9; white-space: nowrap; }
	tr:last-child td { border-bottom: none; }
	.mono { font-family: ui-monospace, monospace; font-size: 12px; }
	.badge { display: inline-flex; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: #f1f5f9; color: var(--muted); }
	.badge.active { background: #e6fcf0; color: var(--primary-dark); }
	.badge.invited { background: #fef3c7; color: #92400e; }
	.role-badge { padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; }
	.btn-remove { padding: 4px 12px; border: 1px solid var(--line); border-radius: 4px; background: #fff; font-size: 12px; color: var(--muted); cursor: pointer; }
	.btn-remove:hover { border-color: #dc2626; color: #dc2626; }
	.error-banner { padding: 10px 14px; background: #fef2f2; color: #dc2626; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
</style>
