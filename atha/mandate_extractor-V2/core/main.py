import pandas as pd

def clean_file(file_name):

    clean_file_name = f"results/{file_name}_cleaned.csv"

    file = open(f"statements/{file_name}.csv", "r")
    data = file.readlines()
    data.pop(0)
    heading = data.pop(0)

    file = open(f"{clean_file_name}", "w")
    file.write(heading)

    for line in data:
        splitted_line = line.split(",")
        if len(splitted_line) > 7:
            middle = splitted_line[3:-3]
            reformatted_middle = " ".join(middle)

            splitted_line[3:-3] = [reformatted_middle]

        file.write(",".join(splitted_line))
    file.close()
    
    return clean_file_name

def extract_mandates(clean_file_name):

    data = pd.read_csv(clean_file_name)

    payday_mask = data[" DESCRIPTION"].str.contains("PayDay")
    payday = data[payday_mask]

    payday["mandates"] = payday[" DESCRIPTION"].str.extract(r":([0-9]*)-PayDay")

    summed_duplicates = payday.groupby("mandates").sum().reset_index()
    mandates_and_credits = summed_duplicates[["mandates", " CREDIT"]]

    mandates_and_credits.to_csv(f"{clean_file_name}-mandates-credits.csv")
    
    print("\n\nSuccessfully.!!!\n\nCheck results folder for following.\n\n")
    print(f"\t1. {clean_file_name}\n\t2. {clean_file_name}-mandates-credits.csv\n")

    return {
                "status":"success"
            }

    