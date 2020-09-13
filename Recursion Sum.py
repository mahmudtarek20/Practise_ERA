#str.join()
#The join() method returns a string in which the string elements of sequence have been joined by str separator.
string = "-"
string = string.join(["abc",'def',"IJK"])
#output abc-def-IJK


#str.capitalize()	Converts the first character to upper case
string ="xyzw"
string = string.capitalize()
print(string)
#output: XYZW


#casefold()	Converts string into lower case
string ="XYZW"
string = string.casefold()
print(string)
#output: xyzw


#center()	method will center align the string
string ="XYZW"
string = string.center(10) # it will create 10 charecter string
print(string)
#output:      xyzw

#count()	Returns the number of times a specified value occurs in a string
string ="ADCBD"
string = string. count('D') 
print(string)
#output: 2



#endswith()	Returns true if the string ends with the specified value
string ="TAREK"
string = string.endswith("R")
print(string)
#output: True



#expandtabs()	Sets the tab size of the string
string ="TAREK\tMAHMUD"
string = string.expandtabs(16)
print(string)
#output: TAREK           MAHMUD

#find()	Searches the string for a specified value and returns the position of where it was found
string ="TAREK"
string = string.find("I")
print(string)
#output: 4


#format()	Formats specified values in a string
string = "For only {price:.2f} dollars!"
print(string.format(price = 100))
#output: For only 100.00 dollars!



#index()	Searches the string for a specified value and returns the position of where it was found
string ="TANVIR"
string = string.index("I")
print(string)
#output: 4


#isalnum()	Returns True if all characters in the string are alphanumeric
string ="ABC123"
string = string.isalnum()
print(string)
#output: True


#isalpha()	Returns True if all characters in the string are in the alphabet
string ="ABC123"
string = string.isalpha()
print(string)
#output: False


#isdecimal()	Returns True if all characters in the string are decimals
string ="123"
string = string.isdecimal()
print(string)
#output: True
# float number willl return false


#isidentifier()	Returns True if the string is an identifier
string ="ABC123"
string = string.isidentifier()
print(string)
#output: True
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.


#islower()	Returns True if all characters in the string are lower case
string ="Abc"
string = string.islower()
print(string)
#output: False



#isprintable()	Returns True if all characters in the string are printable
string ="Hello!\nAre you #1?"
string = string.isprintable()
print(string)
#output: True



#isspace()	Returns True if all characters in the string are whitespaces
string ="   T   "
string = string.isspace()
print(string)
#output: False

#istitle()	Returns True if the string follows the rules of a title
string ="Welcome To ERA-INFOTECH"
string = string.istitle()
print(string)
#output: True

#isupper()	Returns True if all characters in the string are upper case
string ="ABC"
string = string.isupper()
print(string)
#output: True


#ljust()	Returns a left justified version of the string
string ="Tarek"
string = string.ljust(20)
print(string, 'is my good friend')
#output: Tarek                is my good friend
#Return a 20 characters long, left justified version of the word "Tarek"

#lower()	Converts a string into lower case
string ="AbCD"
string = string.lower()
print(string)
#output: abcd  


#lstrip()	Returns a left trim version of the string
string ="       XYZW"
string = string.lstrip()
print(string)
#output: XYZW  


#partition()	Returns a tuple where the string is parted into three parts
string ="I love travelling"
string = string.partition("love")
print(string)
#output: ('I', 'love', ' travelling')   


#replace()	Returns a string where a specified value is replaced with a specified value
string ="I am ABC"
string = string.replace("ABC","XYZ")
print(string)
#output: I am XYZ


#rfind()	Searches the string for a specified value and returns the last position of where it was found
string ="Tarek"
string = string.rfind("e")
print(string)
#output: 3 



#rjust()	Returns a right justified version of the string
string ="ABC"
string = string.rjust(20)
print("Hello", string)
#output: Hello                ABC 



#rsplit()	Splits the string at the specified separator, and returns a list
string = "Mango, Orange, Apple"
string = string.rsplit(", ")
print(string)
#output: ['Mango', 'Orange', 'Apple']



#rstrip()	Returns a right trim version of the string
string ="     ABC     "
string = string.rstrip()
print(string)
#output:     ABC



#split()	Splits the string at the specified separator, and returns a list
string = "Mango, Orange, Apple"
string = string.rsplit(", ")
print(string)
#output: ['Mango', 'Orange', 'Apple']



#splitlines()	Splits the string at line breaks and returns a list
string = "hello I am Tarek Mahmud.\n I love to play cricket. "
string = string.splitlines()
print(string)
#output: ['hello I am Tarek Mahmud.', ' I love to play cricket. ']



#startswith()	Returns true if the string starts with the specified value
string ="ABC"
string = string.startswith('A')
print(string)
#output: True 


#strip()	Returns a trimmed version of the string
string ="      ABC       "
string = string.strip()
print(string)
#output: ABC 


#swapcase()	Swaps cases, lower case becomes upper case and vice versa
string ="AbCd"
string = string.swapcase()
print(string)
#output: aBcD


#title()	Converts the first character of each word to upper case
string ="grapes are sour"
string = string.title()
print(string)
#output: Grapes Are Sour
 

#upper()	Converts a string into upper case
string ="AbcD"
string = string.upper()
print(string)
#output: ABCD


#zfill()	Fills the string with a specified number of 0 values at the beginning
string ="AbcD"
string = string.zfill(10)
print(string)
#output: 00000ABCD
