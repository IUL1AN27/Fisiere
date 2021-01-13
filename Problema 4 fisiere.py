with open('input.txt','r') as f:
    z=f.readline()
v=int(z)-2
w=int(z)-1
x=int(z)+1
y=int(z)+2
with open ('output.txt', 'w') as f:
   f.write(str(v) + str(w) + z + str(x) + str(y))