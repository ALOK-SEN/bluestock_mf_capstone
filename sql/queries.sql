-- 1. Top 5 funds by AUM
SELECT fund_house, AVG(aum_crore) as avg_aum
FROM fact_aum GROUP BY fund_house ORDER BY avg_aum DESC LIMIT 5;

-- 2. Average NAV per month per fund
SELECT amfi_code, strftime('%Y-%m', date) as month, AVG(nav) as avg_nav
FROM fact_nav GROUP BY amfi_code, month;

-- 3. SIP YoY growth (total SIP transaction amount by year)
SELECT strftime('%Y', transaction_date) as year, SUM(amount_inr) as total_sip
FROM fact_transactions WHERE transaction_type = 'Sip' GROUP BY year;

-- 4. Transactions by state
SELECT state, COUNT(*) as txn_count, SUM(amount_inr) as total_amount
FROM fact_transactions GROUP BY state ORDER BY total_amount DESC;

-- 5. Funds with expense_ratio < 1%
SELECT scheme_name, expense_ratio_pct FROM dim_fund WHERE expense_ratio_pct < 1.0;

-- 6. Top 5 funds by 3-year return
SELECT df.scheme_name, fp.return_3yr_pct
FROM fact_performance fp JOIN dim_fund df ON fp.amfi_code = df.amfi_code
ORDER BY fp.return_3yr_pct DESC LIMIT 5;

-- 7. Average transaction amount by age group
SELECT age_group, AVG(amount_inr) as avg_amount FROM fact_transactions GROUP BY age_group;

-- 8. Fund count by category
SELECT category, COUNT(*) as fund_count FROM dim_fund GROUP BY category;

-- 9. Highest Sharpe ratio funds (risk-adjusted return)
SELECT df.scheme_name, fp.sharpe_ratio
FROM fact_performance fp JOIN dim_fund df ON fp.amfi_code = df.amfi_code
ORDER BY fp.sharpe_ratio DESC LIMIT 10;

-- 10. Transaction volume by city tier and type
SELECT city_tier, transaction_type, COUNT(*) as cnt, SUM(amount_inr) as total
FROM fact_transactions GROUP BY city_tier, transaction_type;