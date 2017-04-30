# -*- coding: utf-8 -*-
import vk
from my_data import MyVKData
session = vk.AuthSession(app_id=MyVKData.APP_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.PASSWORD(), scope='wall')
vkapi = vk.API(session)
MESSAGE = "DEL"
vkapi.wall.post(message=MESSAGE)
