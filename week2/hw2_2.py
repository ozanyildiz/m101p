
import pymongo
import sys

#establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

#get a handle to the school database
db = connection.students
grades = db.grades

def del_lowest_hw_score():
		
	query = {'type': 'homework'}
	
	try:
		cursor = grades.find(query).sort([("student_id", \
				 pymongo.ASCENDING), ("score", pymongo.ASCENDING)])
	except:
		print "Unexpected error: ", sys.exc_info()[0]
		
	previous_student_id = -1
	current_student_id = -1
	for doc in cursor:
		current_student_id = doc['student_id']
		if current_student_id != previous_student_id:
			#print doc
			grades.remove({"_id": doc["_id"]})
		previous_student_id = current_student_id
	
del_lowest_hw_score()
	
