<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Webhook Endpoints API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Webhook Endpoints API</h1>
	<p class="lead">Register and manage webhook endpoints programmatically. Each endpoint defines a URL that receives event notifications.</p>

	<h2>The WebhookEndpoint Object</h2>
	<pre class="cb-code">&#123;
  "id": "dp_we_789xyz",
  "object": "webhook_endpoint",
  "url": "https://example.com/webhooks",
  "status": "active",
  "events": [
    "payment.succeeded",
    "payment.failed"
  ],
  "secret": "whsec_••••••••••••",
  "created": 1719500000
&#125;</pre>

	<h2>Endpoints</h2>

	<h3>Create a webhook endpoint</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/webhook_endpoints</span></div>
	<CodeBlock
		response={`&#123;
  "id": "dp_we_789xyz",
  "object": "webhook_endpoint",
  "url": "https://example.com/webhooks",
  "status": "active",
  "events": ["payment.succeeded", "payment.failed"],
  "created": 1719500000
&#125;`}
		examples={{
			curl: `curl -X POST https://api.drizlepay.com/v1/webhook_endpoints \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{&#123;
    "url": "https://example.com/webhooks",
    "events": ["payment.succeeded", "payment.failed"],
    "description": "Production webhook"
  &#125;}'`,
			python: `import requests

response = requests.post(
    "https://api.drizlepay.com/v1/webhook_endpoints",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
        "Content-Type": "application/json"
    },
    json={
        "url": "https://example.com/webhooks",
        "events": ["payment.succeeded", "payment.failed"],
        "description": "Production webhook"
    }
)
print(response.json())`,
			js: `const response = await fetch("https://api.drizlepay.com/v1/webhook_endpoints", {
  method: "POST",
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    url: "https://example.com/webhooks",
    events: ["payment.succeeded", "payment.failed"],
    description: "Production webhook"
  })
});
const endpoint = await response.json();`,
			php: `$client = new GuzzleHttp\\Client();
$response = $client->post('https://api.drizlepay.com/v1/webhook_endpoints', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
        'Content-Type' => 'application/json',
    ],
    'json' => [
        'url' => 'https://example.com/webhooks',
        'events' => ['payment.succeeded', 'payment.failed'],
        'description' => 'Production webhook',
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
			<tr><td><code>url</code></td><td>string</td><td>Required. HTTPS endpoint URL.</td></tr>
			<tr><td><code>events</code></td><td>array</td><td>Required. List of event types to subscribe to.</td></tr>
			<tr><td><code>description</code></td><td>string</td><td>Optional. Max 255 characters.</td></tr>
			<tr><td><code>metadata</code></td><td>object</td><td>Optional. Up to 20 key-value pairs.</td></tr>
		</tbody>
	</table>

	<h3>List webhook endpoints</h3>
	<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/webhook_endpoints</span></div>
	<pre class="cb-code">curl https://api.drizlepay.com/v1/webhook_endpoints \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h3>Update a webhook endpoint</h3>
	<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/webhook_endpoints/:id</span></div>
	<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/webhook_endpoints/dp_we_789xyz \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '&#123;
    "events": ["payment.succeeded", "payment.failed", "refund.succeeded"]
  &#125;'</pre>

	<h3>Delete a webhook endpoint</h3>
	<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/webhook_endpoints/:id</span></div>
	<pre class="cb-code">curl -X DELETE https://api.drizlepay.com/v1/webhook_endpoints/dp_we_789xyz \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"</pre>

	<h2>Webhook Signatures</h2>
	<p>Each endpoint has a unique signing secret (<code>whsec_</code> prefix). Use it to verify that incoming webhooks are genuinely from Drizle Pay. See the <a href="/docs/webhooks">Webhooks guide</a> for verification code examples.</p>

	<div class="next-steps">
		<strong>Related guides</strong>
		<ul>
			<li><a href="/docs/webhooks">Webhooks overview & verification</a></li>
			<li><a href="/docs/errors">Error codes</a></li>
		</ul>
	</div>
</div>
