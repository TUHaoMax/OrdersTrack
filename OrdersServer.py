import pandas as pd
import pymongo as pm
import json
import trackApi

class OrdersServer(object):

    client = pm.MongoClient()

    def __init__(self, dbName, colName,apikey):
        self.mydb = self.client[dbName]
        self.mycol = self.mydb[colName]
        self.apiKey = apikey
        self.tracker = trackApi.TrackingApi(self.apiKey)
        self.tracker.sandbox = True

    def readerData(self, fileName):
        with open("./{}".format(fileName)) as f:
            data = pd.read_csv(f)
        return data

    def insertData(self, data):
        self.mycol.insert_many(json.loads(data))

    def gettrackData(self, tracklist):
        delivery_status = []
        shipping_date = []
        scheduled_delivery_date = []
        for trackNumber in tracklist:
           get: str = "get?tracking_numbers={}".format(trackNumber)
           result = self.tracker.doRequest(get)
           data = json.loads(result.decode('utf-8'))
           delivery_status.append( (data["data"][0]["delivery_status"]) )
           shipping_date.append( (data["data"][0]["shipping_date"])  )
           scheduled_delivery_date.append( (data["data"][0]["scheduled_delivery_date"])  )

        return delivery_status,shipping_date,scheduled_delivery_date