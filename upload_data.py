import pandas as pd
from pymongo import MongoClient

# 1. Use your working connection string and password here
MONGO_DB_URL = "mongodb+srv://mayankbazinga_db_user:Admin1234@cluster0.qxbi90u.mongodb.net/?appName=Cluster0"

try:
    print("Connecting to MongoDB Atlas...")
    client = MongoClient(MONGO_DB_URL)
    db = client["NetworkSecurity"]
    collection = db["phishing_data"]

    # 2. Load your local CSV file (Make sure the filename matches exactly!)
    csv_file_path = "Network_Data/phisingData.csv" 
    print(f"Reading local file: {csv_file_path}...")
    df = pd.read_csv(csv_file_path)

    # 3. Convert dataframe to a list of dictionaries (JSON format for Mongo)
    print(f"Preparing to upload {len(df)} records...")
    data_dict = df.to_dict(orient="records")

    # 4. Insert the data into Atlas
    # We clear the collection first just in case there's any stray dummy row
    collection.delete_many({}) 
    result = collection.insert_many(data_dict)

    print("\n" + "="*40)
    print("         SUCCESSFULLY UPLOADED!         ")
    print("="*40)
    print(f"Total rows sent to Atlas: {len(result.inserted_ids)}")
    print("="*40)

except FileNotFoundError:
    print(f"❌ Error: Could not find the file '{csv_file_path}' in this folder. Double check your file name!")
except Exception as e:
    print(f"❌ An error occurred: {e}")