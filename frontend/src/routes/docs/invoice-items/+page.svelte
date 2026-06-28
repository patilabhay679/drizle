<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Invoice Items API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Invoice Items API</h1>
<p class="lead">The <code>InvoiceItem</code> object represents a line item added to an invoice. Use it to add one-time charges or credits.</p>

<h2>The InvoiceItem Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_ii_001234",
  "object": "invoice_item",
  "amount": 5000,
  "currency": "AED",
  "description": "Setup fee",
  "invoice": "dp_inv_001234",
  "customer": "dp_cus_xyz789",
  "period": &#123;"start": 1719500000, "end": 1722180000&#125;,
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create an invoice item</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/invoiceitems</span></div>

<h3>Retrieve an invoice item</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/invoiceitems/:id</span></div>

<h3>Update an invoice item</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/invoiceitems/:id</span></div>

<h3>List invoice items</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/invoiceitems</span></div>

<h3>Delete an invoice item</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/invoiceitems/:id</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/invoices">Invoices API</a></li>
<li><a href="/docs/credit-notes">Credit Notes</a></li>
</ul>
</div>
</div>
