<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Idempotency | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Idempotency</h1>
	<p class="lead">The Drizle Pay API supports idempotency for safely retrying requests without accidentally performing the same operation twice.</p>

	<h2>How It Works</h2>
	<p>Send a unique <code>Idempotency-Key</code> header with your request. If a network error occurs, you can retry the same request with the same key, and the API will return the result of the original request.</p>

	<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/payments \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 8a7b6c5d-4e3f-2a1b-0c9d-8e7f6a5b4c3d" \
  -d '&#123;
    "amount": 5000,
    "currency": "AED",
    "payment_method": "card"
  &#125;'</pre>

	<h2>Idempotency Key Format</h2>
	<p>Keys should be a UUID (v4) string. We also accept any string up to 255 characters. Each key is unique per secret key — different merchants with the same key won't conflict.</p>

	<h2>Expiration</h2>
	<p>Idempotency keys expire <strong>24 hours</strong> after the initial request. After expiration, the same key can be reused for a new request.</p>

	<table class="params">
		<thead>
			<tr><th>Scenario</th><th>Behavior</th></tr>
		</thead>
		<tbody>
			<tr><td>Same key, same request within 24h</td><td>Returns original response (safe to retry)</td></tr>
			<tr><td>Same key, different request within 24h</td><td>Returns <code>409 Conflict</code> error</td></tr>
			<tr><td>Same key after 24h</td><td>Treated as a new request</td></tr>
			<tr><td>No idempotency key</td><td>Request processed normally (may create duplicates on retry)</td></tr>
		</tbody>
	</table>

	<h2>Which Methods Support Idempotency?</h2>
	<p>All <code>POST</code> and <code>DELETE</code> requests support idempotency keys. <code>GET</code> requests are inherently idempotent and don't require a key.</p>

	<h2>Generating a Key</h2>
	<pre class="cb-code"># Python
import uuid
key = str(uuid.uuid4())

# JavaScript
const key = crypto.randomUUID();

# PHP
$key = uuid_create();

# Terminal
uuidgen</pre>

	<div class="next-steps">
		<strong>Related guides</strong>
		<ul>
			<li><a href="/docs/payments">Payments API</a></li>
			<li><a href="/docs/errors">Error codes</a></li>
		</ul>
	</div>
</div>
