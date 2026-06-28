<script>
	let tab = $state('card');

	let cardNumber = $state('');
	let expiry = $state('');
	let cvc = $state('');
	let name = $state('');

	function onCardInput(e) {
		let v = e.target.value.replace(/\D/g, '').slice(0, 16);
		cardNumber = v.replace(/(\d{4})(?=\d)/g, '$1 ');
	}

	function onExpiryInput(e) {
		let v = e.target.value.replace(/\D/g, '').slice(0, 4);
		if (v.length >= 2) v = v.slice(0, 2) + ' / ' + v.slice(2);
		expiry = v;
	}

	function onCvcInput(e) {
		cvc = e.target.value.replace(/\D/g, '').slice(0, 3);
	}

	const scheme = $derived.by(() => {
		const n = cardNumber.replace(/\D/g, '');
		if (!n) return null;
		if (/^4/.test(n)) return 'visa';
		if (n[0] === '5' && (n.length === 1 || /^5[1-5]/.test(n))) return 'mastercard';
		if (/^2(2[2-7][1-9]|[3-6]\d{2}|7[0-1]\d|720)/.test(n)) return 'mastercard';
		if (/^3[47]/.test(n)) return 'amex';
		if (/^3(0[0-5]|[68]|9)/.test(n)) return 'diners';
		if (/^6395/.test(n)) return 'jaywan';
		return null;
	});
</script>

<aside class="hero-card checkout-card" aria-label="Modern checkout preview">
	<div class="checkout">
		<div class="checkout-top">
			<span class="checkout-badge">
				<svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M3 11h18" stroke="currentColor" stroke-width="1.5"/></svg>
				Branded Checkout
			</span>
			<span class="live-badge"><span class="live-dot"></span>Live</span>
		</div>
		<div class="checkout-merchant">
			<span class="merchant-avatar">D</span>
			<div><strong>Global SaaS Corp</strong><small>Order #DP-1042</small></div>
		</div>
		<div class="amount">AED 420.00</div>
		<div class="checkout-tabs" aria-label="Checkout payment options">
			<button class="checkout-tab" class:active={tab === 'card'} onclick={() => tab = 'card'}>Card</button>
			<button class="checkout-tab" class:active={tab === 'wallet'} onclick={() => tab = 'wallet'}>Wallet</button>
			<button class="checkout-tab" class:active={tab === 'bnpl'} onclick={() => tab = 'bnpl'}>BNPL</button>
			<button class="checkout-tab" class:active={tab === 'bank'} onclick={() => tab = 'bank'}>Bank</button>
		</div>
		<div class="payment-box">
			{#if tab === 'card'}
				<div class="payment-brands">
					<span class="card-brands-label">Accepted cards</span>
					<span class="card-brands" aria-label="Accepted card networks">
						<img src="/icons/visa.svg" alt="Visa" width="24" height="16" loading="lazy">
						<img src="/icons/mastercard.svg" alt="Mastercard" width="24" height="16" loading="lazy">
						<img src="/icons/amex.svg" alt="Amex" width="24" height="16" loading="lazy">
						<img src="/icons/diners.svg" alt="Diners" width="24" height="16" loading="lazy">
						<img src="/icons/jaywan.png" alt="Jaywan" width="24" height="12" loading="lazy" style="object-fit:contain;">
					</span>
				</div>
				<div class="card-field-group">
					<span class="field-label">Card number</span>
					<div class="card-input">
						<div class="card-number-row">
							<input class="card-input-field" value={cardNumber} oninput={onCardInput} placeholder="0000 0000 0000 0000" maxlength={19}>
							{#if scheme}
								<img src="/icons/{scheme}.svg" alt={scheme} width="24" height="16" loading="lazy">
							{/if}
						</div>
					</div>
				</div>
				<div class="checkout-row-group">
					<div class="inline-field">
						<span class="field-label-inline">Expiry</span>
						<div class="checkout-row"><input class="card-input-field field-right" value={expiry} oninput={onExpiryInput} placeholder="MM / YY" maxlength={7}></div>
					</div>
					<div class="inline-field">
						<span class="field-label-inline">CVV</span>
						<div class="checkout-row"><input class="card-input-field field-right" value={cvc} oninput={onCvcInput} placeholder="***" maxlength={3}></div>
					</div>
				</div>
				<div class="card-field-group">
					<span class="field-label">Name on card</span>
					<div class="card-input"><input class="card-input-field" value={name} oninput={(e) => name = e.target.value} placeholder="John Doe" maxlength={50}></div>
				</div>
			{:else if tab === 'wallet'}
				<div class="payment-methods-stack">
					<div class="payment-method-card"><span>Apple Pay</span></div>
					<div class="payment-method-card"><span>Google Pay</span></div>
					<div class="payment-method-card"><span>Samsung Pay</span></div>
				</div>
			{:else if tab === 'bnpl'}
				<div class="payment-methods-stack">
					<div class="payment-method-card">
						<img src="/icons/tabby.svg" alt="Tabby" height="36" loading="lazy" style="width:auto;">
					</div>
					<div class="payment-method-card">
						<img src="/icons/tamara.svg" alt="Tamara" height="36" loading="lazy" style="width:auto;">
					</div>
				</div>
			{:else if tab === 'bank'}
				<div class="payment-methods-stack">
					<div class="payment-method-card">
						<img src="/icons/aani.png" alt="Aani" height="36" loading="lazy" style="width:auto;">
					</div>
					<div class="payment-method-card">
						<img src="/icons/visa.svg" alt="Visa AFT" height="36" loading="lazy" style="width:auto;">
					</div>
				</div>
			{/if}
		</div>
		<a class="btn primary checkout-pay" href="/login?register=true">
			Complete Purchase
			<svg class="btn-arrow" width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path class="arrow-shaft" d="M0.5 5.5h7"/><path class="arrow-head" d="M1.5 1.5l4 4-4 4"/></svg>
		</a>
		<div class="secure-badge">
			<svg width="12" height="12" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2L4 5v6c0 5.25 3.15 10.13 8 11 4.85-.87 8-5.75 8-11V5l-8-3z" stroke="currentColor" stroke-width="1.5" fill="none"/><path d="M10 12.5l1.5 1.5 3-3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
			<span>Secured with end-to-end encryption</span>
		</div>
	</div>
</aside>
