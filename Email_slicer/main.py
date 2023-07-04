def Email_Slicer():
    email_address = input('Enter email address: ')
    (username, domain) = email_address.split('@')
    (domain, extension) = domain.split('.')

    print(f'Username: {username}')
    print(f'Domain: {domain}')
    print(f'Extension: {extension}')

while True:
    Email_Slicer()