from pymongo import MongoClient

def connect_to_mongo():
    try:
        # MongoDB connection string
        mongo_uri = "mongodb://localhost:27017"  # Update for MongoDB Atlas if needed
        client = MongoClient(mongo_uri)

        # Test connection
        print("MongoDB connection successful!")
        return client

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

# Run the function to test connection
if __name__ == "__main__":
    connect_to_mongo()
