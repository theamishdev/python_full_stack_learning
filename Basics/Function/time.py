""" import time 
from datetime import datetime
def update_logged_in():
    global last_logged_in_time
    last_logged_in_time=datetime.fromtimestamp(a)
    print(last_logged_in_time)
a=time.time()
last_logged_in_time=datetime.fromtimestamp(a)
print(a)
print(last_logged_in_time)
update_logged_in()
 """
from datetime import datetime

last_logged_in_time = datetime.now()
print(last_logged_in_time)

def update_in():
    global last_logged_in_time
    last_logged_in_time = datetime.now()
    print("Updated to:" , last_logged_in_time)

update_in()
