# from VK api to database

These part of data2you projects implemets some scripts like sql_connector, vkToSql, vkTableMaker. You have an example of how to get data form VK and export it in your mySQL server in vkToSql file;

## Getting Started

To start with clone our rep
```
git clone https://github.com/data2you-ru/d2u
```

### Prerequisites

python 2.7 or higher required
MySQLdb library
tqdm
vk

```
pip install vk
pip install MySQL-python
conda install -c conda-forge tqdm=4.11.2
```

### Using and examples

this code gets some data from vk-api and puts it in your local sql server database using config.py file and my_data.py where are your vk configs
```
from vkToSql import Vkinterests
vkint = Vkinterests()
vkint.get_data()
vkint.add_all_data_to_sql(local=True, append=False)
```



