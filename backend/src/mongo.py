from bson.objectid import ObjectId
from pymongo import MongoClient


class MongoDBHelper:
    def __init__(
        self, connection_string: str, database_name: str, collection_name: str
    ):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def create(self, document: dict) -> str:
        """
        Insert a new document into the collection.
        :param document: The document to insert.
        :return: The ID of the inserted document.
        """
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def retrieve(self, document_id: str) -> dict:
        """
        Retrieve a single document by its ID.
        :param document_id: The ID of the document to retrieve.
        :return: The document, or None if not found.
        """
        return self.collection.find_one({"_id": ObjectId(document_id)})

    def update(self, document_id: str, updates: dict) -> bool:
        """
        Update a document by its ID.
        :param document_id: The ID of the document to update.
        :param updates: A dictionary of updates to apply.
        :return: True if the document was updated, False otherwise.
        """
        result = self.collection.update_one(
            {"_id": ObjectId(document_id)}, {"$set": updates}
        )
        return result.modified_count > 0

    def delete(self, document_id: str) -> bool:
        """
        Delete a document by its ID.
        :param document_id: The ID of the document to delete.
        :return: True if the document was deleted, False otherwise.
        """
        result = self.collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count > 0

    def close_connection(self):
        """
        Close the connection to the MongoDB server.
        """
        self.client.close()

