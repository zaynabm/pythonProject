import tornado.web
# import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from pymongo import MongoClient

class IndexHandler(tornado.web.RequestHandler):
      notFriendsNames=[]
      notFriendsImg=[]
      notFriendsNames=[]
      notGroupsImg=[]
      def allgroupsFun(self,email,db):
          userName=email
          myGroupsIDs=db.users.find_one({"email":userName},{"_id":0,"groups":1})
          myGroupsVal=[]
          myGroups=[]
          allGroups=[]
          notGroupsID=[]
          global notGroupsNames
          global notGroupsImg
          notGroupsNames=[]
          notGroupsImg=[]


          for key, myGroups in myGroupsIDs.items():
                  print ("val")
                  #  myGroups.append(val)

          allGroupsIDs=db.groups.find({})
          for   val in allGroupsIDs:
                  #  print("sss",val['_id'])
                   allGroups.append(val['_id'])
          for elem in allGroups:
             # if elem == myID:
             #     continue
             if elem not in myGroups:
                  # print (elem)# prints users thats is not my friends ids
                   notGroupsID.append(elem)
          for val in notGroupsID:
              myGroupsObjects=db.groups.find_one({"_id":val},{"name":1,"_id":0})
              notGroupsObjects2=db.groups.find_one({"_id":val},{"img":1,"_id":0})
              print(notGroupsObjects2)
              for  key, val in notGroupsObjects2.items():
                        #print("notgimg",val)
                        notGroupsImg.append(val)
              print(myGroupsObjects)
              for  key, val in myGroupsObjects.items():
                  #print("notGN",val)
                  notGroupsNames.append(val)

      def allusersFun(self,email,db):
          global notFriendsNames
          notFriendsNames=[]
          global notFriendsImg
          notFriendsImg=[]
          userName=email
          myFriendsIDs=db.users.find_one({"email":userName},{"_id":0,"friends":1})
          myFriendsVal=[]
          myFriends=[]
          allUsers=[]
          notFriendsID=[]
          myIDObj=db.users.find_one({"email":userName},{"_id":1})
          myID=myIDObj['_id']
          print(myID)
          for key, myFriendsVal in myFriendsIDs.items():
                   print(myFriendsVal)
          for key, val in myFriendsIDs.items():
                  #  print (val)
                   myFriends.append(val)
          allUsersIDs=db.users.find({},{"_id":1})
          for   val in allUsersIDs:
                  #  print(val['_id'])
                   allUsers.append(val['_id'])
          for elem in allUsers:
             if elem == myID:
                 continue
             if elem not in myFriendsVal:
                   #print (elem)# prints users thats is not my friends ids
                   notFriendsID.append(elem)

          for val in notFriendsID:
              myFriendsObjects=db.users.find_one({"_id":val},{"name":1,"_id":0})
              #print(myFriendsObjects)
              notFriendsObjects2=db.users.find_one({"_id":val},{"img":1,"_id":0})
              #print(notFriendsObjects2)
              for  key, val in notFriendsObjects2.items():
                        #print("notfimg",val)
                        notFriendsImg.append(val)

              for  key, val in myFriendsObjects.items():
                  #print("notf",val)
                  notFriendsNames.append(val)


      def post(self):
        #   name=""
          #print("hiiiiiiiii")
        #   self.render("../templates/index.html")
          #print("hellooooo")
          client = MongoClient('localhost', 27018)

          db = client.chatRR  # name of database
          collection=db['users'] # name of collection
          groupCollection=db['groups']
          usersCollection=db['allusers']
          # result = db.createCollection("users")
          name= self.get_argument("name", "")
          if (name==""):
             # print("oooooooooo")
              email=self.get_argument("email", "")
              password=self.get_argument("password", "")
              # name="aya"
              flag="false"
              userID=db.users.find_one({"email":email},{"_id":1})# 1 for true to get id only
              print(userID)
              #///////////////////////////////////////////
              #///////////////////// Zaynab //////////////////////
              global ID
              ID=userID['_id']
              print("zaynaaaaaaaaaab",ID)
            #   global toChat

              if(userID is None):
                 self.render("../templates/MainPage.html",test=".")
              if not(userID is None):
                  #print("hi")
                  flag="true"
                  for key, val in userID.items():

                     userPassword=db.users.find_one({"_id":val},{"password":1,"_id":0})# 1 for true to get pwd only

              givenPass=password
              if (flag is "true"):
                 for key, val in userPassword.items():
                    #print("ho")
                    #print("val",val)
                    #print("given",givenPass)
                    if(givenPass == val):
                       print("Right user")
                       userObj=db.users.find_one({"email":email},{"name":1})
                       name=userObj['name']
                       print("name of user ",name)

                       #//////////////////////////////////////////
                       #/////////////////// zaynab ///////////////////////
                       global clientName
                       print("zaaaaaaaaaaaynab",name)
                       clientName=name




                     #  ---------------my friends------------------------
                       userName=email
                       myFriendsIDs=db.users.find_one({"email":userName},{"_id":0,"friends":1})
                       print(myFriendsIDs)
                       myFriendsVal=[]
                       myFriendsNames=[]
                       myFriendsImgs=[]
                       for key, myFriendsVal in myFriendsIDs.items():
                                print("friendsval",myFriendsVal)
                       for val in myFriendsVal:
                           myFriendsObjects=db.users.find_one({"_id":val},{"name":1,"_id":0})
                          # print("myFriendsObjects",myFriendsObjects)
                           #self.write(myFriendsObjects)
                           myFriendsObjects2=db.users.find_one({"_id":val},{"img":1,"_id":0})
                           for  key, val in myFriendsObjects.items():
                                #print("val",val)
                                myFriendsNames.append(val)
                           for  key, val in myFriendsObjects2.items():
                                #print("img",val)
                                myFriendsImgs.append(val)
                       for val in myFriendsNames:
                                print(myFriendsNames)
                                #self.write("<p> val Hello hello hellooooo</p>")
                    #    -----------------------all users----------------------
                       self.allusersFun(email,db)
                     # -------------my groups----------------
                       userName=email
                       myGroupsImgs=[]
                       print(userName)
                       myGroupsIDs=db.users.find_one({"email":userName},{"_id":0,"groups":1})
                       myGroupsVal=[]
                       myGroupsNames=[]
                       #print("myGroupsIDs",myGroupsIDs)
                       for key, myGroupsVal in myGroupsIDs.items():
                                print("myGroupsVal",myGroupsVal)
                       for val in myGroupsVal:
                          # print("val",val)
                           myGroupsObjects=db.groups.find_one({"_id":val},{"name":1,"_id":0})
                           #print("myGroupsObjects",myGroupsObjects)
                           for  key, val in myGroupsObjects.items():
                                myGroupsNames.append(val)


                       for val in myGroupsNames:
                                 print(val)
                                 myGroupsObjects2=db.groups.find_one({"name":val},{"img":1,"_id":0})
                                 for  key, val in myGroupsObjects2.items():
                                            print("img",val)
                                            myGroupsImgs.append(val)
                       self.allgroupsFun(email,db)
                       self.render("../templates/index.html",loginName=name,user=myFriendsNames,img=myFriendsImgs,group=myGroupsNames,img2=myGroupsImgs,nf=notFriendsNames,nfi=notFriendsImg,ng=notGroupsNames,ngi=notGroupsImg,flag="true")
                    else:
                       print("No Login")
                       self.render("../templates/MainPage.html",test="")


          else:
              print("naaaaaaaaaaaame",name)
              email=self.get_argument("email", "")
              age=self.get_argument("age", "")
              password=self.get_argument("password", "")
              #-------------add user (sign up)----------------

              userObj=db.users.find_one({"name":name},{"_id":1})
              print("userObj",userObj)

              #////////////////////////////////
              #//////////////// Zaynab ///////////////
            #   ID=userObj['_id']
            #   print("kkkkkkkkkkkkk",ID)

              if (userObj is None):

                  addUser = db.users.insert_one(
                  {
                          "name": name,
                          "password":password,
                          "age": age,
                          "email":email,
                          "img":"111.jpg"
                  }
                  )
                  userObj=db.users.find_one({"name":name},{"_id":1})
                  print("userObj",userObj)

                    #////////////////////////////////
                    #//////////////// Zaynab ///////////////
                  ID=userObj['_id']
                  print("kkkkkkkkkkkkk",ID)
                  self.allusersFun(email,db)
                  self.allgroupsFun(email,db)
                  self.render("../templates/index.html",loginName=name,user=name,img="test",nf=notFriendsNames,nfi=notFriendsImg,ng=notGroupsNames,ngi=notGroupsImg,flag="false")

                  #////////////////////////////////////////////////////////////////////////
                  #////////////////////////////zaynabm///////////////////////////////
                  print("zayyyyyyyyyyyynab",name)

              else:
                  print("User already exists")
                  self.render("../templates/MainPage.html",test="User already exists !!")


# //////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////// zaynab //////////////////////////////////////////
################## Send Data to Chat.py #####################################################
      def sendToChat():
            toChat=clientName
            return toChat
