<script>
	import '../docs.css';
</script>

<svelte:head>
	<title>Reporting API | DrizlePay</title>
</svelte:head>

<div class="ref">
	<h1>Reporting API</h1>
<p class="lead">The Reporting API lets you generate and download reports about your Drizle Pay account activity.</p>

<h2>The ReportRun Object</h2>
<pre class="cb-code">&#123;
  "id": "dp_rr_001234",
  "object": "report_run",
  "report_type": "balance_summary",
  "status": "succeeded",
  "parameters": &#123;
    "interval_start": 1719500000,
    "interval_end": 1722180000
  &#125;,
  "result": &#123;
    "url": "https://files.drizlepay.com/reports/report_001234.csv"
  &#125;,
  "created": 1719500000
&#125;</pre>

<h2>Endpoints</h2>

<h3>Create a report run</h3>
<div class="endpoint"><span class="method post">POST</span> <span class="path">/v1/reporting/report_runs</span></div>

<h3>Retrieve a report run</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/reporting/report_runs/:id</span></div>

<h3>List report runs</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/reporting/report_runs</span></div>

<h3>List report types</h3>
<div class="endpoint"><span class="method get">GET</span> <span class="path">/v1/reporting/report_types</span></div>

<h2>Report Types</h2>
<table class="params">
<thead><tr><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>balance_summary</code></td><td>Account balance over time.</td></tr>
<tr><td><code>payment_summary</code></td><td>Payment volume and status breakdown.</td></tr>
<tr><td><code>payout_summary</code></td><td>Payout history and details.</td></tr>
<tr><td><code>settlement_summary</code></td><td>Settlement details.</td></tr>
</tbody>
</table>

<div class="next-steps">
<strong>Next steps</strong>
<ul>
<li><a href="/docs/balance">Balance API</a></li>
<li><a href="/docs/payouts">Payouts</a></li>
</ul>
</div>
</div>
