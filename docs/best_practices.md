# Development Best Practices & Recommendations

While your current setup works, maintaining a separate `index.html` and copying it over is not standard practice and will slow you down as your application grows. Here is a breakdown of what to change, why, and how to do it.

---

## 1. Eliminate `index.html` (One Source of Truth)
**The Problem**: Editing a separate `index.html` requires a manual "sync" step: extracting CSS, copying markup, escaping curly braces (`{}`), and rebuilding. 
**The Recommendation**: Delete or archive `index.html`. Do all future HTML, CSS, and copy changes **directly in Svelte components**. Svelte allows you to write standard HTML and CSS inside `.svelte` files directly, but gives you native reactivity and component scoping.

---

## 2. Leverage SvelteKit’s Component Architecture
Currently, your entire landing page is a single, massive 150+ line HTML block inside `+page.svelte`. You should break it down into modular, reusable Svelte components.

### Recommended Directory Structure:
```text
frontend/src/
├── routes/
│   ├── +layout.svelte        <-- Global Layout (Header & Footer live here)
│   ├── +page.svelte          <-- Renders Hero, Features, Methods, Developers
│   └── pricing/
│       └── +page.svelte      <-- Inherits Header & Footer automatically
└── lib/
    └── components/
        ├── Hero.svelte
        ├── FeatureGrid.svelte
        ├── PaymentMethods.svelte
        └── CheckoutSimulator.svelte  <-- Interactive state-driven component
```

### Move Header & Footer to `+layout.svelte`
By putting layout-level elements in `+layout.svelte`, they wrap every page automatically. When you add a `/pricing` or `/login` page later, they will share the exact same header and footer without copy-pasting code.

---

## 3. Make the Checkout Card Dynamic (Interactive Svelte State)
Your landing page has a "Branded Checkout" preview card. Currently, clicking "Wallet", "BNPL", or "Bank" does nothing. With Svelte, you can make this interactive in just a few lines of code:

```svelte
<!-- Example inside CheckoutSimulator.svelte -->
<script>
  let activeTab = $state('Card'); // Reactive state
</script>

<div class="checkout-tabs">
  {#each ['Card', 'Wallet', 'BNPL', 'Bank'] as tab}
    <button 
      class:active={activeTab === tab} 
      onclick={() => activeTab = tab}
    >
      {tab}
    </button>
  {/each}
</div>

<div class="payment-box">
  {#if activeTab === 'Card'}
    <!-- Show Credit Card Fields -->
    <div class="card-input"><span>Card number</span><strong>4111 1111 1111 1111</strong></div>
  {:else if activeTab === 'Wallet'}
    <!-- Show Apple/Google Pay Buttons -->
    <button class="btn-wallet apple-pay">Pay with Apple Pay</button>
  {:else if activeTab === 'BNPL'}
    <!-- Show Tabby/Tamara Options -->
    <div class="bnpl-row">Installments with Tabby</div>
  {:else if activeTab === 'Bank'}
    <!-- Show Direct Debit Selector -->
    <div class="bank-row">SEPA Bank Transfer</div>
  {/if}
</div>
```

---

## 4. Reorganize Styling (Global vs Component Scopes)
- **Global Variables**: Keep custom properties (`:root` colors, spacing, fonts) inside a global file like `layout.css`.
- **Component Styles**: Put component-specific styles inside the `<style>` tag of that Svelte component. This keeps your styles isolated: Svelte automatically scopes them so classes on the landing page won't accidentally break styles on the billing dashboard.

---

## 5. Deployment separation (Vite/Static vs FastAPI)
Serving the compiled frontend directly from FastAPI (`backend/build`) is a solid, cost-effective choice for early-stage B2B SaaS. 
- **In Development**: Keeping them separate (Vite on `5173`, FastAPI on `8000`) is the correct practice. Vite's Hot Module Replacement (HMR) is extremely fast.
- **In Production**: As traffic grows, consider hosting the static SvelteKit files on a CDN (Vercel, Cloudflare, Netlify) and keeping FastAPI strictly as an API service.
