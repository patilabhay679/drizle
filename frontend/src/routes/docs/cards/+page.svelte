<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Cards API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Cards API</h1>
	<p class="lead">The <code>Card</code> object represents a credit or debit card attached to a customer. Cards are a type of payment method.</p>

<h2>The Card Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_card_abc123",
  "object": "card",
  "brand": "visa",
  "last4": "4242",
  "exp_month": 12,
  "exp_year": 2029,
  "fingerprint": "abc123def456",
  "customer": "dp_cus_xyz789",
  "name": "Ahmed Al Maktoum",
  "address_city": "Dubai",
  "address_country": "AE",
  "cvc_check": "pass",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a card</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/customers/:customer_id/cards</span></div>

<h3>Retrieve a card</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/customers/:customer_id/cards/:id</span></div>

<h3>List cards</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/customers/:customer_id/cards</span></div>

<h3>Delete a card</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/customers/:customer_id/cards/:id</span></div>

<h2>Card Brands</h2>
<table class="params">
<thead><tr><th>Brand</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>visa</code></td><td>Visa credit/debit cards.</td></tr>
<tr><td><code>mastercard</code></td><td>Mastercard credit/debit cards.</td></tr>
<tr><td><code>amex</code></td><td>American Express cards.</td></tr>
<tr><td><code>jcb</code></td><td>JCB cards (Japan).</td></tr>
<tr><td><code>diners</code></td><td>Diners Club cards.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payment-methods">Payment Methods</a></li>
<li><a href="/docs/customers">Customers API</a></li>
</ul>
</div>

</div>
