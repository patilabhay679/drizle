<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Invoices API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Invoices API</h1>
<p class="lead">The <code>Invoice</code> object represents a billing statement generated for a subscription or one-time charge.</p>

<h2>The Invoice Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_inv_001234",
  "object": "invoice",
  "amount_due": 9900,
  "amount_paid": 9900,
  "amount_remaining": 0,
  "currency": "AED",
  "status": "paid",
  "customer": "dp_cus_xyz789",
  "subscription": "dp_sub_001234",
  "lines": &#123;
    "data": [
      &#123;
        "description": "Premium Plan",
        "amount": 9900,
        "period": &#123;"start": 1719500000, "end": 1722180000&#125;
      &#125;
    ]
  &#125;,
  "paid_at": 1719500000,
  "created": 1719500000,
  "pdf_url": "https://pay.drizlepay.com/invoice/dp_inv_001234.pdf"
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create an invoice</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/invoices</span></div>

<h3>Retrieve an invoice</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/invoices/:id</span></div>

<h3>List invoices</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/invoices</span></div>

<h3>Finalize an invoice</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/invoices/:id/finalize</span></div>

<h3>Pay an invoice</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/invoices/:id/pay</span></div>

<h3>Void an invoice</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/invoices/:id/void</span></div>

<h2>Invoice Statuses</h2>
<table class="params">
<thead><tr><th>Status</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>draft</code></td><td>Invoice is being prepared.</td></tr>
<tr><td><code>open</code></td><td>Invoice finalized and awaiting payment.</td></tr>
<tr><td><code>paid</code></td><td>Invoice has been paid.</td></tr>
<tr><td><code>uncollectible</code></td><td>Payment could not be collected.</td></tr>
<tr><td><code>void</code></td><td>Invoice was voided.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/subscriptions">Subscriptions</a></li>
<li><a href="/docs/credit-notes">Credit Notes</a></li>
</ul>
</div>
</div>
