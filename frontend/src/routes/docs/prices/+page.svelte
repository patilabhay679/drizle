<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Prices API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Prices API</h1>
<p class="lead">The <code>Price</code> object defines the cost of a product. Prices can be one-time or recurring, with different currency and billing intervals.</p>

<h2>The Price Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_price_001234",
  "object": "price",
  "product": "dp_prod_001234",
  "unit_amount": 9900,
  "currency": "AED",
  "recurring": &#123;
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": 14
  &#125;,
  "active": true,
  "nickname": "Monthly Premium",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a price</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/prices</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>product</code></td><td>string</td><td>Required. Product ID.</td></tr>
<tr><td><code>unit_amount</code></td><td>integer</td><td>Required. Price in smallest currency unit.</td></tr>
<tr><td><code>currency</code></td><td>string</td><td>Required. Three-letter ISO code.</td></tr>
<tr><td><code>recurring</code></td><td>object</td><td>Optional. &#123;<code>interval</code>: <code>day</code>,<code>week</code>,<code>month</code>,<code>year</code>&#125;.</td></tr>
<tr><td><code>nickname</code></td><td>string</td><td>Optional. Internal label for the price.</td></tr>
</tbody>
</table>

<h3>Retrieve a price</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/prices/:id</span></div>

<h3>Update a price</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/prices/:id</span></div>

<h3>List prices</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/prices</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/products">Products API</a></li>
<li><a href="/docs/subscriptions">Subscriptions API</a></li>
</ul>
</div>
</div>
