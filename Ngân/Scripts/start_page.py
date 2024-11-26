
# GUI first page
# Driver and emergency contact details before starting driving


# import packages
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

# import scripts
import drowsiness_classification

class InfoPage:

    def __init__(self, root):
        """This function initializes the info-page"""

        # root
        self.root = root
        self.root.title("SLEEP ALERT APP")
        self.root.geometry("800x420+100+50")

        # background image
        background_image = Image.open("../Data/background.png")
        background_image = background_image.resize((800, 420), Image.Resampling.LANCZOS)
        background = ImageTk.PhotoImage(background_image)
        Label(self.root, image=background).place(x=300, y=0)

        title_label = Label(self.root, text="SLEEP ALERT APP", font=("times new roman", 24, 'bold'), bg="white",fg="blue")
        title_label.place(x=100, y=100)

        # start button
        Button(self.root, command=self.start_function, text="Start Driving", bg="#ABCAD5", font=("times new roman", 12)).place(x=150, y=350, width=100, height=30)

        # infinite loop waiting for an event to occur and process the event as long as the window is not closed
        root.mainloop()

    def start_function(self):
        messagebox.showinfo("Start Driving", f"Have a pleasant journey!")
        self.root.destroy()
        drowsiness_classification.start_driving()

def main():
    InfoPage(Tk())


if __name__ == '__main__':
    main()
