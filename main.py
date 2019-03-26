import pandas as pd
from pymongo import MongoClient
import pymongo
from pymongo.results import UpdateResult
import json
from pprint import pprint


def connect(address="mongodb://localhost:27017/"):
    myclient = MongoClient(address)
    return myclient


def add_csv(myclient, csv_file='autos.csv', db='udacity', col='autos'):
    mydb = myclient[db]
    mycol = mydb[col]

    df = pd.read_csv(csv_file, encoding='ISO-8859-1')

    # important - must have orient as records
    jsoned_data = json.loads(df.to_json(orient='records'))
    try:
        from pymongo.errors import BulkWriteError
        result = mycol.insert_many(jsoned_data)
    except BulkWriteError as bwe:
        print("Bulk write error occurred")
        pprint(bwe.details)


    #print(result.matched_count)


def get_distinct(myclient=MongoClient("mongodb://localhost:27017/"), db='udacity', col='autos'):
    distinct = myclient[db][col].distinct("URI")
    print("{} distinct records".format(len(distinct)))


def in_query():
    # Modify the below line with your query; try to use the $in operator.
    query = {}

    return query

if __name__ == "__main__":
    connect = connect()
    get_distinct()
    add_csv(myclient=connect)
