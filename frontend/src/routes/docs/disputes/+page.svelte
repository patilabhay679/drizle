<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Disputes API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Disputes API</h1>
	<p class="lead">The <code>Dispute</code> object represents a chargeback filed by a cardholder against a payment. Respond with evidence to contest disputes.</p>

<h2>The Dispute Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_dis_456def",
  "object": "dispute",
  "amount": 5000,
  "currency": "AED",
  "status": "needs_response",
  "payment": "dp_pay_abc123",
  "reason": "fraudulent",
  "evidence": &#123;&#125;,
  "due_by": 1720000000,
  "created": 1719586400
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve a dispute</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/disputes/:id</span></div>

<h3>List disputes</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/disputes</span></div>

<h3>Update a dispute</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/disputes/:id</span></div>

<h3>Submit evidence</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/disputes/:id/submit</span></div>

<h2>Dispute Statuses</h2>
<table class="params">
<thead><tr><th>Status</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>needs_response</code></td><td>Evidence must be submitted before due date.</td></tr>
<tr><td><code>under_review</code></td><td>Evidence submitted; awaiting bank decision.</td></tr>
<tr><td><code>won</code></td><td>Dispute resolved in your favor.</td></tr>
<tr><td><code>lost</code></td><td>Dispute resolved against you.</td></tr>
</tbody>
</table>

<h2>Events</h2>
<table class="params">
<thead><tr><th>Event</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>dispute.created</code></td><td>A new dispute was filed.</td></tr>
<tr><td><code>dispute.updated</code></td><td>Dispute evidence or status updated.</td></tr>
<tr><td><code>dispute.resolved</code></td><td>Dispute resolved (won or lost).</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/refunds">Refunds</a></li>
<li><a href="/docs/errors">Error codes</a></li>
</ul>
</div>

</div>
