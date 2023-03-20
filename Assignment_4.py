# Elaction Program
a = int( input('Enter First Candidate Vote: '))
b = int( input('Enter Second Candidate Vote: '))
c = int( input('Enter Third Candidate Vote: '))

if (a > b and a > c):
    print(f'Congratulations First Candidate Win Election {a} ')
elif(b > a and b > c):
    5
    print(f'Congratulations Second Candidate Win Election {b}')
elif( a == b or a == c or c == a  ):
    print('Candidate optain Same Result')
else:
    print(f'Congratulations Third Candidate Win Election {c}')