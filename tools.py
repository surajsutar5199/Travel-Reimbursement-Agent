# from rag import retriever


def policy_lookup(query: str):
    """
    Temporary policy (without RAG)
    """

    return """
Hotel reimbursement limit is ₹5000.
Meal reimbursement limit is ₹1000.
Taxi reimbursement limit is ₹1500.
Receipt is mandatory.
Duplicate claims are not allowed.
"""

def check_receipt(receipt_attached: bool):
    """
    Check whether receipt is available.
    """

    if receipt_attached:
        return {
            "status": True,
            "message": "Receipt is available."
        }

    return {
        "status": False,
        "message": "Receipt is missing."
    }

LIMITS = {
    "Hotel": 5000,
    "Meal": 1000,
    "Taxi": 1500
}


def check_limit(category, amount):

    limit = LIMITS.get(category)

    if limit is None:
        return {
            "status": False,
            "message": "Unknown category"
        }

    if amount <= limit:

        return {
            "status": True,
            "approved_amount": amount,
            "rejected_amount": 0
        }

    return {
        "status": False,
        "approved_amount": limit,
        "rejected_amount": amount - limit
    }

import json


def check_duplicate(employee_id, date):

    with open("data/history.json", "r") as f:

        history = json.load(f)

    for claim in history:

        if (
            claim["employee_id"] == employee_id
            and claim["date"] == date
        ):

            return {
                "status": True,
                "message": "Duplicate claim found."
            }

    return {
        "status": False,
        "message": "No duplicate claim."
    }