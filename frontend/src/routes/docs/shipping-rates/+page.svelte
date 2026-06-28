<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Shipping Rates API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Shipping Rates API</h1>
<p class="lead">The <code>ShippingRate</code> object defines the cost of shipping a product. Use shipping rates with invoices and checkout.</p>

<h2>The ShippingRate Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_sr_001234",
  "object": "shipping_rate",
  "display_name": "Standard Shipping",
  "amount": 1500,
  "currency": "AED",
  "delivery_estimate": &#123;
    "minimum": &#123;"unit": "business_day", "value": 3&#125;,
    "maximum": &#123;"unit": "business_day", "value": 5&#125;
  &#125;,
  "active": true,
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a shipping rate</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/shipping_rates</span></div>

<h3>Retrieve a shipping rate</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/shipping_rates/:id</span></div>

<h3>List shipping rates</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/shipping_rates</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/products">Products</a></li>
<li><a href="/docs/invoices">Invoices</a></li>
</ul>
</div>
</div>
