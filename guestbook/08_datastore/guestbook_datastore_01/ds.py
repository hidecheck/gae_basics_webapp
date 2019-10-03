from datetime import datetime

from google.cloud import datastore


def insert(author, message):
    client = datastore.Client()
    key = client.key("Greeting")
    entity = datastore.Entity(key=key)
    entity["author"] = author
    entity["message"] = message
    entity["created"] = datetime.now()
    client.put(entity)
    entity['id'] = entity.key.id
    return entity
