#This program translate the point score to letter grade EX: A+,A etc

score = int(input())

if score >100:
    print('good job for getting bonus, but still A+')
elif 100>= score >=97 :
    print('A+')
elif 97> score >=93 :
    print('A')
elif 93> score >=90 :
    print('A-')
elif 90> score >=87 :
    print('B+')
elif 87> score >=83 :
    print('B')
elif 83> score >=80 :
    print('B-')
elif 80> score >=77 :
    print('C+')
elif 77> score >=73 :
    print('C')
elif 73> score >=70 :
    print('C-')
elif 70> score >=67 :
    print('D+')
elif 67> score >=63 :
    print('D')
elif 63> score >=60 :
    print('D-')
elif 60> score >=0 :
    print('F')
else:
    print('F- ....seems like teacher doesnt like you :P')
