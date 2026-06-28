<script>
	import './docs.css';
	import CodeBlock from '$lib/components/CodeBlock.svelte';
</script>

<svelte:head>
	<title>API Reference | DrizlePay</title>
	<meta name="description" content="Drizle Pay API reference. Build payment experiences with our REST API." />
</svelte:head>

<div class="ref">
	<h1>API Reference</h1>
	<p class="lead">The Drizle Pay API is organized around REST. It accepts JSON request bodies, returns JSON responses, and uses standard HTTP response codes, authentication, and verbs.</p>

	<h2>Base URL</h2>
	<div class="cb-code">https://api.drizlepay.com/v1</div>

	<h2>Authentication</h2>
	<p>Authenticate using a secret API key via the <code>Authorization</code> header:</p>
	<div class="cb-code">Authorization: Bearer sk_live_YOUR_SECRET_KEY</div>
	<p>Get your API keys from the <a href="/login">dashboard</a>. Use test keys (prefixed with <code>sk_test</code>) for development.</p>

	<h2>Making a Request</h2>
	<CodeBlock examples={{
		curl: `curl -X POST https://api.drizlepay.com/v1/payments \\
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{&#123;
    "amount": 5000,
    "currency": "AED",
    "payment_method": "card",
    "description": "Test payment",
    "customer": &#123;
      "email": "customer@example.com"
    &#125;
  &#125;}'`,
		python: `import drizlepay

drizlepay.api_key = "sk_live_YOUR_SECRET_KEY"

payment = drizlepay.Payment.create(
    amount=5000,
    currency="AED",
    payment_method="card",
    description="Test payment",
    customer={&#123;"email": "customer@example.com"&#125;},
)`,
		js: `import DrizlePay from 'drizlepay';

const dp = new DrizlePay('sk_live_YOUR_SECRET_KEY');

const payment = await dp.payments.create({
  amount: 5000,
  currency: 'AED',
  payment_method: 'card',
  description: 'Test payment',
  customer: { email: 'customer@example.com' },
});`,
		php: `require 'vendor/autoload.php';

$dp = new \\DrizlePay\\DrizlePay('sk_live_YOUR_SECRET_KEY');

$payment = $dp->payments->create([
  'amount' => 5000,
  'currency' => 'AED',
  'payment_method' => 'card',
  'description' => 'Test payment',
  'customer' => ['email' => 'customer@example.com'],
]);`,
	}} />

	<h2>Response Format</h2>
	<p>All responses are JSON. Successful requests return a 2xx status. Errors return a relevant 4xx or 5xx status with an error object.</p>
	<pre class="cb-code">&#123;
  "id": "dp_pay_abc123",
  "object": "payment",
  "amount": 5000,
  "currency": "AED",
  "status": "succeeded",
  "created": 1719500000,
  "customer": "dp_cus_xyz789",
  "description": "Test payment"
&#125;</pre>

	<h2>Pagination</h2>
	<p>List endpoints return paginated results. Use <code>page</code> and <code>limit</code> parameters:</p>
	<pre class="cb-code">GET /v1/payments?page=1&limit=20

&#123;
  "data": [ ... ],
  "total": 142,
  "page": 1,
  "limit": 20
&#125;</pre>

	<div class="card quick-links">
		<h3>Explore the API</h3>
		<div class="link-grid">
			<a href="/docs/getting-started" class="link-card">
				<strong>Quickstart</strong>
				<span>Integrate in minutes</span>
			</a>
			<a href="/docs/authentication" class="link-card">
				<strong>Authentication</strong>
				<span>API keys & security</span>
			</a>
			<a href="/docs/payments" class="link-card">
				<strong>Payments</strong>
				<span>Accept payments</span>
			</a>
			<a href="/docs/customers" class="link-card">
				<strong>Customers</strong>
				<span>Manage customers</span>
			</a>
		</div>
	</div>
</div>

<style>
	.card.quick-links {
		margin-top: 40px;
		padding: 28px 24px;
		border: 1px solid var(--line);
		border-radius: 8px;
		background: #f8fafc;
	}
	.card h3 { font-size: 18px; font-weight: 700; color: var(--hero-bg); margin: 0 0 16px; }
	.link-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
	.link-card {
		padding: 16px;
		border: 1px solid var(--line);
		border-radius: 6px;
		background: #fff;
		text-decoration: none;
		transition: all 0.15s;
	}
	.link-card:hover { border-color: var(--primary); box-shadow: 0 2px 8px rgba(2,195,102,0.08); }
	.link-card strong { display: block; font-size: 15px; font-weight: 600; color: var(--hero-bg); margin-bottom: 4px; }
	.link-card span { font-size: 13px; color: var(--muted); }
	@media (max-width: 680px) {
		.link-grid { grid-template-columns: 1fr; }
	}
</style>
