<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Persons API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Persons API</h1>
<p class="lead">The <code>Person</code> object represents an individual associated with a connected account (directors, owners, executives).</p>

<h2>The Person Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_person_001234",
  "object": "person",
  "account": "dp_acct_001234",
  "first_name": "Ahmed",
  "last_name": "Al Maktoum",
  "email": "ahmed@example.com",
  "relationship": &#123;
    "director": true,
    "owner": true,
    "percent_ownership": 100
  &#125;,
  "verification": &#123;
    "status": "verified"
  &#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a person</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts/:account_id/persons</span></div>

<h3>Retrieve a person</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts/:account_id/persons/:id</span></div>

<h3>Update a person</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/accounts/:account_id/persons/:id</span></div>

<h3>List persons</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/accounts/:account_id/persons</span></div>

<h3>Delete a person</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/accounts/:account_id/persons/:id</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/accounts">Accounts API</a></li>
<li><a href="/docs/capabilities">Capabilities</a></li>
</ul>
</div>
</div>
