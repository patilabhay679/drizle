<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Credit Notes API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Credit Notes API</h1>
<p class="lead">The <code>CreditNote</code> object represents a credit or refund applied to an invoice. Issue credit notes to correct billing errors.</p>

<h2>The CreditNote Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_cn_001234",
  "object": "credit_note",
  "amount": 5000,
  "currency": "AED",
  "invoice": "dp_inv_001234",
  "customer": "dp_cus_xyz789",
  "type": "post_payment",
  "reason": "duplicate",
  "status": "issued",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a credit note</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/credit_notes</span></div>

<h3>Retrieve a credit note</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/credit_notes/:id</span></div>

<h3>List credit notes</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/credit_notes</span></div>

<h3>Void a credit note</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/credit_notes/:id/void</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/invoices">Invoices API</a></li>
<li><a href="/docs/refunds">Refunds</a></li>
</ul>
</div>
</div>
