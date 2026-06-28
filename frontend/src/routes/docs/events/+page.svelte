<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Events API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Events API</h1>
	<p class="lead">The <code>Event</code> object represents an occurrence in your Drizle Pay account. Events are used for webhooks and audit trails.</p>

<h2>The Event Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_evt_001234",
  "object": "event",
  "type": "payment.succeeded",
  "created": 1719500000,
  "data": &#123;
    "object": &#123;
      "id": "dp_pay_abc123",
      "object": "payment",
      "amount": 5000,
      "status": "succeeded"
    &#125;
  &#125;,
  "pending_webhooks": 0,
  "request": &#123;
    "id": "req_abc123",
    "idempotency_key": null
  &#125;
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve an event</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/events/:id</span></div>

<h3>List events</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/events</span></div>
<pre class="cb-code">curl https://api.drizlepay.com/v1/events?type=payment.succeeded&limit=10 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

<h2>Event Types</h2>
<table class="params">
<thead><tr><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>payment.succeeded</code></td><td>Payment completed.</td></tr>
<tr><td><code>payment.failed</code></td><td>Payment failed.</td></tr>
<tr><td><code>payment.refunded</code></td><td>Payment refunded.</td></tr>
<tr><td><code>customer.created</code></td><td>Customer created.</td></tr>
<tr><td><code>customer.updated</code></td><td>Customer updated.</td></tr>
<tr><td><code>charge.succeeded</code></td><td>Charge succeeded.</td></tr>
<tr><td><code>charge.failed</code></td><td>Charge failed.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/webhooks">Webhooks guide</a></li>
<li><a href="/docs/webhook-endpoints">Webhook Endpoints API</a></li>
</ul>
</div>

</div>
