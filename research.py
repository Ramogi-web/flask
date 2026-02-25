import os

#is the standard way to access operating system-dependent functionality in Python
#Think of the
#os module as a remote control for your computer. Just like you use your mouse and keyboard to click on folders or delete files. In Python, import os lets you do those same things by writing a few lines of code


#. The "Universal" Trick (os.path.join)
#Windows uses backslashes (\) for file paths, while Macs and Linux use forward slashes (/). 

   #If you use os.path.join("Homework", "Python", "task1.py"), your code will work on any computer without you having to worry about which slash to use

# When you write a file path like
#  "Homework/Python/task1.py", it might work on your Mac, but it will likely crash on  Windows computer because Windows expects backslashes (\). 
# os.path.join() solves this by acting as a smart translator. 


#When you run os.path.join("Homework", "Python", "task1.py"), Python checks your computer's operating system first: 

   #1. On Windows: It automatically produces "Homework\\Python\\task1.py".
   #2. On Mac/Linux: It automatically produces "Homework/Python/task1.py".     
        
 # os: The module (a file containing code).
#.path: A sub-module inside os specifically for handling file names and locations.
#.join():  The function (the action) that takes your strings and glues them together with the correct slashes.      
