"""Whitelisted endpoints used by the React frontend."""

import frappe

from genysis_pos.etims.settings import is_etims_enabled


@frappe.whitelist(allow_guest=True)
def ping():
    """Health check: GET/POST /api/method/genysis_pos.api.ping"""
    return {
        "app": "genysis_pos",
        "status": "ok",
        "etims_enabled": is_etims_enabled(),
    }
