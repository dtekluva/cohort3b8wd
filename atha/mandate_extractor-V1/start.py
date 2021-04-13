from app import clean_file, extract_mandates

target_file_name = input("Please enter file name to process.\n\n> ")

try:

    extract_mandates(clean_file(target_file_name))

except ZeroDivisionError:
    
    print("Sorry the file name you entered might not exist.")