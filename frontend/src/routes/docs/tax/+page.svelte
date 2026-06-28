<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Tax API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Tax API</h1>
<p class="lead">The Drizle Pay Tax API automates tax calculation and collection for your transactions. Configure tax settings and calculate taxes automatically.</p>

<h2>The TaxCalculation Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_taxcalc_001234",
  "object": "tax_calculation",
  "amount_total": 10395,
  "tax_amount": 495,
  "currency": "AED",
  "customer": "dp_cus_xyz789",
  "line_items": [
    &#123;
      "amount": 9900,
      "tax_amount": 495,
      "tax_rates": ["dp_tr_001234"],
      "product": "dp_prod_001234"
    &#125;
  ],
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Calculate tax</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/tax/calculations</span></div>

<h3>Retrieve a calculation</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/tax/calculations/:id</span></div>

<h3>Create a tax transaction</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/tax/transactions</span></div>

<h3>Update tax settings</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/tax/settings</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/tax-codes">Tax Codes</a></li>
<li><a href="/docs/tax-rates">Tax Rates</a></li>
</ul>
</div>
</div>
