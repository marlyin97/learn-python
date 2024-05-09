
#EXCEPTION HANDLING
#Understanding of Exception: what, exception handler blocks (try,except,else,finally)
#Exception handling methodologies: Block level or Statement level
#Types of Exception: Predefined (TypeError, ValueError, KeyError,DivideByZero,IndexError,FileNotFound..) & Userdefined/CustomExceptions
#importance - Dataengineer less (already framework spark or any other handled the exceptions)
#importance - python developer (application/framework/tool/automation) medium (already framework spark handled the exceptions)
#What? - Exception is a error occurrs when the program is executing at any stage for any
# reasons (data error, name/key/value error, type error, environment error, file not found, format error)
# and makes the flow of program terminated abruptly (out of control)
# Exception Handler (graceful handling of program termination by generating logs, messages, alternative codes, releasing of resources, closing of connections)
# help us handle or take the control from the line where main program got terminated - is a construct/code that help us handle the state of exception
#Example:
#exception->exceptional cases, unexpected events, unusual, abnormal..
#1. try - I am going to a store to buy something to my home (plan it perfectly to avoid any unexpected events)
    #take a vehicle
    # go to shop,
    # add different items in the cart,
    # pay the bill,
    # take a vehicle
    # come back home
#2. except - any unexpected event occurs, handle it accordingly
    #exception1 - trip got cancelled because of some other priority work came
    #exception2 - vehicle is not starting, but i may use some other vehicle or go by walk or call the mechanic and abort my journey
    #exception3 - shop is closed
    #exception4 - some products are not available...
    #exp5- card declined/not accepted or wallet is lost
    #exp6 - vehicle is not starting
    #exp7 - something went wrong which i didn't predicted (expect unexpected)
#3. else - (If except doesn't happened) If I am not getting any exception, what I have to do then?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
#4. (If 1 or 2  happened) If I am not getting any exception or I got some exception, what I have to do?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
    #plan for some other alternative journey
#1 and 2 are mandatory
#3 and 4 are not mandatory

print("Example 1 - to understand what, why, when, blocks/constructs of exception handler in python")
try:
    sal=int(input("Enter the salary\n")) # if anything goes wrong, the exit(1) will occur
    bon_pct=10
    den = int(input("Enter the denominator\n"))
    final_sal=sal+(sal*(10/den)) #;exit(1)
    print(f"Main program - bonus applied sal is {final_sal}")
    #print("bonus given for this month is "+bon_pct)
except ValueError as err_msg:
    print("ValueError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block")
    print(f"Enter the salary in a int format for eg. 10000 or 20000 like that and retry - Actual Err message is : {err_msg}")
except ZeroDivisionError as err_msg:
    print("ZeroDivisionError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block and apply some alternative solution")
    print(f"Zero division error have occured, let the exception handler handles it gracefully  : {err_msg}")
    final_sal=sal+(sal*(10/100))
    print(f"Exception handler program -  bonus applied sal is {final_sal}")
except Exception as err_msg:
    print(f"Exception handler program -  Some unexpected exception occured, lets make some common arrangements {err_msg}")
else:
    print("Else Block - (TRY something if anything goes wrong goto EXCEPTION block else go to ELSE block) Else block in Exception handler program is called if no exception occurs when the main block runs")
    print("If main program complete success, then what I have to do, will be happening in the else block")
    #Close all the files I opened, clean the temporary files if the program complete successfully..
finally:
    print("Finally Block - (TRY something if anything goes wrong goto EXCEPTION block else go to ELSE block but go to FINALLY block whether you goto EXCEPTION or ELSE block)")
    print("At any cost whether Exception occurs or not, got to finally block finally - What ever happens finally runs")
    #Close all the files I opened, DB connections opened, clean the temporary files if the program complete successfully or failed..

print("Example 2 - Exception Handler Types (Predefined & Userdefined/Custom) + Different Types of Predefined Exceptions in exception handler in python")
print("Let's see about Predefined/Builtin Exception types - If already the Python has some regular exception classes/programs created and kept ready to use")
print("Eg. ValueError,ZeroDivisionError ")
#Depends upon the program, logic, functions used - we have to use the necessary exception classes
try:
    sal=int(input("Enter the salary\n")) # if anything goes wrong, the exit(1) will occur
    bon_pct=10
    den = int(input("Enter the denominator\n"))
    assert den!=100,"denominator should be 100"
    bonus_pct=(10/100)
    final_sal=sal+(sal*bonus_pct) #;exit(1)
    print(f"Main program - bonus applied sal is {final_sal}")
    #print("bonus given for this month is "+bon_pct)

except AssertionError as err_msg:
    print(f"AssertionError - {err_msg}")
except ValueError as err_msg:
    print("ValueError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block")
    print(f"Enter the salary in a int format for eg. 10000 or 20000 like that and retry - Actual Err message is : {err_msg}")
except IndentationError as err_msg:
    print("IndentationError - Indentation error occured")
except ArithmeticError as err_msg:
    print("ArithmeticError - Some Arithmetic error occured")
except ZeroDivisionError as err_msg:
    print("ZeroDivisionError - Rather than abruptly aborting the program, I am going to take the control in the exception handler block and apply some alternative solution")
    print(f"Zero division error have occured, let the exception handler handles it gracefully  : {err_msg}")
    final_sal=sal+(sal*(10/100))
    print(f"Exception handler program -  bonus applied sal is {final_sal}")
except Exception as err_msg:
    print(f"Exception handler program -  Some unexpected exception occured, lets make some common arrangements {err_msg}")


print("Example 3 - Exception handling methodologies: Block level or Statement level")
try:
    print("write lines of code")
except Exception as msg:
    print(f"some exception occured {msg}")
