products = [("ΓΑΛΑ 1LT", 1.5), ("ΓΙΑΟΥΡΤΙ ΣΤΡΑΓΓΙΣΤΟ 2%", 2.0), ("ΠΑΓΩΤΟ", 2.5), ("ΝΕΣ ΚΑΦΕ", 7.5), ("ΜΠΙΣΚΟΤΑ ΓΕΜΙΣΤΑ", 1.0),
            ("ΣΑΛΑΤΑ ΣΕΦ", 1.0), ("ΤΥΡΙ ΤΟΣΤ", 6.0), ("ΕΞ. ΠΑΡΘΕΝΟ ΕΛΑΙΟΛΑΔΟ", 8.0), ("ΚΑΦΕΣ ΦΙΛΤΡΟΥ", 7.0), ("ΨΩΜΙ ΤΟΣΤ", 1.5)]

cart = []


def add_products(product, quantity):
    if (product.isdigit() and quantity.isdigit()):
        cart.insert(0, (product, quantity))
    else:
        print('Η επιλογές πρέπει να είναι αριθμοί. ')
    pass


def display_basket():
    # displaying header του table
    print("{:<8} {:<12} {:<10} {:<10} {:<10}".format(
        'ΑΑ', 'ΕΙΔΟΣ', 'ΤΜΧ', 'ΤΙΜΗ ΤΜΧ', 'ΑΞΙΑ'))

    # displaying την λιστα των προιον που εχει επιλεξει ο χρηστης σε μορφη table
    idx = 1
    sum = 0
    for (a, b) in cart:
        eidos = products[int(a)][0]
        priceTMX = products[int(a)][1]
        price = int(b) * products[int(a)][1]
        print("{:<8} {:<12} {:<10} {:<10} {:<10}".format(
            str(idx) + '.', eidos[0:10], b, priceTMX, price))
        idx += 1
        sum = sum + price

    # συνολικη αξια
    synoliko = sum
    print("{:<43} {:<6}".format("", synoliko))

    pass


def remove_product(product):

    pass


def buy_products(cart):
    display_basket()
    confirm = input("Παρακαλώ επιβεβαιώστε την αγορά (ν/ο): ")
    if (confirm == "ν"):
        member = input("Έχετε κάρτα μέλους (ν/ο): ")

        multiply = 1

        if (member == "ν"):
            multiply = 0.8

        sum = 0
        for (a, b) in cart:
            price = int(b) * products[int(a)][1]
            sum = sum + price

        buy = input("Παρακαλούμε πληρώστε ", sum * multiply)

        if (buy == ""):
            print("Σας ευχαριστούμε για την αγορά σας!")
    else:
        print("Ακύρωση παραγγελίας.")

    pass


if __name__ == "__main__":
    while True:
        print("Επιλογές")
        print("========")
        print("1. Προσθήκη προϊόντων στο καλάθι")
        print("2. Εμφάνιση περιεχομένου καλαθιού")
        print("3. Αφαίρεση προϊόντος")
        print("4. Πληρωμή")

        choice = input("Εισάγετε την επιλογή σας: ")

        if (choice == "1" or choice == "2" or choice == "3" or choice == "4"):
            # 1. Προσθήκη προϊόντων στο καλάθι
            if choice == "1":
                answer = None
                while answer != "ο":
                    index = 0
                    for i in products:
                        res = ("Προϊόν #" + str(index) + ': ' +
                               str(i[0]) + ' ' + str(i[1]))
                        print('\n'.join([res]))
                        index += 1
                    product = input("Επέλεξε αριθμό προϊόντος: ")
                    quantity = input("Εισάγετε την επιθυμητή ποσότητα: ")

                    add_products(product, quantity)

                    answer = input(
                        "Επιθυμείτε να εισάγετε άλλο προϊόν (ν/ο): ")

            # 2. Εμφάνιση περιεχομένου καλαθιού
            elif choice == "2":
                display_basket()

            # 3. Αφαίρεση προϊόντος
            elif choice == "3":
                answer = input("Επέλεξε γραμμή προϊόντος προς αφαίρεση: ")
                confirm = input("Παρακαλώ επιβεβαιώστε την αφαίρεση (ν/ο): ")

                if (confirm == "ν"):
                    remove_product(answer)
                    print("Το προϊόν αφαιρέθηκε επιτυχώς από το καλάθι αγορών ")

            # 4. Πληρωμή
            elif choice == "4":
                if not cart:
                    print("Άδειο καλάθι")
                else:
                    buy_products(cart)

        # ο χρήστης μπορει να σταματήσει το πρόγραμμα με enter
        elif choice == "":
            break

        # ειδοποιηση στον χρήστη
        else:
            print("Μη διαθέσιμη επιλογή... επιτρεπομένες επιλογές είναι:")
