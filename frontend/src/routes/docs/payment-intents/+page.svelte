<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Payment Intents API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Payment Intents API</h1>
	<p class="lead">The <code>PaymentIntent</code> object tracks the lifecycle of a payment from creation through authentication and capture. Use it for dynamic payment flows.</p>

<h2>The PaymentIntent Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_pi_abc123",
  "object": "payment_intent",
  "amount": 5000,
  "currency": "AED",
  "status": "requires_payment_method",
  "payment_method": null,
  "customer": "dp_cus_xyz789",
  "description": "Premium Plan",
  "next_action": null,
  "client_secret": "pi_abc123_secret_xyz789",
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a PaymentIntent</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payment_intents</span></div>

<h3>Retrieve a PaymentIntent</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/payment_intents/:id</span></div>

<h3>Update a PaymentIntent</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payment_intents/:id</span></div>

<h3>Confirm a PaymentIntent</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payment_intents/:id/confirm</span></div>

<h3>Cancel a PaymentIntent</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payment_intents/:id/cancel</span></div>

<h3>List PaymentIntents</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/payment_intents</span></div>

<h2>PaymentIntent Statuses</h2>
<table class="params">
<thead><tr><th>Status</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>requires_payment_method</code></td><td>Awaiting a payment method.</td></tr>
<tr><td><code>requires_confirmation</code></td><td>Ready to confirm.</td></tr>
<tr><td><code>requires_action</code></td><td>Customer must complete authentication.</td></tr>
<tr><td><code>processing</code></td><td>Payment is being processed.</td></tr>
<tr><td><code>succeeded</code></td><td>Payment completed successfully.</td></tr>
<tr><td><code>canceled</code></td><td>Payment was canceled.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payments">Payments API</a></li>
<li><a href="/docs/setup-intents">Setup Intents</a></li>
</ul>
</div>

</div>
