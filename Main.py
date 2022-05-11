from OrdersServer import OrdersServer

server = OrdersServer("taskdb","orders","pd54geui-pqrd-f6ao-u99e-whhz1lpjle0y")
data=server.readerData("tracking_numbers.csv")

tracklist = list(data["tracking_number"])
delivery_status=[]
shipping_date=[]
scheduled_delivery_date=[]

delivery_status,shipping_date,scheduled_delivery_date=server.gettrackData(tracklist)
print(delivery_status)
print(shipping_date)
print(scheduled_delivery_date)

#data.insert(data.shape[1],'shipping_date',delivery_status)
print(data)
data=data.to_json(orient = 'records')
server.insertData(data)


