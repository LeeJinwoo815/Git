def inputmark() :
    print('ENTER STUDENT ID : ')
    id=int(input())
    print('ENTER EXAM SCORE: ')
    exam=int(input())
    print('ENTER ALL TEST SCORES: ')
    mark1=int (input())
    mark1=int (input())
    mark3=int (input())
    mark4=int (input())
    mark5=int (input())
    mark6=int (input())
    mark7=int (input())
    mark8=int (input())
    mark9=int (input())
    mark10=int (input())
    mark11=int (input())
    mark12=int (input())
    mark13=int (input())
    mark14=int (input())
    mark15=int (input())
    sum=(mark1+mark2+mark3+mark4+mark5+mark6+mark7+mark8+mark9+mark10+mark11+mark12+mark13+mark14+mark15)
    avge=sum/15
    print('TEST AVERAGE IS :' +str(avge))
    print('Final mark is: ',compute_mark(avge,exam))
    print('Letter Grade is: ',getgrade(compute_mark(avge,exam)))
    return avge
def compute_mark(avge,exam) :
    final_mark=0.4*avge+0.6*exam
    return final_mark
def getgrade(final_mark) :
    if 90<=final_mark<=100:
        grade='A'
    elif 80<=final_mark<=89:
        grade='B'
    elif 70<=final_mark<=79:
        grade='C'
    elif 60<=final_mark<=69:
        grade='D'
    else:
        grade='F'
    return grade
inputmark()