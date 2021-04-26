#Write a small program that takes in any sentence or 
#speech and breaks down all the word into a dictionary 
#containing the word as key and a 
#list/dictionary of the length of the word, 
#and number of vowels in the word

# take_in= (input("enter your take_in:").casefold()).split(" ")
# print(take_in)
# takein_dic = {}
# vowels = ("a","e","i","o","u")

# for word in take_in:
#     vowelscount = 0
#     for char in word:
#         if char in vowels:
#             vowelscount +=1
#     takein_dic[word] = {"lenght":len(word),"vowels":vowelscount}
# print(takein_dic)

"""
    CREATE TABLE userTable (id INT(9) PRIMARY KEY AUTO_INCREMENT NOT NULL, 
                            name char(50), 
                            bank_name CHAR(30), 
                            account_no CHAR(12), 
                            employed DATE()
                            );


    CREATE TABLE salary (id INT(9) PRIMARY KEY AUTO_INCREMENT NOT NULL, 
                            userId INT(9), 
                            salaryFor DATE, 
                            netPay FLOAT(12,3), 
                            FOREIGN KEY (userId) references userTable (id)
                            )

"""


import pandas as pd
import pymysql.cursors

def format_date(bad_date):

    if isinstance(bad_date, float):
        return "0000-00-00"
    else:
        bad_date = bad_date.split("/")
        
        good_date = f"{bad_date[2]}-{bad_date[1]}-{bad_date[0]}"
        ############### year           month          day
        # print(good_date)
        return good_date


file = pd.read_csv("C:/Users/kboys/OneDrive/Desktop/CLASSES/UNIVELCITY CLASSES/cohort3b8wd/atha/mysql/June payslip with DOB-DOH.csv")


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='liberty',
                             cursorclass=pymysql.cursors.DictCursor)



with connection:
    with connection.cursor() as cursor:

        for index, row in file.iterrows():
            employee_no   = row["Employee Number"]      
            sname   = str(row["Surname Name"])      
            fname   = str(row["First Name"])        
            mname   = str(row["Middle Name"])        
            bank_name   = row["Bank Name"]   
            acct        = row["Account No"]    
            pay         = row["Netpay"]          
            hired       = row["Date of Hire" ]
            # print(sname, fname)
            command = f"""
                            INSERT INTO usertable(EmployeeId, 
                                                    name , 
                                                    bank_name, 
                                                    account_no, 
                                                    employed) 
                                                    VALUES(
                                                        {employee_no}, 
                                                        "{sname + " " + fname + " " + mname}", 
                                                        "{bank_name}", 
                                                        "{acct}", 
                                                        "{format_date(hired)}");
                        """
            cursor.execute(command)

            command_salary = f"""
                                INSERT INTO salary(userId, salaryFor , netPay) VALUES("{employee_no}", "2020-06-28", "{pay}");
            """
            
            cursor.execute(command_salary)


        connection.commit()
        