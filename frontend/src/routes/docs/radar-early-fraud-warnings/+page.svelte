<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Early Fraud Warnings API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Early Fraud Warnings API</h1>
<p class="lead">The <code>EarlyFraudWarning</code> object represents a notification from card networks about potentially fraudulent transactions.</p>

<h2>The EarlyFraudWarning Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_efw_001234",
  "object": "early_fraud_warning",
  "charge": "dp_ch_abc123",
  "payment": "dp_pay_abc123",
  "fraud_type": "card_not_present",
  "actionable": true,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve an early fraud warning</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/radar/early_fraud_warnings/:id</span></div>

<h3>List early fraud warnings</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/radar/early_fraud_warnings</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/reviews">Reviews</a></li>
<li><a href="/docs/disputes">Disputes</a></li>
</ul>
</div>
</div>
