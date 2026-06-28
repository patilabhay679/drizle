<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>External Accounts API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>External Accounts API</h1>
<p class="lead">The <code>ExternalAccount</code> object represents a bank account or card attached to a connected account for payouts.</p>

<h2>The ExternalAccount Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_ba_001234",
  "object": "bank_account",
  "account": "dp_acct_001234",
  "bank_name": "Emirates NBD",
  "last4": "1234",
  "currency": "AED",
  "country": "AE",
  "status": "new",
  "default_for_currency": true
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create an external account</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts/:account_id/external_accounts</span></div>

<h3>Retrieve an external account</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts/:account_id/external_accounts/:id</span></div>

<h3>Update an external account</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts/:account_id/external_accounts/:id</span></div>

<h3>List external accounts</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts/:account_id/external_accounts</span></div>

<h3>Delete an external account</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/accounts/:account_id/external_accounts/:id</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/accounts">Accounts API</a></li>
<li><a href="/docs/payouts">Payouts</a></li>
</ul>
</div>
</div>
