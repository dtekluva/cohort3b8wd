from dbmanager import Db_Guru


# username = doadmin
# password = yl3n3b1wwbi2qtcd hide
# host = db-mysql-nyc3-47818-do-user-4304571-0.b.db.ondigitalocean.com
# port = 25060
# database = defaultdb
# sslmode = REQUIRED


guru = Db_Guru("104.248.234.43", "monty", "todo", password="19Sedimat@54") # CREATE AN INSTANCE OUR DB_MANAGER CLASS WHICH WOULD BE USED FOR ALL INTERACTIONS
logged_in_user = None # GLOBAL VARIABLE TO HOUSE USER DETAILS WHEN SUCCESSFULLY LOGGED IN, VALUE IS EMPTY AT FIRST AND DATA IS ASSIGNED WHEN A SUCCESSFUL LOGGIN OCCURS.

def login(name, password): 
    """ THIS FUNCTION LOGS IN A USER AND ASSIGNS THE USER DETAILS TO THE GLOBAL LOGGED IN USER"""

    search = guru.read(f"SELECT * FROM users WHERE name = '{name}' AND password = '{password}'") # FETCH USER WITH INPUTTED DETAILS FROM DATABASE

    if search:
        logged_in_user = search[0]
        print("Login Successful")
        
        return logged_in_user
    else:

        print("Details might be wrong..!!!")
        return False

def display_titles(data):
    # print(data)
    for todo in data:
        print(str(todo["id"]).ljust(4), todo["title"].ljust(20))

def get_todos(userid):

    result = guru.read(f"SELECT * FROM todo WHERE uid = '{userid}' ")
    return result

print("WELCOME TO SHA")
logged_in_user = login("kunle", "12345ab")
data = get_todos(logged_in_user["id"])

display_titles(data)