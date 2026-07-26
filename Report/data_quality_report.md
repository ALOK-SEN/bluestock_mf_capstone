# Data Quality Report

## File: `01_fund_master.csv`
- **Rows:** 40
- **Columns:** 15
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `02_nav_history.csv`
- **Rows:** 46000
- **Columns:** 3
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `03_aum_by_fund_house.csv`
- **Rows:** 90
- **Columns:** 5
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `04_monthly_sip_inflows.csv`
- **Rows:** 48
- **Columns:** 6
- **Missing Values:**
  - `yoy_growth_pct`: 12
- **Duplicate Rows:** 0

## File: `05_category_inflows.csv`
- **Rows:** 144
- **Columns:** 3
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `06_industry_folio_count.csv`
- **Rows:** 21
- **Columns:** 6
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `07_scheme_performance.csv`
- **Rows:** 40
- **Columns:** 19
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `08_investor_transactions.csv`
- **Rows:** 32778
- **Columns:** 13
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `09_portfolio_holdings.csv`
- **Rows:** 322
- **Columns:** 8
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `10_benchmark_indices.csv`
- **Rows:** 8050
- **Columns:** 3
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## File: `HDFC_Top100_NAV.csv`
- **Rows:** 3129
- **Columns:** 2
- **Missing Values:**
  - None
- **Duplicate Rows:** 0

## AMFI Code Validation
- **Status:** ✅ All AMFI codes in `01_fund_master.csv` are present in `02_nav_history.csv`.

## Recommendations
1. Impute or drop missing values depending on the column's importance before feeding into models.
2. Remove any duplicate rows found during the inspection step.
3. Standardize column names across all files to ensure consistent data pipelines.
