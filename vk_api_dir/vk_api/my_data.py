"""
    created by Sergei Troshin 3 May 2017.
"""
class MyVKData:
    # my user id for vk.com
    MY_USER_ID = '40819504'

    DUROV_USER_ID = '1'

    API_URL = 'https://api.vk.com/method/'
    #  id of my vk app
    APP_ID = '6010130'

    LOGIN = 'sergei-troshin@mail.ru'

    @staticmethod
    def PASSWORD():
        print "password: "
        # return raw_input().strip()
        f = open('/Users/istar/Documents/PASSWORDS/vk_pass.txt').read().strip()
        return f




