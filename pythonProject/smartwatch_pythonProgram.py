import datetime 

def timeAndDate():
    print('this is the time and date')
    x = datetime.datetime.now()
    print(x)

def holiday():
    Holiday= int(input("what is the numerical month right now ?"))
    if Holiday==12:
        print('The next holday would be christmas and new years eve. ')
    elif Holiday==1:
        print ('The next holiday is new year day and mlk day.`')
    elif Holiday==2:
        print('The next holiday is valentines day.')
    else:
        print('sorry, can only search holiday within the next 90 days. ')

def temp_inFahrenheit():
    
    celsius = float(input("What is the temperature in Celsius with a decimal? "))
    
    fahrenheit = (1.8 * celsius) + 32.00

    print('this is the temperature in Fahrenheit: ' + str(fahrenheit))


def smartWatch():
    #input to take in the user selection.
    print('please select a watch option.')
   
    print('type 1 for time, 2 for the next upcoming holiday , 3 for temperature in fahrenheit.')
    
    selection=int(input('please enter a number: '))
    
    if (selection == 1):
        timeAndDate()
    elif (selection == 2):
           holiday()
    elif (selection == 3):
            temp_inFahrenheit() 
    else:
        print('please select somthing')

smartWatch()  