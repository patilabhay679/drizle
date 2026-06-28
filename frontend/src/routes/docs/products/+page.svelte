<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Products API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Products API</h1>
<p class="lead">The <code>Product</code> object represents a good or service that you sell. Products can be used with prices and subscriptions.</p>

<h2>The Product Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_prod_001234",
  "object": "product",
  "name": "Premium Plan",
  "description": "Monthly subscription with all features",
  "active": true,
  "type": "service",
  "images": [],
  "metadata": &#123;&#125;,
  "created": 1719500000,
  "updated": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a product</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/products</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>name</code></td><td>string</td><td>Required. Product name (max 255 chars).</td></tr>
<tr><td><code>description</code></td><td>string</td><td>Optional. Product description.</td></tr>
<tr><td><code>type</code></td><td>string</td><td>Optional. <code>good</code> or <code>service</code>.</td></tr>
<tr><td><code>active</code></td><td>boolean</td><td>Optional. Whether the product is active.</td></tr>
<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
</tbody>
</table>

<h3>Retrieve a product</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/products/:id</span></div>

<h3>Update a product</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/products/:id</span></div>

<h3>List products</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/products</span></div>

<h3>Delete a product</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/products/:id</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/prices">Prices API</a></li>
<li><a href="/docs/subscriptions">Subscriptions API</a></li>
</ul>
</div>
</div>
