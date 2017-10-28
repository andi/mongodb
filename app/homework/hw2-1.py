# Andrew Erlichson
# MongoDB, Inc. Copyright 2015 - All Rights Reserved

import pymongo

def findStudent():
    connection = pymongo.MongoClient("mongodb://db")

    db = connection.students
    grades = db.grades

    # let's get ourselves a sequence number
    # note there are two other varients of this call as well:
    # find_one_and_delete
    # find_one_and_replace
    # all these map to the the command find_and_modify

    
    try: 
        counter = grades.find({'type': 'exam', 'score': {'$gte': 65}}).sort('score', pymongo.ASCENDING)
    except Exception as e:
        print "Exception: ", type(e), e

    return counter.next()


print findStudent()
