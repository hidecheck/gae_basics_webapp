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


def get_all():
    client = datastore.Client()
    query = client.query(kind='Greeting')
    query.order = '-created'
    greetings = list(query.fetch())
    for entity in greetings:
        entity['id'] = entity.key.id
    return greetings


def get_by_id(key_id):
    client = datastore.Client()
    key = client.key('Greeting', int(key_id))
    entity = client.get(key=key)
    if entity:
        entity['id'] = entity.key.id
    return entity


def update(entity):
    if 'id' in entity:
        del entity['id']
    client = datastore.Client()
    client.put(entity)
    entity['id'] = entity.key.id
    return entity
