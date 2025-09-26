n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nStudent {i+1}:")
    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))
    
    
    student = {"name": name, "mark": mark}
    students.append(student)

print("\nStudent List:")
for s in students:
    print(f"Name: {s['name']}, Mark: {s['mark']}")
