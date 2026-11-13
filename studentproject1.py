#!/usr/bin/env python
# coding: utf-8

# In[1]:


students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Marks": marks
    }

    print("Student Added Successfully!")

def display_students():
    print("\nStudent Details:")
    for roll, details in students.items():
        print(roll, details)

add_student()
display_students()


# In[2]:


def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        print("Student Found!")
        print("Name:", students[roll]["Name"])
        print("Marks:", students[roll]["Marks"])
    else:
        print("Student Not Found")

search_student()


# In[3]:


def update_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        name = input("Enter New Name: ")
        marks = int(input("Enter New Marks: "))

        students[roll]["Name"] = name
        students[roll]["Marks"] = marks

        print("Student Updated Successfully!")
    else:
        print("Student Not Found")

update_student()


# In[4]:


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found")

delete_student()


# In[5]:


while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")


# In[ ]:




