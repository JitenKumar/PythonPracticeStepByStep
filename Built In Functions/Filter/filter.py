
# filter : results which returns True are included in the output

list = [1,874.42,864.4284284,8247,4248,98724]

var_fil = filter(lambda num: num%2 == 0,list)
print([x for x in var_fil])

