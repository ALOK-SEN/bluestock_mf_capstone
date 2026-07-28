# Bluestock Mutual Fund Capstone

## 📌 Project Overview

This project is part of the **Bluestock Mutual Fund Capstone**. The objective is to build an end-to-end data analytics pipeline for Indian Mutual Fund data by collecting, validating, processing, and analyzing multiple datasets.

The project begins with data ingestion and quality assessment and will later include SQL analysis, dashboard development, and business insights.

---

## 📂 Project Structure

```
bluestock_mf_capstone/
│
├── dashboard/              # Dashboard files
├── data/
│   ├── raw/                # Raw datasets
│   ├── processed/          # Cleaned datasets
│   └── db/                 # Database files
│
├── notebooks/             # Jupyter notebooks
├── reports/               # Data quality reports
├── scripts/               # Python scripts
│
├── live_nav_fetch.py      # Fetches live NAV data using MFAPI
├── data_ingestion.py      # Data ingestion script
├── requirements.txt
└── README.md
```

---

## 📊 Datasets

The project includes the following datasets:

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices
- Live Mutual Fund NAV Data (MFAPI)

---

## ⚙️ Technologies Used

- Python
- Pandas
- Requests
- Jupyter Notebook
- Git & GitHub

---

## ✅ Day 1 Tasks Completed

- Project setup completed
- Folder structure organized
- Data ingestion completed
- Data quality analysis performed
- Duplicate and missing value checks completed
- AMFI code validation completed
- Live NAV data fetched using MFAPI
- Data Quality Report generated

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/ALOK-SEN/bluestock_mf_capstone.git
```

2. Move into the project folder

```bash
cd bluestock_mf_capstone
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the data ingestion script

```bash
python data_ingestion.py
```

5. Fetch live NAV data

```bash
python live_nav_fetch.py
```

---

## 📈 Data Quality Summary

- No duplicate records found across datasets.
- Missing values were identified only in the `yoy_growth_pct` column of the Monthly SIP Inflows dataset.
- All AMFI codes were successfully validated against the NAV History dataset.

---

## 👨‍💻 Author

**Alok Sen**

GitHub: https://github.com/ALOK-SEN