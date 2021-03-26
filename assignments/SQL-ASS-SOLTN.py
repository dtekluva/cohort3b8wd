# import pymysql.cursors

# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='',
#                              database='univelcity',
#                              cursorclass=pymysql.cursors.DictCursor)

# file = open("C:/Users/kboys/OneDrive/Desktop/CLASSES/UNIVELCITY CLASSES/cohort3b8wd/assignments/application_data.csv", "r")
# data = file.readlines() # READ FILE LINE BY LINE

# first_row = data.pop(0) # SEE THE HEADERS OF THE FILE. THIS IS THE FIRST COLUMN OF OUR FILE.
# print(first_row) # print headers

# file.close() # close file after reading values.


# with connection:
#     with connection.cursor() as cursor:
#         # # LOOP THROUGH EACH LINE OF THE TEXT
#         for line in data:
#             # print(line)
#             splitted_row = line.split(",")
#             # print(splitted_row)

#             command = f"""
#                             INSERT INTO application_data (customerID,
#                                                         loanId,
#                                                         appilcationDate,
#                                                         LoanNumber,
#                                                         LoanAmount,
#                                                         InterestRate,
#                                                         TermDays,
#                                                         repaymentDueDate,
#                                                         repaymentPaidDate
#                                                         )
#                                                 VALUES(
#                                                     "{splitted_row[0]}",
#                                                     "{splitted_row[1]}",
#                                                     "{splitted_row[2]}",
#                                                     "{splitted_row[3]}",
#                                                     "{splitted_row[4]}",
#                                                     "{splitted_row[5]}",
#                                                     "{splitted_row[6]}",
#                                                     "{splitted_row[7]}",
#                                                     "{splitted_row[8]}"
#                                                     )
#                         """

#             cursor.execute(command)

#         # connection is not autocommit by default. So you must commit to save
#         # your changes.
#         connection.commit()



# """
# CREATE TABLE application_data (customerID VARCHAR(9),
#                                     loanId VARCHAR(9),
#                                     appilcationDate VARCHAR(9),
#                                     LoanNumber VARCHAR(9),
#                                     LoanAmount INT(9),
#                                     InterestRate INT(9),
#                                     TermDays INT(9),
#                                     repaymentDueDate VARCHAR(9),
#                                     repaymentPaidDate VARCHAR(9)
#                                     )
# """




#################################################################
########### DEVIATION FOR LAMI ##################################
##############   AUTOMATIC TIME POPULATE#########################
#################################################################


import pymysql.cursors
from datetime import datetime

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='univelcity',
                             cursorclass=pymysql.cursors.DictCursor)

file = open("C:/Users/kboys/OneDrive/Desktop/CLASSES/UNIVELCITY CLASSES/cohort3b8wd/assignments/application_data.csv", "r")
data = file.readlines() # READ FILE LINE BY LINE

first_row = data.pop(0) # SEE THE HEADERS OF THE FILE. THIS IS THE FIRST COLUMN OF OUR FILE.
print(first_row) # print headers

file.close() # close file after reading values.


with connection:
    with connection.cursor() as cursor:
        # # LOOP THROUGH EACH LINE OF THE TEXT
        for line in data:
            # print(line)
            splitted_row = line.split(",")
            # print(splitted_row)

            command = f"""
                            INSERT INTO application_data (customerID,
                                                        loanId,
                                                        appilcationDate,
                                                        LoanNumber,
                                                        LoanAmount,
                                                        InterestRate,
                                                        TermDays,
                                                        repaymentDueDate,
                                                        repaymentPaidDate
                                                        )
                                                VALUES(
                                                    "{splitted_row[0]}",
                                                    "{splitted_row[1]}",
                                                    "{splitted_row[2]}",
                                                    "{splitted_row[3]}",
                                                    "{splitted_row[4]}",
                                                    "{splitted_row[5]}",
                                                    "{splitted_row[6]}",
                                                    "{splitted_row[7]}",
                                                    "{(datetime.now())}"
                                                    )
                        """

            cursor.execute(command)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()



"""
CREATE TABLE application_data (customerID VARCHAR(9),
                                    loanId VARCHAR(9),
                                    appilcationDate VARCHAR(9),
                                    LoanNumber VARCHAR(9),
                                    LoanAmount INT(9),
                                    InterestRate INT(9),
                                    TermDays INT(9),
                                    repaymentDueDate VARCHAR(9),
                                    repaymentPaidDate VARCHAR(9)
                                    )
"""