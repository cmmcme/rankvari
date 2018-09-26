import pymongo
import re

conn = pymongo.MongoClient('127.0.0.1', 27017)
db = conn.get_database('rankvari')
collection = db.get_collection('javavari')

dataArr = collection.find()
newcollection = db.get_collection('wordjavavari')
print(dataArr.count())

for data in dataArr:
    count = data['count']
    vari = str(data['vari'])
    pattern = re.compile('[A-Z][a-z0-9]+')
    words = pattern.findall(vari)
    for word in words:
        print(word, count)
        newcollection.update( {'vari': word}, {'$inc': {'count': count}}, upsert = True)
