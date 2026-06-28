<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Identity API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Identity API</h1>
<p class="lead">The Identity API verifies user identities using government-issued ID documents and selfie videos. Prevent fraud and comply with KYC regulations.</p>

<h2>The VerificationSession Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_vs_001234",
  "object": "verification_session",
  "status": "verified",
  "type": "document",
  "client_secret": "vs_abc123_secret_xyz789",
  "last_error": null,
  "verified_details": &#123;
    "first_name": "Ahmed",
    "last_name": "Al Maktoum",
    "dob": "1990-01-15"
  &#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a verification session</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/identity/verification_sessions</span></div>

<h3>Retrieve a verification session</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/identity/verification_sessions/:id</span></div>

<h3>Update a verification session</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/identity/verification_sessions/:id</span></div>

<h3>List verification sessions</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/identity/verification_sessions</span></div>

<h3>Cancel a verification session</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/identity/verification_sessions/:id/cancel</span></div>

<h3>Redact a verification session</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/identity/verification_sessions/:id/redact</span></div>

<h2>Verification Statuses</h2>
<table class="params">
<thead><tr><th>Status</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>processing</code></td><td>Verification is in progress.</td></tr>
<tr><td><code>verified</code></td><td>Identity was verified successfully.</td></tr>
<tr><td><code>failed</code></td><td>Verification failed.</td></tr>
<tr><td><code>canceled</code></td><td>Session was canceled.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/customers">Customers API</a></li>
<li><a href="/docs/accounts">Accounts API</a></li>
</ul>
</div>
</div>
