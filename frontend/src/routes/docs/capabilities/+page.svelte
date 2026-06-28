<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Capabilities API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Capabilities API</h1>
<p class="lead">The <code>Capability</code> object represents a feature that a connected account can enable (e.g., card payments, transfers).</p>

<h2>The Capability Object</h2>
<pre class="cb-code">&#123;
  "id": "card_payments",
  "object": "capability",
  "account": "dp_acct_001234",
  "status": "active",
  "requirements": [],
  "settings": &#123;
    "requested": true
  &#125;
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve a capability</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts/:account_id/capabilities/:id</span></div>

<h3>Update a capability</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts/:account_id/capabilities/:id</span></div>

<h3>List capabilities</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts/:account_id/capabilities</span></div>

<h2>Capability Statuses</h2>
<table class="params">
<thead><tr><th>Status</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>active</code></td><td>Capability is enabled.</td></tr>
<tr><td><code>inactive</code></td><td>Capability is not enabled.</td></tr>
<tr><td><code>pending</code></td><td>Capability request is being reviewed.</td></tr>
<tr><td><code>unrequested</code></td><td>Capability has not been requested.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/accounts">Accounts API</a></li>
<li><a href="/docs/account-links">Account Links</a></li>
</ul>
</div>
</div>
