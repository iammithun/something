
class User:
    def __init__(self):
        print("new user being created...")

user_1=User()
user_1.id='001'
user_1.username="mithun"

print(user_1.username)

user_2=User()
user_2.id="002"



class User:
    def __init__(self, user_id, username):
        self.id=user_id
        self.username=username      


print(user_1.username)

user_2=User()
user_2.id="002"


class User:
    def __init__(self, user_id, username):
        self.id=user_id
        self.username=username      
        self.followers=0  

user_1=User("001", "mithunk")

print(user_1.username)

user_2=User()
user_2.id="002"

print(user_1.followers)


class User:
    def __init__(self, user_id, username):
        self.id=user_id
        self.username=username      
        self.followers=0  
        self.following=0
    def follow(self,user):
        user.following+=1
        self.following+=1


user_1=User("001", "mithun")






print(user_1.followers)
print(user_1.following)
