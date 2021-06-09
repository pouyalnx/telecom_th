from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types.contacts import Contacts
from telethon.tl.types import User,Chat
from telethon.tl.types import Dialog
from telethon.tl.patched import Message
from telethon.events import NewMessage

###################################################################
api_id = 5910285
api_hash = "24e02b08be3f6a8085264780efb57af9"
client=TelegramClient('anon',api_id,api_hash)
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

def chat2entity(usr): #id title
    if usr[0]!="":
        return int(usr[0])
    return ""

####################################################################
# commands

key_contacts="contacts"
key_chats_id="chat_id"
key_new_message="new_message"
key_new_message_id="new_message_id"
key_inbox_id="inbox_id"
key_dialog_id="dialog_id"

stack[key_contacts]={}
stack[key_chats_id]={}
stack[key_new_message_id]={}
stack[key_inbox_id]={}
stack[key_dialog_id]={}


####################################################################
def get_at_least_one_name(name1,name2,name3):
    if name1:
        return f"{name1}"
    elif name2:
        return f"{name2}"
    elif name3:
        return f"{name3}"
    return "[u[k[no]w]n]"

####################################################################
inbox=[]

#events
@client.on(NewMessage(incoming=True))
async def newMessage(event:NewMessage.Event):
    msg:Message=event.message
    sender:User=await msg.get_sender()
    inbox.append([msg.chat_id,get_at_least_one_name(sender.username,sender.first_name,sender.last_name)])
    print(f">>**icnome_message from {get_at_least_one_name(sender.username,sender.first_name,sender.last_name)}**<<")




#####################################################################
import asyncio
import threading

async def ainput():
    loop=asyncio.get_event_loop()
    fut=loop.create_future()
    def _run():
        inp=input()
        loop.call_soon_threadsafe(fut.set_result,inp)
    threading.Thread(target=_run,daemon=True).start()
    return await fut

###############################################################################################################################
async def handler(client):
    while True:
        print("********************************************")
        print("enter command\n\texit\n\tcontacts <pattern>\n\tsend <index> <text|file> <msg|filename>\n\tdialog <pattern>\n\tinbox [clr]")
        print("--------------------------------------------")
        data=(await ainput()).split(" ")
        cmd=data.pop(0)
        ###########################################################################################################################
        if cmd=="exit":
            print("exiting...")
            await client.disconnect()
            #if we save json it so good
            break
        ###########################################################################################################################
        elif cmd=="contacts":
            #######################################################################################################################
            # load users
            if contacts==[]:
                result:Contacts=await client(GetContactsRequest(0))
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
            elif len(usr)>=2 and usr[0]=='c' and usr[1:].isdigit() and int(usr[1:])>=0 and len(stack[key_chats_id])>int(usr[1:]):
                usr=stack[key_chats_id][int(usr[1:])]
                entity=chat2entity(usr)
                if entity=="":
                    print("this user have no connect line.")
                    continue
            elif len(usr)>=2 and usr[0]=='i' and usr[1:].isdigit() and int(usr[1:])>=0 and len(stack[key_new_message_id])>int(usr[1:]):
                usr=stack[key_new_message_id][int(usr[1:])]
                entity=chat2entity(usr)
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
                    f=open(fname,'rb')
                except:
                    print("Cant find this file.")
                    continue
                
                await client.send_message(entity,file=f)
                f.close()
            elif typ=="text":
                msg=" ".join(data)
                await client.send_message(entity,msg)

            else:
                print("unkown message type.")
                continue
        #############################################################################################################################
        elif cmd=="dialog":
            if data==[]:
                data.append("")
            stack[key_dialog_id]={}

            pos=0
            async for dialog in client.iter_dialogs():
                dialog:Dialog
                for pat in data:
                    if pat.lower() in  dialog.title.lower():
                        stack[key_dialog_id][f"d{pos}"]=[dialog.id,get(dialog.title)]


            print("|\tindex\t|\t info")
            for pos,infos in stack[key_dialog_id].items():
                txt=""
                for info in infos:
                    txt+=f"{info} "
                print(f"|\t{pos}\t|\t{txt}")    
            print(f"<<<<<<results {len(stack[key_dialog_id])}>>>>>>>>")
        ##############################################################################################################################
        elif cmd=="inbox":
            global inbox
            if data==[] or data[0]=="list":
                if len(inbox):
                    checked=[]
                    stack[key_inbox_id]={}
                    inbox_id=[x[0] for x in inbox]

                    ptr=0
                    chat_id_pos=len(inbox_id)
                    print("id\tsender\ttext") 
                    for chat_id in reversed(inbox_id):
                        chat_id_pos-=1
                        
                        if not(chat_id in checked):
                            checked.append(chat_id)
                            cnt=inbox_id.count(chat_id)
                            stack[key_inbox_id][f"i{ptr}"]=[inbox[chat_id_pos][0],inbox[chat_id_pos][1]] # for avoid pointers
                            ptr+=1
                            
                            print(f"i{ptr}\t{inbox[chat_id_pos][1]}")
                            async for msg in client.iter_messages(chat_id,from_user=chat_id,):
                                if cnt==0:
                                    break
                                cnt-=1
                                msg:Message
                                print(f"\t\t\t{msg.raw_text}")
                    
                else:
                    print("inbox is empty")
            elif data[0]=="clr":
                inbox=[]
                print("inbox cleared")
            else:
                print("I can't decode ur input")
        ######################################################################################################################################
        elif cmd=="stack":
            pass    

#####################################################################
client.start()
client.loop.create_task(handler(client))
print("telegram connected...")
client.run_until_disconnected()
###############################################################################################################################
######################################################################################################################
#   this type of apps realy new for me all of it just a one thread and controling app new to use 
#   async and event asyc for suspending all operations that new time to executed and give control
#   to other functions
#   
#   
