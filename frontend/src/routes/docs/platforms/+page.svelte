<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Platforms & Marketplaces | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Platforms &amp; Marketplaces</h1>
	<p class="lead">Drizle Pay enables platforms and marketplaces to accept payments, manage payouts, and orchestrate multiparty funds movement.</p>

	<h2>Platform Model</h2>
	<p>A <strong>platform</strong> is a business that facilitates transactions between multiple parties — such as a marketplace connecting buyers and sellers, or a SaaS platform collecting fees on behalf of service providers.</p>

	<h2>Key Concepts</h2>

	<h3>Connected Accounts</h3>
	<p>Each seller or service provider on your platform is represented as a <a href="/docs/accounts">connected account</a>. Funds settle to their balance and can be paid out on their own schedule.</p>

	<h3>Application Fees</h3>
	<p>Charge a platform fee on any transaction. When a payment is created, specify an <a href="/docs/application-fees">application fee</a> amount that is deducted before the remaining funds are made available to the connected account.</p>

	<h3>Split Payments</h3>
	<p>Use the Payments API to split a single transaction across multiple destinations. Funds are distributed in real time, with each party receiving their share directly.</p>

	<h3>Payouts</h3>
	<p>Initiate <a href="/docs/payouts">payouts</a> to connected accounts. Funds can be sent to bank accounts or debit cards, with support for both instant and standard settlement timelines.</p>

	<h2>Getting Started</h2>
	<p>Create your platform account and onboard connected accounts via the <a href="/docs/account-links">account links</a> API or OAuth flow. Test the full payment lifecycle in sandbox mode before going live.</p>
</div>
