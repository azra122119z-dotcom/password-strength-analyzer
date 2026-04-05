password= input("Create password: ")
score=0
suggestions=[]
if len(password)>=9:
    score+=2
else:
    m=("add more characters")
    suggestions.append(m)
if any(c.isdigit() for c in password):
    score+=2
else:
    n=("add digits")
    suggestions.append(n)
if any(c.isalpha() for c in password):
    score+=2
else:
    l=("add letters ")
    suggestions.append(l)
if any(c.isupper() for c in password):
    score+=2
else:
    a=("include more uppercase letters")
    suggestions.append(a)
if any(c.islower() for c in password):
    score+=2
else:
    b=("include lowercase letters")
    suggestions.append(b)
if '1234'in(password):
    score-=2
if 'abcd'in(password):
    score-=2
print("your score is",score, "/10")

if score ==10:
    print("Strong password")
    print("no suggestion ")
elif score >=6:
    print("moderate password")
    print("suggestions:")
    for s in suggestions:
        print('-', s)
else:
    print("weak password ")
    print("suggestions:")
    for s in suggestions:
        print ('-', s)
    
    
