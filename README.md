
# Trade Reconciliation & Data Quality Dashboard

## Project Objective

This project simulates a real-world scenario where a Senior Reporting Analyst is tasked with automating the trade reconciliation process between a front-office trading system and a back-office accounting system. The goal is to identify, categorize, and visualize data discrepancies to ensure data integrity and provide actionable insights for the Operations team.

The final output is an interactive Power BI dashboard that provides a clear overview of all trade breaks.

---

## Dashboard Preview

![Dashboard Screenshot](dashboard.png)

---

## Key Features & Skills Demonstrated

This project showcases a blend of business analysis, data engineering, and business intelligence skills:

*   **Business Analysis:** Translated a business problem into technical requirements by creating a **Business Requirements Document (BRD)** and a **Data Mapping Document**.
*   **Data Generation:** Developed a Python script (`generate_trade_data.py`) to create realistic, synthetic datasets with intentional discrepancies, simulating real-world data quality challenges.
*   **Database Management:** Utilized Python's built-in `sqlite3` library to create a database, import CSV data, and serve as the backend for the analysis.
*   **Complex SQL Querying:** Wrote a sophisticated SQL query (`reconciliation_query.sql`) using `FULL OUTER JOIN` to find mismatches and `CASE` statements to categorize different types of data breaks.
*   **Data Reconciliation & Validation:** The core logic successfully identifies breaks such as missing trades, quantity mismatches, and settlement date errors.
*   **BI Dashboarding (Power BI):** The final `reconciliation_breaks.csv` dataset was used to build an interactive dashboard in Power BI, featuring KPIs, charts, and filterable tables for deep-dive analysis.

---

## How to Run This Project

To replicate this analysis, follow these steps:

### Prerequisites
*   Python 3.x
*   pandas library (`pip install pandas`)
*   A BI Tool like Power BI or Tableau

### Steps

1.  **Generate Raw Data:** Run the data generation script from your terminal. This will create `front_office_trades.csv` and `back_office_trades.csv` in the `/data` directory.
    ```shell
    python generate_trade_data.py
    ```

2.  **Set Up the Database:** Run the database setup script. This creates the `trades.db` file and populates it with the data from the CSVs.
    ```shell
    python setup_database.py
    ```

3.  **Run the Reconciliation Query:** Execute the main query script. This reads the SQL file, runs the reconciliation against the database, and exports the results.
    ```shell
    python run_query.py
    ```
    This will produce the final `reconciliation_breaks.csv` file in the `/data` directory.

4.  **Visualize the Data:**
    *   Open the `Trade Lifecycle Reconciliation.pbix` file in Power BI.
    *   Alternatively, in your BI tool, connect to the `reconciliation_breaks.csv` file located in the `/data` folder to build the dashboard from scratch.

---

## Project Artifacts

*   **Business Documentation:**
    *   `TradeReconciliation_BRD.md`: Outlines the project goals and requirements.
    *   `TradeReconciliation_DataMap.md`: Documents the mapping between source and target data fields.
*   **Core Logic:**
    *   `reconciliation_query.sql`: The SQL query that performs the reconciliation.
*   **Data:**
    *   `/data/reconciliation_breaks.csv`: The final, clean dataset ready for visualization.
