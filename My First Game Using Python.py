                            # My First Game Using Python
                                #Game On Squaring numbers
                                    #Patterns, Table of a number, Printing a factorial
                                        #And a report Card

"""Following is for asking normal
                        Details of a person playing the game"""


print('Welcome To Tejas Help.')
name=input("What Is Your Name? ")

while 0<100:
        print("How Can We Help You Today? ")
        print()
        print('Write 1 for squaring numbers')
        print('Write 2 for making a number pattern')
        print('Write 3 for printing a number table')
        print('Write 4 for getting a repot card using your details')
        print('Write 5 for getting a factorial')
        print()
        gameState=int(input("What is Your Decided Number from the above options? "))

        #Following code is for the whole game
        if(gameState==1):
            a=int(input('Okay So Till Which number are the squares to be printed? (We recommend that they are less than 100) '))
            b=1
            print()
            print(name, 'Here Are Your Required Square numbers Till',a)
            print()
            while b<=a:
                print(b*b)
                b=b+1

        elif(gameState==2):
            a=int(input('Okay So How many numbers in pattern should be there? (Remember that there will be 2 extra numbers to make the number) '))
            b=0
            c=1
            print()
            print(name, 'Here Is Your Number Pattern:- ')
            print()
            print(b)
            print(c)
            for i in range(b,a+1):
                d=b+c
                print(d)
                b=c
                c=d

        elif(gameState==3):
            a=int(input('Okay So Of Which Number Table Do you Want? '))
            c=int(input('Till Which Number Will Your given number be multiplied? '))
            b=1
            print()
            print(name, 'Following is the Table Of', a)
            print()
            while b<=c:
                print(a,'*',b,'=',b*a)
                b+=1

        elif(gameState==4):
            print('Okay so fill the following Details To make the report card of the person you want.','\n','If it is for you only then also fill the same' )
            name_a=input('What is The Name? ')
            age=int(input('What Is The age? '))
            name_b=input('What Is The Mother name? ')
            name_c=input('What Is The Father Name ')
            print()
            print(name, 'Following is the report card of', name_a)
            print()
            print('Name: ',name_a)
            print('Age: ',age)
            print("Mother's name: ",name_b)
            print("Father's name: ",name_c)

        elif(gameState==5):
            a=int(input('Okay So What Is The number to make the factorial of? '))
            b=1
            print()
            print(name,'Following is the Factorial of', a)
            for i in range(1,a+1):
                b=b*i
            print()
            print(b)

        print()

