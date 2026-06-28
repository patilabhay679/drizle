<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Payment Methods API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Payment Methods API</h1>
	<p class="lead">The <code>PaymentMethod</code> object represents a payment instrument attached to a customer. Save cards, wallets, and BNPL tokens for future use.</p>

	<h2>The PaymentMethod Object</h2>
	<pre class="cb-code">&#123;
  "id": "dp_pm_def456",
  "object": "payment_method",
  "type": "card",
  "card": &#123;
    "brand": "visa",
    "last4": "4242",
    "exp_month": 12,
    "exp_year": 2029
  &#125;,
  "customer": "dp_cus_xyz789",
  "created": 1719500000
&#125;</pre>

	<h3>Supported Types</h3>
	<table class="params">
		<thead>
			<tr><th>Type</th><th>Description</th><th>Markets</th></tr>
		</thead>
		<tbody>
			<tr><td><code>card</code></td><td>Credit/debit cards (Visa, Mastercard, JCB, Diners)</td><td>Global</td></tr>
			<tr><td><code>apple_pay</code></td><td>Apple Pay (web + in-app)</td><td>Global</td></tr>
			<tr><td><code>google_pay</code></td><td>Google Pay (web + Android)</td><td>Global</td></tr>
			<tr><td><code>tabby</code></td><td>BNPL — pay in 4 installments</td><td>UAE, KSA</td></tr>
			<tr><td><code>tamara</code></td><td>BNPL — pay later or in installments</td><td>UAE, KSA</td></tr>
			<tr><td><code>aani</code></td><td>Instant bank transfer (UAE)</td><td>UAE</td></tr>
			<tr><td><code>direct_debit</code></td><td>Direct debit / SEPA</td><td>EU, UK</td></tr>
		</tbody>
	</table>

	<h2>Endpoints</h2>

	<h3>Attach a payment method</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payment_methods</span></div>
	<CodeBlock
		response={`&#123;
  "id": "dp_pm_def456",
  "object": "payment_method",
  "type": "card",
  "card": &#123;
    "brand": "visa",
    "last4": "4242",
    "exp_month": 12,
    "exp_year": 2029
  &#125;,
  "customer": "dp_cus_xyz789",
  "created": 1719500000
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/payment_methods \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "customer": "dp_cus_xyz789",
    "type": "card",
    "card": &#123;
      "number": "4111111111111111",
      "exp_month": 12,
      "exp_year": 2029,
      "cvc": "123"
    &#125;
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/payment_methods",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "customer": "dp_cus_xyz789",
        "type": "card",
        "card": {
            "number": "4111111111111111",
            "exp_month": 12,
            "exp_year": 2029,
            "cvc": "123"
        }
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/payment_methods", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    customer: "dp_cus_xyz789",
    type: "card",
    card: {
      number: "4111111111111111",
      exp_month: 12,
      exp_year: 2029,
      cvc: "123"
    }
  })
});
const pm = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/payment_methods', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'customer' => 'dp_cus_xyz789',
        'type' => 'card',
        'card' => [
            'number' => '4111111111111111',
            'exp_month' => 12,
            'exp_year' => 2029,
            'cvc' => '123',
        ],
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
			<tr><td><code>customer</code></td><td>string</td><td>Required. Customer ID to attach to.</td></tr>
			<tr><td><code>type</code></td><td>string</td><td>Required. One of the supported types above.</td></tr>
			<tr><td><code>card</code></td><td>object</td><td>Required for card type. Fields: <code>number</code>, <code>exp_month</code>, <code>exp_year</code>, <code>cvc</code>.</td></tr>
			<tr><td><code>billing_details</code></td><td>object</td><td>Optional. <code>name</code>, <code>email</code>, <code>phone</code>, <code>address</code>.</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
		</tbody>
	</table>

	<h3>List payment methods for a customer</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/customers/:id/payment_methods</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/customers/dp_cus_xyz789/payment_methods \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h3>Detach a payment method</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/payment_methods/:id/detach</span></div>
	<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/payment_methods/dp_pm_def456/detach \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h2>Events</h2>
	<table class="params">
		<thead>
			<tr><th>Event</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>payment_method.attached</code></td><td>A payment method was attached to a customer.</td></tr>
			<tr><td><code>payment_method.detached</code></td><td>A payment method was detached from a customer.</td></tr>
		</tbody>
	</table>

	<div class="next-steps">
		<strong>Next steps</strong>
		<ul>
			<li><a href="/docs/customers">Customers API</a></li>
			<li><a href="/docs/payments">Payments API</a></li>
		</ul>
	</div>
</div>
