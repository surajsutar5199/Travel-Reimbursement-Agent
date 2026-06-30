from graph import graph

claim = {
    "employee_id": "EMP001",
    "employee_name": "Rahul Sharma",
    "trip_type": "Domestic",
    "category": "Hotel",
    "amount": 4500,
    "date": "2026-06-25",
    "vendor": "Taj Hotel",
    "receipt_attached": True,
    "manager_approval": False
}

result = graph.invoke({
    "claim": claim
})

print(result)

result = graph.invoke({
    "claim": claim
})

print(result.keys())
print(result)