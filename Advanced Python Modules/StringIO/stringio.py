import io
string = 'This is a simple string'

fil = io.StringIO(string)

print(fil.read())
fil.write('\nthis is second line to simple string')
fil.seek(0)
print(fil.read())
fil.close()