# Repository Strategy Handbook

This handbook provides the architectural blueprints, folder structures, README templates, and commit guidelines for the six core learning repositories in your portfolio. 

---

## 🔧 Core Standards for All Lab Notebooks

To represent a **production engineering mindset**, all repositories must follow these conventions:
1. **Conventional Commits**: Commit messages must use a prefix (e.g., `feat:`, `fix:`, `docs:`, `test:`, `refactor:`).
2. **Telemetry/Logging**: Avoid silent code. Include debugging outputs, assertions, or logging modules.
3. **Tests Included**: Every algorithm or foundation code file must be accompanied by a unit test (using `unittest` or `pytest`).
4. **Structured Documentation**: No undocumented code blocks.

---

## 1. `python-foundations`

### Description
Laboratory notebooks covering core Python, standard libraries, I/O operations, context managers, decorators, and system scripts.

### Folder Structure
```text
python-foundations/
├── .github/
│   └── workflows/
│       └── lint.yml          # Ruff or Flake8 lint checker
├── src/
│   ├── week1_env/            # Environment setup scripts & WSL2 diagnostics
│   ├── week2_oop/            # Classes, interfaces, encapsulation labs
│   └── week3_stdlib/         # os, sys, datetime, json libraries
├── tests/
│   ├── __init__.py
│   ├── test_week2_oop.py
│   └── test_week3_stdlib.py
├── .gitignore
├── README.md
├── requirements.txt          # Minimal dependencies (e.g., pytest, black)
└── pyproject.toml            # Code styling configs
```

### README Template
```markdown
# Python Foundations Lab

Lab notebook documenting deep-dives into Python syntax, internals, OOP, and system scripting.

## 🧪 Modules
- **src/week1_env/**: Environment validation, pathing configurations, and WSL setup scripts.
- **src/week2_oop/**: OOP implementations, design patterns, and interface models.

## ⚙️ Running Tests
```bash
pip install -r requirements.txt
pytest tests/
```
```

### Learning Progression & Commit Strategy
- **Stage 1 (Weeks 1-2)**: Basic structures and classes. Commit standard: `feat(oop): implement polymorphism and abstract base class tests`.
- **Stage 2 (Weeks 3-4)**: Context managers, file streams. Commit standard: `docs(io): document context manager behavior for file streams`.

---

## 2. `dsa-python`

### Description
Implementations of classical Data Structures and Algorithms with runtime benchmarks, time/space complexity documentation, and test validations.

### Folder Structure
```text
dsa-python/
├── data_structures/
│   ├── arrays/
│   ├── linked_lists/
│   └── trees/
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   └── graph_traversal/
├── benchmark/
│   └── run_benchmarks.py     # Custom benchmark script comparing algorithm execution speeds
├── tests/
│   ├── test_structures.py
│   └── test_algorithms.py
├── README.md
└── pytest.ini
```

### README Template
```markdown
# DSA Implementation Notebook

Classical data structures and algorithms written from scratch in Python, verified by tests, and benchmarked for efficiency.

## 📊 Complexity Log
| Structure / Algorithm | Time Complexity (Avg/Worst) | Space Complexity | Status |
|:----------------------|:---------------------------|:-----------------|:-------|
| Linked List           | O(N)                       | O(N)             | [x]    |
| Quick Sort            | O(N log N)                 | O(log N)         | [ ]    |

## 🧪 Testing
```bash
pytest tests/
```
```

### Learning Progression & Commit Strategy
- **Stage 1 (Weeks 2-3)**: Linear data structures. Commit standard: `feat(ds): implement doubly linked list with structural integrity tests`.
- **Stage 2 (Weeks 4-5)**: Sorting, recursion. Commit standard: `test(algos): add unit tests and execution benchmarks for quicksort`.

---

## 3. `roadmap-notes`

### Description
Central archive of educational diagnostics, paper summaries, reading logs, and academic journals tracking your progress toward systems engineering.

### Folder Structure
```text
roadmap-notes/
├── phase1_foundations/       # Week 1 - 4 study summaries, lecture notes
├── phase2_systems/           # Week 5 - 8 networking, databases, OS theory
├── phase3_agents/            # Week 9 - 12 AI Agentic architectures, LLM papers
├── reading_list/             # Book & paper reviews (e.g. DDIA, clean code)
└── README.md
```

### README Template
```markdown
# Systems Engineering & AI Roadmap Logs

Chronological study notes, conceptual architectures, reading reviews, and roadmap milestones.

## 📖 Directory Index
- [Phase 1 Summary](phase1_foundations/README.md)
- [Phase 2 Goals](phase2_systems/README.md)
- [Reading Log](reading_list/README.md)

## 🕒 Current Station
- **Active Focus**: Phase 1 - Transitioning from Python basics to Computer Science principles.
```

### Learning Progression & Commit Strategy
- Keep notes clean and formatted in Markdown. 
- Commit standard: `docs(notes): update Week 1 review notes on Unix file systems`.

---

## 4. `ml-foundations`

### Description
Mathematical fundamentals of machine learning (Linear Algebra, Calculus, Statistics) and models (Linear/Logistic Regression, Neural Networks) implemented from scratch.

### Folder Structure
```text
ml-foundations/
├── math/
│   ├── linear_algebra/       # Matrix multiplications, vector projections
│   └── calculus/             # Gradient descent, partial derivatives
├── models_from_scratch/
│   ├── linear_regression.py
│   └── logistic_regression.py
├── notebooks/                # Exploratory Jupyter Notebooks
├── tests/
│   └── test_math.py
├── README.md
└── requirements.txt
```

### README Template
```markdown
# Machine Learning Foundations from Scratch

Mathematical concepts and machine learning algorithms written without high-level ML frameworks (pure NumPy/Math).

## 🛠️ Models List
- **Linear Regression**: Gradient descent optimization implemented in pure Python.
- **Logistic Regression**: Sigmoid function activation and cross-entropy loss tracking.

## 🧪 Testing Math
```bash
pytest tests/
```
```

### Learning Progression & Commit Strategy
- **Stage 1 (Weeks 4-5)**: Linear Algebra scripts. Commit standard: `feat(math): add matrix transformation functions and unit tests`.
- **Stage 2 (Weeks 6-7)**: Supervised learning models. Commit standard: `feat(models): implement gradient descent for linear regression`.

---

## 5. `backend-engineering`

### Description
Backend infrastructure logs: network sockets, HTTP servers from scratch, database integration, API designs, and middleware logic.

### Folder Structure
```text
backend-engineering/
├── network/
│   ├── tcp_sockets/          # Pure TCP client-server protocols
│   └── http_parser/          # Parse raw HTTP/1.1 requests
├── api_services/
│   └── fast_api/             # Modern RESTful API prototypes
├── databases/
│   ├── sql_schemas/
│   └── migration/
├── tests/
│   └── test_api.py
├── README.md
└── requirements.txt
```

### README Template
```markdown
# Backend Engineering & Network Sandbox

Experimental implementations of low-level networking, protocols, and backend API structures.

## ⚙️ Prototypes
- **network/tcp_sockets**: Standard multi-threaded TCP server and client.
- **api_services/fast_api**: Clean API endpoints, validating request bodies and parameters.

## 🧪 Run Tests
```bash
pytest tests/
```
```

### Learning Progression & Commit Strategy
- **Stage 1 (Weeks 6-7)**: TCP/IP socket practice. Commit: `feat(net): build multi-threaded TCP echo server in python`.
- **Stage 2 (Weeks 8-9)**: Web APIs and databases. Commit: `feat(api): design structured SQLite endpoints with transaction tracking`.

---

## 6. `system-design-notes`

### Description
Case studies, block diagrams, architectural write-ups on scaling systems, cache design, load balancing, and distributed communication structures.

### Folder Structure
```text
system-design-notes/
├── architecture_patterns/
│   ├── caching/              # Redis strategies, LRU cache scripts
│   └── load_balancing/       # Round robin, weighted distribution algorithms
├── case_studies/
│   ├── tiny_url/             # Design and scale a short URL system
│   └── chat_app/             # Real-time WebSocket architectures
├── diagrams/                 # Mermaid diagram codes and PNG exports
└── README.md
```

### README Template
```markdown
# System Design & Distributed Systems Analysis

Theoretical study guides, architectural diagrams, caching algorithms, and system models.

## 🗺️ Index
- **LRU Cache Implementation**: Local caching simulation with expiry eviction.
- **System Analysis**: Documenting message queues and event-driven backends.
```

### Learning Progression & Commit Strategy
- **Stage 1 (Weeks 8-9)**: Eviction cache code. Commit: `feat(cache): implement LRU cache with O(1) lookups and eviction tests`.
- **Stage 2 (Weeks 10-12)**: System architecture study reports. Commit: `docs(design): draft architecture diagram for event-driven telemetry pipeline`.
