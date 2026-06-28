<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Quotes API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Quotes API</h1>
<p class="lead">The <code>Quote</code> object represents a price estimate for a subscription or payment. Generate quotes and convert them to invoices.</p>

<h2>The Quote Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_qt_001234",
  "object": "quote",
  "amount_subtotal": 9900,
  "amount_total": 10395,
  "currency": "AED",
  "customer": "dp_cus_xyz789",
  "status": "draft",
  "lines": &#123;
    "data": [
      &#123;
        "price": "dp_price_001234",
        "quantity": 1,
        "amount": 9900
      &#125;
    ]
  &#125;,
  "expires_at": 1720000000,
  "invoice": null,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a quote</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/quotes</span></div>

<h3>Retrieve a quote</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/quotes/:id</span></div>

<h3>Update a quote</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/quotes/:id</span></div>

<h3>List quotes</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/quotes</span></div>

<h3>Accept a quote</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/quotes/:id/accept</span></div>

<h3>Cancel a quote</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/quotes/:id/cancel</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/invoices">Invoices API</a></li>
<li><a href="/docs/subscriptions">Subscriptions</a></li>
</ul>
</div>
</div>
