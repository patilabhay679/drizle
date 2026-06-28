<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Customers API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Customers API</h1>
	<p class="lead">The <code>Customer</code> object represents a buyer in your system. Use it to track payments, save payment methods, and manage recurring billing.</p>

	<h2>The Customer Object</h2>
	<pre class="cb-code">&#123;
  "id": "dp_cus_xyz789",
  "object": "customer",
  "email": "customer@example.com",
  "name": "Ahmed Al Maktoum",
  "phone": "+971501234567",
  "payment_methods": [
    &#123;
      "id": "dp_pm_def456",
      "type": "card",
      "last4": "4242",
      "brand": "visa"
    &#125;
  ],
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

	<h2>Endpoints</h2>

	<h3>Create a customer</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/customers</span></div>
	<CodeBlock
		response={`&#123;
  "id": "dp_cus_xyz789",
  "object": "customer",
  "email": "customer@example.com",
  "name": "Ahmed Al Maktoum",
  "phone": "+971501234567",
  "payment_methods": [],
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/customers \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "email": "customer@example.com",
    "name": "Ahmed Al Maktoum",
    "phone": "+971501234567"
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/customers",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "email": "customer@example.com",
        "name": "Ahmed Al Maktoum",
        "phone": "+971501234567"
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/customers", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    email: "customer@example.com",
    name: "Ahmed Al Maktoum",
    phone: "+971501234567"
  })
});
const customer = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/customers', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'email' => 'customer@example.com',
        'name' => 'Ahmed Al Maktoum',
        'phone' => '+971501234567',
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
			<tr><td><code>email</code></td><td>string</td><td>Required. Customer email address.</td></tr>
			<tr><td><code>name</code></td><td>string</td><td>Optional. Customer's full name.</td></tr>
			<tr><td><code>phone</code></td><td>string</td><td>Optional. Customer phone number.</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
		</tbody>
	</table>

	<h3>Retrieve a customer</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/customers/:id</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/customers/dp_cus_xyz789 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h3>List all customers</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/customers</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/customers?page=1&limit=20 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<table class="params">
		<thead>
			<tr><th>Param</th><th>Type</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>page</code></td><td>integer</td><td>Page number (default 1).</td></tr>
			<tr><td><code>limit</code></td><td>integer</td><td>Results per page (default 20, max 100).</td></tr>
			<tr><td><code>email</code></td><td>string</td><td>Filter by email address.</td></tr>
		</tbody>
	</table>

	<h3>Update a customer</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/customers/:id</span></div>
	<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/customers/dp_cus_xyz789 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '&#123;
    "name": "Updated Name",
    "phone": "+971509876543"
  &#125;'</pre>

	<h3>Delete a customer</h3>
	<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/customers/:id</span></div>
	<pre class="cb-code">curl -X DELETE https://api.drizlepay.com/v1/customers/dp_cus_xyz789 \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h2>Events</h2>
	<table class="params">
		<thead>
			<tr><th>Event</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>customer.created</code></td><td>A new customer was created.</td></tr>
			<tr><td><code>customer.updated</code></td><td>A customer's details were updated.</td></tr>
			<tr><td><code>customer.deleted</code></td><td>A customer was deleted.</td></tr>
		</tbody>
	</table>

	<div class="next-steps">
		<strong>Next steps</strong>
		<ul>
			<li><a href="/docs/payment-methods">Payment Methods API</a></li>
			<li><a href="/docs/subscriptions">Subscriptions API</a></li>
		</ul>
	</div>
</div>
