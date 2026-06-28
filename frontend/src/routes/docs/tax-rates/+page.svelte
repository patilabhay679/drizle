<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Tax Rates API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Tax Rates API</h1>
<p class="lead">The <code>TaxRate</code> object defines a tax percentage that can be applied to invoices, subscriptions, and checkout.</p>

<h2>The TaxRate Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_tr_001234",
  "object": "tax_rate",
  "display_name": "VAT 5%",
  "description": "UAE Standard VAT",
  "percentage": 5.0,
  "country": "AE",
  "state": null,
  "jurisdiction": "UAE",
  "active": true,
  "inclusive": false,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a tax rate</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/tax_rates</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>display_name</code></td><td>string</td><td>Required. Display name.</td></tr>
<tr><td><code>percentage</code></td><td>number</td><td>Required. Tax percentage (up to 4 decimals).</td></tr>
<tr><td><code>inclusive</code></td><td>boolean</td><td>Optional. Whether tax is inclusive.</td></tr>
<tr><td><code>country</code></td><td>string</td><td>Optional. Two-letter ISO country code.</td></tr>
</tbody>
</table>

<h3>Retrieve a tax rate</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/tax_rates/:id</span></div>

<h3>List tax rates</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/tax_rates</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/tax-codes">Tax Codes</a></li>
<li><a href="/docs/tax">Tax API</a></li>
</ul>
</div>
</div>
