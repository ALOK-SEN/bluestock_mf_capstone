import os
import pandas as pd

# Data folder ka path
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Data', 'Raw')

def ingest_and_inspect_data():
    if not os.path.exists(DATA_DIR):
        print(f"Error: Folder path '{DATA_DIR}' nahi mila!")
        return

    # Folder me se saari CSV files ki list nikalna
    files = [f for f in sorted(os.listdir(DATA_DIR)) if f.endswith('.csv')]
    
    if not files:
        print("Koi CSV file nahi mili data/raw folder me!")
        return

    print(f"Total {len(files)} CSV files mili hain. Inspection shuru ho raha hai...\n")
    print("=" * 60)

    for file in files:
        file_path = os.path.join(DATA_DIR, file)
        print(f"\n📄 FILE: {file}")
        print("-" * 60)
        
        try:
            # 1. Sab CSV read karna
            df = pd.read_csv(file_path)
            
            # 2. Shape print karna
            print(f"🔹 Shape (Rows, Columns): {df.shape}")
            
            # 3. First 5 rows print karna
            print("\n🔹 First 5 Rows:")
            print(df.head())
            
            # 4. Datatype print karna
            print("\n🔹 Data Types:")
            print(df.dtypes)
            
            # 5. Missing values check karna
            print("\n🔹 Missing Values (per column):")
            print(df.isnull().sum())
            
            # 6. Duplicate check karna
            print(f"\n🔹 Duplicate Rows Count: {df.duplicated().sum()}")
            
        except Exception as e:
            print(f"Error reading {file}: {e}")
            
        print("=" * 60)

if __name__ == "__main__":
    ingest_and_inspect_data()