# DUMMY DATA

users = {                               # dictionary: key & value
    'id': (1,),                         # tuple: can't change or remove items
    'email': ('davis@test.com',),
    'password': ('davis',),
    'name': ('davis',),
    'num_of_data': 1
}

financialAccounts = {
    'id': [1, 2, 3],                                # list: can change or remove items
    'user_id': [1, 1, 1],
    'account_type': ['bank', 'ewallet', 'others'],
    'account_name': ['bca', 'gopay', 'cash'],
    'balance': [10000000, 1000000, 500000],
    'num_of_data': 3
}

transactions = {
    'id': [1, 2, 3, 4, 5],                                                                                  # list: can change or remove items
    'user_id': [1, 1, 1, 1, 1],
    'date': ['2024-08-30', '2024-09-02', '2024-09-07', '2024-09-11', '2024-09-12'],
    'type': ['expense', 'expense', 'expense', 'expense', 'income'],
    'category': ['food & beverages', 'food & beverages', 'food & beverages', 'entertainment', 'others inc.'],
    'amount': [35000, 25000, 40000, 100000, 100000],
    'vendor': ['kfc', 'mcd', 'subway', 'netflix', '-'],
    'account_type': ['bank', 'others', 'ewallet', 'bank', 'others'],
    'account_name': ['bca', 'cash', 'gopay', 'bca', 'cash'],
    'num_of_data': 5
}

budgets = {
    'id': [1],                          # list: can change or remove items
    'user_id': [1],
    'category': ['food & beverages'],
    'start_date': ['2024-09-01'],
    'end_date': ['2024-09-30'],
    'amount': [1000000],
    'budget_used': [65000],
    'transaction_id': [{2, 3}],         # set: unqiue
    'num_of_data': 1
}

userFinancials = {
    'id': [1],              # list: can change or remove items
    'user_id': [1],
    'balance': [11500000],
    'expense': [200000],
    'income': [100000],
    'num_of_data': 1
}

# FINANCIAL ACCOUNT & CATEGORY LIST

bank_name_list = ['bca', 'mandiri', 'bni', 'bri', 'others']
ewallet_name_list = ['gopay', 'ovo', 'dana', 'shopeepay', 'others']
others_name_list = ['cash', 'emoney', 'others']
expense_category_list = ['food & beverages', 'transportation', 'house needs', 'bills & utilities', 'pet', 'family', 'shopping', 'health & sports', 'donation', 'travel', 'entertainment', 'education', 'others exp.']
income_category_list = ['salary', 'business', 'investment', 'gift', 'others inc.']

def index_list(lst, value):
    result = [i for i in range(len(lst)) if lst[i] == value]
    return result

def main_menu():
    while True:
        main_menu_input = input('''
=================================
   Personal Finance Management
=================================
                    
     "You can make money 2 
        ways - make more, 
         or spend less."                        

1. Log In
2. Register
3. Exit
Please select an option from the menu above (1-3): ''')

        if main_menu_input == '1':
            login_page()
        elif main_menu_input == '2':
            register_page()
        elif main_menu_input == '3':
            print('Thank you for using this App. Have a great day!\n')
            break
        # If option not in (1-3)
        else:
            print('Invalid option. Please select an option from the menu above (1-3).\n')

def login_page():
    while True:
        email_input = input('Enter your email: ')
        password_input = input('Enter your password: ')
        if email_input in users['email']:
            email_index = users['email'].index(email_input)
            if password_input == users['password'][email_index]:
                user_id = users['id'][email_index]
                homepage(user_id=user_id)
                break
            else:
                print('Password is wrong.')
        # If email_input not in users['email']
        else:
            print('Couldn\'t find your account.')

        # Will be run if 'else' block run
        while True:
            back_input = input('Back to main menu (yes/no)? ')
            if back_input.lower() == 'yes':
                return 
            elif back_input.lower() == 'no':
                break 
            else:
                print('Invalid option. Please select an option between "yes" or "no".')

def register_page():
    while True:
        email_input = input('Enter your email: ')
        if email_input in users['email']:
            print('Email is already used.')
        else:
            password_input = input('Enter your password: ')
            name_input = input('Enter your name: ')
            
            # Generate ID
            users['num_of_data'] += 1
            user_id = users['num_of_data']

            # Store data to users
            users['id'] += (user_id,)
            users['email'] += (email_input,)
            users['password'] += (password_input,)
            users['name'] += (name_input,)
            
            # Generate ID & initialize data
            userFinancials['num_of_data'] += 1
            userFinancial_id = userFinancials['num_of_data']
            balance = 0
            expense = 0
            income = 0

            # Store data to userFinancials
            userFinancials['id'].append(userFinancial_id)
            userFinancials['user_id'].append(user_id)
            userFinancials['balance'].append(balance)
            userFinancials['expense'].append(expense)
            userFinancials['income'].append(income)
            
            print('Account has been created. Proceed to homepage.')

            # Go to homepage
            homepage(user_id=user_id)
            break

        # Will be run if 'if' block run
        while True:
            back_input = input('Back to main menu (yes/no)? ')
            if back_input.lower() == 'yes':
                return
            elif back_input.lower() == 'no':
                break
            else:
                print('\nInvalid option. Please enter "yes" or "no".\n')

def homepage(user_id):
    while True:
        
        # Indexing
        uf_user_id_index = userFinancials['user_id'].index(user_id)
        uf_balance = userFinancials['balance'][uf_user_id_index]
        uf_expense = userFinancials['expense'][uf_user_id_index]
        uf_income = userFinancials['income'][uf_user_id_index]

        homepage_input = input(f'''
=================================
            Homepage
=================================
                               
    Balance: {uf_balance}
    Cash Flow: {uf_income - uf_expense}

1. Financial Accounts
2. Transactions
3. Expense Summary
4. Budgets
5. Log Out
Please select an option from the menu above (1-5): ''')

        if homepage_input == '1':
            financial_accounts_page(user_id=user_id)
        elif homepage_input == '2':
            transactions_page(user_id=user_id)
        elif homepage_input == '3':
            expense_summary_page(user_id=user_id)
        elif homepage_input == '4':
            budgets_page(user_id=user_id)
        elif homepage_input == '5':
            break
        # If option not in (1-5)
        else:
            print('Invalid option. Please select an option from the menu above (1-5).\n')

def financial_accounts_page(user_id):
    while True:
        financial_accounts_input = input('''
=================================
        Financial Accounts
=================================
                                         
1. Add Financial Accounts
2. View Financial Accounts
3. Edit Balance
4. Delete Financial Accounts
5. Back to Homepage
Please select an option from the menu above (1-5): ''')

        if financial_accounts_input == '1':
            add_financial_accounts(user_id=user_id)
        elif financial_accounts_input == '2':
            view_financial_accounts(user_id=user_id)
        elif financial_accounts_input == '3':
            edit_balance(user_id=user_id)
        elif financial_accounts_input == '4':
            delete_financial_accounts(user_id=user_id)
        elif financial_accounts_input == '5':
            break
        # If option not in (1-5)
        else:
            print('Invalid option. Please select an option from the menu above (1-5).\n')

def display_financial_accounts(account_type):
    if account_type == 'bank':
        name_list = bank_name_list
    elif account_type == 'ewallet':
        name_list = ewallet_name_list
    # Others
    else:
        name_list = others_name_list
        
    # Print list name
    print(f'\n{account_type.capitalize()} Name List')
    results = ''
    for i in range(0, len(name_list)):
        result = f'| {i + 1}. {name_list[i]}'
        results += result + (12 - len(result)) * ' '
        if (i + 1) % 5 == 0:
            results += '\n'
    print(results)

def add_financial_accounts(user_id):
    while True:

        # Financial account user_id account indexing
        fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
        fa_bank_index = index_list(lst=financialAccounts['account_type'], value='bank')
        fa_ewallet_index = index_list(lst=financialAccounts['account_type'], value='ewallet')
        fa_others_index = index_list(lst=financialAccounts['account_type'], value='others')

        account_type_input = input('Enter your account type (bank/ewallet/others): ').lower()
        while account_type_input not in ['bank', 'ewallet', 'others']:
            print('Invalid option. Please enter "bank" or "ewallet" or "others".')
            account_type_input = input('Enter your account type (bank/ewallet/others): ').lower()
        else:
            display_financial_accounts(account_type=account_type_input)
            
            if account_type_input == 'bank':
                fa_account_index = fa_bank_index
                name_list = bank_name_list
            elif account_type_input == 'ewallet':
                fa_account_index = fa_ewallet_index
                name_list = ewallet_name_list
            # Others
            else:
                fa_account_index = fa_others_index
                name_list = others_name_list
            
            account_no_input = int(input('Enter your account no.: '))
            while (account_no_input - 1) not in range(0, len(name_list)):
                print('Invalid option. Please enter a number from the list.')
                account_no_input = int(input('Enter your account no.: '))
            
            fa_user_id_account_index = list(set(fa_user_id_index).intersection(set(fa_account_index)))
            fa_user_id_name_list = [financialAccounts['account_name'][i] for i in fa_user_id_account_index]
            account_name = name_list[account_no_input - 1]
            if account_name in fa_user_id_name_list:
                print('Financial account is already added.')
                back_input = input('Back to financial accounts page (yes/no)? ').lower()
                while back_input not in ['yes', 'no']:
                    print('Invalid option. Please select an option between "yes" or "no".')
                    back_input = input('Back to financial accounts page (yes/no)? ').lower()
                else:
                    if back_input == 'yes':
                        return
                    else:
                        continue
            else:
                account_balance = int(input('Enter your account balance: '))

            # Generate ID
            financialAccounts['num_of_data'] += 1
            financialAccount_id = financialAccounts['num_of_data']

            # Store data to financialAccounts & userFinancials
            financialAccounts['id'].append(financialAccount_id)
            financialAccounts['user_id'].append(user_id)
            financialAccounts['account_type'].append(account_type_input)
            financialAccounts['account_name'].append(account_name)
            financialAccounts['balance'].append(account_balance) 
            userFinancials['balance'][userFinancials['user_id'].index(user_id)] += account_balance
            
            print('Financial account has been added.')

            # Add more financial account
            more_input = input('Add more financial account (yes/no)? ').lower()
            while more_input not in ['yes', 'no']:
                print('Invalid option. Please select an option between "yes" or "no".')
                more_input = input('Add more financial account (yes/no)? ').lower()
            else:
                if more_input == 'yes':
                    continue
                else:
                    break

def view_financial_accounts(user_id):
    if user_id not in financialAccounts['user_id']:
        print('You haven\'t added any financial account.')
    else:
        fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
        print('-------------------------------------------------------')
        print('| ID. | Account Name  | Account Type  | Balance       |')
        print('-------------------------------------------------------')
        for i in fa_user_id_index:
            result = f'| {financialAccounts['id'][i]}' + (7 - len(f'| {i}.')) * ' ' + f'| {financialAccounts['account_name'][i]}' + (16 - len(f'| {financialAccounts['account_name'][i]}')) * ' '  + f'| {financialAccounts['account_type'][i]}' + (16 - len(f'| {financialAccounts['account_type'][i]}')) * ' '  + f'| {financialAccounts['balance'][i]}' + (16 - len(f'| {financialAccounts['balance'][i]}')) * ' ' + '|'
            print(result)
        print('-------------------------------------------------------')

def edit_balance(user_id):
    while True:
        # If user haven't add any financial account
        if user_id not in financialAccounts['user_id']:
            print('You haven\'t added any financial account.')
            break
        
        # Financial account id indexing
        fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
        fa_id = [financialAccounts['id'][i] for i in fa_user_id_index]

        view_financial_accounts(user_id=user_id)
        edit_account_id_input = int(input('Please enter account id to edit: '))
        while edit_account_id_input not in fa_id:
            print('Invalid option. Please select a valid option from the list.')
            edit_account_id_input = int(input('Please enter account id to edit: '))
        else:
            new_balance_input = int(input('Please enter new balance: '))
            confirm_input = input('Are you sure to change the balance (yes/no)? ').lower()
            while confirm_input.lower() not in ['yes', 'no']:
                print('Invalid option. Please select an option between "yes" or "no".')
                confirm_input = input('Are you sure to change the balance (yes/no)? ').lower()
            else:
                if confirm_input.lower() == 'yes':
                    # Edit account id indexing on financialAccounts
                    edit_account_id_index = financialAccounts['id'].index(edit_account_id_input)
                    # Change the balance to new balance on userFinancials
                    userFinancials['balance'][userFinancials['user_id'].index(user_id)] += new_balance_input - financialAccounts['balance'][edit_account_id_index]
                    # Change the balance to new balance on financialAccounts
                    financialAccounts['balance'][edit_account_id_index] = new_balance_input

                    print('Changed success.')
                    
                    more_input = input('Edit more balance (yes/no)? ').lower()
                    while more_input not in ['yes', 'no']:
                        print('Invalid option. Please select an option between "yes" or "no".')
                        more_input = input('Edit more balance (yes/no)? ').lower()
                    else:
                        if more_input == 'yes':
                            continue
                        else:
                            break
                else:
                    print('Changed failed.')
                    break

def delete_financial_accounts(user_id):
        while True:
            # If user haven't add any financial account
            if user_id not in financialAccounts['user_id']:
                print('You haven\'t added any financial accounts.')
                break
            
            # Financial account id indexing
            fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
            fa_id = [financialAccounts['id'][i] for i in fa_user_id_index]

            view_financial_accounts(user_id=user_id)
            delete_account_id_input = int(input('Please enter account id to delete: '))
            while delete_account_id_input not in fa_id:
                print('Invalid option. Please select a valid option from the list.')
                delete_account_id_input = int(input('Please enter account id to delete: '))
            else:
                confirm_input = input('''Deleting a financial account will permanently remove all associated transactions and may affect your expense summary and budget.
Do you still want to proceed (yes/no)? ''').lower()
                while confirm_input not in ['yes', 'no']:
                    print('Invalid option. Please select an option between "yes" or "no".')
                    confirm_input = input('''Deleting a financial account will permanently remove all associated transactions and may affect your expense summary and budget.
Do you still want to proceed (yes/no)? ''').lower()
                else:
                    if confirm_input == 'yes':
                        # Reduce balance in userFinancials
                        uf_user_id_index = userFinancials['user_id'].index(user_id)
                        fa_id_index = financialAccounts['id'].index(delete_account_id_input)
                        userFinancials['balance'][uf_user_id_index] -= financialAccounts['balance'][fa_id_index]

                        # Find associated transactions
                        t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
                        t_account_name_index = index_list(lst=transactions['account_name'], value=financialAccounts['account_name'][fa_id_index])
                        delete_transaction_list = list(set(t_user_id_index).intersection(t_account_name_index))

                        b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)

                        for i in delete_transaction_list:
                            delete_transaction_id = transactions['id'][i]
                            delete_transaction_amount = transactions['amount'][i]

                            if transactions['type'][i] == 'expense':
                                userFinancials['expense'][uf_user_id_index] -= delete_transaction_amount
                            elif transactions['type'][i] == 'income':
                                userFinancials['income'][uf_user_id_index] -= delete_transaction_amount

                            for j in b_user_id_index:
                                if delete_transaction_id in budgets['transaction_id'][j]:
                                    budgets['transaction_id'][j].remove(delete_transaction_id)
                                    max_budget_used = budgets['budget_used'][j] - delete_transaction_amount
                                    # To prevent negative budget used
                                    budgets['budget_used'][j] = max(max_budget_used, 0)

                        # Delete associated transactions
                        if delete_transaction_list:
                            delete_transaction_list.sort(reverse=True) 
                            for i in delete_transaction_list:
                                for key in transactions:
                                    if key != 'num_of_data':
                                        transactions[key].pop(i)

                        # Remove all data in financialAccounts that associated with the account
                        for key in financialAccounts:
                            if key != 'num_of_data':
                                financialAccounts[key].pop(fa_id_index)

                        if user_id in financialAccounts['user_id']:
                            # Ask if the user wants to delete more accounts
                            more_input = input('Delete more account (yes/no)? ').lower()
                            while more_input not in ['yes', 'no']:
                                print('Invalid option. Please select an option between "yes" or "no".')
                                more_input = input('Delete more account (yes/no)? ').lower()
                            else: 
                                if more_input == 'no':
                                    break
                        # If user doesn't have financial account anymore will be break
                        else:
                            break
                    else:
                        break

def expense_summary_page(user_id):
    # User expense transaction indexing
    t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
    t_expense_index = index_list(lst=transactions['type'], value='expense')
    t_user_id_expense_index = list(set(t_user_id_index).intersection(set(t_expense_index)))

    if t_user_id_expense_index == []:
        print('You haven\'t added any expense transaction.')
    else:
        uf_user_id_index = userFinancials['user_id'].index(user_id)
        total_expense = userFinancials['expense'][uf_user_id_index]
        print(f'\nTotal expense: {total_expense}\n')
        for value in ['category', 'account_name', 'vendor']:
            if value != 'account_name':
                print(f'-----By {value.title()}-----')
            else:
                print('-----By Account Name-----')
            
            expense = {}
            for i in t_user_id_expense_index:
                if transactions[value][i] not in expense.keys():
                    expense[transactions[value][i]] = transactions['amount'][i]
                else:
                    expense[transactions[value][i]] += transactions['amount'][i]

            for key, value in expense.items():
                expense_percentage = round(value / total_expense, 4) * 100
                print(f'{key}:  {value} ({expense_percentage:.2f}%)')
            print('\n')

def transactions_page(user_id):
    while True:
        transactions_input = input('''
=================================
            Transactions
=================================
                                         
1. Add Transactions
2. View Transactions
3. Edit Transactions
4. Delete Transactions
5. Back to Homepage
Please select an option from the menu above (1-5): ''')

        if transactions_input == '1':
            add_transactions(user_id=user_id)
        elif transactions_input == '2':
            if user_id not in transactions['user_id']:
                print('You haven\'t added any transaction.')
            else:
                view_input = input('''\n1. View without sort & filter
2. View with sort by date
3. View with filter by category
Please select an option from the menu above (1-3): ''')
                if view_input == '1':
                    view_transactions(user_id=user_id)
                elif view_input == '2':
                    view_transactions(user_id=user_id, date_sorted=True)
                elif view_input == '3':
                    view_transactions(user_id=user_id, date_sorted=False, category_filtered=True)
                else:
                    print('Invalid option. Please select an option from the menu above (1-3).')
        elif transactions_input == '3':
            edit_transactions(user_id=user_id)
        elif transactions_input == '4':
            delete_transactions(user_id=user_id)
        elif transactions_input == '5':
            break
        else:
            print('Invalid option. Please select an option from the menu above (1-5).')

def display_category(category_type):
    category_list = expense_category_list if category_type == 'expense' else income_category_list

    # Print result
    print(f'\n{category_type.capitalize()} Name List')
    results = ''
    for i in range(0, len(category_list)):
        result = f'| {i + 1}. {category_list[i]}'
        decorator = 0 if (i + 1) % 5 == 0 else 25
        results += result + (decorator - len(result)) * ' '
        if (i + 1) % 5 == 0:
            results += '\n'
    print(results)

def add_transactions(user_id):
    while True:
        if user_id not in financialAccounts['user_id']:
            print('You don\'t have any financial account.')
            break
        else:
            transaction_date_input = input('Please enter transaction date (YYYY-MM-DD): ')
            view_financial_accounts(user_id)
            financial_account_id_input = int(input('Please enter financal account id: '))
            
            # Financial account id indexing
            fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
            fa_id_list = [financialAccounts['id'][i] for i in fa_user_id_index]
            while financial_account_id_input not in fa_id_list:
                print('Invalid option. Please select an option from the list above.')
                financial_account_id_input = int(input('Please enter financal account id: '))
            else:
                transaction_type_input = input('Please enter transaction type (expense/income): ').lower()
                while transaction_type_input not in ['expense', 'income']:
                    print('Invalid option. Please select an option between "expense" or "income".')
                    transaction_type_input = input('Please enter transaction type (expense/income): ').lower()
                else:
                    # Assign & display category list based on transaction type input
                    if transaction_type_input == 'expense':
                        category_list = expense_category_list
                        display_category(category_type='expense')
                    else:
                        category_list = income_category_list
                        display_category(category_type='income')

                    transaction_category_input = int(input('Please enter transaction category no.: '))
                    while (transaction_category_input - 1) not in range(0, len(category_list)):
                        print('Invalid option. Please select an option from the list above.')
                        transaction_category_input = int(input('Please enter transaction category no.: '))
                    else:
                        financial_account_id = financialAccounts['id'].index(financial_account_id_input)
                        transaction_amount_input = int(input('Please enter transaction amount: '))
                        while transaction_type_input == 'expense' and transaction_amount_input > financialAccounts['balance'][financial_account_id]:
                            print('Your transaction amount is more than your balance.')
                            transaction_amount_input = int(input('Please enter transaction amount: '))
                        else:
                            transaction_vendor_input = input('Please enter vendor: ') 
                            
                            # Generate ID
                            transactions['num_of_data'] += 1
                            transaction_id = transactions['num_of_data']

                            # Store data to transactions
                            transactions['id'].append(transaction_id)
                            transactions['user_id'].append(user_id)
                            transactions['date'].append(transaction_date_input)
                            transactions['account_type'].append(financialAccounts['account_type'][financial_account_id])
                            transactions['account_name'].append(financialAccounts['account_name'][financial_account_id])
                            transactions['type'].append(transaction_type_input)
                            transactions['category'].append(category_list[transaction_category_input - 1])
                            transactions['amount'].append(transaction_amount_input)
                            transactions['vendor'].append(transaction_vendor_input)

                            # Update data on financialAccounts & userFinancials
                            if transaction_type_input == 'expense':
                                financialAccounts['balance'][financial_account_id] -= transaction_amount_input
                                userFinancials['balance'][userFinancials['user_id'].index(user_id)] -= transaction_amount_input
                                userFinancials['expense'][userFinancials['user_id'].index(user_id)] += transaction_amount_input
                            else:
                                financialAccounts['balance'][financial_account_id] += transaction_amount_input
                                userFinancials['balance'][userFinancials['user_id'].index(user_id)] += transaction_amount_input
                                userFinancials['income'][userFinancials['user_id'].index(user_id)] += transaction_amount_input

                            # Update data on budgets if any
                            b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
                            b_category_index = index_list(lst=budgets['category'], value=category_list[transaction_category_input - 1])
                            b_user_id_category_index = list(set(b_user_id_index).intersection(b_category_index))
                            if b_user_id_category_index:
                                for i in b_user_id_category_index:
                                    if budgets['start_date'][i] <= transaction_date_input <= budgets['end_date'][i]:
                                        budgets['budget_used'][i] += transaction_amount_input
                                        budgets['transaction_id'][i].add(transaction_id)

                            more_input = input('Add more transactions (yes/no)? ').lower()
                            while more_input not in ['yes', 'no']:
                                print('Invalid option. Please select an option between "yes" or "no".')
                                more_input = input('Add more transactions (yes/no)? ').lower()
                            else:
                                if more_input == 'no':
                                    break
                                else:
                                    continue

def view_transactions(user_id, date_sorted=False, category_filtered=False):
    if user_id not in transactions['user_id']:
        print('You haven\'t added any transaction.')
    else:
        t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
        if date_sorted:
            t_user_id_index.sort(key=lambda i: transactions['date'][i])
        if category_filtered:
            user_category = list(set(transactions['category'][i] for i in t_user_id_index))
            index = 0
            print('List of your transaction category')
            for value in user_category:
                print(f'{index + 1}. {value}')
                index += 1
            category_input = int(input('Please select category no. you want to see: '))
            while (category_input - 1) not in range(0, len(user_category)):
                print('Invalid option. Please select an option from the list above.')
                category_input = int(input('Please select category no. you want to see: '))
            else:
                select_category = user_category[category_input - 1]
                t_user_id_index = [i for i in t_user_id_index if transactions['category'][i] == select_category]

        print('----------------------------------------------------------------------------------------------------------------------------')
        print('| ID. | Date          | Type          | Category           | Amount        | Vendor        | Account Type  | Account Name  |')
        print('----------------------------------------------------------------------------------------------------------------------------')
        for i in t_user_id_index:
            result = f'| {transactions['id'][i]}' + (6 - len(f'| {i}')) * ' ' + \
                    f'| {transactions['date'][i]}' + (16 - len(f'| {transactions['date'][i]}')) * ' ' + \
                    f'| {transactions['type'][i]}' + (16 - len(f'| {transactions['type'][i]}')) * ' ' + \
                    f'| {transactions['category'][i]}' + (21 - len(f'| {transactions['category'][i]}')) * ' ' + \
                    f'| {transactions['amount'][i]}' + (16 - len(f'| {transactions['amount'][i]}')) * ' ' + \
                    f'| {transactions['vendor'][i]}' + (16 - len(f'| {transactions['vendor'][i]}')) * ' ' + \
                    f'| {transactions['account_type'][i]}' + (16 - len(f'| {transactions['account_type'][i]}')) * ' ' + \
                    f'| {transactions['account_name'][i]}' + (16 - len(f'| {transactions['account_name'][i]}')) * ' ' + \
                    '|'
            print(result)
        print('----------------------------------------------------------------------------------------------------------------------------')

def edit_transactions(user_id):
    while True:
        if user_id not in transactions['user_id']:
            print('You haven\'t added any transaction.')
            break
        else:
            view_transactions(user_id=user_id)
            edit_transaction_id_input = int(input('Please select transaction id to edit: '))

            # Transaction id list
            t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
            t_id_list = [transactions['id'][i] for i in t_user_id_index]
            while edit_transaction_id_input not in t_id_list:
                print('Invalid option. Please select an option from the list above.')
                edit_transaction_id_input = int(input('Please select transaction id to edit: '))
            else:
                part_to_edit_input = input('Please select which part to edit (all/category/amount/vendor)? ').lower()
                while part_to_edit_input not in ['all', 'category', 'amount', 'vendor']:
                    print('Invalid option. Please select an option between "all", "category", "amount", or "vendor".')
                    part_to_edit_input = input('Please select which part to edit (all/category/amount/vendor)? ').lower()
                else:
                    if part_to_edit_input == 'all':
 
                        category = transactions['type'][transactions['id'].index(edit_transaction_id_input)]
                        category_list = expense_category_list if category == 'expense' else income_category_list

                        display_category(category_type=category)
                        new_category_input = int(input('Please enter new category no.: '))
                        while (new_category_input - 1) not in range(0, len(category_list)):
                            print('Invalid option. Please select an option from the list above.')
                            new_category_input = int(input('Please enter new category no.: '))

                        # Find financial account the transaction use
                        fa_account_name_index = index_list(lst=financialAccounts['account_name'], value=transactions['account_name'][transactions['id'].index(edit_transaction_id_input)])
                        fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
                        fa_account_name_user_id_index = list(set(fa_account_name_index).intersection(fa_user_id_index))

                        new_amount_input = int(input('Please enter new amount: '))
                        if transactions['type'][transactions['id'].index(edit_transaction_id_input)] == 'expense':
                            for i in fa_account_name_user_id_index:
                                while new_amount_input > financialAccounts['balance'][i]:
                                    print('New amount is more than your balance. Please enter the correct amount.')
                                    new_amount_input = int(input('Please enter new amount: '))
                        
                        # Update budgets for new category
                        b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
                        b_new_category_index = index_list(lst=budgets['category'], value=category_list[new_category_input - 1])
                        b_user_id_new_category_index = list(set(b_user_id_index).intersection(set(b_new_category_index)))
                        if b_user_id_new_category_index:
                            for i in b_user_id_new_category_index:
                                if budgets['start_date'][i] <= transactions['date'][transactions['id'].index(edit_transaction_id_input)] <= budgets['end_date'][i]:
                                    if edit_transaction_id_input not in budgets['transaction_id'][i]:
                                        budgets['budget_used'][i] += new_amount_input
                                        budgets['transaction_id'][i].add(edit_transaction_id_input)
                                    #else:
                                    #    budgets['budget_used'][i] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]

                        # Update budgets for the old category
                        b_old_category_index = index_list(lst=budgets['category'], value=transactions['category'][transactions['id'].index(edit_transaction_id_input)])
                        b_user_id_old_category_index = list(set(b_user_id_index).intersection(set(b_old_category_index)))
                        for i in b_user_id_old_category_index:
                            if edit_transaction_id_input in budgets['transaction_id'][i] and budgets['start_date'][i] <= transactions['date'][transactions['id'].index(edit_transaction_id_input)] <= budgets['end_date'][i]:
                                budgets['budget_used'][i] -= transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                                budgets['transaction_id'][i].remove(edit_transaction_id_input)

                        # Update transaction's category
                        transactions['category'][transactions['id'].index(edit_transaction_id_input)] = category_list[new_category_input - 1]

                        # Update financialAccounts
                        for i in fa_account_name_user_id_index:
                            if transactions['type'][transactions['id'].index(edit_transaction_id_input)] == 'expense':
                                financialAccounts['balance'][i] += transactions['amount'][transactions['id'].index(edit_transaction_id_input)] - new_amount_input
                            else: 
                                financialAccounts['balance'][i] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]

                        # Update userFinancials data
                        if transactions['type'][transactions['id'].index(edit_transaction_id_input)] == 'expense':
                            userFinancials['expense'][userFinancials['id'].index(user_id)] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                            userFinancials['balance'][userFinancials['id'].index(user_id)] += transactions['amount'][transactions['id'].index(edit_transaction_id_input)] - new_amount_input
                        else:
                            userFinancials['income'][userFinancials['id'].index(user_id)] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                            userFinancials['balance'][userFinancials['id'].index(user_id)] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]

                        transactions['amount'][transactions['id'].index(edit_transaction_id_input)] = new_amount_input

                        new_vendor_input = input('Please enter new vendor: ')
                        transactions['vendor'][transactions['id'].index(edit_transaction_id_input)] = new_vendor_input
                    
                    elif part_to_edit_input == 'category':
                        category = transactions['type'][transactions['id'].index(edit_transaction_id_input)]
                        category_list = expense_category_list if category == 'expense' else income_category_list

                        display_category(category_type=category)
                        new_category_input = int(input('Please enter new category no.: '))

                        while (new_category_input - 1) not in range(0, len(category_list)):
                            print('Invalid option. Please select an option from the list above.')
                            new_category_input = int(input('Please enter new category no.: '))

                        # Update budgets data for old category
                        b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
                        b_old_category_index = index_list(lst=budgets['category'], value=transactions['category'][transactions['id'].index(edit_transaction_id_input)])
                        b_user_id_old_category_index = list(set(b_user_id_index).intersection(set(b_old_category_index)))
                        
                        for i in b_user_id_old_category_index:
                            if edit_transaction_id_input in budgets['transaction_id'][i] and budgets['start_date'][i] <= transactions['date'][transactions['id'].index(edit_transaction_id_input)] <= budgets['end_date'][i]:
                                budgets['budget_used'][i] -= transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                                budgets['transaction_id'][i].remove(edit_transaction_id_input)

                        # Update budgets data for new category
                        b_new_category_index = index_list(lst=budgets['category'], value=category_list[new_category_input - 1])
                        b_user_id_new_category_index = list(set(b_user_id_index).intersection(set(b_new_category_index)))

                        for i in b_user_id_new_category_index:
                            if edit_transaction_id_input not in budgets['transaction_id'][i] and budgets['start_date'][i] <= transactions['date'][transactions['id'].index(edit_transaction_id_input)] <= budgets['end_date'][i]:
                                budgets['budget_used'][i] += transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                                budgets['transaction_id'][i].add(edit_transaction_id_input)

                        # Update transaction's category
                        transactions['category'][transactions['id'].index(edit_transaction_id_input)] = category_list[new_category_input - 1]

                    elif part_to_edit_input == 'amount':
                        # Find financial account the transaction use
                        fa_account_name_index = index_list(lst=financialAccounts['account_name'], value=transactions['account_name'][transactions['id'].index(edit_transaction_id_input)])
                        fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
                        fa_account_name_user_id_index = list(set(fa_account_name_index).intersection(fa_user_id_index))

                        new_amount_input = int(input('Please enter new amount: '))
                        if transactions['type'][transactions['id'].index(edit_transaction_id_input)] == 'expense':
                            for i in fa_account_name_user_id_index:
                                while new_amount_input > financialAccounts['balance'][i]:
                                    print('New amount is more than your balance. Please enter the correct amount.')
                                    new_amount_input = int(input('Please enter new amount: '))

                        # Update budgets data
                        b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
                        b_category_index = index_list(lst=budgets['category'], value=transactions['category'][transactions['id'].index(edit_transaction_id_input)])
                        b_user_id_category_index = list(set(b_user_id_index).intersection(set(b_category_index)))
                        for i in b_user_id_category_index:
                            budgets['budget_used'][i] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                        
                        # Update financialAccounts data
                        for i in fa_account_name_user_id_index:
                            if transactions['type'][transactions['id'].index(edit_transaction_id_input)] == 'expense':
                                financialAccounts['balance'][i] += transactions['amount'][transactions['id'].index(edit_transaction_id_input)] - new_amount_input
                            # Income
                            else:
                                financialAccounts['balance'][i] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]

                        # Update userFinancials data
                        if transactions['type'][transactions['id'].index(edit_transaction_id_input)] == 'expense':
                            userFinancials['expense'][userFinancials['id'].index(user_id)] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                            userFinancials['balance'][userFinancials['id'].index(user_id)] += transactions['amount'][transactions['id'].index(edit_transaction_id_input)] - new_amount_input
                        else:
                            userFinancials['income'][userFinancials['id'].index(user_id)] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]
                            userFinancials['balance'][userFinancials['id'].index(user_id)] += new_amount_input - transactions['amount'][transactions['id'].index(edit_transaction_id_input)]

                        transactions['amount'][transactions['id'].index(edit_transaction_id_input)] = new_amount_input
                    
                    else:
                        new_vendor_input = input('Please enter new vendor: ')
                        transactions['vendor'][transactions['id'].index(edit_transaction_id_input)] = new_vendor_input

                    more_input = input('Edit more transactions (yes/no)? ').lower()
                    while more_input not in ['yes', 'no']:
                        print('Invalid option. Please select an option between "yes" or "no".')
                        more_input = input('Edit more transactions (yes/no)? ').lower()
                    else:
                        if more_input == 'no':
                            break

def delete_transactions(user_id):
    while True:
        if user_id not in transactions['user_id']:
            print('You haven\'t added any transaction.')
            break
        else:
            view_transactions(user_id=user_id)
            delete_transaction_id_input = int(input('Please select transaction id to edit: '))

            t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
            t_id_list = [transactions['id'][i] for i in t_user_id_index]
            while delete_transaction_id_input not in t_id_list:
                print('Invalid option. Please select an option from the list above.')
                delete_transaction_id_input = int(input('Please select transaction id to edit: '))
            else:
                confirm_input = input('Are you sure to delete this transaction (yes/no)? ').lower()
                while confirm_input not in ['yes', 'no']:
                    print('Invalid option. Please select an option between "yes" or "no".')
                    confirm_input = input('Are you sure to delete this transaction (yes/no)? ').lower()
                else:
                    if confirm_input == 'no':
                        break
                    else:
                        delete_transaction_index = transactions['id'].index(delete_transaction_id_input)
                        account_name = transactions['account_name'][transactions['id'].index(delete_transaction_id_input)]
                        fa_user_id_index = index_list(lst=financialAccounts['user_id'], value=user_id)
                        fa_account_name_index = index_list(lst=financialAccounts['account_name'], value=account_name)
                        fa_user_id_account_name_index = list(set(fa_user_id_index).intersection(set(fa_account_name_index)))
                        if transactions['type'][delete_transaction_index] == 'expense':
                            b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
                            b_category_index = index_list(lst=budgets['category'], value=transactions['category'][delete_transaction_index])
                            b_user_id_category_index = list(set(b_user_id_index).intersection(set(b_category_index)))
                            
                            # Update budgets data
                            for i in b_user_id_category_index:
                                if delete_transaction_id_input in budgets['transaction_id'][i] and budgets['start_date'][i] <= transactions['date'][delete_transaction_index] <= budgets['end_date'][i]:
                                    budgets['budget_used'][i] -= transactions['amount'][delete_transaction_index]
                                    budgets['transaction_id'][i].remove(delete_transaction_id_input)
                            
                            # Update financialAccounts & userFinancials data
                            financialAccounts['balance'][fa_user_id_account_name_index[0]] += transactions['amount'][delete_transaction_index]
                            userFinancials['balance'][userFinancials['user_id'].index(user_id)] += transactions['amount'][delete_transaction_index]
                            userFinancials['expense'][userFinancials['user_id'].index(user_id)] -= transactions['amount'][delete_transaction_index]
                        # Income
                        else:
                            financialAccounts['balance'][fa_user_id_account_name_index[0]] -= transactions['amount'][delete_transaction_index]
                            userFinancials['balance'][userFinancials['user_id'].index(user_id)] -= transactions['amount'][delete_transaction_index]
                            userFinancials['income'][userFinancials['user_id'].index(user_id)] -= transactions['amount'][delete_transaction_index]
                        # Delete all data that associated with delete_transaction_index
                        for key in transactions:
                            if key != 'num_of_data':
                                transactions[key].pop(delete_transaction_index)
                        
                        if user_id in transactions['user_id']:
                            more_input = input('Delete more transactions (Yes/No)? ').lower()
                            while more_input not in ['yes', 'no']:
                                print('Invalid optioon. Please select an option between "yes" or "no".')
                                more_input = input('Delete more transactions (Yes/No)? ').lower()
                            else:
                                if more_input == 'no':
                                    break
                        else:
                            break

def budgets_page(user_id):
    while True:
        budgets_input = input('''
=================================
            Budgets
=================================
                                         
1. Add Budgets
2. View Budgets
3. Edit Budgets
4. Delete Budgets
5. Back to Homepage
Please select an option from the menu above (1-5): ''')
        
        if budgets_input == '1':
            add_budgets(user_id=user_id)
        elif budgets_input == '2':
            view_budgets(user_id=user_id)
        elif budgets_input == '3':
            edit_budgets(user_id=user_id)
        elif budgets_input == '4':
            delete_budgets(user_id=user_id)
        elif budgets_input == '5':
            break
        else:
            print('Invalid option. Please select an option from the menu above.\n')
        
def add_budgets(user_id):
    while True:
        # Check if user has financial account or not
        if user_id not in financialAccounts['user_id']:
            print('Add financial account first.')
            break
        else:
            start_date_input = input('Please enter start date (YYYY-MM-DD): ')
            end_date_input = input('Please enter end date (YYYY-MM-DD): ')
            while start_date_input > end_date_input:
                print('Wrong date. Please enter correct date.')
                start_date_input = input('Please enter start date (YYYY-MM-DD): ')
                end_date_input = input('Please enter end date (YYYY-MM-DD): ')
            else:
                display_category(category_type='expense')
                category_input = int(input('Please enter category no. for budget: '))
                while (category_input - 1) not in range(0, len(expense_category_list)):
                    print('Invalid option. Please select an option from the list above.')
                    category_input = int(input('Please enter category no. for budget: '))
                else:
                    b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
                    b_category_index = index_list(lst=budgets['category'], value=expense_category_list[category_input - 1])
                    b_user_id_category_index = list(set(b_user_id_index).intersection(b_category_index))

                    exists = False
                    condition = False

                    # Check if user already has budget with same category & period
                    if b_user_id_category_index:
                        for i in b_user_id_category_index:
                            if budgets['start_date'][i] <= start_date_input <= budgets['end_date'][i]:
                                print('You already have budget on this category on the same date.')
                                exists = True
                        if exists:
                            back_input = input('Back to budget page (yes/no)? ').lower()
                            while back_input not in ['yes', 'no']:
                                print('Invalid option. Please select an option between "yes" or "no".')
                                back_input = input('Back to budget page (yes/no)? ').lower()
                            else:
                                if back_input == 'yes':
                                    condition = True
                                    return
                                else:
                                    continue
                    if not condition:
                        budget_input = int(input('Enter the budget amount: '))
                        
                        # Generate ID
                        budgets['num_of_data'] += 1
                        budget_id = budgets['num_of_data']

                        # Store data to budgets
                        budgets['id'].append(budget_id)
                        budgets['user_id'].append(user_id)
                        budgets['category'].append(expense_category_list[category_input - 1])
                        budgets['start_date'].append(start_date_input)
                        budgets['end_date'].append(end_date_input)
                        budgets['amount'].append(budget_input)
                        budgets['budget_used'].append(0)
                        budgets['transaction_id'].append(set())

                        t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
                        t_category_index = index_list(lst=transactions['category'], value=expense_category_list[category_input - 1])
                        t_user_id_category_index = list(set(t_user_id_index).intersection(set(t_category_index)))
                        b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
                        b_category_index = index_list(lst=budgets['category'], value=expense_category_list[category_input - 1])
                        b_user_id_category_index = list(set(b_user_id_index).intersection(set(b_category_index)))
                        
                        # Automatically add user's transactions to budget with same category & period
                        for i in b_user_id_category_index:
                            for j in t_user_id_category_index:
                                if transactions['id'][j] not in budgets['transaction_id'][i] and budgets['start_date'][i] <= transactions['date'][j] <= budgets['end_date'][i]:
                                    budgets['transaction_id'][i].add(transactions['id'][j])
                                    budgets['budget_used'][i] += transactions['amount'][j]
                        
                        more_input = input('Add more budgets (yes/no)? ').lower()
                        while more_input not in ['yes', 'no']:
                            print('Invalid option. Please select an option between "yes" or "no".')
                            more_input = input('Add more budgets (yes/no)? ').lower()
                        else:
                            if more_input == 'yes':
                                continue
                            else:
                                break

def view_budgets(user_id):
    if user_id not in budgets['user_id']:
        print('You haven\'t added any budget.')
    else:
        b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
        for i in b_user_id_index:
            print('\n')
            print('----------------------------------------------------------------------------------------------------------------------------')
            print(f' {budgets['category'][i].title()} Budget')
            print(f' ID Budget: {budgets['id'][i]}')
            print(f' Date: {budgets['start_date'][i]} ~ {budgets['end_date'][i]}')
            print(f' Budget: {budgets['amount'][i]}')
            budget_used_percentage = round(budgets['budget_used'][i] / budgets['amount'][i], 4) * 100
            print(f' Budget Used: {budget_used_percentage:.2f}%')
            print('----------------------------------------------------------------------------------------------------------------------------')
            print('| ID. | Date          | Type          | Category           | Amount        | Vendor        | Account Type  | Account Name  |')
            print('----------------------------------------------------------------------------------------------------------------------------')
            for y in list(budgets['transaction_id'][i]):
                result = f'| {transactions['id'][transactions['id'].index(y)]}' + (6 - len(f'| {i}')) * ' ' + \
                         f'| {transactions['date'][transactions['id'].index(y)]}' + (16 - len(f'| {transactions['date'][transactions['id'].index(y)]}')) * ' ' + \
                         f'| {transactions['type'][transactions['id'].index(y)]}' + (16 - len(f'| {transactions['type'][transactions['id'].index(y)]}')) * ' ' + \
                         f'| {transactions['category'][transactions['id'].index(y)]}' + (21 - len(f'| {transactions['category'][transactions['id'].index(y)]}')) * ' ' + \
                         f'| {transactions['amount'][transactions['id'].index(y)]}' + (16 - len(f'| {transactions['amount'][transactions['id'].index(y)]}')) * ' ' + \
                         f'| {transactions['vendor'][transactions['id'].index(y)]}' + (16 - len(f'| {transactions['vendor'][transactions['id'].index(y)]}')) * ' ' + \
                         f'| {transactions['account_type'][transactions['id'].index(y)]}' + (16 - len(f'| {transactions['account_type'][transactions['id'].index(y)]}')) * ' ' + \
                         f'| {transactions['account_name'][transactions['id'].index(y)]}' + (16 - len(f'| {transactions['account_name'][transactions['id'].index(y)]}')) * ' ' + \
                         '|'
                print(result)
            print('----------------------------------------------------------------------------------------------------------------------------')
            print('\n')

def edit_budgets(user_id):
    while True:
        if user_id not in budgets['user_id']:
            print('You haven\'t added any budget.')
            break
        else:
            view_budgets(user_id=user_id)
            edit_budget_id = int(input('Enter budget id to edit: '))

            # User budget id indexing
            b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
            budget_id = [budgets['id'][i] for i in b_user_id_index]
            while edit_budget_id not in budget_id:
                print('Invalid option. Please select an option from the list above.')
                edit_budget_id = int(input('Enter budget id to edit: '))
            else:
                part_to_edit = input('Which part of the budget you want to edit (all/category/amount)? ').lower()
                while part_to_edit not in ['all', 'category', 'amount']:
                    print('Invalid option. Please select an option between "all", "category", or "amount".')
                    part_to_edit = input('Which part of the budget you want to edit (all/category/amount)? ').lower()
                else:
                    if part_to_edit == 'all':
                        display_category(category_type='expense')
                        new_category_input = int(input('Please enter new category: '))
                        while (new_category_input - 1) not in range(0, len(expense_category_list)):
                            print('Invalid option. Please select an option from the list above.')
                            new_category_input = int(input('Please enter new category: '))
                        else:
                            # Check if after change budget category, it will duplicate with other budget
                            for i in budget_id:
                                if i != edit_budget_id:
                                    if budgets['category'][budgets['id'].index(i)] == expense_category_list[new_category_input - 1]:
                                        if budgets['start_date'][budgets['id'].index(i)] <= budgets['start_date'][budgets['id'].index(edit_budget_id)] <= budgets['end_date'][budgets['id'].index(i)] or budgets['start_date'][budgets['id'].index(i)] <= budgets['end_date'][budgets['id'].index(edit_budget_id)] <= budgets['end_date'][budgets['id'].index(i)]:
                                            print('You already have budget with same category & period.')
                                            return
                                        
                            new_amount_input = int(input('Please enter new amount: ')) 
                            confirm_input = input('Are you sure to edit the budget (yes/no)? ').lower()
                            while confirm_input not in ['yes', 'no']:
                                print('Invalid option. Please select an option between "yes" or "no".')
                                confirm_input = input('Are you sure to edit the budget (yes/no)? ').lower()
                            else:
                                if confirm_input == 'yes':
                                    budgets['category'][budgets['id'].index(edit_budget_id)] = expense_category_list[new_category_input - 1]
                                    t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
                                    t_category_index = index_list(lst=transactions['category'], value=expense_category_list[new_category_input - 1])
                                    t_user_id_category_index = list(set(t_user_id_index).intersection(set(t_category_index)))
                                    
                                    # Collect transaction id that associated to the budget
                                    associated_transactions = set()
                                    for i in t_user_id_category_index:
                                        if budgets['start_date'][budgets['id'].index(edit_budget_id)] <= transactions['date'][i] <= budgets['end_date'][budgets['id'].index(edit_budget_id)]: 
                                            associated_transactions.add(transactions['id'][i])
                                    
                                    # Assign transaction id to the budget
                                    budgets['transaction_id'][budgets['id'].index(edit_budget_id)] = associated_transactions

                                    budgets['amount'][budgets['id'].index(edit_budget_id)] = new_amount_input
                                    budgets['budget_used'][budgets['id'].index(edit_budget_id)] = 0


                                    # Update budget_used if user has asscoiated transactions
                                    if associated_transactions:
                                        for i in associated_transactions:
                                            if budgets['start_date'][budgets['id'].index(edit_budget_id)] <= transactions['date'][transactions['id'].index(i)] <= budgets['end_date'][budgets['id'].index(edit_budget_id)]: 
                                                budgets['budget_used'][budgets['id'].index(edit_budget_id)] += transactions['amount'][transactions['id'].index(i)]
                                else:
                                    break
                    elif part_to_edit == 'category':
                        display_category(category_type='expense')
                        new_category_input = int(input('Please enter new category: '))
                        while (new_category_input - 1) not in range(0, len(expense_category_list)):
                            print('Invalid option. Please select an option from the list above.')
                            new_category_input = int(input('Please enter new category: '))
                        else:
                            # Check if after change budget category, it will duplicate with other budget
                            for i in budget_id:
                                if i != edit_budget_id:
                                    if budgets['category'][budgets['id'].index(i)] == expense_category_list[new_category_input - 1]:
                                        if budgets['start_date'][budgets['id'].index(i)] <= budgets['start_date'][budgets['id'].index(edit_budget_id)] <= budgets['end_date'][budgets['id'].index(i)] or budgets['start_date'][budgets['id'].index(i)] <= budgets['end_date'][budgets['id'].index(edit_budget_id)] <= budgets['end_date'][budgets['id'].index(i)]:
                                            print('You already have budget with same category & period.')
                                            return
                                        
                            confirm_input = input('Are you sure to edit the budget (yes/no)? ').lower()
                            while confirm_input not in ['yes', 'no']:
                                print('Invalid option. Please select an option between "yes" or "no".')
                                confirm_input = input('Are you sure to edit the budget (yes/no)? ').lower()
                            else:
                                if confirm_input == 'yes':
                                    budgets['category'][budgets['id'].index(edit_budget_id)] = expense_category_list[new_category_input - 1]
                                    t_user_id_index = index_list(lst=transactions['user_id'], value=user_id)
                                    t_category_index = index_list(lst=transactions['category'], value=expense_category_list[new_category_input - 1])
                                    t_user_id_category_index = list(set(t_user_id_index).intersection(set(t_category_index)))
                                    
                                    associated_transactions = set()
                                    for i in t_user_id_category_index:
                                        if budgets['start_date'][budgets['id'].index(edit_budget_id)] <= transactions['date'][i] <= budgets['end_date'][budgets['id'].index(edit_budget_id)]: 
                                            associated_transactions.add(transactions['id'][i])
                                    
                                    # Assign transaction id to the budget
                                    budgets['transaction_id'][budgets['id'].index(edit_budget_id)] = associated_transactions

                                    budgets['amount'][budgets['id'].index(edit_budget_id)] = new_amount_input
                                    budgets['budget_used'][budgets['id'].index(edit_budget_id)] = 0


                                    # Update budget_used if user has asscoiated transactions
                                    if associated_transactions:
                                        for i in associated_transactions:
                                            if budgets['start_date'][budgets['id'].index(edit_budget_id)] <= transactions['date'][transactions['id'].index(i)] <= budgets['end_date'][budgets['id'].index(edit_budget_id)]: 
                                                budgets['budget_used'][budgets['id'].index(edit_budget_id)] += transactions['amount'][transactions['id'].index(i)]
                                else:
                                    break
                    else:
                        new_amount_input = input('Please enter new amount: ')
                        confirm_input = input('Are you sure to edit the budget (yes/no)? ').lower()
                        while confirm_input not in ['yes', 'no']:
                            print('Invalid option. Please select an option between "yes" or "no".')
                            confirm_input = input('Are you sure to edit the budget (yes/no)? ').lower()
                        else:
                            if confirm_input == 'yes':
                                budgets['amount'][budgets['id'].index(edit_budget_id)] = int(new_amount_input)
                            else:
                                break
                    
                    more_input = input('Edit more budget (yes/no)? ').lower()
                    while more_input not in ['yes', 'no']:
                        print('Invalid option. Please select an option between "yes" or "no".')
                        more_input = input('Edit more budget (yes/no)? ').lower()
                    else:
                        if more_input == 'no':
                            break

def delete_budgets(user_id):
    while True:
        if user_id not in budgets['user_id']:
            print('You haven\'t added any budget.')
            break
        else:
            view_budgets(user_id=user_id)
            delete_budget_input = int(input('Please enter budget ID to delete: '))
            b_user_id_index = index_list(lst=budgets['user_id'], value=user_id)
            budget_id = [budgets['id'][i] for i in b_user_id_index]

            while delete_budget_input not in budget_id:
                print('Invalid option. Please try select an option from the list above.')
                delete_budget_input = int(input('Please enter budget ID to delete: '))
            else:
                confirm_input = input('Are you sure to delete the budget (yes/no)? ').lower()
                while confirm_input not in ['yes', 'no']:
                    print('Invalid option. Please select an option between "yes" or "no".')
                    confirm_input = input('Are you sure to delete the budget (yes/no)? ').lower()
                else:
                    if confirm_input == 'yes':
                        index_to_delete = budgets['id'].index(delete_budget_input)
                        for key in budgets:
                            if key != 'num_of_data':
                                budgets[key].pop(index_to_delete)
                        # If user still has budget
                        if user_id in budgets['user_id']:
                            more_input = input('Delete more budget (yes/no)? ').lower()
                            while more_input not in ['yes', 'no']:
                                print('Invalid option. Please select an option between "yes" or "no".')
                                more_input = input('Delete more budget (yes/no)? ').lower()
                            else:
                                if more_input == 'no':
                                    break
                        else:
                            break
                    else:
                        break

main_menu()