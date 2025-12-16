# AI System Failure Detection

## Overview

This project, **AI System Failure Detection**, is designed to automatically analyze AI system outputs and detect failures related to functionality, performance, and code quality. It simulates how an AI assistant or system can be evaluated using structured checks and produces a clear pass/fail decision.

---

## How the Project Works (Detailed)

1. **Input Collection**
   The system takes structured input such as AI-generated outputs, logs, or execution results (for example, JSON system reports). These inputs represent how an AI system behaved during execution.

2. **Rule-Based & Metric Analysis**
   The project applies predefined rules and evaluation criteria such as functional correctness, performance metrics (CPU usage, execution time, memory), and code quality checks (e.g., linting results).

3. **Failure Detection Engine**
   Each check is independently evaluated. If any critical rule fails (for example, linting errors or abnormal resource usage), the system flags the corresponding component as a failure.

4. **Decision Aggregation**
   Results from all checks are aggregated into a single final decision (`PASS` or `FAIL`). Along with the decision, detailed reasons and evidence are preserved for transparency.

5. **Human-Readable Reporting**
   The final output is generated in a clean, readable format (JSON / console output), making it easy for developers to understand what failed, why it failed, and where to fix the issue.

---

## Features

* Clean and modular code structure
* Easy local setup
* Beginner-friendly
* Version controlled with Git

---

## Tech Stack

- **Programming Language:** Python  
- **Version Control:** Git  
- **Environment Management:** Python Virtual Environment (`.venv`)  
- **LLM Integration:** Ollama (Phi-3) used to summarize system errors and generate human-readable explanations

---

## Project Structure

```
project-root/
│── .venv/
│── src/
│── app/
│── requirements.txt
│── README.md
│── .gitignore
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create and activate virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python app/main.py
```

(Adjust the entry file if needed)

---

## Git Commands (Quick Reference)

```bash
git status
git add .
git commit -m "message"
git push
```

---

## Common Issues

* **Virtual environment not activating**: Ensure you are inside the project folder
* **Permission error on Windows**:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```




