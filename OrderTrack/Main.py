from OrdersServer import OrdersServer
import pandas as pd


server = OrdersServer("taskdb","orders","pd54geui-pqrd-f6ao-u99e-whhz1lpjle0y")
data=server.readerData("tracking_numbers.csv")

tracklist = list(data["tracking_number"])

data=server.createTrackData(data,tracklist)

'''Output data as panda.DataFrame'''
print(data)

'''Insert data to MongoDB'''
data=data.to_json(orient = 'records')
server.insertData(data)


