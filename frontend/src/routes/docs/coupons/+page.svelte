<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Coupons API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Coupons API</h1>
<p class="lead">The <code>Coupon</code> object represents a discount that can be applied to a subscription or invoice. Coupons can be percentage or fixed amount.</p>

<h2>The Coupon Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_cpn_001234",
  "object": "coupon",
  "name": "Summer Sale",
  "percent_off": 20,
  "amount_off": null,
  "currency": "AED",
  "duration": "repeating",
  "duration_in_months": 3,
  "max_redemptions": 1000,
  "redeem_by": 1720000000,
  "times_redeemed": 45,
  "valid": true,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a coupon</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/coupons</span></div>
<h4>Parameters</h4>
<table class="params">
<thead><tr><th>Param</th><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>name</code></td><td>string</td><td>Required. Coupon name.</td></tr>
<tr><td><code>percent_off</code></td><td>integer</td><td>Optional. Percentage discount (1-100).</td></tr>
<tr><td><code>amount_off</code></td><td>integer</td><td>Optional. Fixed amount discount.</td></tr>
<tr><td><code>currency</code></td><td>string</td><td>Required if amount_off set.</td></tr>
<tr><td><code>duration</code></td><td>string</td><td>Optional. <code>forever</code>, <code>once</code>, or <code>repeating</code>.</td></tr>
</tbody>
</table>

<h3>Retrieve a coupon</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/coupons/:id</span></div>

<h3>Update a coupon</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/coupons/:id</span></div>

<h3>List coupons</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/coupons</span></div>

<h3>Delete a coupon</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/coupons/:id</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/promotion-codes">Promotion Codes</a></li>
<li><a href="/docs/subscriptions">Subscriptions</a></li>
</ul>
</div>
</div>
