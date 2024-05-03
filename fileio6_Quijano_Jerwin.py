import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
# from tkcalendar import DateEntry 


# LOGIN INTERFACE WITH A DIMENSION OF 350 - w and 200 height, with a 
# login button and a cancel button
# after a successful login, the user with be redirected to the personal information form
# below the personal information form is a NEXT button and a cancel button
# after pressing the Next button, the user is redirected to the College Qualification form
# all data must be saved in a json file with an optional TreeView requirement 


root = Tk()
systemFont = "Roboto 13"

Label(root, text="Log in", font="Roboto 20").grid(row=0, column=0,padx=10, pady=10,columnspan=3)

# name widgets
name_lbl = Label(root, text="Name: ", font=systemFont)
nameEntry = Entry(root, font=systemFont)
name_lbl.grid(row=1, column=0, pady=10,padx=10,sticky=W)
nameEntry.grid(row=1, column=1, pady=10,padx=10,sticky=E)
# password widgets
password_lbl = Label(root, text="Password: ", font=systemFont)
passwordEntry = Entry(root, font=systemFont, show="*")
password_lbl.grid(row=2, column=0, pady=10,padx=10,sticky=W)
passwordEntry.grid(row=2, column=1, pady=10,padx=10,sticky=E)
# buttons widgets 
registerBtn = Button(root, text="Register", font=systemFont, command=lambda:register())    
registerBtn.grid(row=3, column=0, padx=10, pady=10,sticky=W)
loginBtn = Button(root, text="Login", font=systemFont, command=lambda:loginValidate())
loginBtn.grid(row=3, column=1, padx=10, pady=10, sticky=E)

def back2main(name):
    name.withdraw()
    root.deiconify()
            
def submit(filename,title, data):
    if os.path.exists(filename):
        with open(filename, 'r') as readFile:
            name = json.load(readFile)
    else:
        name = {title:[]}
        
    if not data:
        messagebox.showerror("Alert!","Please fill up the form before proceeding.")
        return
    
    name[title].append(data)
    with open(filename, 'w') as updataedFile:
        json.dump(name, updataedFile, indent=4)
    messagebox.showinfo("test",f"Successfully registered!")
    

def register():
    global credentialsDatas, creds_data
    root.withdraw()
    register = Toplevel()
    Label(register, text="Register", font="Roboto 20").grid(row=0, column=0,padx=10, pady=10,columnspan=3)

    credentialsDatas = "creds.json"
    
    # name widgets
    Rname_lbl = Label(register, text="Name: ", font=systemFont)
    RnameEntry = Entry(register, font=systemFont)
    Rname_lbl.grid(row=1, column=0, pady=10,padx=10,sticky=W)
    RnameEntry.grid(row=1, column=1, pady=10,padx=10,sticky=E)
    # password widgets
    Rpassword_lbl = Label(register, text="Password: ", font=systemFont)
    RpasswordEntry = Entry(register, font=systemFont, show="*")
    Rpassword_lbl.grid(row=2, column=0, pady=10,padx=10,sticky=W)
    RpasswordEntry.grid(row=2, column=1, pady=10,padx=10,sticky=E)
    
    # buttons widgets 
    cancelBtn = Button(register, text="Cancel", font=systemFont, command=lambda:back2main(register))    
    cancelBtn.grid(row=3, column=0, padx=10, pady=10,sticky=W)
    submitBtn = Button(register, text="Submit", font=systemFont, command=lambda:submit(credentialsDatas,"credentials", get_data()))
    submitBtn.grid(row=3, column=1, padx=10, pady=10, sticky=E)
    
    def get_data(): 
        '''what im trying to say po is when the register form start it will instantly get 
        what is inside the entries thus geting the "". so i figure out to put it
        on a function to catch it''' 
        
        name = RnameEntry.get()
        passoword = RpasswordEntry.get()
        
        if name == "" and passoword == "":
            return
        
        creds_data = {
            "name": name,
            "password": passoword
        }
        RnameEntry.delete(0,END)
        RpasswordEntry.delete(0,END)
        return creds_data
    
    register.mainloop()

def loginValidate():
    with open("creds.json", 'r') as readFile:
        datas = json.load(readFile)

    name = nameEntry.get()
    password = passwordEntry.get()
    
    if not name or not password:
        messagebox.showerror("Alert!", "Please fill up the form before proceeding.")
        return
    
    
    for data in datas["credentials"]:
        if name == data["name"] and password == data["password"]:
            messagebox.showinfo("Login","Log in Successfully!")
            PersonalWind()
        else:
            messagebox.showerror("Alert!", "Access denied.")
            return

def PersonalWind():
    # Create the main window
    global entry_name, text_address, entry_contact_number, entry_email,date_of_birth,combobox_marital_status,sex_var,combobox_nationality,lang_vars, entry_qualification, personal_wind
    root.withdraw()
    personal_wind = Toplevel()
    personal_wind.title("Personal Information Form")

    # Name Entry
    label_name = Label(personal_wind, text="Name:") 
    label_name.grid(row=0, column=0, padx=5, pady=5,sticky=W)
    entry_name = Entry(personal_wind)
    entry_name.grid(row=0, column=1, padx=5, pady=5,sticky=NW)

    # Address Text
    label_address = Label(personal_wind, text="Address:")
    label_address.grid(row=1, column=0, padx=5, pady=5,sticky=W)
    text_address = Text(personal_wind, height=4, width=30)
    text_address.grid(row=1, column=1, padx=5, pady=5,sticky=NW)

    # Contact Number Entry
    label_contact_number = Label(personal_wind, text="Contact Number:")
    label_contact_number.grid(row=2, column=0, padx=5, pady=5,sticky=W)
    entry_contact_number = Entry(personal_wind)
    entry_contact_number.grid(row=2, column=1, padx=5, pady=5,sticky=NW)

    # Email Address Entry
    label_email = Label(personal_wind, text="Email Address:")
    label_email.grid(row=3, column=0, padx=5, pady=5,sticky=W)
    entry_email = Entry(personal_wind)
    entry_email.grid(row=3, column=1, padx=5, pady=5,sticky=NW)

    # Date of Birth DateEntry
    label_dob = Label(personal_wind, text="Date of Birth:")
    label_dob.grid(row=4, column=0, padx=5, pady=5,sticky=W)
    date_of_birth = Entry(personal_wind, width=12, borderwidth=2)
    date_of_birth.grid(row=4, column=1, padx=5, pady=5,sticky=NW)

    # Marital Status Combobox
    label_marital_status = Label(personal_wind, text="Marital Status:")
    label_marital_status.grid(row=5, column=0, padx=5, pady=5,sticky=W)
    marital_statuses = ["Single", "Married", "Divorced", "Widowed"]
    combobox_marital_status = ttk.Combobox(personal_wind, values=marital_statuses)
    combobox_marital_status.grid(row=5, column=1, padx=5, pady=5,sticky=NW)

    # Sex Radio Buttons
    label_sex = Label(personal_wind, text="Sex:")
    label_sex.grid(row=6, column=0, padx=5, pady=5,sticky=W)
    sex_var = StringVar()
    radio_male = Radiobutton(personal_wind, text="Male", variable=sex_var, value="Male",)
    radio_male.grid(row=6, column=1, padx=5, pady=5,sticky=NW)
    radio_female = Radiobutton(personal_wind, text="Female", variable=sex_var, value="Female")
    radio_female.grid(row=6, column=2, padx=5, pady=5,sticky=NW)

    # Nationality Combobox
    label_nationality = Label(personal_wind, text="Nationality:")
    label_nationality.grid(row=7, column=0, padx=5, pady=5,sticky=W)
    nationalities = ["USA", "UK", "Canada", "Australia", "Japan"]
    combobox_nationality = ttk.Combobox(personal_wind, values=nationalities)
    combobox_nationality.grid(row=7, column=1, padx=5, pady=5,sticky=NW)

    # Known Languages Checkbuttons
    label_known_languages = Label(personal_wind, text="Known Languages:")
    label_known_languages.grid(row=8, column=0, padx=5, pady=5,sticky=W)
    languages = ["English", "Tagalog", "Spanish", "Japanese"]
    lang_vars = []
    
    lang1 = Checkbutton(personal_wind, text="English", onvalue=1, offvalue=0, command=lambda:lang_vars.append(languages[0]))
    lang2 = Checkbutton(personal_wind, text="Tagalog", onvalue=1, offvalue=0, command=lambda:lang_vars.append(languages[1]))
    lang3 = Checkbutton(personal_wind, text="Spanish", onvalue=1, offvalue=0, command=lambda:lang_vars.append(languages[2]))
    lang4 = Checkbutton(personal_wind, text="Japanese", onvalue=1, offvalue=0, command=lambda:lang_vars.append(languages[3]))
    
    lang1.grid(row=9, column=0,columnspan=2,padx=10, pady=10,sticky=NSEW)
    lang2.grid(row=10, column=0,columnspan=2,padx=10, pady=10, sticky=NSEW)
    lang3.grid(row=11, column=0,columnspan=2, padx=10, pady=10, sticky=NSEW)
    lang4.grid(row=12, column=0,columnspan=2,padx=10, pady=10, sticky=NSEW)
    
    cancelbtn = Button(personal_wind, text="Cancel", command=lambda:cancel_button(personal_wind))
    nextbtn = Button(personal_wind, text="Next", command=lambda:qualificationWind())
    
    cancelbtn.grid(row=13, column=0, padx=10, pady=10,sticky=NW)
    nextbtn.grid(row=13, column=1,sticky=E,columnspan=4,padx=10, pady=10)
    
    personal_wind.mainloop()

def cancel_button(name):
    new = Toplevel()
    def cancel_action():
        name.destroy()
        root.deiconify()
        new.destroy()
    
    mylabel = Label(new, text="Are you sure you want to cancel?")
    mylabel.grid(row=0, column=0, columnspan=2, sticky=NSEW)
    
    b1 = Button(new, text="Yes", command=cancel_action)
    b2 = Button(new, text="No", command=lambda:new.destroy())
    b1.grid(row=1, column=0, padx=10, pady=10,sticky=W)
    b2.grid(row=1, column=1, padx=10, pady=10,sticky=E)
    
    new.mainloop()
    
def qualificationWind():
    global entry_test_no, entry_exam_detail, combobox_shs_school, entry_gwa, text_other_skills
    # Top Level for Qualification
    root.withdraw()
    top_level_qualification = Toplevel(root)
    top_level_qualification.title("Qualification Information")
    personal_wind.withdraw()

    # Test No Entry
    label_test_no = Label(top_level_qualification, text="Test No:")
    label_test_no.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    entry_test_no = Entry(top_level_qualification)
    entry_test_no.grid(row=0, column=1, padx=5, pady=5,sticky=NW)

    # Exam Detail Entry
    label_exam_detail = Label(top_level_qualification, text="Exam Detail:")
    label_exam_detail.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    entry_exam_detail = Entry(top_level_qualification)
    entry_exam_detail.grid(row=1, column=1, padx=5, pady=5, sticky=NW)

    # Senior HighSchool Combobox
    label_shs_school = Label(top_level_qualification, text="Senior High School:")
    label_shs_school.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    shs_schools = ["School A", "School B", "School C", "School D", "School E"]
    combobox_shs_school = ttk.Combobox(top_level_qualification, values=shs_schools)
    combobox_shs_school.grid(row=2, column=1, padx=5, pady=5, sticky=NW)

    # GWA Entry
    label_gwa = Label(top_level_qualification, text="GWA:")
    label_gwa.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    entry_gwa = Entry(top_level_qualification)
    entry_gwa.grid(row=3, column=1, padx=5, pady=5, sticky=NW)

    # Other Skills Text
    label_other_skills = Label(top_level_qualification, text="Other Skills:")
    label_other_skills.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    text_other_skills = Text(top_level_qualification, height=3, width=30)
    text_other_skills.grid(row=4, column=1, padx=5, pady=5,sticky=NW)

    # Tree view
    global myTreeview
    myColumns = ("Name", "Address", "Contact", "Email", "Dob", "Martial", "Sex", "Nationality", "Lang", "Test_No", "Exam","shs_school","Gwa","Other_skills")
    myTreeview = ttk.Treeview(top_level_qualification, columns=myColumns)
    myTreeview.heading("Name", text="Name")
    myTreeview.heading("Address", text="Address")
    myTreeview.heading("Contact", text="Contact No")
    myTreeview.heading("Email", text="Email")
    myTreeview.heading("Dob", text="Date of birth")
    myTreeview.heading("Martial", text="Matial Status")
    myTreeview.heading("Sex", text="Sex")
    myTreeview.heading("Nationality", text="Nationality")
    myTreeview.heading("Lang", text="Languages")
    myTreeview.heading("Test_No", text="Test Number")
    myTreeview.heading("Exam", text="Exam_detail")
    myTreeview.heading("shs_school", text="SHS_School")
    myTreeview.heading("Gwa", text="GWA")
    myTreeview.heading("Other_skills", text="Other skills")
    
    myTreeview.column("#0", width=0, stretch=NO)
    myTreeview.column("Name", width=100)
    myTreeview.column("Address", width=150)
    myTreeview.column("Contact", width=100)
    myTreeview.column("Email", width=150)
    myTreeview.column("Dob", width=100)
    myTreeview.column("Martial", width=100)
    myTreeview.column("Sex", width=100)
    myTreeview.column("Nationality", width=100)
    myTreeview.column("Lang", width=100)
    myTreeview.column("Test_No", width=100)
    myTreeview.column("Exam", width=100)
    myTreeview.column("shs_school", width=100)
    myTreeview.column("Gwa", width=100)
    myTreeview.column("Other_skills", width=100)

    myTreeview.grid(row=0, column=2, columnspan=5, rowspan=10, padx=10, pady=10)
    
    load_treeview()
    
    # Save Button
    btn_save = Button(top_level_qualification, text="Save", command=lambda:save_data())
    btn_save.grid(row=9, column=1, sticky=W, padx=10, pady=10)
    
    cancelbtn1 = Button(top_level_qualification, text="Cancel", command=lambda:cancel_button(top_level_qualification))
    cancelbtn1.grid(row=9, column=0, sticky=E, padx=10)
    

def load_treeview(): 
    with open("students_data.json", 'r') as readFile:
        data = json.load(readFile)
        
    rows = myTreeview.get_children() # THIS INSURE TO DELETE ALL THE PREVIOUS DATAS IN THE TREEVIEW HAD TO RESEARCH THIS ONE PO.
    for row in rows:
        myTreeview.delete(row)
         
    for datas in data["students_data"]:
        myTreeview.insert("", "end", values=(datas["name"],datas["address"],datas["contact_number"],datas["email"],datas["Date_of_birth"],datas["martial_status"],datas["sex"],datas["nationality"],datas["known_languages"],datas["Test_no"],datas["exam_detial"],datas["shs_school"],datas["GWA"],datas["Other_skills"]))
        
def save_data():
    # Retrieve data from widgets
    
    name = entry_name.get()
    address = text_address.get("1.0", END).strip()
    contact_number = entry_contact_number.get()
    email = entry_email.get()
    dob = date_of_birth.get()
    marital_status = combobox_marital_status.get()
    sex = sex_var.get()
    nationality = combobox_nationality.get()
    known_languages = ", ".join(lang_var for lang_var in lang_vars)
    test_no = entry_test_no.get()
    exam_detail = entry_exam_detail.get()
    shs_school = combobox_shs_school.get()
    gwa = entry_gwa.get()
    other_skills = text_other_skills.get("1.0", END).strip()

    sample_data = {
        "name": name,
        "address": address,
        "contact_number": contact_number,
        "email": email,
        "Date_of_birth": dob,
        "martial_status": marital_status,
        "sex": sex,
        "nationality": nationality,
        "known_languages": known_languages,
        "Test_no": test_no,
        "exam_detial": exam_detail,
        "shs_school": shs_school,
        "GWA": gwa,
        "Other_skills": other_skills
    }
    
    submit("students_data.json", "students_data", sample_data)
    load_treeview()
    
    # Print or save the retrieved data (for demonstration)
    # print("Name:", name)
    # print("Address:", address)
    # print("Contact Number:", contact_number)
    # print("Email:", email)
    # print("Date of Birth:", dob)
    # print("Marital Status:", marital_status)
    # print("Sex:", sex)
    # print("Nationality:", nationality)
    # print("Known Languages:", known_languages)

    # print("Test No:", test_no)
    # print("Exam Detail:", exam_detail)
    # print("Senior High School:", shs_school)
    # print("GWA:", gwa)
    # print("Other Skills:", other_skills)




root.mainloop()
