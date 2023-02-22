dictt= {"Will":88,"Lado":98,"Zach":70,"Jack":76,"Tom":85,"Ria":88,"Marrie":92,"Sam":78}
print(dictt)
# Length of the dictionary
num_students=len(dictt)
print("number of students",num_students)

#avg student scores
totalscore=sum(dictt.values())
avg_score=totalscore/num_students
print("avg scores",avg_score)

#The number of student that score about avg
num_avg_students=0
for score in dictt.values():
    if score > avg_score:
        num_avg_students +=1
print("The number of student that score about avg",num_avg_students)

# the student with the highest score
scores=list(dictt.values())
scores.sort()
print(scores[-1])

# update sam score to 95
x=78
if x in dictt =="Sam" += 17
print(x)