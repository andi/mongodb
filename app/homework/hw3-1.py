# Andrew Erlichson
# MongoDB, Inc. Copyright 2015 - All Rights Reserved

import pymongo

def removeWorstHomework():
    connection = pymongo.MongoClient("mongodb://db")

    db = connection.school
    students = db.students

    # let's get ourselves a sequence number
    # note there are two other varients of this call as well:
    # find_one_and_delete
    # find_one_and_replace
    # all these map to the the command find_and_modify

    
    try: 
        cursor = students.find()                
        for student in cursor:
            print "student with id " + str(student['_id'])
            min_score = 100
            for score in student['scores']:
                if score['type'] == 'homework':
                    print "score " + str(score)
                    if score['score'] < min_score:
                        min_score = score['score']
            print "removing min score " + str(min_score)
            students.update_one({'_id': student['_id']}, {'$pull': {'scores': {'type': 'homework', 'score': min_score}}})
    except Exception as e:
        print "Exception: ", type(e), e

    #return counter.next()


removeWorstHomework()

