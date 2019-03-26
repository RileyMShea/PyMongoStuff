import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["proxies"]

addresses = mycol.find({}, {"_id": 0, "IP_Address": 1, "Port": 1})

ready_list = []
for address in addresses:
    out = "{}:{}".format(address['IP_Address'],
                         address['Port'])

    ready_list.append(out)

[print(x) for x in ready_list]
