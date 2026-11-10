# Genysis POS

A SaaS point-of-sale system with a React frontend and a Frappe / ERPNext
backend, integrated with KRA e-TIMS (Kenya).

```
Genysis-POS/
├── frontend/   React + TypeScript + Vite POS UI
└── backend/    Frappe app "genysis_pos" (API + e-TIMS integration)
```

The frontend talks to Frappe over its REST API. ERPNext handles items, stock,
customers and invoices; `genysis_pos` adds the POS-specific API and sends
submitted invoices to KRA e-TIMS.

## Requirements

- Node.js 20+ and npm, for the frontend
- A Frappe v15 bench with ERPNext (Python 3.10+, MariaDB, Redis), for the backend.
  See the [Frappe install guide](https://docs.frappe.io/framework/user/en/installation).

## Running locally

1. **Backend.** Link `backend/` into your bench and install it on a site, then
   run `bench start` (serves on `http://localhost:8000`). Full steps are in
   [backend/README.md](backend/README.md).
2. **Frontend.**
   ```bash
   cd frontend
   cp .env.example .env
   npm install
   npm run dev      # http://localhost:5173
   ```
   The dev server proxies `/api` to the bench. Details in
   [frontend/README.md](frontend/README.md).

Open `http://localhost:5173`; the home page shows whether it can reach the
backend and whether e-TIMS is configured.

## e-TIMS

Configure it in the Frappe desk under **eTIMS Settings** (KRA PIN, branch ID,
device serial, API URL). It's disabled by default. The client and payload
mapping in `backend/genysis_pos/etims/` are placeholders for now.
