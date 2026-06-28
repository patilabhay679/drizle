<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Tokens API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Tokens API</h1>
	<p class="lead">The <code>Token</code> object represents a sensitive payment credential (card number, bank account) that can be used safely in API requests.</p>

<h2>The Token Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_tok_abc123",
  "object": "token",
  "type": "card",
  "card": &#123;
    "brand": "visa",
    "last4": "4242",
    "exp_month": 12,
    "exp_year": 2029,
    "fingerprint": "abc123def456"
  &#125;,
  "used": false,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a token</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/tokens</span></div>
<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/tokens \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '&#123;
    "card": &#123;
      "number": "4111111111111111",
      "exp_month": 12,
      "exp_year": 2029,
      "cvc": "123"
    &#125;
  &#125;'</pre>

<h3>Retrieve a token</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/tokens/:id</span></div>

<h2>Token Types</h2>
<table class="params">
<thead><tr><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>card</code></td><td>A card token created with card details.</td></tr>
<tr><td><code>bank_account</code></td><td>A bank account token for payouts.</td></tr>
<tr><td><code>apple_pay</code></td><td>An Apple Pay payment token.</td></tr>
<tr><td><code>google_pay</code></td><td>A Google Pay payment token.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payments">Payments API</a></li>
<li><a href="/docs/payment-methods">Payment Methods</a></li>
</ul>
</div>

</div>
