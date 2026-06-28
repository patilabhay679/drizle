<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Reviews API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Reviews API</h1>
<p class="lead">The <code>Review</code> object represents a payment flagged by our fraud detection system. Reviews require manual inspection.</p>

<h2>The Review Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_rv_001234",
  "object": "review",
  "charge": "dp_ch_abc123",
  "payment": "dp_pay_abc123",
  "reason": "unusual_activity",
  "status": "open",
  "open": true,
  "closed_reason": null,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve a review</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/reviews/:id</span></div>

<h3>List reviews</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/reviews</span></div>

<h3>Approve a review</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/reviews/:id/approve</span></div>

<h2>Review Reasons</h2>
<table class="params">
<thead><tr><th>Reason</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>unusual_activity</code></td><td>Suspicious spending pattern detected.</td></tr>
<tr><td><code>high_risk</code></td><td>Payment matches high-risk indicators.</td></tr>
<tr><td><code>new_account</code></td><td>Payment from a newly created account.</td></tr>
<tr><td><code>velocity</code></td><td>Unusual transaction velocity.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/radar-value-lists">Value Lists</a></li>
<li><a href="/docs/disputes">Disputes</a></li>
</ul>
</div>
</div>
