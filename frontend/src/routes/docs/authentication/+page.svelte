<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Authentication | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Authentication</h1>
	<p class="lead">The Drizle Pay API uses API keys to authenticate requests. You can manage your keys from the dashboard.</p>

	<h2>API Key Types</h2>
	<table class="params">
		<thead>
			<tr><th>Key Type</th><th>Prefix</th><th>Usage</th></tr>
		</thead>
		<tbody>
			<tr><td><strong>Secret Key</strong></td><td><code>sk_live_</code> / <code>sk_test_</code></td><td>Server-side. Never expose in client code.</td></tr>
			<tr><td><strong>Publishable Key</strong></td><td><code>pk_live_</code> / <code>pk_test_</code></td><td>Client-side. Safe to expose in frontend code.</td></tr>
		</tbody>
	</table>

	<h2>Authenticating Requests</h2>
	<p>Send your secret key as a Bearer token in the <code>Authorization</code> header:</p>
	<CodeBlock examples={{
		curl: `curl https://api.drizlepay.com/v1/payments \\
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY"`,
		python: `import requests

response = requests.get(
    "https://api.drizlepay.com/v1/payments",
    headers={
        "Authorization": "Bearer sk_live_YOUR_SECRET_KEY"
    }
)`,
		js: `const response = await fetch("https://api.drizlepay.com/v1/payments", {
  headers: {
    "Authorization": "Bearer sk_live_YOUR_SECRET_KEY"
  }
});`,
		php: `$client = new GuzzleHttp\\Client();
$response = $client->get('https://api.drizlepay.com/v1/payments', [
    'headers' => [
        'Authorization' => 'Bearer sk_live_YOUR_SECRET_KEY',
    ],
]);`,
	}} />
	<p>All API requests must be made over HTTPS. Calls made over plain HTTP will fail.</p>

	<h2>Test Mode vs Live Mode</h2>
	<p>Keys prefixed with <code>sk_test_</code> operate in test mode. No real money is moved. Use test card numbers to simulate various scenarios:</p>
	<table class="params">
		<thead>
			<tr><th>Card Number</th><th>Scenario</th></tr>
		</thead>
		<tbody>
			<tr><td><code class="mono">4111 1111 1111 1111</code></td><td>Success</td></tr>
			<tr><td><code class="mono">4000 0000 0000 0002</code></td><td>Declined</td></tr>
			<tr><td><code class="mono">4000 0025 0000 3155</code></td><td>Requires 3D Secure</td></tr>
		</tbody>
	</table>

	<h2>Key Security</h2>
	<ul>
		<li>Never share your secret key or commit it to version control.</li>
		<li>Use environment variables to store keys in production.</li>
		<li>Rotate keys periodically from the dashboard.</li>
		<li>Use separate keys for development and production.</li>
	</ul>
</div>
