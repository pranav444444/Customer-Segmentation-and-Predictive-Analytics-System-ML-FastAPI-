from src.configuration.mongo_db_connection import MongoDBClient

client = MongoDBClient()

print("MongoDB Connected Successfully")
print("Database:", client.database_name)

# Upload dataset
client.upload_csv_to_mongodb("notebooks/marketing_campaign.csv")