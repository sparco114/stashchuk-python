import re
import string


def check():
    def check_email():
        global email
        email = input("Insert email: ")
        email_format = r"^[a-zA-Z0-9-.]+@[a-zA-Z0-9-.]+\.[a-zA-Z]+$"
        email_check_pattern = re.compile(email_format)
        res = email_check_pattern.fullmatch(email)
        if res:
            print('valid')
        else:
            print('not valid email')
            check_email()

    check_email()

    def check_password():
        global password
        password = input("Insert password: ")
        low = r"[a-z]"
        low_pattern = re.compile(low)
        up = r"[A-Z]"
        up_pattern = re.compile(up)
        num = r"[0-9]"
        num_pattern = re.compile(num)
        symb = r"[\W]"  # \W - значит любой не цифро-буквенный символ
        symb_pattern = re.compile(symb)
        if len(password) < 8:
            print('Password must have 8 or more symbols')
            check_password()
        elif not low_pattern.search(password):
            print('Password must have lower letters')
            check_password()
        elif not up_pattern.search(password):
            print('Password must have upper letters')
            check_password()
        elif not num_pattern.search(password):
            print('Password must have numbers')
            check_password()
        elif not symb_pattern.search(password):
            print('Password must have symbols')
            check_password()
        else:
            pass

    check_password()


check()

print(f"Your EMAIL: {email}")
print(f"Your PASSWORD: {password}")
