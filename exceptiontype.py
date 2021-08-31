import sys
random = ['a',0,2]
for i in random:
     try:
         print("The entry is",i)
         r=1/int(i)
         break
     except:
         print("Warning!",sys.exc_info()[0],"occurred.")
         print("Next entry.")
         print()