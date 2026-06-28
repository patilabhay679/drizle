<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Charges API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Charges API</h1>
	<p class="lead">The <code>Charge</code> object represents a successful payment captured by Drizle Pay. Charges are the fundamental transaction record.</p>

<h2>The Charge Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_ch_abc123",
  "object": "charge",
  "amount": 5000,
  "currency": "AED",
  "status": "succeeded",
  "paid": true,
  "refunded": false,
  "description": "Premium Plan",
  "payment_method": "dp_pm_def456",
  "customer": "dp_cus_xyz789",
  "failure_code": null,
  "failure_message": null,
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a charge</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/charges</span></div>
<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/charges \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '&#123;
    "amount": 5000,
    "currency": "AED",
    "source": "dp_cus_xyz789",
    "description": "Premium Plan"
  &#125;'</pre>

<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>amount</code></td><td>integer</td><td>Required. Amount in smallest currency unit.</td></tr>
<tr><td><code>currency</code></td><td>string</td><td>Required. Three-letter ISO code.</td></tr>
<tr><td><code>source</code></td><td>string</td><td>Required. Customer ID or token to charge.</td></tr>
<tr><td><code>description</code></td><td>string</td><td>Optional. Description of the charge.</td></tr>
<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
</tbody>
</table>

<h3>Retrieve a charge</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/charges/:id</span></div>

<h3>List charges</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/charges</span></div>

<h3>Capture a charge</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/charges/:id/capture</span></div>

<h2>Events</h2>
<table class="params">
<thead><tr><th>Event</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>charge.succeeded</code></td><td>A charge completed successfully.</td></tr>
<tr><td><code>charge.failed</code></td><td>A charge attempt failed.</td></tr>
<tr><td><code>charge.refunded</code></td><td>A charge was refunded.</td></tr>
<tr><td><code>charge.captured</code></td><td>An uncaptured charge was captured.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payments">Payments API</a></li>
<li><a href="/docs/refunds">Refunds</a></li>
</ul>
</div>

</div>
