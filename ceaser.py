userval=input("Enter a text ")
key=int(input("Enter a number "))

l=[(ord(c)+key) for c in userval] #Converting to ascii
print(l)

print("Encrypted Data is ")
cipher=''.join(chr(i) for i in l) #Coverting list to String

print(cipher)



l1=[(ord(c)-key) for c in cipher]

recover=''.join(chr(i) for i in l1)
print("Recover Data is "+recover)
