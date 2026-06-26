# Project Status: Drizle Pay

## Environment & OS
- **OS**: macOS
- **Node.js**: `v22.18.0`
- **Python**: `3.13.7`
- **Git status**: The local branch `main` and `origin/main` have diverged (each has 1 different commit).
  - Local commit: `958d045bbe71ad68fec0f6d431f701b45e736433` ("project kickoff")
  - Origin commit: `c1997a66c45ed4fc806200437d485532facfb741` ("Initial commit")

---

## Workspace Structure

The project is split into two major parts: [backend](file:///Users/abhay/Desktop/drizle/backend) and [frontend](file:///Users/abhay/Desktop/drizle/frontend).

### 1. [Backend](file:///Users/abhay/Desktop/drizle/backend)
- **[app.py](file:///Users/abhay/Desktop/drizle/backend/app.py)**: A Flask server configured to serve `src/index.html` on various paths: `/`, `/core/`, `/kernel/`, `/engine/`.
- **[vir_env.txt](file:///Users/abhay/Desktop/drizle/backend/vir_env.txt)**: Python package list (Flask 3.1.3, requests, etc.).
- **[next steps.txt](file:///Users/abhay/Desktop/drizle/backend/next%20steps.txt)**: Integration details for OpenRouter and `Qwen3-VL-235B-A22B-Instruct` model APIs.

### 2. [Frontend](file:///Users/abhay/Desktop/drizle/frontend)
- **SvelteKit App**: Standard SvelteKit structure configured with `@sveltejs/adapter-static` in [vite.config.js](file:///Users/abhay/Desktop/drizle/frontend/vite.config.js).
- **[src/index.html](file:///Users/abhay/Desktop/drizle/frontend/src/index.html)**: The static HTML landing page for **Drizle Pay**. Currently sits inside the `src/` directory, but is not integrated as a Svelte route or component yet.

---

## Critical Issues & Observations

1. **Flask Endpoint Overwrites**: In [backend/app.py](file:///Users/abhay/Desktop/drizle/backend/app.py#L11-L24), multiple routes (`/core/`, `/kernel/`, `/engine/`) use the same function name:
   ```python
   def serve_index():
   ```
   This will raise an `AssertionError: View function mapping is overwriting an existing endpoint function: serve_index` on Flask startup.
2. **Missing `src/index.html` for Flask**: The Flask app uses `send_file('src/index.html')`, but there is no `src/index.html` in the `backend/` directory. The file was moved to [frontend/src/index.html](file:///Users/abhay/Desktop/drizle/frontend/src/index.html).
3. **Port 80 Bindings**: Flask is configured to run on port 80 (`port=80` in [app.py](file:///Users/abhay/Desktop/drizle/backend/app.py#L30)), which requires administrator (`sudo`) privileges on macOS.
4. **SvelteKit Landing Page Integration**: SvelteKit does not serve static HTML files from `src/index.html` on `/` routing. The landing page needs to be moved to [src/routes/+page.svelte](file:///Users/abhay/Desktop/drizle/frontend/src/routes/+page.svelte) or served as a static asset.
