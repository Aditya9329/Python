r =open("tester.txt","r")
print(r.read())
print(r.read()) #end of line o/p will be ''
# reset the cursor 
r.seek(0)
print(r.read())
# what position cursor is available 
print(r.tell())