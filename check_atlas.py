import os
from pymongo import MongoClient

# Paste your actual connection string here
MONGO_DB_URL = "mongodb+srv://mayankbazinga_db_user:Admin1234@cluster0.qxbi90u.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(MONGO_DB_URL)
    
    # Replace these with your actual database and collection names
    db = client["NetworkSecurity"]  # Or whatever your DB is named
    collection = db["phishing_data"] # Or whatever your collection is named
    
    # Count the documents
    doc_count = collection.count_documents({})
    
    print("\n" + "="*40)
    print("      MONGODB ATLAS CONNECTION SUCCESS      ")
    print("="*40)
    print(f"Database Name:   {db.name}")
    print(f"Collection Name: {collection.name}")
    print(f"Total Documents currently in Atlas: {doc_count}")
    print("="*40)
    
    if doc_count == 0:
        print("⚠️ WARNING: Your collection is EMPTY. Data is not uploading.")
    elif doc_count == 1:
        print("⚠️ WARNING: Only 1 document found. This is why train_test_split is crashing!")
    else:
        print("✅ SUCCESS: Data is present and ready for your ML pipeline.")

except Exception as e:
    print(f"❌ Connection Failed: {e}")