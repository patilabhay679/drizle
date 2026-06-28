<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>API Versioning | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>API Versioning</h1>
	<p class="lead">The Drizle Pay API is versioned. When we make backwards-incompatible changes, we release a new version. You can choose which version to use.</p>

<h2>Current Version</h2>
<p>The current API version is <code>2025-03-01</code>. All requests use this version by default unless you specify otherwise.</p>

<h2>Specifying a Version</h2>
<p>Set the API version via the <code>DrizlePay-Version</code> header:</p>
<div class="endpoint"><span class="method get">HEADER</span> <span class="path">DrizlePay-Version: 2024-06-01</span></div>
<pre class="cb-code">curl https://api.drizlepay.com/v1/payments \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -H "DrizlePay-Version: 2024-06-01"</pre>

<h2>Version History</h2>
<table class="params">
<thead><tr><th>Version</th><th>Release Date</th><th>Changes</th></tr></thead>
<tbody>
<tr><td><code>2025-03-01</code></td><td>March 2025</td><td>Latest. Added BNPL support, improved webhook signatures.</td></tr>
<tr><td><code>2024-06-01</code></td><td>June 2024</td><td>Added idempotency, expanded customer objects.</td></tr>
<tr><td><code>2024-01-01</code></td><td>January 2024</td><td>Initial GA release.</td></tr>
</tbody>
</table>

<h2>Upgrading</h2>
<p>We recommend pinning to a specific version in production. Test new versions in your sandbox before upgrading. See our <a href="/docs/changelog">changelog</a> for detailed migration guides.</p>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/authentication">Authentication</a></li>
<li><a href="/docs/errors">Error codes</a></li>
</ul>
</div>

</div>
