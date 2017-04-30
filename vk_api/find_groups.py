# -*- coding: utf-8 -*-
import vk
from my_data import MyVKData
session = vk.AuthSession(app_id=MyVKData.APP_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.PASSWORD())
vkapi = vk.API(session)
groups = vkapi.groups.search(q='Музыка', count=30)
print(groups)
