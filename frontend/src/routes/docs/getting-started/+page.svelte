<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Quickstart | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Quickstart</h1>
	<p class="lead">Get from zero to your first payment in under 10 minutes.</p>

	<h2>1. Create an account</h2>
	<p>Sign up at <a href="/login?register=true">drizlepay.com</a> and verify your email. Once logged in, you'll land on your dashboard where you can find your API keys.</p>

	<h2>2. Get your API keys</h2>
	<p>Navigate to <strong>Settings → API Keys</strong> in your dashboard. You'll find two keys:</p>
	<ul>
		<li><strong>Publishable key</strong> — used in client-side code (safe to expose)</li>
		<li><strong>Secret key</strong> — used server-side. Never expose this in client-side code.</li>
	</ul>
	<p>By default, keys are in test mode. Switch to live mode when you're ready to process real payments.</p>

	<h2>3. Make your first API call</h2>
	<p>Use your secret key to authenticate:</p>
	<CodeBlock
		response={`&#123;
  "id": "dp_pay_abc123",
  "object": "payment",
  "amount": 5000,
  "currency": "AED",
  "status": "succeeded",
  "created": 1719500000
&#125;`}
		examples={{
			curl: `curl https://api.drizlepay.com/v1/payments \
  -H "Authorization: Bearer sk_test_YOUR_TEST_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "amount": 5000,
    "currency": "AED",
    "payment_method": "card",
    "description": "First payment"
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/payments",
    headers={
        "Authorization": "Bearer sk_test_YOUR_TEST_KEY",
        "Content-Type": "application/json"
    },
    json={
        "amount": 5000,
        "currency": "AED",
        "payment_method": "card",
        "description": "First payment"
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/payments", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_test_YOUR_TEST_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    amount: 5000,
    currency: "AED",
    payment_method: "card",
    description: "First payment"
  })
});
const payment = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/payments', [
    'headers' => [
        'Authorization' => 'Bearer sk_test_YOUR_TEST_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'amount' => 5000,
        'currency' => 'AED',
        'payment_method' => 'card',
        'description' => 'First payment',
    ],
]);
echo $response->getBody();`,
		}}
	/>

	<h2>4. Handle the response</h2>
	<p>A successful response returns the payment object with a <code>succeeded</code> status.</p>

	<h2>5. Listen for webhooks</h2>
	<p>Set up a webhook endpoint to receive real-time payment events. See the <a href="/docs/webhooks">Webhooks guide</a> for details.</p>

	<div class="next-steps">
		<strong>Next steps</strong>
		<ul>
			<li><a href="/docs/authentication">Learn more about authentication</a></li>
			<li><a href="/docs/payments">Explore the Payments API</a></li>
			<li><a href="/docs/webhooks">Set up webhooks</a></li>
		</ul>
	</div>
</div>
