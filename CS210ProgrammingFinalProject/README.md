Summarize the project and what problem it was solving.

The purpose of this program was to provide a method for a grocery store to track the inventory of items that were purchased on a given day based on a list of raw data that generated the name of the item at the time it was purchased. The problem it was solving is that the items were sorted by time of purchase with no timestamp, so there was no easy way to reference the data, it was disorganized. The program sorts the items and provides an easy to read the count in both numerical and graphical representations. It also allows the user to search for a count by item.

What did you do particularly well?

I am particularly proud of my menu display. I finally got the hang of switch/ case conditional statements, so I was able to generate the menu options quickly and more organized than past iterations. I was also very please that I was able to put this program together with only one call and a return in main. I think that is one of the benefits of programming in two different languages, it forces you to use more encapsulated code.

Where could you enhance your code? How would these improvements make your code more efficient, secure, and so on?

I considered making an input formatting function for my python code since all three of the other functions used .strip() and .lower() for input validation. I also considered how I would check the list of purchased items against a store inventory to track whether the store carries the item at all, that way I could implement a separate error message if a user searched for something the store doesn't carry. That functionaliy would also be useful if I appended daily purchases to a purchase history file that could be compared to the inventory file, and provided a message when the inventory of an item is nearly depleted.

Which pieces of the code did you find most challenging to write, and how did you overcome this? What tools or resources are you adding to your support network?

I actually had the most issues with the provided template code. Also I was getting a memory leak every time the exe crashed, but that went away when I resolved all the other bugs.

What skills from this project will be particularly transferable to other projects or course work?

This project really refined my ability to debug runtime errors and to figure out how to resolve issues with pointers and memory allocation that have error messages that are not human readable.

How did you make this program maintainable, readable, and adaptable?

I spent more time thinking about how to break this program down into its component parts that I have in previous projects. I also wrote more descriptive multiline overview comments for each method. In the past, I tended to just use inline comments and not describe the overall functionality. That should help future programmers add functionality without breaking what is already there.

# Cplusplus-Program

CS210_Project3_CornerGrocerApp

Consider the coding work you have completed for the grocery-tracking program. You will now take the time to think more deeply regarding how you were able to combine two different programming languages, C++ and Python, to create a complete program. The following should be completed as a written explanation. 

Explain the benefits and drawbacks of using C++ in a coding project. Think about the user-focused portion of the grocery-tracking program you completed using C++.  What control does this give you over the user interface?  How does it allow you to use colors or formatting effectively? 

C++ performs calculations very quickly due to its low memory requirements but requires 	a programmer to include pointers to handle memory allocation in order to prevent 			memory leaks because it doesn’t do its own garbage collection. It is a strictly typed 	object-oriented language that uses very little memory, but it requires many lines of code 	to create high level programs. 

Colors and formatting are bit-encoded in C++, which enables you to easily change the color, font, or size of the text in the console using many different libraries, or by using the system function. 

Explain the benefits and drawbacks of using Python in a coding project. Think about the analysis portions of the grocery-tracking program you completed using Python. How does Python allow you to deal with regular expressions? How is Python able to work through large amounts of data? What makes it efficient for this process? 

Python is an ideal programming language for processing data. It is a high-level, dynamically typed, object-oriented language that is easy to learn, read, and write. It is highly efficient at processing data, handles its own memory, and does its own garbage collection because it runs on an interpreter rather than compiling. The major drawback to all of the above advantages is that this makes Python a memory-intensive language, so it is slower and takes more memory than other languages. 

Discuss when two or more coding languages can effectively be combined in a project. Think about how C++ and Python’s different functions were able to support one another in the overall grocery-tracking program. How do the two function well together? What is another scenario where you may wish to use both? Then, consider what would happen if you added in a third language or switched Python or C++ for something else. In past courses, you have worked with Java as a possible example. What could another language add that would be unique or interesting? Could it help you do something more effectively or efficiently in the grocery-tracking program? 

C++ worked very well to build the framework of the program and handle the UI and object-oritented functions quickly and efficiently while Python handled the data processing, utilizing the strengths of each. As for a third language, I can imagine a scenario where it would be more efficient to organize large amounts of table data with many different data points using SQL allowing Python to parse it faster without bogging down as much. 
