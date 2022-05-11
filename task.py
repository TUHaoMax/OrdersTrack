import pymongo as pm
from zmq.sugar import tracker
import pandas
import pandas as pd
import json

#client = pm.MongoClient()
#mydb = client["taskdb"]
#mycol = mydb["orders"]

#def readerData( fileName):
#    with open("./{}".format(fileName)) as f:
#        data = pd.read_csv(f)
#    return data

#data = readerData("tracking_numbers.csv")
#data=data.to_json(orient = 'records')
#print(data)
#data = json.loads( data )
#mycol.insert_many(data)