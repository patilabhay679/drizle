<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Value Lists API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Value Lists API</h1>
<p class="lead">The <code>ValueList</code> object contains a list of values used by Radar fraud rules. Use them to block or allow specific entities.</p>

<h2>The ValueList Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_vl_001234",
  "object": "value_list",
  "name": "Blocked Emails",
  "item_type": "email",
  "alias": "blocked_emails",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a value list</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/radar/value_lists</span></div>

<h3>Retrieve a value list</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/radar/value_lists/:id</span></div>

<h3>Update a value list</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/radar/value_lists/:id</span></div>

<h3>List value lists</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/radar/value_lists</span></div>

<h3>Delete a value list</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/radar/value_lists/:id</span></div>

<h2>Item Types</h2>
<table class="params">
<thead><tr><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>email</code></td><td>Email addresses.</td></tr>
<tr><td><code>ip_address</code></td><td>IP addresses (v4 or v6).</td></tr>
<tr><td><code>card_fingerprint</code></td><td>Card fingerprints.</td></tr>
<tr><td><code>country</code></td><td>Two-letter ISO country codes.</td></tr>
<tr><td><code>string</code></td><td>Free-form strings.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/reviews">Reviews</a></li>
<li><a href="/docs/radar-early-fraud-warnings">Early Fraud Warnings</a></li>
</ul>
</div>
</div>
