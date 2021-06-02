# try and except - an error catching method ("insurance policy")
# minimize code inside try and except blocks
# Once bad line is hit, the code breaks and exits the try and except block
astr = "bob"
try:
    istr = int(astr) # try to convert the variable astr to an integer
except:
    istr = -1 
print('First',istr)

astr = '123'
try:
    istr = int(astr) # try to convert the variable astr to an integer
except:
    istr = -1 
print('Second',istr)

