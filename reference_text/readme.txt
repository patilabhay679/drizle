```
<welcome>Welcome back, Test HSBC</welcome>

<tabs>
  <tab active>Transactions</tab>
  <tab>Pay by link</tab>
</tabs>

<filters>
  <datepicker label="Date Range">01 Mar 2026 - 31 Mar 2026</datepicker>
  <button>Filters</button>
</filters>

<metrics>
  <card value="136.25 AED" change="-28.92% vs last period" label="Transaction amount" />
  <card value="35 transactions" change="+48.57% vs last period" label="Number of transactions" />
  <card value="3.89 AED" change="-50.67% vs last period" label="Average transactions" />
</metrics>

<chart type="line" title="Transaction Volume Over Time">
  <axis>1 Mar, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31</axis>
  <legend>Custom, Last period</legend>
</chart>

<chart type="pie" title="Top stores">
  <subtitle>Chart displays data for up to five selected stores</subtitle>
  <data label="Total">136.25 AED</data>
  <legend>TEST HSBC Geidea Payment LLC</legend>
</chart>

<chart type="bar" title="Top schemes">
  <subtitle>Chart displays data for up to five selected schemes</subtitle>
  <axis>Visa, Mastercard</axis>
</chart>

<sidebar-widget title="Recent payouts">
  <list>
    <item value="1.08 USD" date="26 Jun 2026" />
    <item value="0.99 AED" date="25 Jun 2026" status="Completed" />
    <item value="1.90 USD" date="25 Jun 2026" />
    <item value="2.00 AED" date="25 Jun 2026" status="Completed" />
  </list>
  <button>See more</button>
</sidebar-widget>

```

```
<filters>
  <datepicker label="Date Range">29 May 2026 - 27 Jun 2026</datepicker>
  <dropdown label="Reference type">Refer...</dropdown>
  <search placeholder="Search" />
  <button>Filters</button>
  <dropdown label="Export Action">Export</dropdown>
</filters>

<table title="Transactions List">
  <cols>Reference / Order ID, Date and time, Terminal ID, Scheme, Amount, Tags, Type, Card Class, Card Segment, Card Origin, Actions</cols>
  <row>#bc0ddc4...c8bcada, 26 Jun 2026 02:19 pm, Online E0000003, Mastercard, AED 2.39, , Purchase, N/A, N/A, Domestic</row>
  <row>#bc0ddc4...c8bcada, 26 Jun 2026 02:14 pm, Online E0000003, Mastercard, AED 2.39, , Refund, N/A, N/A, Domestic</row>
  <row>#494612...b7ddda1, 26 Jun 2026 01:24 pm, Online GP121015, Meeza/Jaywan, AED 1.00, , Purchase, N/A, N/A, Domestic</row>
  <row>#566dec...b7ddda1, 26 Jun 2026 01:00 pm, Online E0000003, Mastercard, AED 1.00, , Purchase, N/A, N/A, International</row>
  <row>#802a3b...b7ddda1, 25 Jun 2026 02:55 am, Online E0000003, Mastercard, USD 0.27, DCC, Purchase, N/A, N/A, International</row>
  <row>#d3a26f...b7ddda1, 25 Jun 2026 02:53 am, Online E0000003, Mastercard, USD 0.27, DCC, Purchase, N/A, N/A, International</row>
  <row>#12b2df...b7ddda1, 25 Jun 2026 02:00 am, Online E0000003, Mastercard, USD 0.27, DCC, Purchase, N/A, N/A, International</row>
  <row>#23a39f...c572c1, 25 Jun 2026 01:17 am, Online E0000003, Mastercard, USD 0.27, DCC, Purchase, N/A, N/A, International</row>
  <row>#fb7eae3...b7ddda1, 25 Jun 2026 01:11 am, Online E0000003, Mastercard, USD 0.27, DCC, Purchase, N/A, N/A, International</row>
  <row>#73489d...c572c1, 25 Jun 2026 00:57 am, Online E0000003, Mastercard, USD 0.27, DCC, Purchase, N/A, N/A, International</row>
</table>

<pagination>
  <summary>Show 10 of 85 transactions</summary>
  <page current>1</page>
  <page>2</page>
  <page>3</page>
  <page>4</page>
  <page>5</page>
  <separator>...</separator>
  <page>9</page>
</pagination>

```

```
<filters>
  <datepicker label="Date Range">29 May 2026 - 27 Jun 2026</datepicker>
  <dropdown label="Filter Type">Payo...</dropdown>
  <search placeholder="Search" />
  <button>Filters</button>
  <dropdown label="Export Action">Export</dropdown>
</filters>

<table title="Payouts List">
  <cols>Payout ID, Date and time, IBAN, Number of transactions, Net payout, Status</cols>
  <row>#3869190, 26 Jun 2026 12:00 am, AE770260001014273931915, 8, USD 1.08, </row>
  <row>#3848721, 25 Jun 2026 12:00 am, AE770260001014273931915, 1, AED 0.99, Completed</row>
  <row>#3848732, 25 Jun 2026 12:00 am, AE770260001014273931915, 7, USD 1.90, </row>
  <row>#3848733, 25 Jun 2026 12:00 am, AE770260001014273931915, 1, AED 2.00, Completed</row>
  <row>#3820865, 23 Jun 2026 12:00 am, AE770260001014273931915, 1, USD 0.27, </row>
  <row>#3821233, 23 Jun 2026 12:00 am, AE770260001014273931915, 1, AED 2.00, </row>
</table>

<pagination>
  <summary>Show 6 of 6 payouts</summary>
  <page current>1</page>
</pagination>

```