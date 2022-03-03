import cx_Oracle as ora
from seoul.models import Vaccine

# try:
#     conn=ora.connect("ora_user/1234@localhost:1521/orcl")
# except Exception as e:
#         print('예외 발생')
# return conn
# print(conn)

qs = Vaccine.objects.all()
    
# cursor.close()
# conn.close()

