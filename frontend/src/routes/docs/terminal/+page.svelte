<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Terminal API | Drizle Pay</title>
</svelte:head>

<div class="ref">
	<h1>Terminal API</h1>
<p class="lead">The Terminal API lets you process in-person payments using Drizle Pay Terminal devices.</p>

<h2>The TerminalReader Object</h2>
<pre class="cb-code">&#123;
  "id": "tmr_001234",
  "object": "terminal.reader",
  "device_type": "bbpos_wisecube",
  "location": "tml_001234",
  "status": "online",
  "ip_address": "192.168.1.100",
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a terminal reader</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/terminal/readers</span></div>

<h3>Retrieve a reader</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/terminal/readers/:id</span></div>

<h3>List readers</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/terminal/readers</span></div>

<h3>Create a location</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/terminal/locations</span></div>

<h3>List locations</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/terminal/locations</span></div>

<h3>Process a payment</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/terminal/readers/:id/process_payment</span></div>

<h2>Device Types</h2>
<table class="params">
<thead><tr><th>Device</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>bbpos_wisecube</code></td><td>BBPOS WiseCube (smart terminal).</td></tr>
<tr><td><code>bbpos_chipper2x</code></td><td>BBPOS Chipper 2X (mobile reader).</td></tr>
<tr><td><code>stripe_m2</code></td><td>Stripe M2 (countertop).</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/payments">Payments API</a></li>
<li><a href="/docs/refunds">Refunds</a></li>
</ul>
</div>
</div>
