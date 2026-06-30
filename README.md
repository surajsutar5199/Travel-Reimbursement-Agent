# Travel Reimbursement Agent

## Project Overview

This project is an AI-powered Travel Reimbursement Approval System built using FastAPI, LangGraph, and Google Gemini.

The system validates employee travel reimbursement claims using business rules and company policy, then generates an approval decision using Gemini.

---

## Features

- Validate receipt availability
- Check reimbursement limits
- Detect duplicate claims
- Retrieve reimbursement policy
- AI-based approval using Gemini
- FastAPI REST API
- LangGraph workflow

---

## Tech Stack

- Python
- FastAPI
- LangGraph
- LangChain
- Google Gemini
- FAISS
- Sentence Transformers

---

## Project Structure

```
Travel-Reimbursement-Agent/

│── app.py
│── agents.py
│── graph.py
│── tools.py
│── rag.py
│── models.py
│── config.py
│── prompts.py
│── requirements.txt
│── README.md

├── data
│   ├── policy.txt
│   ├── claims.json
│   └── history.json
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GOOGLE_API_KEY=your_google_api_key
```

Run the application

```bash
python -m uvicorn app:app --reload
```

---

## API Endpoint

POST

```
/process-claim
```

---

## Sample Request

```json
{
    "employee_id": "EMP001",
    "employee_name": "Rahul Sharma",
    "trip_type": "Domestic",
    "category": "Hotel",
    "amount": 4500,
    "date": "2026-06-25",
    "vendor": "Taj Hotel",
    "receipt_attached": true,
    "manager_approval": false
}
```

---

## Sample Response

```json
{
    "validation": {
        "receipt": {
            "status": true
        },
        "limit": {
            "approved_amount": 4500
        },
        "duplicate": {
            "status": false
        }
    },
    "decision": "Approve"
}
```

---

## Workflow

Employee Claim

↓

Validation Agent

↓

Receipt Check

↓

Limit Check

↓

Duplicate Check

↓

Policy Lookup

↓

Gemini Decision Agent

↓

Final Approval Response

---

## Future Improvements

- Database integration
- Authentication
- Email notification
- OCR for receipt extraction
- Multi-agent workflow

---

## Author

Suraj Sutar
