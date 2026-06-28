<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Application Fees API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Application Fees API</h1>
<p class="lead">The <code>ApplicationFee</code> object represents a fee collected by the platform from a connected account transaction.</p>

<h2>The ApplicationFee Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_fee_001234",
  "object": "application_fee",
  "amount": 500,
  "currency": "AED",
  "account": "dp_acct_001234",
  "charge": "dp_ch_abc123",
  "refunded": false,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve an application fee</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/application_fees/:id</span></div>

<h3>List application fees</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/application_fees</span></div>

<h3>Refund an application fee</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/application_fees/:id/refund</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/accounts">Accounts API</a></li>
<li><a href="/docs/transfers">Transfers</a></li>
</ul>
</div>
</div>
