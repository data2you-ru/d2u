"""
    created by Sergei Troshin 3 May 2017.
"""
# settings to mysql amazon rds server
class SqlAWSinfo:
    HOST = 'mydata2you.cznxbajzar7d.us-west-2.rds.amazonaws.com'
    USER = 'data2you'
    PORT = 3306
    @staticmethod
    def PASSWORD():
        return open('/Users/istar/Documents/PASSWORDS/password_data2you.txt', 'r').read().strip()


