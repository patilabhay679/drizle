<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Payouts API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Payouts API</h1>
	<p class="lead">The <code>Payout</code> object represents a transfer of funds from your Drizle Pay balance to your bank account. Create scheduled or instant payouts.</p>

	<h2>The Payout Object</h2>
	<pre class="cb-code">&#123;
  "id": "po_001234",
  "object": "payout",
  "amount": 500000,
  "currency": "AED",
  "status": "paid",
  "destination": "••••1234",
  "description": "Weekly settlement",
  "paid_at": 1719500000,
  "created": 1719413600
&#125;</pre>

	<h3>Payout Statuses</h3>
	<table class="params">
		<thead>
			<tr><th>Status</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>pending</code></td><td>Payout initiated but not yet processed.</td></tr>
			<tr><td><code>paid</code></td><td>Payout completed successfully.</td></tr>
			<tr><td><code>failed</code></td><td>Payout failed (invalid bank details, etc.).</td></tr>
			<tr><td><code>canceled</code></td><td>Payout was canceled before processing.</td></tr>
		</tbody>
	</table>

	<h2>Endpoints</h2>

	<h3>Create a payout</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payouts</span></div>
	<CodeBlock
		response={`&#123;
  "id": "po_001234",
  "object": "payout",
  "amount": 500000,
  "currency": "AED",
  "status": "paid",
  "destination": "••••1234",
  "description": "Weekly settlement",
  "paid_at": 1719500000,
  "created": 1719413600
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/payouts \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "amount": 500000,
    "currency": "AED",
    "destination": "bank_account_id",
    "description": "Weekly settlement"
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/payouts",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "amount": 500000,
        "currency": "AED",
        "destination": "bank_account_id",
        "description": "Weekly settlement"
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/payouts", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    amount: 500000,
    currency: "AED",
    destination: "bank_account_id",
    description: "Weekly settlement"
  })
});
const payout = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/payouts', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'amount' => 500000,
        'currency' => 'AED',
        'destination' => 'bank_account_id',
        'description' => 'Weekly settlement',
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
			<tr><td><code>amount</code></td><td>integer</td><td>Required. Amount in smallest currency unit.</td></tr>
			<tr><td><code>currency</code></td><td>string</td><td>Required. Three-letter ISO code.</td></tr>
			<tr><td><code>destination</code></td><td>string</td><td>Required. Bank account ID.</td></tr>
			<tr><td><code>description</code></td><td>string</td><td>Optional. Max 255 characters.</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
		</tbody>
	</table>

	<h3>List payouts</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/payouts</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/payouts?page=1&limit=20 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<table class="params">
		<thead>
			<tr><th>Param</th><th>Type</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>page</code></td><td>integer</td><td>Page number (default 1).</td></tr>
			<tr><td><code>limit</code></td><td>integer</td><td>Results per page (default 20, max 100).</td></tr>
			<tr><td><code>status</code></td><td>string</td><td>Filter by status: <code>pending</code>, <code>paid</code>, <code>failed</code>.</td></tr>
		</tbody>
	</table>

	<h2>Events</h2>
	<table class="params">
		<thead>
			<tr><th>Event</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>payout.paid</code></td><td>A payout completed successfully.</td></tr>
			<tr><td><code>payout.failed</code></td><td>A payout attempt failed.</td></tr>
			<tr><td><code>payout.pending</code></td><td>A payout is pending processing.</td></tr>
		</tbody>
	</table>

	<div class="next-steps">
		<strong>Next steps</strong>
		<ul>
			<li><a href="/docs/errors">Error codes</a></li>
		</ul>
	</div>
</div>
