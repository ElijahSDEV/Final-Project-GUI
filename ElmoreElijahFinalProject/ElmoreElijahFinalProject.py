import tkinter as tk
from tkinter import messagebox

bookGenre = ['Fantasy','Science Fiction','Non-Fiction']

mainWindow = tk.Tk()
mainWindow.title("Book Lookup")
mainWindow.geometry("300x300")

#Search Box entered here so that functions can be together at top of window
searchBox = tk.Entry()

#Main frame for window
searchFrame = tk.Frame(mainWindow)

##Functions

#Returns the value of the searchbox
def getSearchText():
    return searchBox.get()

#checks to see if the searchbox has whitespace AND if it is in the list of genres
def validateInput(input):
    if input.strip() in bookGenre:
        resultFound(input.strip())
    else:
        invalidInput()

#calls getsearchtext and returns the value into the validateinput function
def clickSearch():
    input = getSearchText()
    validateInput(input)

#Notifies user that the input was invalid or that there were no search results
def invalidInput():
    messagebox.showwarning("Invalid Input", "Invalid Input or No results")

#clears the searchbox
def clearInput():
    searchBox.delete(0, tk.END)

#closes the window
def exitWindow():
    mainWindow.destroy()

#checks the valid search result depending on the genre chosen and opens the new window with the desired genre and book
def resultFound(result):
    if result == bookGenre[0]:
        resultWindow(result, "The Lord of the Rings")
    elif result == bookGenre[1]:
        resultWindow(result, "Dune")
    elif result == bookGenre[2]:
        resultWindow(result, "Ghost Soldiers")

#displays the found book in a new window based on the genre the user searched
def resultWindow(result, bookName):
    #variables declarations
    imagePath = f"C:\\Users\\elija\\OneDrive\\Desktop\\ElmoreElijahFinalProject\\{bookName}.gif"  #

    #window setup
    popupWindow = tk.Toplevel()
    popupWindow.title('Search Result')
    popupWindow.geometry("300x450") 

    #widgets on popup window
    foundLabel = tk.Label(popupWindow, text=f'Found the following {result} book:')
    foundBookLabel = tk.Label(popupWindow, text=bookName, font=(20))
    foundImage = tk.PhotoImage(file=imagePath)
    imageLabel = tk.Label(popupWindow, image=foundImage)
    imageLabel.image = foundImage
    closeButton = tk.Button(popupWindow,text="Close",command=popupWindow.destroy)
    
    #packing widgets
    foundLabel.pack(side="top")
    foundBookLabel.pack()
    imageLabel.pack()
    closeButton.pack()

    #main loop of window to keep it open
    popupWindow.mainloop()

#Buttons on main window
searchButton = tk.Button(searchFrame,text="Search",command=clickSearch)
clearButton = tk.Button(searchFrame,text="Clear", command=clearInput)
exitButton = tk.Button(searchFrame,text="Exit", command=exitWindow)

#Label on main window
lookupLabel = tk.Label(searchFrame,text="Book Lookup\n Search by Genre:")

#packing for main window
searchFrame.pack()
searchBox.pack(side="top", padx=5)
lookupLabel.pack(side="top", padx=5)
searchButton.pack(side="left", padx=5)
clearButton.pack(side="left", padx=5)
exitButton.pack(side="left", padx=5)

#main window loop
mainWindow.mainloop()