from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents import validation_agent, decision_agent


class ClaimState(TypedDict):
    claim: dict
    validation: dict
    decision: str


# Node 1
def validate_claim(state: ClaimState):

    validation_result = validation_agent(state["claim"])

    return {
        "validation": validation_result
    }

def make_decision(state: ClaimState):
    
    return decision_agent(state)

# Build Graph
workflow = StateGraph(ClaimState)

workflow.add_node("validation", validate_claim)
workflow.add_node("decision", make_decision)

workflow.set_entry_point("validation")

workflow.add_edge("validation", "decision")
workflow.add_edge("decision", END)

graph = workflow.compile()