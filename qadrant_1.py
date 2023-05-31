""" 
  Try qdrant 
  https://www.youtube.com/watch?v=LRcZ9pbGnno
  
  uncomment on 1st run : client.create_collection 
"""

from qdrant_client import QdrantClient
from qdrant_client.http import models
import numpy as np
from faker import Faker

# make client : connection
client = QdrantClient(host="localhost",port=6333)

my_collection = "first_collection"
# client.create_collection(collection_name=my_collection, 
#                          vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE))


data = np.random.uniform(low=-1.0, high=1.0, size=(1000, 100))
index = list(range(1_000))
print(data[:2,10])


# upsert
client.upsert(
    collection_name=my_collection,
    points=models.Batch(
        ids=index,
        vectors=data.tolist()
    )
)
 
# retrieve
client.retrieve(collection_name=my_collection,
                ids=[10,14,500],
                # with vectors=True
)


fake_something = Faker()
fsm = fake_something.name(), fake_something.address()
# print(fsm)

payload = []

for i in range(1_000):
    payload.append(
        {
            "artist" : fake_something.name(),
            "song" : "".join(fake_something.words()),
            "url_song" : fake_something.url(),
            "year" : fake_something.year(),
            "country" : fake_something.country(),
            
        }
    )
from pprint import pprint
pprint(payload[:5])

#
# client.upsert(
#     collection_name=my_collection,
#     points = models.Batch(
#         ids=index,
#         vectors=data.tolist(),
#         payloads=payload
        
#     )
# )

living = np.random.uniform(low=-1.0, high=1.0, size=(100)).tolist()

#print(living[:4])

res = client.search(collection_name=my_collection, 
              query_vector=living,
              limit=10)

pprint(res)
