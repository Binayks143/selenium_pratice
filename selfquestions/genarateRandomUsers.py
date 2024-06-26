#wakefit

# "user_id"=66
# "name"="binay"
# "email"="bin@gmail.com"
# "address"=
import string
import random
import uuid


def random_name(l):
    letters=string.ascii_letters
    return  ''.join(random.choice(letters) for i in range(l))

def random_email():
    d=["xyz.com","test.com","mail.com"]
    return f"{random_name(10)}@{random.choice(d)}"

def genrate_unique_user_data(n):
    users=[]

    for i in range(n):
        user={

            'name':f"{random_name(5)} {random_name(9)}",
            'email':random_email(),
            'user_id':str(uuid.uuid4())
        }
        users.append(user)

    return users

user_data=genrate_unique_user_data(10)

for i in user_data:
    print(i)


