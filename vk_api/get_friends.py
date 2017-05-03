"""
    created by Sergei Troshin 3 May 2017.
"""
from __future__ import print_function
import vk
from my_data import MyVKData

session = vk.Session()
vkapi = vk.API(session)
frnds = vkapi.friends.get(user_id=MyVKData.MY_USER_ID, fields='domain, photo')