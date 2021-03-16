class StatementMan():
    
    def __init__(self, file_name) -> None:
        self.csv_file_name = file_name
        self.data = open(self.csv_file_name, "r").readlines() # read data from file

    def get_data(self):
        self.data = open(self.csv_file_name, "r").readlines()
        self.d
        return self.data

    def get_col_names(self, print_col_names = True):
        all_columns = self.data[0]
        
        if print_col_names:
            for index, colname in enumerate(all_columns.split(",")):
                print( index+1, colname)
        else:
            pass
            
        return all_columns.split(",")

    def num_rows(self):
        number_of_rows = len(self.data)
        print("Rows : ", number_of_rows)
        return number_of_rows
    
    def get_numeric_cols(self):
        columns = self.get_col_names(print_col_names=False)
        number_of_cols = len(columns)

        numeric_cols = []

        for index, col in enumerate(columns):
            # print(col)
            for line in self.data[1:]:
                value_at_column = line.replace("\n", "").split(",")[index]
                # print(value_at_column)
                if value_at_column.isnumeric():
                    pass
                else:
                    break
            else:
                numeric_cols.append(col)

        print(numeric_cols)
        return numeric_cols
            

    def describe(self):
        self.get_col_names()
        self.num_rows()
        self.get_numeric_cols()

    def filter(self):
        pass

    def split(self):
        pass

statement = StatementMan(file_name="C:/Users/kboys/OneDrive/Desktop/CLASSES/UNIVELCITY CLASSES/cohort3b8wd/atha/oop_notepad/Book1.csv")
# statement = StatementMan(file_name="C:/Users/kboys/OneDrive/Desktop/CLASSES/TECHBRIDGE CLASSES/TECHBRIDGE - 2/Mr. Sholarin/CONSOLIDATION/RESULTS - ORIGINAL/NITDEF.csv")
# statement = StatementMan(file_name="C:/Users/kboys/OneDrive/Desktop/CLASSES/UNIVELCITY CLASSES/cohort-3b7/CLASS DATA-ATHA/numpy pandas matplot/ML/9_decision_tree/Exercise/titanic.csv")
# print(statement.get_data())
statement.describe()