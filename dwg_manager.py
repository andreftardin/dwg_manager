
class Drawings:
    def __init__(self, subject, revision, has_rfis=False):
        self.subject = subject
        self.revision = revision
        self.has_rfis = has_rfis
    
    def __repr__(self):
        if self.has_rfis == True:
            return "The {subject} drawing is currently on revision {revision} and has RFIs.".format(subject=self.subject, revision=self.revision)
        else:
            return "The {subject} drawing is currently on revision {revision} and has no RFI.".format(subject=self.subject, revision=self.revision)


drawings = {}
rfis = {}


def drawing_menu():
    drawings_menu_selection = input("Select subject:\n 1. Structural;\n 2. Architectural;\n 3. Mechanical.\n")
def rfi_menu_selection():
    rfi_menu_selection = input("Select below:\n 1. Add new RFI;\n 2. View Outstanding RFIs;\n 3. View Completed RFIs. \n")

welcome_message = "Welcome to Drawing Manager!"
options_message = "For Drawings press 1.\nFor RFIs press 2."

user_selection = input(welcome_message + "\n" + options_message + "\nTo exit press 3.\n")

if user_selection == "1":
    drawing_menu()
elif user_selection == "2":
    rfi_menu_selection() 
else:
    while user_selection != "1" and user_selection != "2" and user_selection != "3":
        print("Wrong selection, Try again.\n" + options_message + "\nFor exit press 3.")
        user_selection = input()


