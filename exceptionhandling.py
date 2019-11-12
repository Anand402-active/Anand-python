a=10
b=2
try :
    print("resource got opened")
    print(a/b)
    k=int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("number can't be divisible by zero=",e)
except ValueError as e:
    print("invalid input=",e)
except Exception as e:
    print("something went wrong=",e)
finally:
    print("resource got closed")
