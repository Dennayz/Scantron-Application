### CMPT 120 
### author Diana Cukierman
###
### Project - Scantron Data processing 
###
###  CODE PROVIDED



def read_string_list_from_file(the_file):
    '''
    GENERIC READING OF TEXT FILE
    USE AS TEMPLATE, INCORPORATE IN YOUR FILE
    GENERATES A LIST OF STRINGS, ONE STRING PER ELEMENT
    AUTHOR: Diana Cukierman

    Assumptions:
    1) the_file is in the same directory (folder) as this program 
    2) the_file contains one student per "line"  
    3) lines are separated by "\n", that is, after each "line" (student)
       in the file  there is a return ("\n") . Also there is (one single)
       return ("\n") after the last line  in the_file
    4) Thhis function returns a list of strings
    '''
    
    fileRef = open(the_file,"r")      # opening file to be read
    localList=[]                      # new list being constructed
    for line in fileRef:
        string = line[0:len(line)-1]  # -1: eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)      # appends a new element
                                      # of type string to the list
        
    fileRef.close()  
        
    #........
    print ("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print (element)  # element is a string for one student
    #........
        
    return localList

    
    
def write_result_to_file(lres,the_file):
    '''
    Creates a text output file from a list of strings
    AUTHOR: Diana Cukierman
    
    Assumptions:
    1) lres is a list of strings, where each string
       will be one line in the output file
    2) the_file will contain the name fo the output file.
       for this porgram it shoudl be a name with .csv extension
    3) it is assumed that each string in lres already includes
       the character "\n" at the end
    4) the resulting file will be in the same directory (folder) as this program 
    5) the resulting file will  contain one student data per line 
    '''
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
                                    
    fileRef.close()
    return
def title():
    print("~Welcome to this CMPT 120 Scantron Processing system~")
    print(" ====================================================")
    return

def points():
    new_lst=[]
    st_lst=[]
    new_lst=key[1].split(" ")
    for i in range(len(new_lst)):
        st_lst=float(new_lst[i])
        print(str(st_lst)+" ", end="")
    return

def maximum_point():
    new_lst=[]
    add=0
    new_lst=key[1].split(" ")
    for i in range(len(new_lst)):
        add=add+float(new_lst[i])
    return(add)

real_lst = []
test_lst=[]


def compareAll(alist):
    for i in range(len(alist)):
        test_lst.append(alist[i].split())
        ##print(ans_lst)
        score_lst=key[1].split(" ")
        ##print(point_lst)
        st=" "
        avg=0.0
    for j in range(len(test_lst)):
        total=0.0
        for i in range(len(test_lst[j][1])):
            if test_lst[j][1][i]==key[0][i]:
                total= total + float(score_lst[i])
            avg=total/maximum_point()*100
            st= test_lst[j][0]+ "," + str(total) + "," + str(avg)
        real_lst.append(st.split(","))
        if user_input.lower()=="all":
            print(st)
            print()
            
    return(real_lst)        

def stats (biglist):
    highest_grade=biglist[0][1]
    for i in range(len(biglist)):
        if biglist[i][1]>highest_grade:
            highest_grade=biglist[i][1]
    print("Maximum points: ",highest_grade)
    print()
    average_score=0.0
    tot=0.0
    for i in range(len(biglist)):
        tot=tot+float(biglist[i][1])
    average_score=tot/len(biglist)
    print("Average points: ", average_score)
    print()
    total_students=len(biglist)
    print("Number of students processed: ", total_students)
    return(highest_grade, average_score, total_students)


def all_correct(somelst):
    correct_lst=[]
    for j in range(len(key[0])):
        count=0
        for i in range(len(somelst[j][1])):
            if somelst[j][1][i]==key[0][i]:
                count=count+1
        correct_lst.append(count)
    return(correct_lst)
        


student_ans=read_string_list_from_file("IN_data_studs.txt")
key = read_string_list_from_file("IN_key+pts.txt")
print()
title()
print()
print("The data file in this folder has", len(student_ans),"Students.")
print("There are", len(key[0]),"Questions.")
print()
print("The answer key is: ")
answer_key= ""
for i in range(len(key[0])):
    if (int(key[0][i]) == 1):
        answer_key = answer_key + "A" + " "
    if (int(key[0][i]) == 2):
        answer_key = answer_key + "B" + " "
    if (int(key[0][i]) == 3):
        answer_key = answer_key + "C" + " "
    if (int(key[0][i]) == 4):
        answer_key = answer_key + "D" + " "
    if (int(key[0][i]) == 5):
        answer_key = answer_key + "E" + " "

print(answer_key)
print()
print()
print("The points are:")
points()
print()

print("The maximum points possible are:",maximum_point())
print()
print("You have to choose one of two options:")
print("Type ALL (not case sensitive) to process the whole class.")
print("Type SEL (not case sensitive)  to process selected students.")
print("(up to half of the whole class) for selected students.")
user_input=input("type in your option: ")


while (user_input.isdigit()==True or (user_input.lower()!="all") and (user_input.lower()!="sel")):
    print()
    print("Please retype, ALL or SEL")
    user_input=input("type in your option: ")
    print()
    
if user_input.lower()=="all":
    print("All students have been processed!")
    print()
    print("Here is the output that will be saved in the folder!")
    print()
    real_lst= compareAll(student_ans)

    print("HERE ARE THE STATS!")
    print("===================")
    stats(real_lst)
    print(all_correct(test_lst))

outList=[]

if (user_input.lower()=="sel"):
    real_lst=compareAll(student_ans)
    print("You choose to process provide the name of the student.")
    foundName=False
    half_student=len(real_lst)//2
    num_student=0
    sel_input=input("Type a name or END to finish: ")
    
    while (sel_input.lower()!="end" and num_student<half_student):
        sel_st=""
    
        for student in real_lst:
            if sel_input==student[0]:
                if student not in outList:
                    outList.append(student)
                    point=0
                    foundName=True
                    point=student[1]
                
        if foundName:
            display="Student " + str(sel_input)+" " +"got " + str(point)+" " + "points."
            print(display)
            num_student=num_student+1
            foundName=False
        else:
            print("This name is not in the data or have already been selected, type again")
        sel_input=input("Type a name or END to finish: ")
        
        if num_student>=half_student:
            print("All your selected students have been processed!")
            print()
            print("Here is the output that will be saved in the folder!")
            for i in range(len(outList)):
                sel_st = outList[i][0] +"," + outList[i][1] +"," + outList[i][2]
                print()
                print(sel_st)

            print()
            print("HERE ARE THE STATS!")
            print("===================")
            stats(outList)
        

    if sel_input.lower()=="end":
        if outList==[]:
            print("No students were selected from the data.")
        else:
            print("All your selected students have been processed!")
            print()
            print("Here is the output that will be saved in the folder!")
            for i in range(len(outList)):
                sel_st = outList[i][0] +"," + outList[i][1] +"," + outList[i][2]
                print()
                print(sel_st)

            print()
            print("HERE ARE THE STATS!")
            print("===================")
            stats(outList)
        #print(outList)
        
