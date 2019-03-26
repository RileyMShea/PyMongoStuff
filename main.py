import pandas as pd
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

df = pd.DataFrame(list(mycol.find()))

print(df)