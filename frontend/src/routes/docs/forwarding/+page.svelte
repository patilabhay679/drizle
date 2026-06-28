<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Forwarding API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Forwarding API</h1>
<p class="lead">The Forwarding API allows you to forward API requests to your own servers for processing, enabling custom integrations and middleware.</p>

<h2>The ForwardingRequest Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_fwd_001234",
  "object": "forwarding_request",
  "url": "https://your-server.com/webhook-handler",
  "method": "POST",
  "headers": &#123;
    "Content-Type": "application/json"
  &#125;,
  "body": "&#123; \"event\": \"payment.succeeded\" &#125;",
  "status": "delivered",
  "response_code": 200,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a forwarding request</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/forwarding/requests</span></div>

<h3>List forwarding requests</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/forwarding/requests</span></div>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/webhooks">Webhooks</a></li>
<li><a href="/docs/webhook-endpoints">Webhook Endpoints</a></li>
</ul>
</div>
</div>
