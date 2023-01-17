import hashlib
from getpass import getpass

user_password_dict = {}
successLogins = 0
failLogins = 0


def hash_password(plain_password):
    return hashlib.sha224(plain_password.encode("UTF-8")).hexdigest()


def new_user(user, pswd, pswd2):
    if user not in user_password_dict.keys():
        if pswd == pswd2:
            user_password_dict[user] = hash_password(pswd)
        else:
            print("Τα συνθηματικά δεν ταιριάζουν.")
    else:
        print("Ο χρήστης υπάρχει ήδη.")


def update_password(user, pswd, pswdNew, pswdNew2):
    if user in user_password_dict.keys():
        if user_password_dict[user] == hash_password(pswd):
            if pswdNew == pswdNew2:
                user_password_dict[user] = hash_password(pswdNew)
            else:
                print("Τα συνθηματικά δεν ταιριάζουν.")
        else:
            print("Το συνθηματικό δεν ταιριάζει.")
    else:
        print("Ο χρήστης δεν υπάρχει.")


def login(user, pswd):
    global successLogins
    global failLogins
    if user in user_password_dict.keys():
        if user_password_dict[user] == hash_password(pswd):
            successLogins = successLogins + 1
            print(f"Ο χρήστης {user} εισήχθη στο σύστημα")
            print(
                f"Επιτυχημένες συνδέσεις {successLogins}, αποτυχημένες συνδέσεις {failLogins}")
        else:
            failLogins = failLogins + 1
            print("Το συνθηματικό δεν ταιριάζει.")
    else:
        print("Ο χρήστης δεν υπάρχει.")


def display_users():
    # displaying header του table
    print("{:<15} {:<20} {:<15} {:<15}".format(
        'Αναγνωριστικά', 'Συνθηματικά', 'Επιτ. συνδέσεις', 'Αποτ. συνδέσεις'))

    for key in user_password_dict:
        print("{:<15} {:<20} {:<15} {:<15}".format(
            key[0:10], user_password_dict[key][0:10] + '...', successLogins, failLogins))

    pass


if __name__ == "__main__":
    while True:
        print("Επιλογές")
        print("========")
        print("1. εγγραφή")
        print("2. ενημέρωση συνθηματικού")
        print("3. είσοδος")
        print("4. λίστα χρηστών")

        choice = input("Εισάγετε την επιλογή σας (enter για έξοδο): ")

        if (choice == "1" or choice == "2" or choice == "3" or choice == "4"):

            if choice == "1":
                user = input("Πληκτρολογήστε το αναγνωριστικό χρήστη: ")
                pswd = getpass(
                    prompt="Πληκτρολογήστε το συνθηματικό: ")
                pswd2 = getpass(
                    prompt="Πληκτρολογήστε ξανά το συνθηματικό: ")
                new_user(user, pswd, pswd2)

            elif choice == "2":
                user = input("Πληκτρολογήστε το αναγνωριστικό χρήστη: ")
                pswd = input("Πληκτρολογήστε το τρέχον συνθηματικό: ")
                pswdNew = getpass(
                    prompt="Πληκτρολογήστε το καινούριο συνθηματικό: ")
                pswdNew2 = getpass(
                    prompt="Πληκτρολογήστε ξανά το καινούριο συνθηματικό: ")
                update_password(user, pswd, pswdNew, pswdNew2)

            elif choice == "3":
                user = input("Πληκτρολογήστε το αναγνωριστικό χρήστη: ")
                pswd = getpass(
                    prompt="Πληκτρολογήστε το συνθηματικό: ")
                login(user, pswd)

            elif choice == "4":
                display_users()

        # ο χρήστης μπορει να σταματήσει το πρόγραμμα με enter
        elif choice == "":
            break

        # ειδοποιηση στον χρήστη
        else:
            print("Μη διαθέσιμη επιλογή... επιτρεπομένες επιλογές είναι:")
