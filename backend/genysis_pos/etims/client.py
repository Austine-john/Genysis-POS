"""Placeholder client for the KRA e-TIMS (OSCU/VSCU) API.

Fill in the endpoint paths and payload mapping from the KRA e-TIMS
technical specification once sandbox credentials are available.
"""

import frappe
import requests

from genysis_pos.etims.settings import get_settings


class ETIMSError(Exception):
    pass


class ETIMSClient:
    def __init__(self, settings=None):
        self.settings = settings or get_settings()
        self.base_url = (self.settings.base_url or "").rstrip("/")

    def _headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "tin": self.settings.tin or "",
            "bhfId": self.settings.branch_id or "",
            "cmcKey": self.settings.get_password("cmc_key", raise_exception=False) or "",
        }

    def post(self, path: str, payload: dict) -> dict:
        if not self.base_url:
            raise ETIMSError("eTIMS base URL is not configured")
        res = requests.post(f"{self.base_url}/{path.lstrip('/')}", json=payload, headers=self._headers(), timeout=30)
        res.raise_for_status()
        data = res.json()
        # KRA responses carry resultCd "000" on success.
        if data.get("resultCd") not in ("000", None):
            raise ETIMSError(f"{data.get('resultCd')}: {data.get('resultMsg')}")
        return data

    # --- Endpoints (TODO: confirm paths against the KRA spec) -----------------

    def initialize_device(self) -> dict:
        return self.post("selectInitOsdcInfo", {
            "tin": self.settings.tin,
            "bhfId": self.settings.branch_id,
            "dvcSrlNo": self.settings.device_serial,
        })

    def send_sales_transaction(self, payload: dict) -> dict:
        return self.post("saveTrnsSalesOsdc", payload)


def build_sales_payload(invoice) -> dict:
    """Map an ERPNext Sales/POS Invoice to the e-TIMS sales payload.

    TODO: map items, tax categories (A-E), customer PIN and totals.
    """
    frappe.throw("build_sales_payload is not implemented yet")
