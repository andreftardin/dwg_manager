
#Define Dictionaries for DWG and RFI
drawings = {"Strucutral":0, "Architectural":0, "Mechanical":0}
rfis = {}

#Create Classes
class Drawings:
    def __init__(self, subject, revision, total_rfis=0):
        self.subject = subject
        self.revision = revision
        self.total_rfis = total_rfis
    
    def __repr__(self):
        if self.total_rfis > 0:
            return "The {subject} drawing is currently on revision {revision} and has {total_rfis} RFIs.".format(subject=self.subject, revision=self.revision, total_rfis=self.total_rfis)
        else:
            return "The {subject} drawing is currently on revision {revision} and has no RFIs.".format(subject=self.subject, revision=self.revision)

class RFI:
    def __init__(self, subject, question, number=len(rfis)+1, resolved=False, answer=""):
        self.subject = subject
        self.number = number
        self.question = question
        self.resolved = resolved
        self.answer = answer
    
    def __repr__(self):
        if self.resolved:
            return "The {subject} drawing has RFI {number} resolved. Question below:\n{question}\nAnswer:\n{answer}".format(subject=self.subject, number=self.number, question=self.question, answer=self.answer)
        else:
            return "The {subject} drawing has RFI {number} not resolved. Question below:\n {question}".format(subject=self.subject, number=self.number, question=self.question)

#Define Functions:
#Menu selection functions:
def drawing_menu():
    drawings_menu_selection = input("Select subject:\n 1. Structural;\n 2. Architectural;\n 3. Mechanical.\n")
    return drawings_menu_selection
def rfi_menu_selection():
    rfi_menu_selection = input("Select below:\n 1. Add new RFI;\n 2. View RFIs Status;\n")
    return rfi_menu_selection
#Add new drawing with revision:
def revise_dwg(subject, revision):
    pass




welcome_message = "Welcome to Drawing Manager!"
options_message = "\n For Drawings press 1.\n For RFIs press 2.\n To exit press 3.\n"
user_selection = input(welcome_message + options_message)

#Check for correct input on main menu:
while user_selection != "1" and user_selection != "2" and user_selection != "3":
    user_selection = input("Wrong selection, Try again." + options_message)

#Check for selected main option:
if user_selection == "1":
    selection = drawing_menu()
    if  selection == "1":
        print("Structural selected")
    elif selection == "2":
        print("Architectural selected")
    elif selection == "3":
        print("Mechanical selected")
    else:
        print("Wrong input")
elif user_selection == "2":
    selection = rfi_menu_selection()
    if selection == "1":
        print("Adding new RFI select drawing to add now")
    elif selection == "2":
        print("select subject drawing to show rfi status")
    else:
        print("Wrong Selection") 
else:
    print("Exiting Drawing Manager!")

