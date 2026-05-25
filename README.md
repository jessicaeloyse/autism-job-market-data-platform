# Autism Job Market Data Platform

## Overview

This project aims to build a modern data platform to analyze autism inclusion in the job market, focusing on scalable data engineering practices, data integration, transformation, and analytics.

The platform also explores engineering automation concepts through lightweight repository agents and CI/CD-driven workflows.

---

## Objectives

* Integrate heterogeneous data sources (job postings and socioeconomic data)
* Build scalable data pipelines using PySpark
* Apply medallion architecture (Bronze, Silver, Gold)
* Ensure data quality, consistency, and traceability
* Explore platform engineering and repository automation practices

---

## Architecture

The platform follows a **medallion architecture**, organizing data into three layers:

* **Bronze** → Raw ingested data from external sources
* **Silver** → Cleaned and standardized datasets
* **Gold** → Aggregated, analytics-ready data

---

## Tech Stack

* **PySpark**
* **Delta Lake**
* **Databricks**
* **Python**
* **GitHub Actions**
* **YAML**

---

## Engineering Practices

* Medallion architecture
* Config-driven infrastructure
* Repository automation
* CI/CD-based documentation synchronization
* Static analysis for Spark workloads
* Modular project structure

---

## Automation Agents

The project includes lightweight engineering automation agents designed to improve maintainability and developer experience.

### README Structure Agent

Automatically synchronizes the repository structure section in the README with the actual filesystem structure during merges to the main branch.

### Spark Review Agent

Performs static analysis on PySpark scripts, identifying potential anti-patterns and distributed processing issues such as unsafe `collect()` usage.

---

## Project Structure

<!-- PROJECT_STRUCTURE_START -->

```text
autism-job-market-data-platform
├── agents
│   ├── readme_structure_agent
│   │   ├── constants.py
│   │   ├── readme_updater.py
│   │   └── tree_generator.py
│   └── spark_review_agent
│       ├── sample_code
│       │   └── bad_spark_code.py
│       ├── reviewer.py
│       └── rules.py
├── app
│   ├── common
│   │   ├── context.py
│   │   └── spark_session.py
│   ├── ingestion
│   │   └── __init__.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── create_schemas.py
│   │   └── schemas.yaml
│   ├── __init__.py
│   └── setup.py
├── configs
│   └── local_configs.json
├── docs
│   └── engineering-decisions.md
├── .gitignore
├── LICENSE
└── README.md
```

<!-- PROJECT_STRUCTURE_END -->

---

## Environment Setup

To initialize the platform, run the setup script:

### 1. Configure environment

**Option A — Environment variable (recommended):**

```bash
export SCHEMA_CONFIG_PATH=/path/to/schemas.yaml
```

**Option B — Local config file:**

Create `configs/local_configs.json`:

```json
{
  "schema_config_path": "/Workspace/Repos/autism-job-market-data-platform/platform/schemas/schemas.yaml"
}
```

---

### 2. Run setup

```python
from platform.setup import run_setup

run_setup()
```

---

### Expected Result

The following schemas will be created:

* bronze
* silver
* gold
* metadata

---

## Documentation

Architectural decisions and engineering trade-offs are documented in:

```text
docs/engineering-decisions.md
```

---

## Current Progress

### Completed

* Repository structure automation agent
* Schema creation automation
* Medallion architecture definition
* Environment configuration strategy
* CI/CD workflow for documentation synchronization

### In Progress

* Spark static review agent
* Bronze layer ingestion pipeline

---
