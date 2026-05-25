# Autism Job Market Data Platform

## Overview

This project aims to build a data platform to analyze autism inclusion in the job market, focusing on data integration, transformation, and analytics.

---

## Objectives

* Integrate heterogeneous data sources (job postings and socioeconomic data)
* Build scalable data pipelines using PySpark
* Apply medallion architecture (Bronze, Silver, Gold)
* Ensure data quality, consistency, and traceability

---

## Architecture

The platform follows a **medallion architecture**, organizing data into three layers:

* **Bronze** → Raw ingested data from external sources
* **Silver** → Cleaned and standardized datasets
* **Gold** → Aggregated, analytics-ready data

This structure enables clear data lineage, scalability, and efficient data consumption.

---

## Tech Stack

* **PySpark**
* **Delta Lake**
* **Databricks**

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

Create `configs/local_config.json`:

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

## Design Decisions

Architectural decisions and trade-offs are documented in:

```
docs/engineering-decisions.md
```

---

## Status

🚧 In progress — currently implementing data ingestion (Bronze layer)
