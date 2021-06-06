from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types.contacts import Contacts
from telethon.tl.types import User
####################################################################
def get(val:str):
    if val:
        return f"{val}"
    return ""
####################################################################

stack={} # i like to have clipboard memory for stacking things like user and msgs or etc
contacts=[]
###################################################################
#functions
def contact2entity(usr): #first_name-last_name id username phone
    if usr[1]!="":
        return int(usr[1])
    if usr[2]!="":
        return usr[2]
    if usr[3]!="":
        return "+"+usr[3]
    return ""

####################################################################
# commands

key_contacts="contacts"
stack[key_contacts]=[]


#####################################################################
api_id = 5910285
api_hash = "24e02b08be3f6a8085264780efb57af9"
client=TelegramClient('anon',api_id,api_hash)
client.start()
print("telegram connected...")





while True:
    print("enter command\n\texit\n\tcontacts <pattern>\n\tsend <index> <text|file> <msg|filename>")
    data=input().split(" ")
    cmd=data.pop(0)
    ###########################################################################################################################
    if cmd=="exit":
        print("exiting...")
        client.disconnect()
        #if we save json it so good
        break
    ###########################################################################################################################
    elif cmd=="contacts":
        #######################################################################################################################
        # load users
        if contacts==[]:
            with client:
                result:Contacts=client.loop.run_until_complete(client(GetContactsRequest(0)))
                for user in result.users:
                    user:User
                    contacts.append([get(user.first_name)+" "+get(user.last_name),get(user.id),get(user.username),get(user.phone)])
        ########################################################################################################################               
        stack[key_contacts]=[]
        if data==[]:
            data.append("")
        for pat in data:
            for usr in contacts:
                for usr_info in usr:
                    if pat.lower() in usr_info.lower():
                        stack[key_contacts].append(usr)
                        break

        print("search Result..")
        for i in range(len(stack[key_contacts])):
            res=""
            for user_info in stack[key_contacts][i]:
                res+=f"{user_info} "
            print(f"{i}) {res}")
        print(f"{len(stack[key_contacts])} result.")
    ####################################################################################################################
    elif cmd=="send":
        if len(data)<3:
            print("too low arguments.")
            continue        
        
        usr=data.pop(0)
        if usr.isdigit() and int(usr)>=0 and len(stack[key_contacts])>int(usr):
            usr=stack[key_contacts][int(usr)]
            entity=contact2entity(usr)
            if entity=="":
                print("this user have no connect line.")
                continue
        else:
            print("unable to find user.")
            continue
        
        typ=data.pop(0)
        if typ=="file":
            fname=" ".join(data)
            try:
                f=open(fname)
            except:
                print("Cant find this file.")
                continue
        elif typ=="text":
            msg=" ".join(data)
        else:
            print("unkown message type.")
            continue




