# import hm_message
from packages import hm_message

hm_message.send_message.send("hello")

txt = hm_message.receive_message.receive()
print(txt)
