# Write a program that asks the user for email addresses, one at a time (until the user inputs 'q'), 
# puts them into a list and then prints out a list of tuples of usernames and domains.
 
# The main program is given - DO NOT change it.
 
# Example run:
 
# Email address: siggi@ru.is
# Email address: magga@hi.is
# Email address: stina@ru.is
# Email address: q
# ['siggi@ru.is', 'magga@hi.is', 'stina@ru.is']
# [('siggi', 'ru.is'), ('magga', 'hi.is'), ('stina', 'ru.is')]


def get_emails():
    email_list = []
    while True:
        email = input("Email address: ")
        if email.lower() == "q":
            break
        else:
            email_list.append(email)
    return email_list

def get_names_and_domains(email_list):
    tuple_list =[]
    for email in email_list:
        name_domain = email.split("@")
        tuple_ = name_domain[0], name_domain[1]
        tuple_list.append(tuple_)
    return tuple_list




email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)