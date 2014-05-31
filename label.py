from Tkinter import *

def buttonPushed(): #function to be called when button is pressed
	print "Button Pushed!"

root=Tk() #this create the root(base) window where all widgets go
w=Label(root, text="Hello World") #creates a label with words
w.pack() #Put the label into the window

myButton=Button(root,text="EXIT!",command=buttonPushed) #creates a button
myButton.pack()
root.mainloop()#start the event loop
