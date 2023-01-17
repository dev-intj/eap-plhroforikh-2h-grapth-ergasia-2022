# Όνομα, Επώνυμο, Φύλο, Ημερομηνία Γέννησης, Πτυχίο, Μετακίνηση, Νυχτερινή-Εργασία, Εργασιακό Καθεστώς
personnel = """Πίκος, Απίκος, m, 1983/01/01, y, y, n, Active
Μανόλης, Μανάβης, m, 1985/01/01, n, n, y, Active
Μάγια, Μέλισσα, f, 1975/04/01, y, y, y, Active
Ρόζα, Ροζαλία, f, 1980/12/31, y, n, y, Pending
Νταίζη, Ντακ, f, 1940/06/07, n, y, y, Archived
Μπίλμπο, Μπάγκινς, m, 1937/03/03, n, y, n, Archived
Μιχάλης, Καραμάνος, m, 1938/01/01, y, y, y, Archived
Έλενορ, Ρίγκμπι, f, 1966/08/04, n, n, n, Active"""

# βοηθητική συνάρτηση που εκτυπώνει τα στοιχεία ενός συνόλου


def print_set(set_to_be_printed):
    print(", ".join(set_to_be_printed))


# δημιουργία των συνόλων με βάση τα στοιχεία της συμβολοσειράς personnel
def create_sets():
    pass


# επιστροφή υποσυνόλου μελών προσωπικού με ημερομηνία γέννησης από minDOB και μετά
def age_greater_or_equal(minDOB):
    pass


# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ

# γυναίκες που έχουν πτυχίο ή τη δυνατότητα νυχτερινής εργασίας (ή και τα δύο)
def women_graduate_night_shift():
    pass


# ενεργά μέλη του προσωπικού που έχουν τη δυνατότητα είτε νυχτερινής εργασίας ή μετακίνησης σε κοντινή πόλη, αλλά όχι και τα δύο
def active_night_shift_mobile():
    pass


# μέλη του προσωπικού που έχουν πτυχίο αλλά δεν μπορούν να μετακινηθούν
def graduate_not_mobile():
    pass


# μέλη του προσωπικού που δεν είναι ενεργά
def inactive_staff():
    pass


# μέλη του προσωπικού με ημερομηνία γέννησης από ημερομηνία που εισαγάγει ο χρήστης και μετά
def age_limit():
    pass


#### κυρίως πρόγραμμα ####

# εδώ αρχικοποιήστε τα σύνολα καλώντας τη συνάρτηση create_sets()

print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ:")
# κλήση συναρτήσεων απάντησης ερωτημάτων γ1 έως γ5