import frappe


def get_settings():
    """Return the eTIMS Settings single doc."""
    return frappe.get_cached_doc("eTIMS Settings")


def is_etims_enabled() -> bool:
    try:
        return bool(get_settings().enabled)
    except frappe.DoesNotExistError:
        return False
