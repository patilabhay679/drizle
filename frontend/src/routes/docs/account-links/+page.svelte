<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Account Links API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Account Links API</h1>
<p class="lead">The <code>AccountLink</code> object creates a single-use URL for your platform to redirect connected accounts to complete onboarding.</p>

<h2>The AccountLink Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_al_001234",
  "object": "account_link",
  "account": "dp_acct_001234",
  "url": "https://connect.drizlepay.com/onboard/abc123",
  "type": "account_onboarding",
  "created": 1719500000,
  "expires_at": 1719503600
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create an account link</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/account_links</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>account</code></td><td>string</td><td>Required. Account ID to onboard.</td></tr>
<tr><td><code>type</code></td><td>string</td><td>Required. <code>account_onboarding</code> or <code>account_update</code>.</td></tr>
<tr><td><code>return_url</code></td><td>string</td><td>Optional. URL to redirect after completion.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/accounts">Accounts API</a></li>
<li><a href="/docs/capabilities">Capabilities</a></li>
</ul>
</div>
</div>
