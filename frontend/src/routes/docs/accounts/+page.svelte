<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Accounts API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Accounts API</h1>
<p class="lead">The <code>Account</code> object represents a connected account in your platform. Manage onboarding, capabilities, and payouts.</p>

<h2>The Account Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_acct_001234",
  "object": "account",
  "business_type": "individual",
  "country": "AE",
  "email": "merchant@example.com",
  "capabilities": &#123;
    "transfers": "active",
    "card_payments": "active"
  &#125;,
  "payouts_enabled": true,
  "charges_enabled": true,
  "details_submitted": true,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create an account</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts</span></div>

<h3>Retrieve an account</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts/:id</span></div>

<h3>Update an account</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts/:id</span></div>

<h3>List accounts</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts</span></div>

<h3>Reject an account</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts/:id/reject</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/account-links">Account Links</a></li>
<li><a href="/docs/application-fees">Application Fees</a></li>
</ul>
</div>
</div>
