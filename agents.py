from tools import check_receipt, check_limit, check_duplicate


def validation_agent(claim):
    """
    Validate the reimbursement claim.
    """

    receipt_result = check_receipt(claim["receipt_attached"])

    limit_result = check_limit(
        claim["category"],
        claim["amount"]
    )

    duplicate_result = check_duplicate(
        claim["employee_id"],
        claim["date"]
    )

    return {
        "receipt": receipt_result,
        "limit": limit_result,
        "duplicate": duplicate_result
    }
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY
from tools import policy_lookup

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)

def decision_agent(state):
    """
    Generate final reimbursement decision using Gemini.
    """

    claim = state["claim"]
    validation = state["validation"]

    query = f"{claim['category']} reimbursement policy"
    policy = policy_lookup(query)
    # policy = "Hotel reimbursement limit is ₹5000. Receipt is mandatory."

    prompt = f"""
You are a Travel Reimbursement Approval Assistant.

Policy:
{policy}

Claim:
{claim}

Validation Results:
{validation}

Based on the policy and validation results, return:

1. Decision (Approve / Reject / Partial Approval / Manual Review)
2. Approved Amount
3. Reason
"""

    response = llm.invoke(prompt)

    return {
        "decision": response.content
    }