from pydantic import BaseModel
from typing import Optional


class Claim(BaseModel):
    employee_id: str
    employee_name: str
    trip_type: str
    category: str
    amount: float
    date: str
    vendor: str
    receipt_attached: bool
    manager_approval: bool


class Decision(BaseModel):
    decision: str
    approved_amount: float
    rejected_amount: float
    confidence: float
    reason: str
    policy_reference: str
    missing_documents: Optional[str] = None