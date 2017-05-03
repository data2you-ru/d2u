# -*- coding: utf-8 -*-
import vk
import time
from my_data import MyVKData
session = vk.AuthSession(app_id=MyVKData.APP_ID, user_login=MyVKData.LOGIN, user_password="")
vkapi = vk.API(session)
offs = 0
all_interests = dict()
for i in range(100):
    usrs = vkapi.users.search(interests='Фитнес', extended=1, fields='interests', offset=offs)
    print(usrs)
    break;
    count = usrs[0]
    usrs = usrs[1:]
    offs += len(usrs) + 1
    for i in usrs:
        if ('interests' in i):
            print i['first_name'], i['interests']
            for inter in i['interests'].split(','):
                inter = inter.strip()
                if inter in all_interests:
                    all_interests[inter] += 1
                else:
                    all_interests[inter] = 1
    time.sleep(0.3)
for interest in sorted(all_interests.items(), key=lambda x: x[1], reverse=True):
    print interest[0], interest[1]


