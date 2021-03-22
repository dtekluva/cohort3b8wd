import csv
import pymysql

mydb = pymysql.connect(host='localhost',
    user='root',
    passwd='',
    db='application_data')
cursor = mydb.cursor()

csv_data = csv.read(file('C:/Users/USER/Desktop/cohort3b8wd/assignments/application_data.csv',"r"))
for row in csv_data:

    cursor.execute('INSERT INTO customer_data(customer_id, /
          loan_id,application_date,loan_number,loan_amount,interest_rate,term_day,repayment_duedate,repayment_paiddate )' /
          'VALUES("%s", "%s", "%s""%s", "%s", "%s""%s", "%s", "%s")', 
          row)
#close the connection to the database.
cursor.close()
mydb.commit()


# import csv
# import pymysql
# db = pymysql.connect(host='localhost',
#                     user='root',
#                     password='',
#                     database='application_data',
#                     cursorclass=pymysql.cursors.DictCursor)

# with open("C:/Users/USER/Desktop/cohort3b8wd/assignments/application_data.csv") as csv_file:
#     csvfile = csv.reader(csv_file, delimiter=",")
#     all_value = []
#     for row in csvfile:
#         value = (row[0])
#         all_value.append(value)
#         query= "insert into 'customer_data'('customer_id','loan_id','application_date',
# 'loan_number','loan_amout','interest_rate','terms_day','repayment_duedate','repayment_paiddate')
# value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# cursor = db.cursor()
# cursor.executemany(query,all_value)
# mydb.commit


# file = open("C:/Users/USER/Desktop/cohort3b8wd/assignments/application_data.csv","r")
# data = file.readlines()
# first_row = data.pop(0)
# print(first_row)
