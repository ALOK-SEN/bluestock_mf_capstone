# Data Dictionary — Bluestock MF Capstone

## dim_fund
| Column | Type | Description | Source |
|---|---|---|---|
| amfi_code | TEXT (PK) | Unique AMFI scheme identifier | 01_fund_master.csv |
| fund_house | TEXT | Asset Management Company managing the fund | 01_fund_master.csv |
| scheme_name | TEXT | Name of the mutual fund scheme | 01_fund_master.csv |
| category | TEXT | Broad category (Equity/Debt) | 01_fund_master.csv |
| sub_category | TEXT | Fund sub-category (e.g. Large Cap, Bluechip) | 01_fund_master.csv |
| plan | TEXT | Direct or Regular plan | 01_fund_master.csv |
| launch_date | DATE | Date the scheme was launched | 01_fund_master.csv |
| benchmark | TEXT | Benchmark index the fund is compared against | 01_fund_master.csv |
| expense_ratio_pct | REAL | Annual fee charged as % of AUM | 01_fund_master.csv |
| exit_load_pct | REAL | Fee charged on early redemption | 01_fund_master.csv |
| fund_manager | TEXT | Name of the fund manager | 01_fund_master.csv |
| risk_category | TEXT | Risk classification of the fund | 01_fund_master.csv |
| sebi_category_code | TEXT | SEBI-defined scheme category code | 01_fund_master.csv |

## dim_date
| Column | Type | Description | Source |
|---|---|---|---|
| date_id | DATE (PK) | Calendar date | Derived from nav_history date range |
| year | INTEGER | Calendar year | Derived |
| month | INTEGER | Calendar month (1-12) | Derived |
| quarter | INTEGER | Calendar quarter (1-4) | Derived |
| day_of_week | TEXT | Name of the weekday | Derived |

## fact_nav
| Column | Type | Description | Source |
|---|---|---|---|
| nav_id | INTEGER (PK) | Auto-incrementing row ID | Generated |
| amfi_code | TEXT (FK) | Links to dim_fund | 02_nav_history.csv |
| date | DATE (FK) | Links to dim_date | 02_nav_history.csv |
| nav | REAL | Net Asset Value of the fund on that date | 02_nav_history.csv |

## fact_transactions
| Column | Type | Description | Source |
|---|---|---|---|
| transaction_id | INTEGER (PK) | Auto-incrementing row ID | Generated |
| investor_id | TEXT | Unique investor identifier | 08_investor_transactions.csv |
| transaction_date | DATE (FK) | Date of transaction | 08_investor_transactions.csv |
| amfi_code | TEXT (FK) | Fund the transaction relates to | 08_investor_transactions.csv |
| transaction_type | TEXT | Sip / Lumpsum / Redemption | 08_investor_transactions.csv |
| amount_inr | REAL | Transaction amount in INR | 08_investor_transactions.csv |
| state | TEXT | Investor's state | 08_investor_transactions.csv |
| city | TEXT | Investor's city | 08_investor_transactions.csv |
| city_tier | TEXT | T30 (top 30 cities) or B30 (beyond top 30) | 08_investor_transactions.csv |
| age_group | TEXT | Investor's age bracket | 08_investor_transactions.csv |
| gender | TEXT | Investor's gender | 08_investor_transactions.csv |
| annual_income_lakh | REAL | Investor's annual income (in lakh INR) | 08_investor_transactions.csv |
| payment_mode | TEXT | Mode of payment (UPI/Cheque/etc.) | 08_investor_transactions.csv |
| kyc_status | TEXT | Verified or Pending | 08_investor_transactions.csv |

## fact_performance
| Column | Type | Description | Source |
|---|---|---|---|
| performance_id | INTEGER (PK) | Auto-incrementing row ID | Generated |
| amfi_code | TEXT (FK) | Links to dim_fund | 07_scheme_performance.csv |
| return_1yr_pct | REAL | 1-year trailing return (%) | 07_scheme_performance.csv |
| return_3yr_pct | REAL | 3-year trailing return (%) | 07_scheme_performance.csv |
| return_5yr_pct | REAL | 5-year trailing return (%) | 07_scheme_performance.csv |
| sharpe_ratio | REAL | Risk-adjusted return measure | 07_scheme_performance.csv |
| max_drawdown_pct | REAL | Largest peak-to-trough decline (%) | 07_scheme_performance.csv |
| morningstar_rating | INTEGER | Star rating (1-5) | 07_scheme_performance.csv |
| risk_grade | TEXT | Risk grade classification | 07_scheme_performance.csv |

## fact_aum
| Column | Type | Description | Source |
|---|---|---|---|
| aum_id | INTEGER (PK) | Auto-incrementing row ID | Generated |
| date | DATE (FK) | Reporting date | 03_aum_by_fund_house.csv |
| fund_house | TEXT | Asset Management Company | 03_aum_by_fund_house.csv |
| aum_crore | REAL | Assets Under Management (in ₹ crore) | 03_aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of schemes managed by this fund house | 03_aum_by_fund_house.csv |