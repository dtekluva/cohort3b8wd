from core.main import clean_file, extract_mandates
from core.helpers import display_files_and_obtain_selection

target_file_name = display_files_and_obtain_selection()

extract_mandates(clean_file(target_file_name))

input("\n\n\n\n\nPress enter to quit.!!")