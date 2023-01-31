
drawings = {"Strucutral":0, "Architectural":0, "Mechanical":0}

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

rfis = {}

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


def drawing_menu():
    drawings_menu_selection = input("Select subject:\n 1. Structural;\n 2. Architectural;\n 3. Mechanical.\n")
def rfi_menu_selection():
    rfi_menu_selection = input("Select below:\n 1. Add new RFI;\n 2. View Outstanding RFIs;\n 3. View Completed RFIs. \n")

welcome_message = "Welcome to Drawing Manager!\n For Drawings press 1.\n For RFIs press 2."

user_selection = input(welcome_message + "\n To exit press 3.\n")

if user_selection == "1":
    drawing_menu()
elif user_selection == "2":
    rfi_menu_selection() 
else:
    while user_selection != "1" and user_selection != "2" and user_selection != "3":
        print("Wrong selection, Try again.\n" + options_message + "\nFor exit press 3.")
        user_selection = input()


