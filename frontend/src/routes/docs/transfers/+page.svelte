<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Transfers API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Transfers API</h1>
	<p class="lead">The <code>Transfer</code> object moves funds from your Drizle Pay balance to a connected account or bank account.</p>

<h2>The Transfer Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_tr_001234",
  "object": "transfer",
  "amount": 500000,
  "currency": "AED",
  "destination": "dp_cus_xyz789",
  "description": "Platform payout",
  "reversed": false,
  "balance_transaction": "dp_txn_001234",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a transfer</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/transfers</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>amount</code></td><td>integer</td><td>Required. Amount in smallest currency unit.</td></tr>
<tr><td><code>currency</code></td><td>string</td><td>Required. Three-letter ISO code.</td></tr>
<tr><td><code>destination</code></td><td>string</td><td>Required. Customer or account ID to send funds to.</td></tr>
<tr><td><code>description</code></td><td>string</td><td>Optional. Description of the transfer.</td></tr>
<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
</tbody>
</table>

<h3>Retrieve a transfer</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/transfers/:id</span></div>

<h3>List transfers</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/transfers</span></div>

<h3>Reverse a transfer</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/transfers/:id/reverse</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payouts">Payouts API</a></li>
<li><a href="/docs/balance">Balance API</a></li>
</ul>
</div>

</div>
