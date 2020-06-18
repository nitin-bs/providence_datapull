import pymysql.cursors
import csv
import json
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Inf0w0rks!',
                             db='providence',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
  
    with connection.cursor() as cursor:
        # Read a single record
        sql = "select A.params,B.installationId from DataFoundry as A join license as B on A.provisioningId=B.provisioningId"
        cursor.execute(sql)
        column_names = [i[0] for i in cursor.description]
        result = cursor.fetchall()
        print(result)
        with open('hosts.json', 'w') as outfile:
            json.dump(result, outfile)
        #fp = open('hosts.csv', 'w')
        #myFile = csv.writer(fp)
        #myFile.writerow(column_names)
        #myFile.writerows(result)
        #fp.close()
        #print(result)
finally:
    connection.close()
