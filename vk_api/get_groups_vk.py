import vk
from my_data import MyVKData
session = vk.AuthSession(app_id=MyVKData.APP_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.PASSWORD)
vkapi = vk.API(session)
groups = vkapi.groups.get(user_id=MyVKData.MY_USER_ID, extended=1)
print(groups)
