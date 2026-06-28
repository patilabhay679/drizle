<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Billing Portal API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Billing Portal API</h1>
<p class="lead">The <code>BillingPortal</code> session allows customers to manage their subscriptions, payment methods, and billing information.</p>

<h2>The BillingPortal Session Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_bps_001234",
  "object": "billing_portal_session",
  "customer": "dp_cus_xyz789",
  "url": "https://pay.drizlepay.com/billing/portal/session_abc123",
  "return_url": "https://example.com/account",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a portal session</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/billing_portal/sessions</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>customer</code></td><td>string</td><td>Required. Customer ID.</td></tr>
<tr><td><code>return_url</code></td><td>string</td><td>Required. URL to redirect after session ends.</td></tr>
</tbody>
</table>

<h2>Configuration</h2>
<p>Configure billing portal features in the <a href="/login">dashboard</a> — control which features customers can access.</p>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/subscriptions">Subscriptions API</a></li>
<li><a href="/docs/customers">Customers API</a></li>
</ul>
</div>
</div>
