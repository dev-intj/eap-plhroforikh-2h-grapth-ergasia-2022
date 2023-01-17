# 1. Μετατροπή δεκαδικού αριθμού στο δυαδικό σύστημα


def dec_to_bin(num):
    n = int(num)
    result = []
    exp = 0
    while n > 0:
        if n % 2 == 1:
            result.insert(0, "1")
            n = (n-1)//2
        else:
            result.insert(0, "0")
            n = n//2
        exp += 1
    return result or 0

# 2. Μετατροπή δυαδικού αριθμού στο δεκαδικό σύστημα


def bin_to_dec(num):
    if num == '0':
        return 0
    elif num == '1':
        return 1
    else:
        if num[-1] == '1':
            return bin_to_dec(num[:-1]) * 2 + 1
        else:
            return bin_to_dec(num[:-1]) * 2 + 0

# 3. Εύρεση συμπληρώματος δυαδικού αριθμού


def twos_comp(num):
    arr = []
    firstDigit = False
    for c in reversed(num):
        # βρεθηκε το πρώτο 1, assignment σε variable οτι βρέθηκε
        # και χωρις αλλαγη το βάζουμε στην λίστα
        if (c == "1" and firstDigit == False):
            firstDigit = True
            arr.insert(0, c)
        # αμα δεν έχει βρεθει το πρώτο 1 τοτε μην το αλλαζεις
        elif (firstDigit == False):
            arr.insert(0, c)
        # αλλαγη του 1 με το 0 και αντιστροφα αμα έχει βρεθεί το πρώτο 1
        else:
            if (c == "1"):
                arr.insert(0, "0")
            else:
                arr.insert(0, "1")

    return arr


# ελεγχός δυαδικού αριθμού
def isBinary(num):
    count = 0
    b = '10'
    for char in num:
        if char not in b:
            count = 1
            break
        else:
            pass
    if count:
        return False
    else:
        return True


# ΜΕΝΟΥ
if __name__ == "__main__":
    while True:
        print("Επιλογές")
        print("========")
        print("1. Μετατροπή δεκαδικού αριθμού στο δυαδικό σύστημα")
        print("2. Μετατροπή δυαδικού αριθμού στο δεκαδικό σύστημα")
        print("3. Εύρεση συμπληρώματος δυαδικού αριθμού")

        choice = input("Δώστε την επιλογή σας (enter για έξοδο): ")

        if (choice == "1" or choice == "2" or choice == "3"):

            if choice == "1":
                value = input("Δώσε έναν θετικό αριθμό: ")
                # έλεγχος αμα η απάντηση του είναι θετικός ή integer
                if int(value) and int(value) >= 0:
                    print("H δυαδική αναπαράσταση του αριθμού",
                          value, "είναι", ''.join(dec_to_bin(value)))
                pass

            elif choice == "2":
                value = input(
                    "Δώστε ένα δυαδικό αριθμό (τα ψηφία του είναι 0 ή 1): ")
                # έλεγχος αμα η απάντηση του user ειναι δυαδικός αριθμός
                if (isBinary(value)):
                    # H συνάρτηση αυτή να εμφανίζει το μήκος του αριθμού σε bits ?
                    print("μήκος του αριθμού σε bits :")
                    n = int(value)
                    print(bin(n), (n).bit_length(), len(bin(n)) - 2)

                    print("Ο αριθμός στο δεκαδικό σύστημα είναι",
                          bin_to_dec(value))
                else:
                    print(
                        "Μη σωστός δυαδικός αριθμός, πρεπει να αποτελείται απο στοιχεία 0 ή 1.")
                pass

            elif choice == "3":
                value = input(
                    "Δώστε ένα δυαδικό αριθμό (τα ψηφία του είναι 0 ή 1): ")
                # έλεγχος αμα η απάντηση του user ειναι δυαδικός αριθμός
                if (isBinary(value)):
                    print("Το συμπλήρωμα ως προς 2 του αριθμού",
                          value, "είναι το", ''.join(twos_comp(value)))
                else:
                    print(
                        "Μη σωστός δυαδικός αριθμός, πρεπει να αποτελείται απο στοιχεία 0 ή 1.")

                pass

        # ο χρήστης μπορει να σταματήσει το πρόγραμμα με enter
        elif choice == "":
            break

        # ειδοποιηση στον χρήστη
        else:
            print("Μη διαθέσιμη επιλογή... επιτρεπομένες επιλογές είναι:")
