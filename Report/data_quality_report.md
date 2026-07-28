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
- *Status:* ✅ All AMFI codes in 01_fund_master.csv are present in 02_nav_history.csv.
- *Missing AMFI Codes:* 0

## Summary
- Successfully validated all 10 datasets and the fetched NAV data.
- No duplicate records were found in any dataset.
- Missing values were found only in the yoy_growth_pct column of 04_monthly_sip_inflows.csv (12 missing values).
- All AMFI codes were successfully matched with the NAV history dataset.

## Recommendations
1. Investigate the 12 missing values in yoy_growth_pct and decide whether to impute or exclude them during preprocessing.
2. Maintain consistent naming conventions and data types across all datasets.
3. Continue validating new datasets before loading them into the analytics pipeline.
