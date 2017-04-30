# -*- coding: utf-8 -*-
import vk
from my_data import MyVKData
session = vk.AuthSession(app_id=MyVKData.APP_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.PASSWORD())
vkapi = vk.API(session)

INTERESTS = ['Python, Программирование']

AGE_FROM = 17
AGE_TO = 20

SEX = 1  # женский
CITY = 1 # Москва

users = vkapi.users.search(interests=','.join(INTERESTS), city=CITY, sex=SEX, age_from=AGE_FROM, age_to=AGE_TO)
print(users)
