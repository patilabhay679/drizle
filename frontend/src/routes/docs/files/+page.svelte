<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Files API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Files API</h1>
	<p class="lead">The <code>File</code> object represents an uploaded file (dispute evidence, identity documents, etc.). Upload files directly to Drizle Pay.</p>

<h2>The File Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_file_001234",
  "object": "file",
  "purpose": "dispute_evidence",
  "filename": "receipt.pdf",
  "type": "pdf",
  "size": 245760,
  "created": 1719500000,
  "links": []
&#125;</pre>

<h2>Endpoints</h2>

<h3>Upload a file</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/files</span></div>
<pre class="cb-code">curl -X POST https://api.drizlepay.com/v1/files \
  -H "Authorization: Bearer sk_live_YOUR_SECRET_KEY" \
  -F "purpose=dispute_evidence" \
  -F "file=@/path/to/receipt.pdf"</pre>

<h3>Retrieve a file</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/files/:id</span></div>

<h3>List files</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/files</span></div>

<h2>File Purposes</h2>
<table class="params">
<thead><tr><th>Purpose</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>dispute_evidence</code></td><td>Evidence for a dispute submission.</td></tr>
<tr><td><code>identity_document</code></td><td>Identity verification document.</td></tr>
<tr><td><code>business_icon</code></td><td>Business logo or icon.</td></tr>
<tr><td><code>business_logo</code></td><td>Business logo for checkout.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/disputes">Disputes</a></li>
<li><a href="/docs/identity">Identity</a></li>
</ul>
</div>

</div>
