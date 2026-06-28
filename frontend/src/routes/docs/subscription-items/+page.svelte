<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Subscription Items API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Subscription Items API</h1>
<p class="lead">The <code>SubscriptionItem</code> object represents a single price within a subscription. Use it to add multiple products to one subscription.</p>

<h2>The SubscriptionItem Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_si_001234",
  "object": "subscription_item",
  "subscription": "dp_sub_001234",
  "price": "dp_price_001234",
  "quantity": 1,
  "metadata": &#123;&#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a subscription item</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/subscription_items</span></div>

<h3>Retrieve a subscription item</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/subscription_items/:id</span></div>

<h3>Update a subscription item</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/subscription_items/:id</span></div>

<h3>List subscription items</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/subscription_items</span></div>

<h3>Delete a subscription item</h3>
<div class="endpoint"><span class="method delete">DELETE</span> <span class="path">/v1/subscription_items/:id</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/subscriptions">Subscriptions API</a></li>
<li><a href="/docs/prices">Prices API</a></li>
</ul>
</div>
</div>
