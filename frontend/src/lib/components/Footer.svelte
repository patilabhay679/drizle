<footer>
	<div class="container footer-grid">
		<div>© 2026 Drizle Pay. All rights reserved.</div>
		<div>
			<a href="/pricing">Pricing</a> &nbsp;·&nbsp;
			<a href="/docs">Developers</a> &nbsp;·&nbsp;
			<a href="/contact">Contact Sales</a> &nbsp;·&nbsp;
			<a href="/support">Support</a> &nbsp;·&nbsp;
			<a href="/privacy">Privacy</a> &nbsp;·&nbsp;
			<a href="/terms">Terms</a>
		</div>
	</div>
</footer>

<style>
	footer {
		padding: 48px 0;
		background: var(--hero-bg);
		color: var(--hero-muted);
		font-size: 14px;
		border-top: 1px solid rgba(255, 255, 255, 0.1);
	}
	.footer-grid {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 20px;
		flex-wrap: wrap;
	}
	footer a {
		color: var(--hero-muted);
		transition: color 0.2s;
	}
	footer a:hover { color: var(--primary); }
	@media (max-width: 680px) {
		.footer-grid { flex-direction: column; align-items: flex-start; }
	}
</style>
