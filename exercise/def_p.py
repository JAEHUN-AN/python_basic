def var_param_test(*p):
    return p

a = var_param_test(1,2,3,4,5)
print(a)
print(type(a))