# Sales Data Pipeline Project

Pipeline data moderne avec Snowflake, dbt, FastAPI et visualisation Power BI

## Structure
- `data_generator/` - API FastAPI pour générer les données
- `dbt_project/` - Transformations dbt (ELT)
- `airflow/` - DAGs Airflow (pour plus tard)
- `snowflake/` - Scripts Snowflake
- `dashboards/` - Power BI dashboards
- `docs/` - Documentation

## Installation
1. `python3 -m venv pipeline_env`
2. `source pipeline_env/bin/activate`
3. `pip install -r requirements.txt`
