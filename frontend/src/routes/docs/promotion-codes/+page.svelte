<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Promotion Codes API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Promotion Codes API</h1>
<p class="lead">The <code>PromotionCode</code> object represents a redeemable code that maps to a coupon. Customers enter promotion codes at checkout.</p>

<h2>The PromotionCode Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_promo_001234",
  "object": "promotion_code",
  "code": "SUMMER20",
  "coupon": "dp_cpn_001234",
  "active": true,
  "max_redemptions": 100,
  "times_redeemed": 10,
  "expires_at": 1720000000,
  "first_time_transaction": false,
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a promotion code</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/promotion_codes</span></div>

<h3>Retrieve a promotion code</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/promotion_codes/:id</span></div>

<h3>Update a promotion code</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/promotion_codes/:id</span></div>

<h3>List promotion codes</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/promotion_codes</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/coupons">Coupons API</a></li>
<li><a href="/docs/subscriptions">Subscriptions</a></li>
</ul>
</div>
</div>
