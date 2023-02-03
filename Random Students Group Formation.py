import random

totalStudents = int(input("How many total students are there ? "))
groupSize = int(input("What is the maximum size of a one group ? "))

groups = []
selectedStudents = []

while(len(selectedStudents) != totalStudents):
    group = []
    while(len(group) != groupSize):
        student = random.randrange(totalStudents+1)
        if student not in group and student not in selectedStudents and student != 0:
            group.append(student)
            selectedStudents.append(student)
    if totalStudents - len(selectedStudents) < groupSize :
        break
    groups.append(group)
    
remainingGroup = []
for student in range(1,totalStudents+1):
    if student not in selectedStudents:
        remainingGroup.append(student)
  
groups.append(remainingGroup)    
i = 0
for group in groups:
    i += 1
    print("Group no ",i,"roll nos:","[ total",len(group),"]",*group)