m = int(input())
all_students = None
for _ in range(m):
    k = int(input())
    lesson = set()
    for _ in range(k):
        lesson.add(input().strip())
    if all_students is None:
        all_students = lesson
    else:
        all_students &= lesson

for name in sorted(all_students):
    print(name)