# Drizle Pay — Frontend

## Stack
- **SvelteKit 2** (Svelte 5 runes: `$state`, `$derived`, `$props`)
- **Vite 8** — dev server with `/api` proxy → `http://127.0.0.1:8000`
- **Static adapter** — builds to `../backend/build`
- **CSS** — Vanilla CSS with CSS custom properties (no framework)

## Setup

```bash
cd frontend
npm install
npm run dev   # → http://localhost:5173 (proxies /api to backend)
npm run build # → outputs to ../backend/build
```

## Project Structure

```
frontend/src/
├── app.html                   # SPA shell
├── routes/                    # File-based routing
│   ├── +layout.svelte         # Root layout (Header/Footer, landing.css)
│   ├── +layout.js             # ssr=false, prerender=false
│   ├── +page.svelte           # Landing page (uses 6 section components)
│   ├── landing.css            # Global marketing styles + CSS variables
│   ├── about/
│   ├── contact/               # Contact form → POST /api/v1/contact
│   ├── dashboard/             # Auth-guarded merchant dashboard
│   │   ├── +layout.svelte     # Sidebar, topbar, auth guard
│   │   ├── +page.svelte       # Overview stats + recent transactions
│   │   ├── transactions/      # Paginated transaction table
│   │   ├── payouts/           # Paginated payout table
│   │   └── settings/          # Editable profile, password, API keys
│   ├── docs/
│   │   ├── +layout.svelte     # Docs sidebar (9 groups, 49 items)
│   │   ├── +page.svelte       # Docs landing
│   │   ├── docs.css           # Docs-specific styles
│   │   └── getting-started/ ...  # 49 API reference pages
│   ├── login/                 # Sign in / Register
│   ├── forgot-password/
│   ├── reset-password/
│   ├── verify-email/
│   ├── pricing/
│   ├── privacy/
│   └── terms/
├── lib/
│   ├── api.js                 # HTTP client (auto JWT, 401 redirect)
│   ├── stores/auth.js         # Auth state (localStorage persist)
│   └── components/
│       ├── Header.svelte      # Sticky nav (marketing pages)
│       ├── Footer.svelte      # Site footer (all except dashboard)
│       ├── HeroSection.svelte
│       ├── CheckoutPreview.svelte
│       ├── FeatureGrid.svelte
│       ├── PaymentMethods.svelte
│       ├── DevSection.svelte
│       ├── CTASection.svelte
│       └── CodeBlock.svelte   # Multi-lang code viewer (docs)
```

## Routing & Layouts

```
Root (+layout.svelte)
├── Header — marketing pages only (not /docs, not /dashboard)
├── Footer — all pages except /dashboard
├── landing.css — global styles
│
├── / (home) — landing page sections
├── /about
├── /contact
├── /pricing
├── /privacy
├── /terms
├── /login
├── /forgot-password
├── /reset-password
├── /verify-email
│
├── /docs (+layout.svelte — sidebar + breadcrumbs)
│   └── 49 API reference pages (each: +page.js + +page.svelte)
│
└── /dashboard (+layout.svelte — auth guard, sidebar, topbar)
    ├── overview
    ├── transactions
    ├── payouts
    └── settings
```

The root layout conditionally shows `Header` (non-docs, non-dashboard) and `Footer` (non-dashboard). The docs layout has its own sidebar navigation. The dashboard layout has an app-style sidebar.

## Auth Flow

1. Login/Register → `POST /api/v1/auth/*` → JWT + merchant stored in `localStorage`
2. `api.js` auto-attaches `Authorization: Bearer` header
3. 401 response → auto-logout → redirect to `/login`
4. Dashboard layout redirects unauthenticated users to `/login`
5. Password reset: `/forgot-password` → `/reset-password?token=`

## State Management

- **Auth**: `$lib/stores/auth.js` — `$state()` runes, persisted to localStorage
- **No other stores** — UI state is local per-component with `$state()`

## API Client (`$lib/api.js`)

Single `api` export with methods for every backend endpoint:
```js
api.login(email, password)
api.register({ email, password, name, company })
api.contact({ name, email, company, phone, message })
api.getTransactions(page, limit)
api.updateMe({ name, company })
api.changePassword(current, new_password)
// ... etc
```

## CSS Conventions

- **Global**: `landing.css` — CSS custom properties (`:root`), reset, utility classes (`.btn`, `.container`, `.section-title`)
- **Component-scoped**: `<style>` blocks in each `.svelte` file
- **Docs-specific**: `docs/docs.css`
- **Breakpoints**: `980px` (tablet), `680px` (mobile) — standard across all pages
- No CSS framework — plain vanilla

## Key Conventions

- Every route directory has a `+page.svelte` (markup) and optionally `+page.js` (prerender config)
- All docs pages are prerendered (`export const prerender = true`)
- The marketing pages (home, about, pricing, etc.) don't import Header/Footer — they inherit from root layout
- Never use `import $lib/...` — always `'$lib/...'`
