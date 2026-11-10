# Genysis POS: backend

A custom Frappe app (`genysis_pos`) that runs on a Frappe v15 bench next to
ERPNext. It exposes the API the React frontend uses and holds the KRA e-TIMS
integration.

## Install into a bench

```bash
# one-time: create a bench with ERPNext (skip if you already have one)
bench init frappe-bench --frappe-branch version-15
cd frappe-bench
bench get-app erpnext --branch version-15
bench new-site pos.localhost
bench --site pos.localhost install-app erpnext

# link this folder into the bench as an app
ln -s /path/to/Genysis-POS/backend apps/genysis_pos
./env/bin/pip install -e apps/genysis_pos
echo genysis_pos >> sites/apps.txt
bench --site pos.localhost install-app genysis_pos

bench start            # http://localhost:8000
```

Check it works: `curl http://localhost:8000/api/method/genysis_pos.api.ping`

## Layout

| Path | Purpose |
| --- | --- |
| `genysis_pos/hooks.py` | App metadata, doc events and scheduled jobs |
| `genysis_pos/api.py` | Whitelisted endpoints for the frontend (`ping` for now) |
| `genysis_pos/genysis_pos/` | "Genysis POS" module, for POS DocTypes |
| `genysis_pos/etims/` | "ETIMS" module, the KRA e-TIMS integration |
| `genysis_pos/etims/doctype/etims_settings/` | Single DocType for PIN, branch, device serial and API URL |
| `genysis_pos/etims/client.py` | e-TIMS API client (placeholder endpoints) |
| `genysis_pos/etims/events.py` | Queues submitted Sales/POS Invoices for e-TIMS |

e-TIMS is off until you tick **Enabled** in **eTIMS Settings**, so the hooks do
nothing on a fresh install. `build_sales_payload` and the endpoint paths are
TODOs to fill in from the KRA OSCU/VSCU specification.
