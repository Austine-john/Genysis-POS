import frappe

from genysis_pos.etims.settings import is_etims_enabled


def on_sales_invoice_submit(doc, method=None):
    """Queue the invoice for submission to KRA e-TIMS."""
    if not is_etims_enabled():
        return
    frappe.enqueue(
        "genysis_pos.etims.events.submit_invoice",
        queue="short",
        doctype=doc.doctype,
        name=doc.name,
        enqueue_after_commit=True,
    )


def submit_invoice(doctype: str, name: str):
    from genysis_pos.etims.client import ETIMSClient, build_sales_payload

    invoice = frappe.get_doc(doctype, name)
    payload = build_sales_payload(invoice)
    ETIMSClient().send_sales_transaction(payload)
    # TODO: store the receipt signature / QR data returned by KRA on the invoice.


def retry_failed_submissions():
    """Scheduled job: resend invoices whose e-TIMS submission failed."""
    if not is_etims_enabled():
        return
    # TODO: track submission status and retry failures here.
