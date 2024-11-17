#===========================================================================================================================================================================
#                                                               Absolute beginner concept
#===========================================================================================================================================================================
print('Happy Hacking!!') #This will print the string directly
a = 'Hack'
b = 'the Box'
print(a,b) #this will concatinate the two string and print it
advice = "don't panic" #string type data
answer = 42 #integer type data variable
length = 3.2 #floating type data variable
check = True #boolean type data variable
debug = None #this is null in most other language. Its very useful in error handling and in some case check modifications
print(5+5) #this will perform addition and print it
print(5-5) #this will perform substraction and print it
print(5*5) #this will perform multipication and print it
print(5/5) # this will perform division and print it
print(f'the length of the desk is: {length}') #this is called the f-string which allow us to embeded the variable along with the string
#list in python
shop = [
    'potato', #index 0
    'egg', #index 1
    'Rice', #index 2
    'Oil' #index 3
]
print(a[:2]) #print Ha . means it will print upto 2 index.
print(a[2:]) #print ck means afterward 2 index along with 2 index.

#first test
list_value = ['Accidental', '4daa7fe9', 'eM131Me','Y!.90']
secrect = []
for x in list_value:
    secrect.append(x[:2])
print(''.join(secrect)) #guess and find the output without run the programme

#============================================================ tutorial ends here ===========================================================================================

#we can also use Python IDLE in terminal for better interuption. Just type python3 int he terminal then you are good to go.
#to exit the python3 IDLE you need to type exit(0). 0 indicates that the program will end without error. Rather than 0, it will indicate error.
# NOTE this will only work if you are using bash type terminal. It won't work in the Command Prompt. And use py in powershell for python IDLE

#another method for python to execute without being type python3 at the very first. We can just specify the file that we are encoutering and the Linux operating system
#will interact with it as the define file system. Its called SheBang in Linux operating system which specify the way how it can be treated. SheBang for python is: #!/bin/bash/env python3
#then each time the file will run, the operating system will call the bash terminal and execute it as a python3 script. So now rather than specify the compiler, now we are able
#to run it as a program file. give the executable permission and run directly. for example if you have start.py script then just type ./start.py and your script will run totally
#fine. But make sure you specify the shebang and give the file proper executable permission.

# we can use placeholder to hold the previous value and work with it. NOTE it will only work for IDLE, not in the actual script.
#in script the placeholder is used to specify a ignor input or ignore conditions. the placeholder in python is _ (dash) . Suppose we have a function that needs both x and y
#co-ordinated. but we dont want to pass the y co-ordinate as its not very important to use or just we want t0 skip. So in python we can do it simple by ignor the y co-ordinate
#just by putting placeholder


#we need pwn module for this section. So download it using pip packet manager. just type pip3 install pwn in the terminal and you are good to go

# colon(:) sighn is used to indicate upto. it is used in index to indicate upto value or range
