<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Setup Intents API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Setup Intents API</h1>
	<p class="lead">The <code>SetupIntent</code> object saves a payment method for future use. Use it to securely collect payment details without creating an immediate charge.</p>

<h2>The SetupIntent Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_si_abc123",
  "object": "setup_intent",
  "status": "requires_payment_method",
  "customer": "dp_cus_xyz789",
  "payment_method": null,
  "payment_method_types": ["card"],
  "client_secret": "si_abc123_secret_xyz789",
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a SetupIntent</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/setup_intents</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>customer</code></td><td>string</td><td>Optional. Customer ID to attach the payment method to.</td></tr>
<tr><td><code>payment_method_types</code></td><td>array</td><td>Optional. List of payment method types to allow.</td></tr>
<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
</tbody>
</table>

<h3>Retrieve a SetupIntent</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/setup_intents/:id</span></div>

<h3>Confirm a SetupIntent</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/setup_intents/:id/confirm</span></div>

<h3>Cancel a SetupIntent</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/setup_intents/:id/cancel</span></div>

<h3>List SetupIntents</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/setup_intents</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payment-intents">Payment Intents</a></li>
<li><a href="/docs/payment-methods">Payment Methods</a></li>
</ul>
</div>

</div>
