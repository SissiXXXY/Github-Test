fibo_list = [1, 1]
"""whatever you put in the bracket adds as a single element of the list"""
while True:
    _next = fibo_list[-1] + fibo_list[-2]
    if len(fibo_list) > 1000:
        break
    else:
        fibo_list.append(_next)

print(fibo_list[999])
