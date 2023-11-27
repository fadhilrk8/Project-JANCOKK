from tkinter import *
from tkinter import messagebox, simpledialog

# Assuming you have a Doctor class defined as follows:
class Doctor:
    def __init__(self, name, specialization, phone, schedule):
        self.name = name
        self.specialization = specialization
        self.phone = phone
        self.schedule = schedule

# List of doctors
doctors_list = [
            Doctor("dr. Agung, Sp.M", "Mata", "082145678901", "09:00-12:00, Jumat: 09:00-11:30, Sabtu: 12:00-15:00"),
            Doctor("dr. Adrian, Sp.M", "Mata", "081234567890", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("dr. Cessy, Sp.M", "Mata", "08567890234", "Minggu: 09:00-12:00, Kamis: 12:00-15:00"),
            Doctor("drg. Agnesia", "Gigi", "089789012345", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("drg. Fendly", "Gigi", "081234567891", "Selasa: 09:00-12:00, Jumat: 12:00-15:00, Sabtu: 09:00-11.30"),
            Doctor("drg. Nadila", "Gigi", "082145678902", "Minggu: 09:00-11:30, Kamis: 09:00-12:00"),
            Doctor("dr. Chandra, Sp.KK", "Luar tubuh", "0856789012345", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("dr. Rafika, Sp.DV", "Luar tubuh", "0897890123456", "Selasa: 09:00-12:00, Jumat: 09:00-11:45, Sabtu: 09:00-11:30"),
            Doctor("dr. Parwoto, Sp.KK", "Luar tubuh", "081234567892", "Minggu: 12:00-15:00, Kamis: 09:00-12:00"),
            Doctor("dr. Pratama Sp.PD", "Dalam tubuh", "082145678903", "Senin: 09:00-12:00, Rabu: 12:00-15:00"),
            Doctor("dr. Iskandar Sp.PD", "Dalam tubuh", "085678901236", "Selasa: 09:00-12:00, Jumat: 09:00-11:30, Sabtu:09:00-11:45"),
            Doctor("dr. Theresia Sp.PA", "Dalam tubuh", "089789012347", "Minggu: 09:00-12:00, Kamis: 12:00-15:00"),
            Doctor("dr. Hayulani, Sp.KJ", "Jiwa", "081234567893", "Senin: 09:00-12:00, Rabu: 09:00-11:30"),
            Doctor("dr. Belinda, Sp.Psi.,M.Psi", "Jiwa", "082145678904", "Selasa: 09:00-12:00, Jumat: 09:00-11:30, Sabtu: 12:00-14:00"),
            Doctor("dr. Elissa, Sp.KJ", "Jiwa", "085678901237", "Minggu: 09:00-12:00, Kamis: 09:00-12:00"),
            Doctor("dr. Mega, Sp.THT-KL", "THT", "08125543678", " Senin: 09:00-12:00, Rabu: 09:00-11:30"),
            Doctor("dr. Wicak, Sp.THTBKL", "THT", "089673172258", "Selasa: 09:00-12:00, Jumat: 09:00-11:30"),
            Doctor("dr. Rinindra, Sp.THT", "THT", "081329972375", "Sabtu: 15:30-16:30, Minggu: 11:30-12:00, Kamis: 13:00-15:00"),
]

def display_doctors(doctor_screen, doctors):
    # Create a listbox to display the selected doctors
    listbox = Listbox(doctor_screen, font=('Calibri(Body)', 12))
    for doctor in doctors:
        listbox.insert(END, f"{doctor.name} - {doctor.phone} - {doctor.schedule}")

    listbox.pack(pady=20)

def display_selected_doctor(doctor_screen, selected_doctor):
    # Create a new frame to display the information about the selected doctor
    info_frame = Frame(doctor_screen, bg='white')
    info_frame.pack(pady=20)

    info_text = f"Nama: {selected_doctor.name}\nSpesialisasi: {selected_doctor.specialization}\nNomor Telepon: {selected_doctor.phone}\nJadwal Praktek: {selected_doctor.schedule}"
    Label(info_frame, text=info_text, font=('Calibri(Body)', 12), bg='white').pack()

def select_doctor():
    doctor_screen = Toplevel(root)
    doctor_screen.title("Select Doctor")
    doctor_screen.geometry('600x400+500+200')
    doctor_screen.config(bg='white')

    Label(doctor_screen, text='Select Your Doctor', bg='#fff', font=('Calibri(Body)', 20, 'bold')).pack(pady=20)

    # Create a listbox to display the specializations
    specializations_listbox = Listbox(doctor_screen, selectmode=SINGLE, font=('Calibri(Body)', 12))
    specializations = list(set(doctor.specialization for doctor in doctors_list))  # Get unique specializations
    for specialization in specializations:
        specializations_listbox.insert(END, specialization)
    specializations_listbox.pack(pady=20)

    selected_doctors = []  # Initialize the list to store selected doctors

    # Function to get the selected specialization and display doctors with that specialization
    def get_selected_specialization():
        selected_index = specializations_listbox.curselection()
        if selected_index:
            selected_specialization = specializations[selected_index[0]]
            nonlocal selected_doctors  # Use the nonlocal keyword to modify the outer variable
            selected_doctors = [doctor for doctor in doctors_list if doctor.specialization == selected_specialization]

            if selected_doctors:
                doctor_screen.withdraw()  # Hide the specialization listbox
                display_doctors(doctor_screen, selected_doctors)
            else:
                messagebox.showinfo("No Doctors Found", f"There are no doctors with specialization: {selected_specialization}")
        else:
            messagebox.showwarning("No Specialization Selected", "Please select a specialization.")

    # Button to confirm the specialization selection
    Button(doctor_screen, text='Select Specialization', command=get_selected_specialization, bg='#57a1f8', fg='white').pack()

    # Function to get the selected doctor and display information
    def get_selected_doctor():
        selected_index = listbox.curselection()
        if selected_index:
            selected_doctor = selected_doctors[selected_index[0]]
            display_selected_doctor(doctor_screen, selected_doctor)
        else:
            messagebox.showwarning("No Doctor Selected", "Please select a doctor.")

    # Create a listbox to display the selected doctors
    listbox = Listbox(doctor_screen, font=('Calibri(Body)', 12))
    for doctor in selected_doctors:
        listbox.insert(END, f"{doctor.name} - {doctor.phone} - {doctor.schedule}")
    listbox.pack(pady=20)

    # Button to confirm the doctor selection
    Button(doctor_screen, text='Select Doctor', command=get_selected_doctor, bg='#57a1f8', fg='white').pack()

# Your existing login page code
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        screen = Toplevel(root)
        screen.title("LAPORDOC!")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Welcome to LAPORDOC!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        # Add a button to navigate to the doctor selection page
        Button(screen, text='Select Doctor', command=select_doctor, bg='#57a1f8', fg='white').pack(pady=20)

        screen.mainloop()

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11,))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show="*")
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()
