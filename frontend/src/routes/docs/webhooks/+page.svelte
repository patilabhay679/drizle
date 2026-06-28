<script>
	import '../docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>Webhooks | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Webhooks</h1>
	<p class="lead">Webhooks provide real-time notifications when events happen in your Drizle Pay account. Set up an endpoint to receive them and keep your systems in sync.</p>

	<h2>How It Works</h2>
	<ol>
		<li>You register a webhook endpoint URL in your dashboard.</li>
		<li>When an event occurs (e.g., a payment succeeds), Drizle Pay sends an HTTP POST to your endpoint.</li>
		<li>Your server acknowledges receipt with a <code>200 OK</code> response.</li>
	</ol>

	<h2>Event Payload</h2>
	<pre class="cb-code">&#123;
  "id": "evt_001234",
  "object": "event",
  "type": "payment.succeeded",
  "created": 1719500000,
  "data": &#123;
    "object": &#123;
      "id": "dp_pay_abc123",
      "amount": 5000,
      "currency": "AED",
      "status": "succeeded",
      "customer": "dp_cus_xyz789"
    &#125;
  &#125;
&#125;</pre>

	<h2>Event Types</h2>
	<table class="params">
		<thead>
			<tr><th>Event Type</th><th>Description</th></tr>
		</thead>
		<tbody>
			<tr><td><code>payment.succeeded</code></td><td>A payment completed successfully.</td></tr>
			<tr><td><code>payment.failed</code></td><td>A payment attempt failed.</td></tr>
			<tr><td><code>payment.refunded</code></td><td>A payment was refunded.</td></tr>
			<tr><td><code>customer.created</code></td><td>A new customer was created.</td></tr>
			<tr><td><code>subscription.created</code></td><td>A new subscription started.</td></tr>
			<tr><td><code>subscription.canceled</code></td><td>A subscription was canceled.</td></tr>
			<tr><td><code>subscription.past_due</code></td><td>Subscription payment is overdue.</td></tr>
			<tr><td><code>invoice.paid</code></td><td>An invoice was paid.</td></tr>
			<tr><td><code>invoice.created</code></td><td>A new invoice was generated.</td></tr>
			<tr><td><code>payout.paid</code></td><td>A payout completed.</td></tr>
			<tr><td><code>payout.failed</code></td><td>A payout failed.</td></tr>
		</tbody>
	</table>

	<h2>Verifying Webhook Signatures</h2>
	<p>Each webhook request includes a <code>Drizlepay-Signature</code> header. Use your webhook secret to verify the signature and confirm the request came from Drizle Pay:</p>
	<CodeBlock examples={{
		python: `import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)`,
		js: `import crypto from 'node:crypto';

function verifyWebhook(payload, signature, secret) {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(expected),
    Buffer.from(signature)
  );
}`,
		php: `function verify_webhook(string $payload, string $signature, string $secret): bool {
    $expected = hash_hmac('sha256', $payload, $secret);
    return hash_equals($expected, $signature);
}`,
	}} />

	<h2>Best Practices</h2>
	<ul>
		<li>Respond with <code>200 OK</code> as quickly as possible — process events asynchronously.</li>
		<li>Use idempotency keys to handle duplicate webhook deliveries.</li>
		<li>Verify the signature before processing any webhook event.</li>
		<li>Log webhook receipts for debugging.</li>
	</ul>

	<h2>Retry Policy</h2>
	<p>If your endpoint doesn't respond with <code>200 OK</code> within 5 seconds, Drizle Pay retries up to 3 times with exponential backoff (1 min, 5 min, 15 min). After all retries are exhausted, the event is marked as failed in your dashboard.</p>

	<div class="next-steps">
		<strong>Manage webhooks</strong>
		<p>Configure webhook endpoints in your <a href="/login">dashboard settings</a>. Manage them programmatically via the <a href="/docs/webhook-endpoints">Webhook Endpoints API</a>.</p>
	</div>
</div>
