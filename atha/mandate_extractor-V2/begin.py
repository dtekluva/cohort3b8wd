from core.main import clean_file, extract_mandates
from core.helpers import display_files_and_obtain_statement_selection, display_files_and_loandisk_mandate_obtain_selection
from core.loandisk_compare import  get_mandate_comparison

target_statement_name = display_files_and_obtain_statement_selection()

target_mandates_and_creds_file = extract_mandates(clean_file(target_statement_name)).get("path")

target_loandisk_file = display_files_and_loandisk_mandate_obtain_selection()

get_mandate_comparison(target_mandates_and_creds_file, target_loandisk_file)


input("\n\n\n\n\nPress enter to quit.!!")