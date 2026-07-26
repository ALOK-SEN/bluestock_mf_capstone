import requests
import pandas as pd

# AMFI Scheme Code
scheme_code = "125497"

# API URL
url = f"https://api.mfapi.in/mf/{scheme_code}"

# API Request
response = requests.get(url)

# JSON Data
data = response.json()

# NAV History
nav_data = data["data"]

# DataFrame
df = pd.DataFrame(nav_data)

# CSV Save
df.to_csv("data/raw/HDFC_Top100_NAV.csv", index=False)

print("Live NAV data saved successfully!")