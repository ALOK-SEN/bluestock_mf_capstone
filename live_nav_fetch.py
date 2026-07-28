import os
import requests
import pandas as pd

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# AMFI Scheme Codes
schemes = {
    "HDFC_Top100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841",
}

for name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        if "data" in data:
            df = pd.DataFrame(data["data"])
            file_path = f"data/raw/{name}_NAV.csv"
            df.to_csv(file_path, index=False)
            print(f"✅ {name} NAV data saved successfully!")
        else:
            print(f"❌ No NAV data found for {name}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch {name}: {e}")

print("\n🎉 All NAV fetch operations completed.")
