import requests
from my_data import MyVKData
#  how was before 
response = requests.get(MyVKData.API_URL+'users.get', {'user_ids' : MyVKData.DUROV_USER_ID + ',' + MyVKData.MY_USER_ID})

result = response.text

print(result)