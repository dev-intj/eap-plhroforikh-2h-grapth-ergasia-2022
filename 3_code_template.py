# Όνομα, Επώνυμο, Φύλο, Ημερομηνία Γέννησης, Πτυχίο, Μετακίνηση,
# Νυχτερινή-Εργασία, Εργασιακό Καθεστώς
personnel = """Πίκος, Απίκος, m, 1983/01/01, y, y, n, Active
Μανόλης, Μανάβης, m, 1985/01/01, n, n, y, Active
Μάγια, Μέλισσα, f, 1975/04/01, y, y, y, Active
Ρόζα, Ροζαλία, f, 1980/12/31, y, n, y, Pending
Νταίζη, Ντακ, f, 1940/06/07, n, y, y, Archived
Μπίλμπο, Μπάγκινς, m, 1937/03/03, n, y, n, Archived
Μιχάλης, Καραμάνος, m, 1938/01/01, y, y, y, Archived
Έλενορ, Ρίγκμπι, f, 1966/08/04, n, n, n, Active"""


class Employee:
    def __init__(self, name, last_name, gender, dob, graduate, mobile, night_shift, employment_state):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob

        # representation τιμες
        self.graduateR = graduate
        self.mobileR = mobile
        self.night_shiftR = night_shift

        # αλλαγη απο γραμμα σε Boolean για readibility of code
        if (graduate == "n"):
            self.graduate = False
        else:
            self.graduate = True

        if (mobile == "n"):
            self.mobile = False
        else:
            self.mobile = True
        if (night_shift == "n"):
            self.night_shift = False
        else:
            self.night_shift = True

        self.employment_state = employment_state

    def __repr__(self):
        return repr({", ".join([self.name, self.last_name,
                               self.gender, self.dob, self.graduateR, self.mobileR,
                               self.night_shiftR, self.employment_state])})


# main array
personnel_decoded = []

# δεν χρειαζοταν να τις βαλω εδω αλλα το υποδειγμα υποεργασιας
# με εβαλε σε σκεψεις
female_personnel_set = []
graduate_personnel_set = []
night_shift_personnel_set = []
mobile_personnel_set = []
active_staff_personnel_set = []

# βοηθητική συνάρτηση που εκτυπώνει τα στοιχεία ενός συνόλου


def print_set(set_to_be_printed):
    for i in set_to_be_printed:
        print(i)

# δημιουργία των συνόλων με βάση τα στοιχεία της συμβολοσειράς personnel


def create_sets():

    # building an array for ease of access to everything I need
    splitted = personnel.splitlines()
    for i in splitted:
        res = [x.strip() for x in i.split(',')]
        emp = Employee(*res)
        personnel_decoded.append(emp)

    for employee in personnel_decoded:
        # το προσωπικό που είναι γυναίκες
        if (employee.gender == "f"):
            female_personnel_set.append(employee)

        # το προσωπικό που έχει πτυχίο
        if (employee.graduate == True):
            graduate_personnel_set.append(employee)

        # το προσωπικό που έχει δυνατότητα νυχτερινής εργασίας
        if (employee.night_shift == True):
            night_shift_personnel_set.append(employee)

        # το προσωπικό που έχει τη δυνατότητα μετακίνησης σε κοντινή πόλη
        if (employee.mobile == True):
            mobile_personnel_set.append(employee)

        # το προσωπικό που είναι ενεργό
        if (employee.employment_state == "Active"):
            active_staff_personnel_set.append(employee)

    # print statements
    print("-> Το προσωπικό που είναι γυναίκες")
    print_set(female_personnel_set)

    print("-> Το προσωπικό που έχει πτυχίο")
    print_set(graduate_personnel_set)

    print("-> Το προσωπικό που έχει δυνατότητα νυχτερινής εργασίας")
    print_set(night_shift_personnel_set)

    print("-> Το προσωπικό που έχει τη δυνατότητα μετακίνησης σε κοντινή πόλη")
    print_set(mobile_personnel_set)

    print("-> Το προσωπικό που είναι ενεργό")
    print_set(active_staff_personnel_set)

    pass


# επιστροφή υποσυνόλου μελών προσωπικού με ημερομηνία γέννησης από minDOB και μετά
def age_greater_or_equal(minDOB):
    for employee in personnel_decoded:
        if (employee.dob > minDOB):
            print(employee)
    pass


# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ

# γυναίκες που έχουν πτυχίο ή τη δυνατότητα νυχτερινής εργασίας (ή και τα δύο)
def women_graduate_night_shift():
    for employee in personnel_decoded:
        if (employee.gender == "f"):
            if (employee.graduate or employee.night_shift):
                print(employee)
    pass


# ενεργά μέλη του προσωπικού που έχουν τη δυνατότητα είτε νυχτερινής εργασίας ή μετακίνησης σε κοντινή πόλη, αλλά όχι και τα δύο
def active_night_shift_mobile():
    for employee in personnel_decoded:
        if (employee.employment_state == "Active"):
            if (employee.night_shift and not employee.mobile):
                print(employee)
            elif (employee.mobile and not employee.night_shift):
                print(employee)
    pass


# μέλη του προσωπικού που έχουν πτυχίο αλλά δεν μπορούν να μετακινηθούν
def graduate_not_mobile():
    for employee in personnel_decoded:
        if (employee.graduate and not employee.mobile):
            print(employee)
    pass


# μέλη του προσωπικού που δεν είναι ενεργά
def inactive_staff():
    for employee in personnel_decoded:
        if (employee.employment_state == "Archived" or employee.employment_state == "Pending"):
            print(employee)
    pass


# μέλη του προσωπικού με ημερομηνία γέννησης από ημερομηνία που εισαγάγει ο χρήστης και μετά
def age_limit(dob):
    for employee in personnel_decoded:
        if (employee.dob >= dob):
            print(employee)
    pass


#### κυρίως πρόγραμμα ####

# εδώ αρχικοποιήστε τα σύνολα καλώντας τη συνάρτηση create_sets()

create_sets()

minDOB = input("Δώσε την ημερομηνία γέννησης: ")

age_greater_or_equal(minDOB)

print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ:")


# κλήση συναρτήσεων απάντησης ερωτημάτων γ1 έως γ5

# γ1
print("-> Ποιες γυναίκες έχουν πτυχίο ή τη δυνατότητα νυχτερινής εργασίας (ή και τα δύο)")
women_graduate_night_shift()

# γ2
print("-> Ποια ενεργά (Active) μέλη του προσωπικού έχουν τη δυνατότητα είτε νυχτερινής εργασίας ή μετακίνησης σε κοντινή πόλη, αλλά όχι και τα δύο")
active_night_shift_mobile()

# γ3
print("-> Ποια μέλη του προσωπικού έχουν πτυχίο αλλά δεν μπορούν να μετακινηθούν σε κοντινή πόλη")
graduate_not_mobile()


# γ4
print("-> Ποια μέλη του προσωπικού δεν είναι ενεργά,")
inactive_staff()

# γ5
print("-> Ποια μέλη του προσωπικού έχουν γεννηθεί από μια ημερομηνία που θα δώσει στην είσοδο ο χρήστης και μετά. ")
age_limit(minDOB)
