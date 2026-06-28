<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Subscription Schedules API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Subscription Schedules API</h1>
<p class="lead">The <code>SubscriptionSchedule</code> object allows you to plan and manage a series of changes to a subscription over time.</p>

<h2>The SubscriptionSchedule Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_ss_001234",
  "object": "subscription_schedule",
  "subscription": "dp_sub_001234",
  "status": "active",
  "phases": [
    &#123;
      "start_date": 1719500000,
      "end_date": 1722180000,
      "items": [&#123;"price": "dp_price_001234", "quantity": 1&#125;]
    &#125;
  ],
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a schedule</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/subscription_schedules</span></div>

<h3>Retrieve a schedule</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/subscription_schedules/:id</span></div>

<h3>Update a schedule</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/subscription_schedules/:id</span></div>

<h3>List schedules</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/subscription_schedules</span></div>

<h3>Cancel a schedule</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/subscription_schedules/:id/cancel</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/subscriptions">Subscriptions API</a></li>
<li><a href="/docs/invoices">Invoices API</a></li>
</ul>
</div>
</div>
