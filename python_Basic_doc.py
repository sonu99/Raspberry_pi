Python sample code
http://www.hlevkin.com/Shell_progr/hellopython.htm
for compilation use 
http://www.tutorialspoint.com/execute_python_online.php
#-----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------Quick python guid----------Ref:http://www.tutorialspoint.com/python/python_quick_guide.htm
#------------------------------------------------------------------------------------------------------------------------------------
Numbers
---------------------
var1=10
----------------------------------------------------------------
String
------
str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 6th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string
-----------------------------------------------------------------
List
----
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd to 4th
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists
-------------------------------------------------------------------
Tuple.....diffrence between tuple and list is Tuple is read only
------
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd to 4th
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists
--------------------------------------------------------------------
Dictionary
----------
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict['name']       # Prints value for 'name' key
print dict['dept']           # Prints value for 'dept' key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
-------------------------------------------------------------------------------
and	Called LogicAAND operator.
        If both the operands are true then then condition becomes true.
Syn:    (a and b) is true.
        -------------------------------------

or	Called LogicaOR Operator.
        If any of the two operands are non zero then then condition becomes true.
Syn:    (a or b) is true.
        -----------------------

not	Called LogicaNOT Operator.
        Use to reverses the logical state of its operand.
        If a condition is true then Logical NOT operator will make false.
Syn:    not(a && b) is false.
        ----------------------

in	Evaluates to true if it finds a variable in the specified sequence and false otherwise.
Syn:    x in y,
        here in results in a 1 if x is a member of sequence y.
        -----------------------
        
not in	Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
Syn:    x not in y,
        here not in results in a 1 if x is not a member of sequence y.
        ------------------------
        
is	Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
Syn:    x is y,
        here is results in 1 if id(x) equals id(y).
        ------------------------
        
is not	Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
Syn:    x is not y,
        here is not results in 1 if id(x) is not equal to id(y).

                           
 ------------------------------------------------------------------------------
			if
			--
if expression:
   statement(s)
------------------------------------------------------------------------------------
			if else
			-------
if expression:
   statement(s)
else:
   statement(s)
------------------------------------------------------------------------------------
          
                       if...elif
		      -------------
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
--------------------------------------------------------------------------------------
			Nested if...elif...else
			------------
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)
---------------------------------------------------------------------------------------
 			
			  while Loop:	
			--------------------
while expression:
   statement(s)
---------------------------------------------------------------------------------------
			for Loop:
                         -----------------
for iterating_var in sequence:
   statements(s)
ex...
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"
---------------------------------------------------------------

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
  
var = 10                           # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"

-------------------------------------------------------------------
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      continue

print "Good bye!"

------------------------------------------------------------------
#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str;
   return;

# Now you can call printme function
printme("I'm first call to user defined function!");
printme("Again second call to the same function");
-------------------------------------------------------------------
