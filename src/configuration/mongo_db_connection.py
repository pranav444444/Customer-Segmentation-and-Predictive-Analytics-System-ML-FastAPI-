import os
import sys

import certifi
import pymongo
import pandas as pd
from dotenv import load_dotenv

from src.constant.database import DATABASE_NAME
from src.constant.env_variable import MONGODB_URL_KEY
from src.exception import CustomerException


load_dotenv()

ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME, collection_name="customers") -> None:
        try:
            # Create connection only once
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)

                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.collection = self.database[collection_name]
            self.database_name = database_name

            print("✅ Connected to MongoDB Atlas")

        except Exception as e:
            raise CustomerException(e, sys)

    def upload_csv_to_mongodb(self, file_path):
        try:
            # Delete existing documents
            self.collection.delete_many({})
            print("Deleted existing data from MongoDB")

            # Read dataset
            df = pd.read_csv(file_path, delimiter="\t")

            # Clean column names
            df.columns = df.columns.str.strip()

            # Convert dataframe to dictionary
            records = df.to_dict(orient="records")

            # Insert records
            self.collection.insert_many(records)

            print("✅ Successfully uploaded records to MongoDB")

        except Exception as e:
            raise CustomerException(e, sys)