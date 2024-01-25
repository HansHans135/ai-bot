with open("old_msg.txt","r",encoding="utf-8")as f:
    old=f.readlines()

msg=""
for i in old:
    temp=i.split(":")
    now_msg=""
    for a in temp[1:]:
        now_msg+=a
    if len(now_msg)>3:
        msg+=now_msg[1:]
with open("msg.txt","w",encoding="utf-8")as f:
    f.write(msg)
