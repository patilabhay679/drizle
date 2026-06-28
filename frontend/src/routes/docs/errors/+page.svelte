<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Error Codes | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Error Codes</h1>
	<p class="lead">The Drizle Pay API uses standard HTTP response codes to indicate success or failure. Errors return a JSON object with details.</p>

	<h2>HTTP Status Codes</h2>
	<table class="params">
		<thead>
			<tr><th>Code</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>200</code></td><td>Success — the request was processed successfully.</td></tr>
			<tr><td><code>400</code></td><td>Bad Request — invalid parameters or malformed request.</td></tr>
			<tr><td><code>401</code></td><td>Unauthorized — missing or invalid API key.</td></tr>
			<tr><td><code>404</code></td><td>Not Found — the requested resource doesn't exist.</td></tr>
			<tr><td><code>409</code></td><td>Conflict — duplicate resource (e.g., email already registered).</td></tr>
			<tr><td><code>422</code></td><td>Unprocessable Entity — validation failed.</td></tr>
			<tr><td><code>429</code></td><td>Rate Limited — too many requests. Retry after the time specified in the <code>Retry-After</code> header.</td></tr>
			<tr><td><code>500</code></td><td>Internal Server Error — something went wrong on our end. Try again later.</td></tr>
		</tbody>
	</table>

	<h2>Error Response Format</h2>
	<pre class="cb-code">&#123;
  "error": &#123;
    "type": "invalid_request_error",
    "code": "invalid_amount",
    "message": "Amount must be at least 100 (AED 1.00)",
    "param": "amount",
    "status": 400
  &#125;
&#125;</pre>

	<h2>Error Types</h2>
	<table class="params">
		<thead>
			<tr><th>Type</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>invalid_request_error</code></td><td>Request parameters are invalid or missing.</td></tr>
			<tr><td><code>authentication_error</code></td><td>API key is missing, invalid, or expired.</td></tr>
			<tr><td><code>rate_limit_error</code></td><td>Too many requests hit the API too quickly.</td></tr>
			<tr><td><code>api_error</code></td><td>Server-side error. Retry the request.</td></tr>
			<tr><td><code>processing_error</code></td><td>Payment processing failed (e.g., card declined).</td></tr>
		</tbody>
	</table>

	<h2>Common Error Codes</h2>
	<table class="params">
		<thead>
			<tr><th>Code</th><th>Meaning</th></tr>
		</thead>
		<tbody>
			<tr><td><code>invalid_amount</code></td><td>The transaction amount is invalid (below minimum or exceeds limits).</td></tr>
			<tr><td><code>invalid_currency</code></td><td>The specified currency is not supported.</td></tr>
			<tr><td><code>card_declined</code></td><td>The card was declined by the issuer.</td></tr>
			<tr><td><code>expired_card</code></td><td>The card has expired.</td></tr>
			<tr><td><code>insufficient_funds</code></td><td>The card has insufficient funds.</td></tr>
			<tr><td><code>requires_3ds</code></td><td>3D Secure authentication is required.</td></tr>
			<tr><td><code>duplicate_transaction</code></td><td>A transaction with the same idempotency key already exists.</td></tr>
			<tr><td><code>rate_limit_exceeded</code></td><td>API rate limit exceeded. Slow down requests.</td></tr>
		</tbody>
	</table>

	<h2>Rate Limiting</h2>
	<p>The API allows up to 1,000 requests per minute per secret key. Exceeding this returns a <code>429</code> status. Include the <code>Retry-After</code> header value in your retry logic.</p>
</div>


