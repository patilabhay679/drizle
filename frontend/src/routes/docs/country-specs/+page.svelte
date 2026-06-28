<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Country Specs API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Country Specs API</h1>
<p class="lead">The <code>CountrySpec</code> object describes the requirements for creating accounts in a specific country.</p>

<h2>The CountrySpec Object</h2>
<pre class="cb-code">&#123;
  "id": "AE",
  "object": "country_spec",
  "default_currency": "AED",
  "supported_bank_account_currencies": &#123;
    "AED": ["bank_account"]
  &#125;,
  "supported_payment_currencies": ["AED", "USD"],
  "supported_payment_methods": ["card", "apple_pay"],
  "verification_fields": &#123;
    "individual": &#123;
      "minimum": ["legal_entity.first_name", "legal_entity.last_name"],
      "additional": ["legal_entity.dob"]
    &#125;
  &#125;
&#125;</pre>

<h2>Endpoints</h2>

<h3>Retrieve a country spec</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/country_specs/:id</span></div>

<h3>List country specs</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/country_specs</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/accounts">Accounts API</a></li>
<li><a href="/docs/external-accounts">External Accounts</a></li>
</ul>
</div>
</div>
