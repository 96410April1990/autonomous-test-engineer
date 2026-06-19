                         USER
                          |
                          |
                 Web UI (React)
                          |
                          |
                    FastAPI Gateway
                          |
        -------------------------------------
        |                  |                 |
        v                  v                 v

 Requirement Agent   Test Architect   Code Analyzer
        |                  |                 |
        -------------------------------------
                          |
                          v

                 AI Orchestrator
                  (LangGraph)

                          |
 ---------------------------------------------------
 |              |             |            |        |
 v              v             v            v        v

Test        Playwright     Self Heal   Executor  Reporter
Generator   Generator      Agent       Agent     Agent


                          |
                          v

                 PostgreSQL + Vector DB


                          |
                          v

              CI/CD Integration Layer


Final Product Vision
AI QA Engineer Agent

A user uploads:

Requirement document
JIRA Epic export
Existing Test Plan
Existing Automation Suite
Application codebase

The agent:

Understands requirements
Creates test strategy
Generates complete test suite
Generates Playwright Python code
Creates Page Objects
Executes tests
Analyzes failures
Repairs broken tests
Learns from execution history
Predicts risky areas


# Project structure

autonomous-test-engineer
│
├── backend
│
│   ├── api              (REST endpoints)
│   ├── agents           (AI workers)
│   ├── core             (config/security)
│   ├── models           (shared objects)
│   ├── services         (business services)
│   ├── repositories     (DB access)
│   ├── rag              (vector search)
│   ├── automation       (Playwright)
│   ├── execution        (pytest runner)
│   └── utils
│
├── frontend
│
├── generated_tests
│
├── docker
│
└── docs

git remote add origin <repository-url>

git remote set-url origin <repository-url>