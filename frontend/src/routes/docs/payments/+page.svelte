<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Payments API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Payments API</h1>
	<p class="lead">The <code>Payment</code> object represents a single transaction processed through the Drizle Pay platform. Create, retrieve, list, and refund payments.</p>

	<h2>The Payment Object</h2>
	<pre class="cb-code">&#123;
  "id": "dp_pay_abc123",
  "object": "payment",
  "amount": 5000,
  "currency": "AED",
  "status": "succeeded",
  "description": "Premium Plan – Monthly",
  "payment_method": "card",
  "customer": "dp_cus_xyz789",
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

	<h3>Payment Statuses</h3>
	<table class="params">
		<thead>
			<tr><th>Status</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>pending</code></td><td>Payment initiated but not yet processed.</td></tr>
			<tr><td><code>succeeded</code></td><td>Payment completed successfully.</td></tr>
			<tr><td><code>failed</code></td><td>Payment failed (declined, expired, etc.).</td></tr>
			<tr><td><code>refunded</code></td><td>Payment fully refunded.</td></tr>
			<tr><td><code>partially_refunded</code></td><td>Payment partially refunded.</td></tr>
		</tbody>
	</table>

	<h2>Endpoints</h2>

	<h3>Create a payment</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payments</span></div>
	<CodeBlock
		response={`&#123;
  "id": "dp_pay_abc123",
  "object": "payment",
  "amount": 5000,
  "currency": "AED",
  "status": "succeeded",
  "description": "Premium Plan – Monthly",
  "payment_method": "card",
  "customer": "dp_cus_xyz789",
  "created": 1719500000
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/payments \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "amount": 5000,
    "currency": "AED",
    "payment_method": "card",
    "description": "Premium Plan – Monthly",
    "customer": &#123;
      "email": "customer@example.com"
    &#125;
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/payments",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "amount": 5000,
        "currency": "AED",
        "payment_method": "card",
        "description": "Premium Plan – Monthly",
        "customer": {"email": "customer@example.com"}
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/payments", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    amount: 5000,
    currency: "AED",
    payment_method: "card",
    description: "Premium Plan – Monthly",
    customer: { email: "customer@example.com" }
  })
});
const payment = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/payments', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'amount' => 5000,
        'currency' => 'AED',
        'payment_method' => 'card',
        'description' => 'Premium Plan – Monthly',
        'customer' => ['email' => 'customer@example.com'],
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
			<tr><td><code>amount</code></td><td>integer</td><td>Required. Amount in the smallest currency unit (e.g., 5000 = AED 50.00). Minimum 100.</td></tr>
			<tr><td><code>currency</code></td><td>string</td><td>Required. Three-letter ISO currency code. Supported: AED, USD, EUR, GBP, SAR.</td></tr>
			<tr><td><code>payment_method</code></td><td>string</td><td>Required. One of: <code>card</code>, <code>apple_pay</code>, <code>google_pay</code>, <code>tabby</code>, <code>tamara</code>, <code>aani</code>.</td></tr>
			<tr><td><code>description</code></td><td>string</td><td>Optional. Max 255 characters.</td></tr>
			<tr><td><code>customer</code></td><td>object</td><td>Optional. Customer details: <code>email</code> (required), <code>name</code> (optional), <code>phone</code> (optional).</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
			<tr><td><code>idempotency_key</code></td><td>string</td><td>Optional. Idempotency key to prevent duplicate processing.</td></tr>
		</tbody>
	</table>

	<h3>Retrieve a payment</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/payments/:id</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/payments/dp_pay_abc123 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h3>List all payments</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/payments</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/payments?page=1&limit=20 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<table class="params">
		<thead>
			<tr><th>Param</th><th>Type</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>page</code></td><td>integer</td><td>Page number (default 1).</td></tr>
			<tr><td><code>limit</code></td><td>integer</td><td>Results per page (default 20, max 100).</td></tr>
			<tr><td><code>status</code></td><td>string</td><td>Filter by status: <code>pending</code>, <code>succeeded</code>, <code>failed</code>, <code>refunded</code>.</td></tr>
			<tr><td><code>customer</code></td><td>string</td><td>Filter by customer ID.</td></tr>
		</tbody>
	</table>

	<h3>Refund a payment</h3>
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
			<tr><td><code>amount</code></td><td>integer</td><td>Optional. Amount to refund. If omitted, the full amount is refunded.</td></tr>
			<tr><td><code>reason</code></td><td>string</td><td>Optional. Reason for the refund: <code>customer_request</code>, <code>duplicate</code>, <code>fraudulent</code>.</td></tr>
		</tbody>
	</table>

	<h2>Events</h2>
	<table class="params">
		<thead>
			<tr><th>Event</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>payment.succeeded</code></td><td>A payment completed successfully.</td></tr>
			<tr><td><code>payment.failed</code></td><td>A payment attempt failed.</td></tr>
			<tr><td><code>payment.refunded</code></td><td>A payment was refunded (partial or full).</td></tr>
			<tr><td><code>payment.pending</code></td><td>A payment is pending processing.</td></tr>
		</tbody>
	</table>

	<div class="next-steps">
		<strong>Next steps</strong>
		<ul>
			<li><a href="/docs/payment-methods">Payment Methods API</a></li>
			<li><a href="/docs/refunds">Refunds & Disputes</a></li>
			<li><a href="/docs/idempotency">Idempotency</a></li>
		</ul>
	</div>
</div>
