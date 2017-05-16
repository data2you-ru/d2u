# -*- coding: utf-8 -*-
"""
    created by Sergey Troshin 3 May 2017.
"""
import vk
import time
from my_data import MyVKData
from tqdm import tqdm
from vkTableMaker import VkTableMaker

class VKPerson:
    # fix it - make dict
    def __init__(self, input_dict):
        """VKPerson
        class that contain all data about vk user as a structure
        :param vk_id:
        :param first_name:
        :param last_name:
        :param interests:
        """
        self.kvp = input_dict
        def keys(self):
            return self.kvp.keys()
        def __getitem__(self, k):
            return self.kvp[k]


class Vkinterests:
    main_interest = 'Фитнес'
    popular_interests = dict()

    def __init__(self, main_interest='Фитнес'):
        """
        simple worker with vkapi to get info about personal inerests (hobbies)
        :param main_interest: string that represent information about the interest
        """
        self.main_interest = main_interest
        #  array that collect all persons gotten from vk-api
        self.persons = []

    def process_data(self, local, append):
        """
        :param local:  if local - create connection with local sql mashine
        :param append: if append - just uppend rows in existing table
        this function also create connection to mysql server
        """
        # connect to api using config file - need directory with password!!
        # I used my password and login from VK
        session = vk.AuthSession(app_id=MyVKData.APP_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.PASSWORD())
        vkapi = vk.API(session)
        offs = 0
        #if we need information about all interests
        # maybe to extract more popular
        all_interests = dict()
        # this loop can be depreciated using vk-script /
        # but now it needed due to the problem when vk takes you /
        # information only about small group of people
        # but using the 'offset' field you can make shifts
        # and collect new persons per querry
        table = VkTableMaker(
            title='Таблица вк по интересам',
            table_name='VK_interests',
            params='Id INT PRIMARY KEY AUTO_INCREMENT, vk_id INT, first_name VARCHAR(25), last_name VARCHAR(25), interests VARCHAR(25)',
            russian_keys=['first_name', 'last_name', 'main_interest'],
            local=local
        )
        for i in tqdm(range(100)):
            try:
                usrs = vkapi.users.search(interests=self.main_interest, extended=1, fields='interests', offset=offs)
                # return : [<count> , <dicts>]
                count = usrs[0]
                usrs = usrs[1:]
                offs += len(usrs) + 1
                for usr in usrs:
                    person_info = dict()
                    person_info['vk_id'] = str(usr['uid'])
                    person_info['first_name'] = "'"+usr['first_name']+"'"
                    if ('last_name' in usr):
                        person_info['last_name'] = "'"+usr['last_name']+"'"
                    if ('interests' in usr):
                        person_info['interests'] = "'" + usr['interests'].split(',')[0] + "'"
                        # for inter in usr['interests'].split(','):
                        #    inter = inter.strip()
                        #    if inter in all_interests:
                        #       all_interests[inter] += 1
                        #   else:
                        #       all_interests[inter] = 1
                    self.persons.append(VKPerson(person_info))
                time.sleep(0.3)
            #  fix it
            except Exception('ReadTimeout'):
                time.sleep(1)
                print("ReadTimeOut")
            if i == 0:
                self.add_all_data_to_sql(table, local, append)
            else:
                self.add_all_data_to_sql(table, local, True, False)
            #  free resources
            del self.persons
            self.persons = []
        # self.popular_interests = all_interests
        print("\nall users successfully downloaded and wait u on the server\n".format(len(all_interests)))
        return

    def add_all_data_to_sql(self, table, local, append, ask_permission=True):
        if (not append):
            table.rewrite_table_if_exist()
        if not ask_permission or table.ask_yes("\nDo you want to add rows in table {1}? ".format(len(self.persons), table.table_name)):
            table.add_rows(self.persons)
        else:
            return
        self.table = table



def main():
    vkint = Vkinterests()
    vkint.process_data(local=True, append=False)
main()



