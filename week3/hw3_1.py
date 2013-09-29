
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the reddit database
db=connection.school
students = db.students


def del_lowest_hw():

    try:
        iter = students.find()

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in iter:
        scores = doc["scores"]
        if scores[2]["score"] > scores[3]["score"]:
		    scores.remove(scores[3])
        else:
		    scores.remove(scores[2])
        students.update({'_id': doc['_id']}, {'scores': scores})

del_lowest_hw()

