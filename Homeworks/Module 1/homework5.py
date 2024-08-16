immutable_var = 1, 2, 3, 'hello'
print(immutable_var)
print(type(immutable_var))

#immutable_var[0] = 2
#print(immutable_var)

mutable_list = ['green', 'blue', 'red']
print(mutable_list)
mutable_list[1] = 'black'
mutable_list[-1] = 'white'
print(mutable_list)