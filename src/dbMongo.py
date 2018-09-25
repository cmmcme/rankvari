import pymongo
from javaVari import classnameSet

conn = pymongo.MongoClient('127.0.0.1', 27017)
db = conn.get_database('rankvari')


def Collect(url, language) :
    collection = db.get_collection(language + 'vari')
    for i in classnameSet:
        collection.update( {'vari': i}, {'$inc': {'count': 1}}, upsert = True)


#
# collection = db.get_collection('javavari')
#
# collection.update(
#                     { 'vari' : 'main'}
#                     , { '$inc' : {'count' :  1}}
#                     , upsert = True
#                   )
#
# for i in classnameSet:
#     collection.update(
#         {'vari': i}
#         , {'$inc': {'count': 1}}
#         , upsert = True
#     )