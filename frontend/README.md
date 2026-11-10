# Genysis POS: frontend

React + TypeScript + Vite app for the point-of-sale UI. It talks to the Frappe
backend over the REST API (`/api/method/*` and `/api/resource/*`).

```bash
cp .env.example .env    # point VITE_FRAPPE_URL at your bench (default http://localhost:8000)
npm install
npm run dev             # http://localhost:5173
```

In development, Vite proxies `/api`, `/assets` and `/files` to the bench, so
Frappe's session cookie works without CORS setup.

| Path | Purpose |
| --- | --- |
| `src/api/frappe.ts` | Small Frappe REST client (`call`, `getList`, `login`, `logout`) |
| `src/pages/PosHome.tsx` | Placeholder home page that pings `genysis_pos.api.ping` |

Other scripts: `npm run build`, `npm run lint`, `npm run preview`.
