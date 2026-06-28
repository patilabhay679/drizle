<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Subscriptions API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Subscriptions API</h1>
	<p class="lead">Create and manage recurring billing plans and subscriptions. Drizle Pay handles billing cycles, proration, dunning, and invoice generation.</p>

	<h2>Subscription Lifecycle</h2>
	<p>A <strong>Plan</strong> defines the pricing model (amount, currency, interval). A <strong>Subscription</strong> attaches a customer to a plan and tracks the billing state.</p>

	<h2>The Plan Object</h2>
	<pre class="cb-code">&#123;
  "id": "dp_plan_monthly_001",
  "object": "plan",
  "amount": 29900,
  "currency": "AED",
  "interval": "month",
  "name": "Pro Monthly",
  "trial_days": 14,
  "active": true,
  "created": 1719500000
&#125;</pre>

	<h2>The Subscription Object</h2>
	<pre class="cb-code">&#123;
  "id": "dp_sub_abc456",
  "object": "subscription",
  "customer": "dp_cus_xyz789",
  "plan": "dp_plan_monthly_001",
  "status": "active",
  "current_period_start": 1719500000,
  "current_period_end": 1722188400,
  "cancel_at_period_end": false,
  "created": 1719500000
&#125;</pre>

	<h3>Subscription Statuses</h3>
	<table class="params">
		<thead>
			<tr><th>Status</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>active</code></td><td>Subscription is active and billing.</td></tr>
			<tr><td><code>trialing</code></td><td>In trial period (no charge yet).</td></tr>
			<tr><td><code>past_due</code></td><td>Payment failed; dunning in progress.</td></tr>
			<tr><td><code>canceled</code></td><td>Subscription ended.</td></tr>
			<tr><td><code>incomplete</code></td><td>Initial payment failed or pending.</td></tr>
		</tbody>
	</table>

	<h2>Endpoints</h2>

	<h3>Create a plan</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/plans</span></div>
	<CodeBlock
		response={`&#123;
  "id": "dp_plan_monthly_001",
  "object": "plan",
  "amount": 29900,
  "currency": "AED",
  "interval": "month",
  "name": "Pro Monthly",
  "trial_days": 14,
  "active": true,
  "created": 1719500000
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/plans \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "name": "Pro Monthly",
    "amount": 29900,
    "currency": "AED",
    "interval": "month",
    "trial_days": 14
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/plans",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "name": "Pro Monthly",
        "amount": 29900,
        "currency": "AED",
        "interval": "month",
        "trial_days": 14
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/plans", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    name: "Pro Monthly",
    amount: 29900,
    currency: "AED",
    interval: "month",
    trial_days: 14
  })
});
const plan = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/plans', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'name' => 'Pro Monthly',
        'amount' => 29900,
        'currency' => 'AED',
        'interval' => 'month',
        'trial_days' => 14,
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
			<tr><td><code>name</code></td><td>string</td><td>Required. Plan name.</td></tr>
			<tr><td><code>amount</code></td><td>integer</td><td>Required. Amount per interval in smallest currency unit.</td></tr>
			<tr><td><code>currency</code></td><td>string</td><td>Required. Three-letter ISO code.</td></tr>
			<tr><td><code>interval</code></td><td>string</td><td>Required. One of: <code>day</code>, <code>week</code>, <code>month</code>, <code>year</code>.</td></tr>
			<tr><td><code>trial_days</code></td><td>integer</td><td>Optional. Number of trial days (default 0).</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
		</tbody>
	</table>

	<h3>Create a subscription</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/subscriptions</span></div>
	<CodeBlock
		response={`&#123;
  "id": "dp_sub_abc456",
  "object": "subscription",
  "customer": "dp_cus_xyz789",
  "plan": "dp_plan_monthly_001",
  "status": "active",
  "current_period_start": 1719500000,
  "current_period_end": 1722188400,
  "cancel_at_period_end": false,
  "created": 1719500000
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/subscriptions \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "customer": "dp_cus_xyz789",
    "plan": "dp_plan_monthly_001",
    "payment_method": "card",
    "trial": false
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/subscriptions",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "customer": "dp_cus_xyz789",
        "plan": "dp_plan_monthly_001",
        "payment_method": "card",
        "trial": false
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/subscriptions", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    customer: "dp_cus_xyz789",
    plan: "dp_plan_monthly_001",
    payment_method: "card",
    trial: false
  })
});
const subscription = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/subscriptions', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'customer' => 'dp_cus_xyz789',
        'plan' => 'dp_plan_monthly_001',
        'payment_method' => 'card',
        'trial' => false,
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
			<tr><td><code>customer</code></td><td>string</td><td>Required. Customer ID.</td></tr>
			<tr><td><code>plan</code></td><td>string</td><td>Required. Plan ID.</td></tr>
			<tr><td><code>payment_method</code></td><td>string</td><td>Required. Payment method for recurring charges.</td></tr>
			<tr><td><code>trial</code></td><td>boolean</td><td>Optional. Use plan's trial period (default false).</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
		</tbody>
	</table>

	<h3>Cancel a subscription</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/subscriptions/:id/cancel</span></div>
	<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/subscriptions/dp_sub_abc456/cancel \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h2>Events</h2>
	<table class="params">
		<thead>
			<tr><th>Event</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>subscription.created</code></td><td>A new subscription was created.</td></tr>
			<tr><td><code>subscription.updated</code></td><td>Subscription details changed.</td></tr>
			<tr><td><code>subscription.canceled</code></td><td>A subscription was canceled.</td></tr>
			<tr><td><code>subscription.past_due</code></td><td>A payment failed; dunning started.</td></tr>
			<tr><td><code>invoice.created</code></td><td>A new invoice was generated.</td></tr>
			<tr><td><code>invoice.paid</code></td><td>An invoice was paid successfully.</td></tr>
		</tbody>
	</table>

	<div class="next-steps">
		<strong>Next steps</strong>
		<ul>
			<li><a href="/docs/payment-methods">Payment Methods API</a></li>
			<li><a href="/docs/webhooks">Webhooks</a></li>
		</ul>
	</div>
</div>
