import os

def display_files_and_obtain_selection():
    files = os.listdir("statements")


    while True:

        print("\nFiles Available In Statements Folder : \n\n")

        for index, file in enumerate(files):

            print(f"\t{index+1}. {file}")

        selected_file_index = input("\n\nPlease which file would you like to process?\n> ")

        if not selected_file_index.isnumeric():
            print(f"\nEntry must be a number within available range.\n({selected_file_index}) is not valid.!!")
        elif int(selected_file_index) > len(files):
            print(f"\nNo file available with index : {selected_file_index}.")
        else:
            break

    selected_file_name = files[int(selected_file_index)-1]

    return selected_file_name.replace(".csv", "")