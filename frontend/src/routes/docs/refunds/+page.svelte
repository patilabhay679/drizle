<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Refunds & Disputes | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Refunds & Disputes</h1>
	<p class="lead">The <code>Refund</code> object represents a full or partial return of a payment. The <code>Dispute</code> object represents a chargeback initiated by a cardholder.</p>

	<h2>The Refund Object</h2>
	<pre class="cb-code">&#123;
  "id": "dp_ref_789abc",
  "object": "refund",
  "amount": 5000,
  "currency": "AED",
  "status": "succeeded",
  "payment": "dp_pay_abc123",
  "reason": "customer_request",
  "created": 1719586400
&#125;</pre>

	<h3>Refund Statuses</h3>
	<table class="params">
		<thead>
			<tr><th>Status</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>pending</code></td><td>Refund initiated but not yet processed.</td></tr>
			<tr><td><code>succeeded</code></td><td>Refund completed and funds returned.</td></tr>
			<tr><td><code>failed</code></td><td>Refund could not be processed (insufficient balance, etc.).</td></tr>
		</tbody>
	</table>

	<h2>Endpoints</h2>

	<h3>Create a refund</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payments/:id/refund</span></div>
	<CodeBlock
		response={`&#123;
  "id": "dp_ref_789abc",
  "object": "refund",
  "amount": 5000,
  "currency": "AED",
  "status": "succeeded",
  "payment": "dp_pay_abc123",
  "reason": "customer_request",
  "created": 1719586400
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/payments/dp_pay_abc123/refund \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "amount": 5000,
    "reason": "customer_request"
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/payments/dp_pay_abc123/refund",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "amount": 5000,
        "reason": "customer_request"
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/payments/dp_pay_abc123/refund", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    amount: 5000,
    reason: "customer_request"
  })
});
const refund = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/payments/dp_pay_abc123/refund', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'amount' => 5000,
        'reason' => 'customer_request',
    ],
]);
echo $response->getBody();`,
		}}
	/>

	<h4>Parameters</h4>
	<table class="params">
		<thead>
			<tr><th>Param</th><th>Type</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>amount</code></td><td>integer</td><td>Optional. Amount in smallest currency unit. If omitted, full amount is refunded.</td></tr>
			<tr><td><code>reason</code></td><td>string</td><td>Optional. One of: <code>customer_request</code>, <code>duplicate</code>, <code>fraudulent</code>.</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
		</tbody>
	</table>

	<h3>List refunds</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/refunds</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/refunds?page=1&limit=20 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h2>Disputes (Chargebacks)</h2>
	<p>When a cardholder disputes a charge, a <code>Dispute</code> object is created. You can respond with evidence to contest the dispute.</p>

	<h3>The Dispute Object</h3>
	<pre class="cb-code">&#123;
  "id": "dp_dis_456def",
  "object": "dispute",
  "amount": 5000,
  "currency": "AED",
  "status": "needs_response",
  "payment": "dp_pay_abc123",
  "reason": "fraudulent",
  "due_by": 1720000000,
  "created": 1719586400
&#125;</pre>

	<h3>Dispute Statuses</h3>
	<table class="params">
		<thead>
			<tr><th>Status</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>needs_response</code></td><td>Evidence must be submitted before the due date.</td></tr>
			<tr><td><code>under_review</code></td><td>Evidence submitted; awaiting bank decision.</td></tr>
			<tr><td><code>won</code></td><td>Dispute resolved in your favor.</td></tr>
			<tr><td><code>lost</code></td><td>Dispute resolved against you.</td></tr>
		</tbody>
	</table>

	<h2>Events</h2>
	<table class="params">
		<thead>
			<tr><th>Event</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>refund.created</code></td><td>A refund was initiated.</td></tr>
			<tr><td><code>refund.succeeded</code></td><td>A refund completed successfully.</td></tr>
			<tr><td><code>refund.failed</code></td><td>A refund attempt failed.</td></tr>
			<tr><td><code>dispute.created</code></td><td>A new dispute was filed.</td></tr>
			<tr><td><code>dispute.updated</code></td><td>Dispute status changed.</td></tr>
			<tr><td><code>dispute.resolved</code></td><td>A dispute was resolved (won/lost).</td></tr>
		</tbody>
	</table>

	<div class="next-steps">
		<strong>Related guides</strong>
		<ul>
			<li><a href="/docs/payments">Payments API</a></li>
			<li><a href="/docs/errors">Error codes</a></li>
		</ul>
	</div>
</div>
