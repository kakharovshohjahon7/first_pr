# 2-masala

# from decimal import Decimal

# x = Decimal ('1.23e2')
# y = Decimal ('4.56e1')
# plus = x+y
# print (plus)




# import time


# def _time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'Spend time : {end - start}')
#         return result

#     return wrapper


# @_time
# def _pow(a, b):
#     time.sleep(2)
#     return a ** b


# _pow(12367, 1080)



def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result

    return wrapper


class User:
    
    username = CharField()
    phone_number = PhoneNumberField()
    def __init__(self, username):
        username = CharField()




