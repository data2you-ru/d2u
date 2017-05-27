import vk
from my_data import MyVKData

class API_from_my_data:
    @classmethod
    def get_api(self):
        session = vk.AuthSession(app_id=MyVKData.APP_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.PASSWORD())
        vkapi = vk.API(session)
        return vkapi
class Token_auth:
    @classmethod
    def get_api(self), token):
        session = vk.AuthSession(access_token=token)
        vkapi = vk.API(session)
        return vkapi
