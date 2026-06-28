<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Tax Codes API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Tax Codes API</h1>
<p class="lead">The <code>TaxCode</code> object represents a tax classification for products. Use tax codes to calculate applicable taxes automatically.</p>

<h2>The TaxCode Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_tc_001234",
  "object": "tax_code",
  "name": "Digital Services",
  "description": "Digital products and electronic services",
  "active": true
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve a tax code</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/tax_codes/:id</span></div>

<h3>List tax codes</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/tax_codes</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/tax-rates">Tax Rates</a></li>
<li><a href="/docs/tax">Tax API</a></li>
</ul>
</div>
</div>
