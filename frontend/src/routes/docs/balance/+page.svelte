<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Balance API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Balance API</h1>
	<p class="lead">The <code>Balance</code> object represents the current funds in your Drizle Pay account. Retrieve it to check available, pending, and reserved balances.</p>

<h2>The Balance Object</h2>
<pre class="cb-code">&#123;
  "object": "balance",
  "available": [
    &#123;
      "amount": 1500000,
      "currency": "AED",
      "source_types": &#123;
        "card": 1000000,
        "bank_transfer": 500000
      &#125;
    &#125;
  ],
  "pending": [
    &#123;
      "amount": 250000,
      "currency": "AED",
      "source_types": &#123;
        "card": 250000
      &#125;
    &#125;
  ],
  "reserved": [
    &#123;
      "amount": 50000,
      "currency": "AED"
    &#125;
  ]
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve balance</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/balance</span></div>
<pre class="cb-code">curl https://api.drizlepay.com/v1/balance \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

<h2>Balance Types</h2>
<table class="params">
<thead><tr><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>available</code></td><td>Funds that can be paid out or used to process refunds.</td></tr>
<tr><td><code>pending</code></td><td>Funds from payments that haven't settled yet.</td></tr>
<tr><td><code>reserved</code></td><td>Funds held for disputes, reserves, or other obligations.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payouts">Payouts API</a></li>
<li><a href="/docs/transfers">Transfers API</a></li>
</ul>
</div>

</div>
