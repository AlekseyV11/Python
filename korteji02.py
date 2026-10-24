n = int(input())
students = []
for _ in range(n):
    students.append(input())

for s in students:
    print(s)
print()
for s in students:
    name, grade = s.split()
    if grade in ('4', '5'):
        print(s)