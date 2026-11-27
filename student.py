def student_details(name, usn, college, city):
    return {
        "name": name,
        "usn": usn,
        "college": college,
        "city": city,
        "email": email
    }

if __name__ == "__main__":
    name = input("Enter student name: ")
    usn = input("Enter USN: ")
    college = input("Enter college name: ")
    city = input("Enter city: ")
    email = input("Enter email")

    print(student_details(name, usn, college, city, email))