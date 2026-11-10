app_name = "genysis_pos"
app_title = "Genysis POS"
app_publisher = "Genysis"
app_description = "SaaS POS backend for Frappe/ERPNext with KRA e-TIMS integration"
app_email = "dev@example.com"
app_license = "mit"

required_apps = ["erpnext"]

# Document events
# ---------------
# Send submitted sales documents to KRA e-TIMS. The handlers return early
# when e-TIMS is disabled in "eTIMS Settings", so this is safe by default.
doc_events = {
    "Sales Invoice": {
        "on_submit": "genysis_pos.etims.events.on_sales_invoice_submit",
    },
    "POS Invoice": {
        "on_submit": "genysis_pos.etims.events.on_sales_invoice_submit",
    },
}

# Scheduled tasks
# ---------------
scheduler_events = {
    "hourly": [
        "genysis_pos.etims.events.retry_failed_submissions",
    ],
}

# CORS / frontend
# ---------------
# In production, serve the React build from the same domain or set
# "allow_cors" in site_config.json to the frontend origin.
