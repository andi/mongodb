# Andrew Erlichson
# MongoDB, Inc. Copyright 2015 - All Rights Reserved

import pymongo

def removeWorstHomework():
    connection = pymongo.MongoClient("mongodb://db")

    db = connection.students
    grades = db.grades

    # let's get ourselves a sequence number
    # note there are two other varients of this call as well:
    # find_one_and_delete
    # find_one_and_replace
    # all these map to the the command find_and_modify

    
    try: 
        cursor = grades.find({'type': 'homework'}).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])                
        prev_student_id = None
        for grade in cursor:
            if prev_student_id != grade['student_id']:
                print "deleting grade with id " + str(grade['_id'])
                grades.delete_one({'_id': grade['_id']})
                prev_student_id = grade['student_id']
            #if prev_student_id != grade
    except Exception as e:
        print "Exception: ", type(e), e

    #return counter.next()


removeWorstHomework()

