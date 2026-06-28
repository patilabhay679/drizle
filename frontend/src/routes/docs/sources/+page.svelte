<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Sources API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Sources API</h1>
	<p class="lead">The <code>Source</code> object represents a reusable payment instrument. Sources handle the full payment flow including authentication.</p>

<h2>The Source Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_src_abc123",
  "object": "source",
  "type": "card",
  "status": "chargeable",
  "amount": null,
  "currency": null,
  "customer": "dp_cus_xyz789",
  "usage": "reusable",
  "flow": "none",
  "client_secret": "src_client_secret_abc123",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a source</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/sources</span></div>

<h3>Retrieve a source</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/sources/:id</span></div>

<h3>Attach a source to a customer</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/customers/:customer_id/sources</span></div>

<h2>Source Types</h2>
<table class="params">
<thead><tr><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>card</code></td><td>Credit or debit card.</td></tr>
<tr><td><code>apple_pay</code></td><td>Apple Pay token.</td></tr>
<tr><td><code>google_pay</code></td><td>Google Pay token.</td></tr>
<tr><td><code>tabby</code></td><td>Tabby BNPL installment source.</td></tr>
<tr><td><code>tamara</code></td><td>Tamara BNPL source.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payment-methods">Payment Methods</a></li>
<li><a href="/docs/tokens">Tokens API</a></li>
</ul>
</div>

</div>
