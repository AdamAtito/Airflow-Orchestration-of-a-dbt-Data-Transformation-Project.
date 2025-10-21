# Store Pipeline Project

## Overview
This project is a **data pipeline system** for an e-commerce store, built using **Airflow**, **dbt**, **Python**, and **DuckDB**. The pipeline automates data extraction, transformation, and loading (ETL), and provides notifications upon successful runs.

## Project Structure
store_pipeline/
│
├─ dags/
│ └─ store_pipeline_dag.py # Airflow DAG for orchestrating the pipeline
├─ store_pipeline/
│ ├─ data_loader.py # Python scripts to load data into DuckDB
│ └─ dashboard.py # Python scripts for analytics/dashboard (optional)
├─ dbt_project/
│ ├─ models/ # dbt models (dimensions, facts, staging)
│ │ ├─ dimensions/
│ │ │ ├─ carts_dim.sql
│ │ │ ├─ products_dim.sql
│ │ │ └─ users_dim.sql
│ │ ├─ facts/
│ │ │ └─ fact_sales.sql
│ │ └─ staging/
│ │ ├─ stg_carts.sql
│ │ ├─ stg_products.sql
│ │ └─ stg_users.sql
│ ├─ seeds/
│ ├─ snapshots/
│ ├─ tests/
│ └─ dbt_project.yml
├─ dev.duckdb
├─ requirements.txt
└─ README.md

## Features
- **Airflow DAG**: Automates ETL process daily, orchestrates tasks for loading data, running dbt transformations, and sending email notifications.  
- **dbt**: Transforms raw data into structured models (facts and dimensions).  
- **Python scripts**: Load raw data into DuckDB, and optionally generate dashboards.  
- **Email notifications**: Sends success emails using `yagmail` after pipeline completion.

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/AdamAtito/Airflow-Orchestration-of-a-dbt-Data-Transformation-Project.git
cd Airflow-Orchestration-of-a-dbt-Data-Transformation-Project
Set up Python environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt


Set up Airflow

export AIRFLOW_HOME=$(pwd)/airflow
airflow db init
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
airflow webserver --port 8080


Configure Email Notifications

Set your email and password in environment variables or .env file:

export SENDER_EMAIL="your_email@gmail.com"
export SENDER_PASSWORD="your_password"


Note: Using Gmail may require enabling "Less Secure Apps" or using an App Password.

Usage

Place your raw data in the appropriate folder (if required by data_loader.py).

Trigger the DAG in Airflow via Web UI or CLI.

The DAG will:

Load raw data using Python scripts

Run dbt transformations

Send an email notification upon completion
