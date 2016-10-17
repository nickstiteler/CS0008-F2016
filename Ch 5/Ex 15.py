

def det_grade(score):
    #intialize output
    grade = 'F'
    # decide grade
    if score>=90 and score<=100:
        grade = 'A'
    elif score>=80 and score<90:
        grade = 'B'
    elif score>=70 and score<80:
        grade = 'C'
    elif score>=60 and score<70:
        grade = 'D'
def get_grade(message):
    #input
    score =int(input(message))
    #validate
    while score<0 and score> 100:
        #user sucks
        print('score is between 0 and 100')
        score = int(input(message,"AGAIN"))
    #END while
    print("you entered score =",score)
    grade = det_grade(score)
    print('your grade is', grade)
    return(score)
#end def
def det_grade(score):
    #intialize output
    grade = 'F'
    # decide grade
    if score>=90 and score<=100:
        grade = 'A'
    elif score>=80 and score<90:
        grade = 'B'
    elif score>=70 and score<80:
        grade = 'C'
    elif score>=60 and score<70:
        grade = 'D'



