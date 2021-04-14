import pandas as pd


def get_mandate_comparison(mandates_n_creds_file_name, loan_disk_file_name):

    mandates_n_creds = pd.read_csv(mandates_n_creds_file_name)
    loan_disk = pd.read_csv(loan_disk_file_name)

    mandates_n_creds = mandates_n_creds.round(2)
    loan_disk = loan_disk.round(2)

    mandates_n_creds.drop(["Unnamed: 0"], axis = 1, inplace = True) # drop the unwanted column Unnamed: 0 from mandates

    mandates_n_creds.columns = ['mandates_bank', ' CREDIT'] # rename mandates to mandates_bank

    required_columns = ['loan_id',
                        'loan_principal_amount',
                        'loan_released_date',
                        'total_amount_due',
                        'balance_amount',
                        'due_date',
                        'total_paid',
                        'custom_field_4361',
                        'custom_field_4178',
                        'custom_field_5262',
                        'borrower_firstname',
                        'borrower_lastname',
                        'borrower_email',
                        'borrower_address',
                        ]
    loan_disk_target = loan_disk[required_columns]

    required_columns_customized = ['loan_id',
                                    'loan_principal_amount',
                                    'loan_released_date',
                                    'total_amount_due',
                                    'balance_amount',
                                    'due_date',
                                    'total_paid',
                                    'bvn',
                                    'account_no',
                                    'mandates_loandisk',
                                    'borrower_firstname',
                                    'borrower_lastname',
                                    'borrower_email',
                                    'borrower_address',
                                    ]

    loan_disk_target.columns = required_columns_customized # change  certain column names in the fields

    merged = pd.merge(
                    left = loan_disk_target, 
                    right=mandates_n_creds, 
                    how="outer", 
                    left_on="mandates_loandisk", 
                    right_on="mandates_bank"
                    )

    credit_difference = merged.total_paid - merged[" CREDIT"]
    merged["credit_difference"] = credit_difference

    excess_mask = merged["credit_difference"] > 0
    less_mask = merged["credit_difference"] < 0
    unknowns_mask = merged["loan_id"].isnull()
    not_in_bank_mask = merged[" CREDIT"].isnull()

    excess = merged[excess_mask]
    less = merged[less_mask]
    unknowns = merged[unknowns_mask]
    not_in_bank = merged[not_in_bank_mask]

    with pd.ExcelWriter('results/result.xlsx') as writer:  
        
        excess.to_excel(writer, sheet_name='excess')
        less.to_excel(writer, sheet_name='less')
        unknowns.to_excel(writer, sheet_name='unknowns')
        not_in_bank.to_excel(writer, sheet_name='not_in_bank')

    print("\n\nDone.!! Please check results folder for result.xlsx")

    return dict(
                    excess = excess,
                    less = less,
                    unknowns = unknowns,
                    not_in_bank = not_in_bank
                )