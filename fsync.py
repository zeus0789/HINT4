from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import json

SECRET = 'KhGkMigTi9aD4Vv4zsz8xISP2kU5I7rgq265DXiZ'
DSN = 'https://hint-ec580.firebaseio.com'
EMAIL = 'abhishek.tiwari3507@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

def uploadarticle(idno, body, headline, author, downvote, upvote):
    data={'body' :body, 'author' :author, 'headline':headline, 'idno': idno,'downvote':downvote, 'upvote':upvote}
    putpath="/articles/"+str(idno)
    firebase.patch(putpath, data)

def fetcharticle(idno):
    data = firebase.get("/articles/"+str(idno), None)
    return data

# #Test
# uploadarticle("2+", "hello hi byt", "HHHH", "HHHHHHHHHH")

