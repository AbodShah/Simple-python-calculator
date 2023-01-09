choose =  input("""what you need?
+
-
×
÷  
type here :  """)
##
print("you need : " +  choose + " " + "Let's Start")
##
x = float(input("choose first number:  "))

y = float(input("choose secont number:  "))

if (choose == "+") :
   print(x + y)
elif (choose == "-"):
   print(x - y)
elif (choose == "×"):
   print(x * y)
elif choose == "÷":
   print(x/y)
else:
   print( choose + "is not correct try again .")
   
