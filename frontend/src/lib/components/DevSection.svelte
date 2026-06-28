<section id="developers">
	<div class="container split">
		<div>
			<h2 class="section-title">As a Platform, We Do All the Heavy Lifting.</h2>
			<p class="section-copy">Integrating with Drizle Pay means you remain PCI-DSS, PSD2, and GDPR/CCPA compliant without the engineering overhead. We actively stay up to date with global and local payment, data privacy, and tax regulations on your behalf.</p>
			<a class="btn primary" href="/docs">Read API Documentation</a>
		</div>
		<pre class="code"><code>POST /v1/checkout/sessions
&#123;
  "amount": 42000,
  "currency": "AED",
  "reference": "INV-10045",
  "customer": &#123;
    "email": "customer@example.com"
  &#125;,
  "features": &#123;
    "tax_calculation": true,
    "fraud_screening": true
  &#125;,
  "payment_methods": [
    "card", "apple_pay", "google_pay",
    "tabby", "tamara", "jaywan"
  ],
  "webhook_url": "https://merchant.example/webhooks"
&#125;</code></pre>
	</div>
</section>
