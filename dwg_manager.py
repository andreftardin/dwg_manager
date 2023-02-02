
#Define List of OBJs for DWG and RFI
drawings = []
rfis = []

#Create Classes
class Drawings:
    def __init__(self, subject, revision=0, total_rfis=0):
        self.subject = subject
        self.revision = revision
        self.total_rfis = total_rfis
    
    def __repr__(self):
        if self.total_rfis > 0:
            return "The {subject} drawing is currently on revision {revision} and has {total_rfis} RFIs.".format(subject=self.subject, revision=self.revision, total_rfis=self.total_rfis)
        else:
            return "The {subject} drawing is currently on revision {revision} and has no RFIs.".format(subject=self.subject, revision=self.revision)

    def change_revision(self):
        #self.revision = new_rev
        for drawing in drawings:
            if subject_selection == drawing.subject:
                new_rev = input("Input new revision number for {subject} drawing:\n".format(subject=self.subject))
                self.revision = new_rev
                print(drawing.revision)
                print("{subject} Drawing changed to revision {revision}.".format(subject=self.subject, revision=self.revision))


class RFI:
    #GENERATE NUMBER FOR RFIS WITHOUT INPUT
    _next_num = 1
    def __init__(self, subject, question, resolved=False, answer=""):
        self.subject = subject
        self.number = self._next_num
        #ADD RFI NUMBER AUTOMATICALLY TO CLASS
        type(self)._next_num += 1 
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
    subject_selection = input("Type selected subject: Structural, Architectural or Mechanical.\n")
    return subject_selection


def rfi_menu_selection():
    rfi_menu_selection = input("Select below:\n 1. Add new RFI;\n 2. View RFIs Status;\n")
    return rfi_menu_selection

#Link RFIs to each subjected drawing - make an update function
def update_rfi_count():
    for drawing in drawings:
        for rfi in rfis:
            if drawing.subject == rfi.subject:
                drawing.total_rfis += 1

stru = Drawings("Structural")
arch = Drawings("Architectural")
mech = Drawings("Mechanical")
drawings.append(stru)
drawings.append(arch)
drawings.append(mech)
#print(drawings)
rfi1 = RFI("Structural", "Confirm size of column C1?")
rfi2 = RFI("Structural", "Review size of elevator shaft opening?")
rfi3 = RFI("Architectural", "Waterproofing detail not on drawings")
rfis.append(rfi1)
rfis.append(rfi2)
rfis.append(rfi3)

#Initialize with an update after creation of RFIs
update_rfi_count()


welcome_message = "Welcome to Drawing Manager!"
options_message = "\n For Drawings press 1.\n For RFIs press 2.\n To exit press 3.\n"
user_selection = input(welcome_message + options_message)

#Check for correct input on main menu:
while user_selection != "1" and user_selection != "2" and user_selection != "3":
    user_selection = input("Wrong selection, Try again." + options_message)


#Check for selected main option:
if user_selection == "1":
    subject_selection = input("Type selected subject: Structural, Architectural or Mechanical.\n")
    action = input("{sub} selected.\n 1. To add revision.\n 2. To view status.\n".format(sub=subject_selection))
    if action == "1":
        for drawing in drawings:
            if drawing.subject == subject_selection:
                drawing.change_revision()
    elif action == "2":
        for drawing in drawings:
            if drawing.subject == subject_selection:
                    print(drawing)
    else:
            print("wrong Selection")            

elif user_selection == "2":
    selection = rfi_menu_selection()
    if selection == "1":
        new_rfi_subject = input("Type subject (Structural/Architectural/Mechanical):\n")
        new_rfi_question = input("Input question:\n")
        new_rfi = RFI(new_rfi_subject, new_rfi_question)
        update_rfi_count()
        print("Adding new RFI for {subject} drawing!".format(subject=new_rfi_subject))
    elif selection == "2":
        subject_selection = input("Type selected subject: Structural, Architectural or Mechanical.\n")
        for drawing in drawings:
            if drawing.subject == subject_selection:
                for rfi in rfis:
                    if rfi.subject == subject_selection:
                        print(rfi)
    else:
        print("Wrong Selection") 
else:
    print("Exiting Drawing Manager!")

