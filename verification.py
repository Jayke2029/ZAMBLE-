def clean():
    if (spin != "y"):
        spiny = spin.strip()
        spin_stripped = spiny.strip ("qwertuiopasdfghjklzxcvbm")
        if (spin_stripped != "y" or spin_stripped != "n"):
            print ("Please, renter your answer is not valid.")
            spin = input("Would you like to spin? enter only the letter "y" or "n" in lowercase with no spaces!)
            spin = spin.strip()
            if (spin == "y" or spin == "n")
                zen = 3
                print ("your inputs were not valid ending game")

