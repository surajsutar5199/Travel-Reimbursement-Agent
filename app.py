from fastapi import FastAPI
from graph import graph
from models import Claim

app = FastAPI()


@app.post("/process-claim")
def process_claim(claim: Claim):

    result = graph.invoke({
        "claim": claim.model_dump()
    })

    return result