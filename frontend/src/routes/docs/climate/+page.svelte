<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Climate API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Climate API</h1>
<p class="lead">The Climate API lets you purchase carbon removal credits to offset your carbon footprint. Choose from verified projects worldwide.</p>

<h2>The ClimateOrder Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_clim_001234",
  "object": "climate_order",
  "product": "dp_climp_001234",
  "amount": 5000,
  "currency": "AED",
  "metric_tons": 10.5,
  "status": "fulfilled",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>List climate products</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/climate/products</span></div>

<h3>Purchase carbon removal</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/climate/orders</span></div>

<h3>Retrieve an order</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/climate/orders/:id</span></div>

<h3>List orders</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/climate/orders</span></div>

<h3>Cancel an order</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/climate/orders/:id/cancel</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/reporting">Reporting</a></li>
<li><a href="/docs/balance">Balance API</a></li>
</ul>
</div>
</div>
