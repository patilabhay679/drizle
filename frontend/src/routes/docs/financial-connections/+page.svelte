<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Financial Connections API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Financial Connections API</h1>
<p class="lead">The Financial Connections API lets you retrieve account information from your customers' financial institutions.</p>

<h2>The FinancialConnectionsAccount Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_fca_001234",
  "object": "financial_connections_account",
  "name": "Business Checking",
  "institution": "Emirates NBD",
  "supported_payment_method_types": ["bank_transfer"],
  "status": "active",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve an account</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/financial_connections/accounts/:id</span></div>

<h3>List accounts</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/financial_connections/accounts</span></div>

<h3>Create a session</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/financial_connections/sessions</span></div>

<h3>Retrieve account owners</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/financial_connections/accounts/:id/owners</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/customers">Customers API</a></li>
<li><a href="/docs/accounts">Accounts API</a></li>
</ul>
</div>
</div>
