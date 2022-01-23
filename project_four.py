# Description: A voice controlled to-do list
# Date: October 18th, 2021
# By: Developer Phil
# Class: Computer Tech Grade 10
# =======================================
# All libraries have been imported below
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import pyttsx3
import speech_recognition as sr
import datetime
import os
from time import strftime
import webbrowser
from speedtest import *
import png
import pyqrcode
from PIL import Image
import time
# =======================================
r = sr.Recognizer()
engine = pyttsx3.init()
human_voice_rate = 145
engine.setProperty('rate',human_voice_rate)

def main_win():
    win = tk.Tk()
    win.title("To-Do list | Developer Phil")
    win.geometry("459x231")
    win.config(bg="black")
    win.overrideredirect(True)
    win.attributes("-alpha",0.7)

    menubar = Menu(win)
    settings = Menu(menubar, tearoff=0)
    settings.add_command(label="Change Color",command=lambda: change_color(3))

    def change_color(arg):
        if arg == 3:
            def sub_window_one():
                color_win = tk.Tk()
                color_win.title("Change Color")
                color_win.geometry("400x100")
                color_win.config(bg="black")
                win.attributes("-alpha",0.7)

                b_nine = Button(color_win,text="Default")
                b_nine.config(width="60",bg="black",foreground="white",command=lambda:default_color(3))
                b_nine.place(x="0",y="0")

                def default_color(arg):
                    if arg == 3:
                        win.config(bg="black")

                b_ten = Button(color_win,text="Green")
                b_ten.config(width="60",bg="green",foreground="white",command=lambda:green_color(4))
                b_ten.place(x="0",y="25")

                def green_color(arg):
                    if arg == 4:
                        win.config(bg="green")

                b_eleven = Button(color_win,text="Red",command=lambda:red_color(5))
                b_eleven.config(width="60",bg="red",foreground="white")
                b_eleven.place(x="0",y="50")

                def red_color(arg):
                    if arg == 5:
                        win.config(bg="red")

                b_twelve = Button(color_win,text="Pink",command=lambda:pink_color(7))
                b_twelve.config(width="60",bg="pink")
                b_twelve.place(x="0",y="75")

                def pink_color(arg):
                    if arg == 7:
                        win.config(bg="pink")

                color_win.mainloop()

            sub_window_one()
    settings.add_command(label="Dock Window",command=lambda:dock_window(8))

    def dock_window(arg):
        if arg == 8:
            win.overrideredirect(False)
            def dock_win_window_thing():
                dock_win = tk.Tk()
                dock_win.title("Dock Window")
                dock_win.geometry("100x100")
                dock_win.attributes("-alpha",0.7)
                dock_win.config(bg="black")

                b_nine = Button(dock_win, text="Undock Window",command=lambda:undock_win(8))
                b_nine.config(bg="black",foreground="white")
                b_nine.pack()

                def undock_win(arg):
                    if arg == 8:
                        win.overrideredirect(True)
                        dock_win.destroy()

                dock_win.mainloop()
            dock_win_window_thing()
    settings.add_command(label="Text To Speech",command=lambda:tts(30))

    def tts(arg):
        if arg == 30:
            engine.say("This is text to speech, Each Time you add a task I will read it out loud for you to hear, You can disable text to speech by clicking on Disable TTS under the Settings poll-down menu")
            engine.runAndWait()
            settings.add_command("Disable TTS",command=lambda:disable_tts(31))

            def disable_tts(arg):
                if arg == 31:
                    settings.delete("Disable TTS")
    settings.add_separator()
    settings.add_command(label="Exit",command=lambda:exit_application(9))

    def exit_application(arg):
        if arg == 9:
            ask = tkinter.messagebox.askyesno("Notification","Confirm Exit")

            if ask == True:
                engine.say("Exiting Application, Have a great day!")
                quit()

            else:
                pass

    menubar.add_cascade(label="Settings", menu=settings)

    bookmark = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Bookmarks", menu=bookmark)
    bookmark.add_command(label="Youtube")
    bookmark.add_command(label="Twitch")
    bookmark.add_command(label="Netflix")
    bookmark.add_command(label="Spotify")
    bookmark.add_command(label="Gmail")
    bookmark.add_separator()
    bookmark.add_command(label="Add Bookmark",command=lambda:add_bookmark(26))
    bookmark.add_separator()

    def add_bookmark(arg):
        if arg == 26:
            def add_book_win():
                win_add_book = tk.Tk()
                win_add_book.title("Add Bookmark")
                win_add_book.geometry("300x300")
                win_add_book.config(bg="black")
                win_add_book.attributes("-alpha",0.7)
                win_add_book.overrideredirect(False)

                l = Label(win_add_book,text="Name:")
                l.place(x="0",y="0")

                e_one = Entry(win_add_book)
                e_one.place(x="40",y="")

                l_one = Label(win_add_book,text="URL:")
                l_one.place(x="0",y="25")

                e_two = Entry(win_add_book)
                e_two.place(x="25",y="25")

                b_324 = Button(win_add_book,text="Submit",command=lambda:submit(28))
                b_324.pack()

                def submit(arg):
                    if arg == 28:
                        name = str(e_one.get())
                        url = str(e_two.get())
                        bookmark.add_command(label=name,command=lambda:open_stuff(29))

                        def open_stuff(arg):
                            if arg == 29:
                                webbrowser.open(url)

                win_add_book.mainloop()
            add_book_win()

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...",command=lambda:about_window(11))

    def about_window(arg):
        if arg == 11:
            def about_win():
                description_win = tk.Tk()
                description_win.title("About....")
                description_win.geometry("800x231")
                description_win.attributes("-alpha", 0.7)
                description_win.config(bg="black")
                description_win.overrideredirect(False)

                b_ten = Button(description_win,text="About Phil",command=lambda: about_phil_open(15))
                b_ten.place(x="0", y="25", width="150")
                b_ten.config(bg="#28231D", foreground="white", font=('bold'))

                def about_phil_open(arg):
                    if arg == 15:
                        webbrowser.open("C:/Users/pmoot/PycharmProjects/pythonthings/about_phil.html")

                b_eleven = Button(description_win,text="About Eli",command=lambda:about_eli_open(16))
                b_eleven.place(x="0", y="50", width="150")
                b_eleven.config(bg="#28231D", foreground="white", font=('bold'))

                def about_eli_open(arg):
                    if arg == 16:
                        webbrowser.open("C:/Users/pmoot/PycharmProjects/pythonthings/about_eli.html")

                b_twelve = Button(description_win,text="About Team",command=lambda:about_team_open(17))
                b_twelve.place(x="", y="75", width="150")
                b_twelve.config(bg="#28231D", foreground="white", font=('bold'))

                def about_team_open(arg):
                    if arg == 17:
                        webbrowser.open("C:/Users/pmoot/PycharmProjects/pythonthings/about_tea.html")

                b_thirteen = Button(description_win,text="Source Code",command=lambda:source_code_open(18))
                b_thirteen.place(x="", y="100", width="150")
                b_thirteen.config(bg="#28231D", foreground="white", font=('bold'))

                def source_code_open(arg):
                    if arg == 18:
                        webbrowser.open("C:/Users/pmoot/PycharmProjects/pythonthings/source_code_web.html")

                b_fourteen = Button(description_win,text="Open Bookmarks")
                b_fourteen.place(x="", y="125", width="150")
                b_fourteen.config(bg="#28231D", foreground="white", font=('bold'))

                b_fifteen = Button(description_win,text="Open To-Do list", command=lambda:open_to_do_list(14))
                b_fifteen.place(x="", y="150", width="150")
                b_fifteen.config(bg="#28231D", foreground="white", font=('bold'))

                def open_to_do_list(arg):
                    if arg == 14:
                        description_win.destroy()

                b_sixteen = Button(description_win, text="Exit", command=lambda: exit_application_three(14))
                b_sixteen.place(x="", y="175", width="150")
                b_sixteen.config(bg="#28231D", foreground="red", font=('bold'))

                t = Text(description_win)
                t.config(width="78")
                t.place(x="170", y="0")

                abt = """This Application is a todo list. Created By Phil Mootheril. This particular to-do list can have up to 3 lists and 10 tasks. This to-do list has a Text to Speech feature (TTS). You can also add tasks using your voice. You can also create and access bookmarks at any given period in time. This application offers alot of flexibility and personalization. You can pick your background and customize various elements within this UI"""

                t.insert(END,abt)
                def exit_application_three(arg):
                    if arg == 14:
                        ask = tkinter.messagebox.askyesno("Notification", "Confirm Exit")

                        if ask == True:
                            description_win.destroy()

                        else:
                            pass

                description_win.mainloop()
            about_win()
    menubar.add_cascade(label="Help", menu=helpmenu)
    win.config(menu=menubar)
    settings.config(bg="black", foreground="white")
    helpmenu.config(bg="black", foreground="white")
    bookmark.config(bg="black", foreground="white")

    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)

    lbl = Label( font=('calibri', 12, 'bold',),
                bg='#28231D',
                foreground='white', width="18")

    lbl.place(x="0", y="0")
    time()


    b_one = Button(text="Add Task (Keyboard)",command=lambda:add_task_key(32))
    b_one.place(x="0", y="25", width="150")
    b_one.config(bg="#28231D", foreground="white", font=('bold'))

    def add_task_key(arg):
        if arg == 32:
            def task_keyboard():
                tkinter.messagebox.showinfo("Notification","Max 21 Characters per task")
                key_win = tk.Tk()
                key_win.title("Add Task (Keyboard)")
                key_win.geometry("250x50")
                key_win.overrideredirect(False)
                key_win.config(bg="black")
                key_win.attributes("-alpha",0.7)

                key_label = Label(key_win,text="Task:")
                key_label.config(bg="black",fg="white")
                key_label.place(x="0",y="0")

                key__e = Entry(key_win)
                key__e.place(x="40",y="0")

                key_b = Button(key_win,text="Submit",command=lambda:submit_task_key(56))
                key_b.config(bg="black",fg="white")
                key_b.place(x="180",y="0")

                def submit_task_key(arg):
                    if arg == 56:
                        task = str(key__e.get())
                        value = IntVar()
                        task_add = Checkbutton(win,text=task,variable=value)
                        task_add.pack(anchor="n",side="top")

                        if len(task) > 21:
                            tkinter.messagebox.showinfo("Error","Max 21 Characters!")
                            task_add.destroy()


                key_win.mainloop()
            task_keyboard()

    b_two = Button(text="Add Task (Voice)",command=lambda:add_voice_task(62))
    b_two.place(x="0", y="50", width="150")
    b_two.config(bg="#28231D", foreground="white",font=('bold'))

    def add_voice_task(arg):
        if arg == 62:
            with sr.Microphone() as source:
                engine.say("You May Speak! ")
                engine.runAndWait()
                audio = r.listen(source)
                text_3 = r.recognize_google(audio)
                print(text_3)
                insert_task = Checkbutton(win,text=text_3)
                insert_task.pack(anchor="n",side="top")
            if r.recognize_google(audio) == "hello":
                print("hello")
                
    
    b_three = Button(text="Settings",command=lambda:settings_win(58))
    b_three.place(x="", y="75", width="150")
    b_three.config(bg="#28231D", foreground="white", font=('bold'))

    def settings_win(arg):
        if arg == 58:
            def settings_window():
                set_win = tk.Tk()
                set_win.title("Settings")
                set_win.geometry("70x80")
                set_win.config(bg="black")
                set_win.attributes("-alpha",0.7)

                settings_button = Button(set_win, text="Change Color",command=lambda:change_color(3))
                settings_button.config(width="150",bg="black",fg="white")
                settings_button.pack()

                settings_button_2 = Button(set_win,text="Dock Window",command=lambda:dock_window(8))
                settings_button_2.config(width="150",bg="black",fg="white")
                settings_button_2.pack()

                settings_button_3 = Button(set_win,text="Text To Speech",command=lambda:dock_window(30))
                settings_button_3.config(width="150",bg="black",fg="white")
                settings_button_3.pack()

                set_win.mainloop()
            settings_window()

    b_four = Button(text="Open Browser",command=lambda:webbrowser.open("google.com"))
    b_four.place(x="",y="100",width="150")
    b_four.config(bg="#28231D",foreground="white", font=('bold'))

    b_five = Button(text="Open Bookmarks", command=lambda:bookmarks_win(18))
    b_five.place(x="",y="125",width="150")
    b_five.config(bg="#28231D", foreground="white", font=('bold'))

    def bookmarks_win(arg):
        if arg == 18:
            def bookmark_win():
                root = tk.Tk()
                root.title("Bookmarks")
                root.geometry("70x500")
                root.config(bg="black")
                root.attributes("-alpha", 0.7)
                root.overrideredirect(False)

                mark_1 = Button(root, text="Youtube",command=lambda:open_youtube(19))
                mark_1.config(bg="black",foreground="white",width="70")
                mark_1.pack()

                def open_youtube(arg):
                    if arg == 19:
                        engine.say("Opening Youtube")
                        engine.runAndWait()
                        webbrowser.open("youtube.com")

                mark_2 = Button(root, text="Twitch",command=lambda:open_twitch(20))
                mark_2.config(bg="black",foreground="white",width="70")
                mark_2.pack()

                def open_twitch(arg):
                    if arg == 20:
                        engine.say("Opening Twitch")
                        engine.runAndWait()
                        webbrowser.open("twitch.tv")

                mark_3 = Button(root, text="Netflix",command=lambda:open_netflix(21))
                mark_3.config(bg="black",foreground="white",width="70")
                mark_3.pack()

                def open_netflix(arg):
                    if arg == 21:
                        engine.say("Opening Netflix")
                        engine.runAndWait()
                        webbrowser.open("netflix.com")

                mark_4 = Button(root, text="Spotify",command=lambda:open_spotify(22))
                mark_4.config(bg="black",foreground="white",width="70")
                mark_4.pack()

                def open_spotify(arg):
                    if arg == 22:
                        engine.say("Opening Spotify")
                        engine.runAndWait()
                        webbrowser.open("https://open.spotify.com/")

                mark_5 = Button(root, text="Gmail",command=lambda:open_gmail(23))
                mark_5.config(bg="black",foreground="white",width="70")
                mark_5.pack()

                def open_gmail(arg):
                    if arg == 23:
                        engine.say("Opening Gmail")
                        engine.runAndWait()
                        webbrowser.open("gmail.com")

                mark_6 = Button(root, text="Google Drive",command=lambda:open_google_drive(24))
                mark_6.config(bg="black", foreground="white", width="70")
                mark_6.pack()

                def open_google_drive(arg):
                    if arg == 24:
                        engine.say("Opening your Google Drive")
                        engine.runAndWait()
                        webbrowser.open("https://drive.google.com/")

                mark_7 = Button(root, text="Google",command=lambda:open_google(25))
                mark_7.config(bg="black", foreground="white", width="70")
                mark_7.pack()

                def open_google(arg):
                    if arg == 25:
                        engine.say("Opening Google")
                        engine.runAndWait()
                        webbrowser.open("google.com")

                root.mainloop()
            bookmark_win()

    b_six = Button(text="Open Other Projects",command=lambda:open_other(34))
    b_six.place(x="", y="150", width="150")
    b_six.config(bg="#28231D", foreground="white", font='bold')

    def open_other(arg):
        if arg == 34:
            def open_other_win():
                win_2 = tk.Tk()
                win_2.title("Open Other Projects")
                win_2.geometry("200x500")
                win_2.attributes("-alpha",0.7)
                win_2.config(bg="black")

                proj_1 = Button(win_2,text="TTHW Project",command=lambda:text_to_handwriting(34))
                proj_1.config(width="40")
                proj_1.pack()

                proj_2 = Button(win_2,text="News Project",command=lambda:news_project(49))
                proj_2.config(width="40")
                proj_2.pack()

                proj_3 = Button(win_2,text="Internet Speed Test project",command=lambda:wifi_speed_tester_app_proj(46))
                proj_3.config(width="40")
                proj_3.pack()

                proj_5 = Button(win_2,text="QR code make project",command=lambda:qr_code_make_proj(50))
                proj_5.config(width="40")
                proj_5.pack()

                proj_6 = Button(win_2,text="Bar Code Maker project",command=lambda:barcode_maker_proj(55))
                proj_6.config(width="40")
                proj_6.pack()

                def barcode_maker_proj(arg):
                    if arg == 55:
                        # All Modules are imported below
                        # ================================================
                        import barcode.pybarcode
                        from barcode import EAN13
                        from barcode.writer import ImageWriter
                        # ================================================

                        # Creaeting a function to store the application in
                        def barcode_win_main():
                            # Creating a window
                            bar_win = tk.Tk()
                            # Adding a title to the window
                            bar_win.title("Barcode Creator")
                            # Configuring the dimmensions for the application
                            bar_win.geometry("320x70")
                            # Configuring the background for the application
                            bar_win.config(bg="black")
                            # Configuring transparency for the application
                            bar_win.attributes("-alpha", 0.7)
                            # Removing top buttons to make the applicaiton more preofessional
                            bar_win.overrideredirect(False)

                            # Creating a label to inform the user
                            bar_l = Label(bar_win, text="Numbers (12 Max): ")
                            # Configuring background and foreground of the label
                            bar_l.config(bg="black", fg="white")
                            # Plaing the label in a specific spot in the application
                            bar_l.place(x="0", y="0")

                            # Creating an entry for the application
                            bar_e = Entry(bar_win)
                            # Configuring background and foreground for the entry
                            bar_e.config(bg="white", fg="black")
                            # Placing the entry in a specific spot in the application
                            bar_e.place(x="110", y="0")

                            # Creating a label to guide the user
                            bar_l_2 = Label(bar_win, text="Name of File: ")
                            # Configuring the backround and foreground of the application
                            bar_l_2.config(bg="black", fg="white")
                            # Placing the label in a specific spot in the application
                            bar_l_2.place(x="0", y="25")

                            # Creating an Entry for the application
                            bar_e_2 = Entry(bar_win)
                            # Configuring backgorund and foreground of the application
                            bar_e_2.config(bg="white", fg="black")
                            # Placing the entry in a specific spot within the application
                            bar_e_2.place(x="110", y="25")

                            # Creating a button for the user to press and submit what htey have typed within the entry's abov.
                            bar_b = Button(bar_win, text="Submit", command=lambda: barcode_submit(53))
                            # Configuring the background, foreground and thickness of the button
                            bar_b.config(bg="black", fg="white", padx="12", pady="12")
                            # Placing the button in a specific spot within the application.
                            bar_b.place(x="235", y="0")

                            # Creating a subroutine for the when the user presses the submit button
                            def barcode_submit(arg):
                                if arg == 53:
                                    # Getting the numbers the user typed from above
                                    x_barcode_var = str(bar_e.get())
                                    # Getting the name of the file that the user typed from above.
                                    y_barcode_var = str(bar_e_2.get())
                                    # Print the number to terminal
                                    print(x_barcode_var)
                                    # If the number is above 12 show a message
                                    if len(x_barcode_var) > 12:
                                        tkinter.messagebox.showinfo("Error", "You must have 12 numbers!")
                                    # If the number is below 12 show a message
                                    if len(x_barcode_var) < 12:
                                        tkinter.messagebox.showinfo("Error", "You must have 12 numbers!")
                                    # if its perfect, pass
                                    else:
                                        pass
                                    # Getting the entry in string format
                                    x_barcode_var_2 = str(bar_e.get())
                                    # Creating the barcode
                                    bar = EAN13(x_barcode_var_2, writer=ImageWriter())
                                    # Saving the barcode as a png file
                                    bar.save(f"C:/Users/pmoot/Pictures/PythonProjectPur/{y_barcode_var}")
                                    # Show a message about the image being created
                                    tkinter.messagebox.showinfo("Notification", "Image has been created!")

                            # Loop the window so that the user can view the application.
                            bar_win.mainloop()

                    # Call the function that was created above that has the application stored within.
                    barcode_win_main()
                def qr_code_make_proj(arg):
                    if arg == 50:
                        # Declaring a function to store the GUI application
                        def qr_code_win():
                            # Creating a window for the application ot run
                            qr_code_win = tk.Tk()
                            # Configuring Window Dimmensions
                            qr_code_win.geometry("270x70")
                            # Adding title to windows
                            qr_code_win.title("QR Code Generator")
                            # Adding a background for all the windows
                            qr_code_win.config(bg="black")
                            # Making the application semi-transparent
                            qr_code_win.attributes("-alpha", 0.7)
                            # Removing top parts to the window
                            qr_code_win.overrideredirect(False)

                            # Creating a label to guide the user
                            qr_l = Label(qr_code_win,text="Text/URL: ")
                            # Configuring background and foreground (color of text) for the label
                            qr_l.config(bg="black", fg="white")
                            # Placing the label in specific co-ordinates
                            qr_l.place(x="0", y="0")

                            # Creating an Entry box for the user to type the text or url
                            qr_e = Entry(qr_code_win)
                            # Configuring background for the Entry box
                            qr_e.config(bg="white")
                            # Placing the entry box in a specific spot
                            qr_e.place(x="61", y="0")

                            # Creating a label to guide the user
                            qr_l_2 = Label(qr_code_win,text="File Name: ")
                            # Configuring background and foreground (color of text) for the label
                            qr_l_2.config(bg="black", fg="white")
                            # Placing the label in a specific spot
                            qr_l_2.place(x="0", y="25")

                            # Creating an entry for the user to type the name of the file
                            qr_e_2 = Entry(qr_code_win)
                            # Configuring background for the entry
                            qr_e_2.config(bg="white")
                            # Placing the label in a specific spot
                            qr_e_2.place(x="61", y="25")

                            # Creating a button for the user to submit all the information that htye have entered into the entry box
                            qr_b = Button(qr_code_win,text="Submit", command=lambda: qr_submit_button(1))
                            # Configuring background and foreground (text of color) for button and adding thickness to the button
                            qr_b.config(bg="black", fg="white", padx="12", pady="12")
                            # Placing the button in a specific spot
                            qr_b.place(x="193", y="0")

                            # Creating a subroutine for the button
                            def qr_submit_button(arg):
                                if arg == 1:
                                    # Getting url/text entry from user
                                    x_qr_var = str(qr_e.get())
                                    # Creating a QR code for the text
                                    url = pyqrcode.create(x_qr_var)
                                    # Getting name of the file from user
                                    y_qr_var = str(qr_e_2.get())
                                    # Naming the file that the qr code is stored in
                                    url.png(f"C:/Users/pmoot/Pictures/PythonProjectPur/{y_qr_var}.png")
                                    # Opening the file the qr code is stored in
                                    show_qr_code = Image.open(
                                        f"C:/Users/pmoot/Pictures/PythonProjectPur/{y_qr_var}.png")
                                    # Opening the file the qr code is stored in
                                    show_qr_code.show()

                            # Looping the window from above so that user can see it
                            qr_code_win.mainloop()

                        # Calling the subroutine, declared above for the user to view the application
                    qr_code_win()

                def news_project(arg):
                    if arg == 49:
                        from GoogleNews import GoogleNews

                        # Declaring a subroutine for the main window
                        def google_news_win():
                            google_news_win = tk.Tk()
                            google_news_win.title("Latest News | Developer Phil")
                            google_news_win.geometry("800x700")
                            google_news_win.config(bg="black")
                            google_news_win.attributes("-alpha", 0.6)
                            google_news_win.overrideredirect(False)
                            google_news_win.state("zoomed")

                            display_google_news = Text(google_news_win)
                            display_google_news.config(bg="black", height=30, width=170, foreground="white")
                            display_google_news.place(x="0", y="0")

                            news = GoogleNews()

                            news = GoogleNews(period='7d')

                            news.search('Canada')

                            x_google_news_win = news.results()

                            for i in x_google_news_win:
                                display_google_news.insert(END, "-" * 160, "\n")
                                display_google_news.insert(END, "Title:" and i['title'])
                                display_google_news.insert(END, "Date/Time:" and i['date'])
                                display_google_news.insert(END, "Description:" and i["desc"])
                                display_google_news.insert(END, "Link:" and i['link'])
                            google_news_win.mainloop()

                        google_news_win()

                def wifi_speed_tester_app_proj(arg):
                    if arg == 46:
                        # ==========================================
                        # All libraries are to be imported below:
                        import tkinter.messagebox
                        # ==========================================

                        # Initializing the speed tester
                        st = Speedtest()

                        # Declaring a subroutine

                        def wstap():
                            # Declaring the window
                            wstap_win = tk.Tk()
                            # Title of the window
                            wstap_win.title("Internet Speed Test | Developer Phil")
                            # Configuring the dimensions of the window
                            wstap_win.geometry("420x389")
                            # Configuring background for window
                            wstap_win.config(bg="black")
                            # configuring transparency for window
                            wstap_win.attributes("-alpha", 0.6)
                            # Disabling the top menu
                            wstap_win.overrideredirect(True)

                            # Creating a display to display text
                            e_wstap_1 = Text(wstap_win)
                            # Configuring background and text color for display
                            e_wstap_1.config(bg="black", foreground="white")
                            # Placing the display in a specific spot in the window (x=193,y=0)
                            e_wstap_1.place(x="193", y="0")

                            # Creating a button for the user to check upload speed
                            b_one_wstap_1 = Button(wstap_win, text="Check Upload Speed",
                                                   command=lambda: check_upload(1), width="26")
                            # Configuring background and text color for the button
                            b_one_wstap_1.config(bg="black", foreground="white")
                            # Placing the button in a specific spot in the window (x=0,y=0)
                            b_one_wstap_1.place(x="0", y="0")

                            # Creating a second button for the user to check download speed
                            b_two_wstap_1 = Button(wstap_win, text="Check Download Speed",
                                                   command=lambda: check_download(2), width="26")
                            # Configuring background and text color for Button two
                            b_two_wstap_1.config(bg="black", foreground="white")
                            # Placing the button in a specific spot in the window (x=0,y=25)
                            b_two_wstap_1.place(x="0", y="25")

                            # creating a third button for the user to clear the display
                            b_three_wstap_3 = Button(wstap_win, text="Clear", command=lambda: clear(3), width="26")
                            # Configuring background and text color for
                            b_three_wstap_3.config(bg="black", foreground="white")
                            # Placing the button in a specific spot in the window
                            b_three_wstap_3.place(x="0", y="50")

                            # Creating a fourth button for the user to dock the display and then undock
                            b_four_wstap_4 = Button(wstap_win, text="Dock Window", command=lambda: dock_win(4),
                                                    width="26")
                            # Configuring background and text color for fourth button
                            b_four_wstap_4.config(bg="black", foreground="white")
                            # Placing the button in a specific spot in the window (x=0,y=75)
                            b_four_wstap_4.place(x="0", y="75")

                            # Creating a fifth button for the user to exit the application
                            b_five_wstap_5 = Button(wstap_win, text="Exit", command=lambda: exit(5), width="26")
                            # Configuring background and text color for fifth button
                            b_five_wstap_5.config(bg="black", foreground="white")
                            # Placing the button in a specific spot in the window (x=0,y=100)
                            b_five_wstap_5.place(x="0", y="100")

                            # ===================================================================================
                            # Creating multiple subroutine that would be functions for the buttons created above
                            # Declaring subroutine to display upload speed into display
                            def check_upload(arg):
                                if arg == 1:
                                    # Getting upload speed
                                    get_speed = st.upload()
                                    # Informing user to wait some time
                                    e_wstap_1.insert(END, "Please Wait A Moment\n")
                                    # Display upload speed to display
                                    e_wstap_1.insert(END, f"Upload Speed: \n{get_speed}\n")

                            # Declaring a subroutine to display download speed

                            def check_download(arg):
                                if arg == 2:
                                    # Getting download speed
                                    get_download = st.download()
                                    # Informing the user to wait some time
                                    e_wstap_1.insert(END, "Please Wait A Moment\n")
                                    # Display download speed to display
                                    e_wstap_1.insert(END, f"Download Speed:\n{get_download}\n")

                            # Declaring a subroutine to clear the text in the display

                            def clear(arg):
                                if arg == 3:
                                    # Clearing text
                                    e_wstap_1.delete("1.0", "end")

                            # Declaring a subroutine to dock window

                            def dock_win(arg):
                                if arg == 4:
                                    # Enabling top menu
                                    wstap_win.overrideredirect(False)

                                    # Declaring a subroutine to display a mini window

                                    def dock_window():
                                        # Initializing the window
                                        dock = tk.Tk()
                                        # Configuring window geometry
                                        dock.geometry("100x100")
                                        # Adding a title to the window
                                        dock.title("dock window")

                                        # Creating a sixth button to undock window when the user needs to
                                        b_six = Button(dock, text="Undock Window", command=lambda: undock_win(6))
                                        # Placing the button in a certain spot in the window
                                        b_six.pack()

                                        # Declaring a subroutine to undock window when the user needs to

                                        def undock_win(arg):
                                            if arg == 6:
                                                # Disabling top menu
                                                wstap_win.overrideredirect(True)
                                                # Destroying dock window
                                                dock.destroy()

                                        # looping the window so its visible to the user
                                        dock.mainloop()

                                    # Calling dock subroutine to display itself
                                    dock_window()

                            # Declaring a subroutine for the user to exit the application at any given point in time

                            def exit(arg):
                                if arg == 5:
                                    # Asking the user if they want to confirm exit
                                    ask_wstap_exit = tkinter.messagebox.askyesno("Notification", "Confirm Exit?")
                                    # else, pass and do not quit the application
                                    if ask_wstap_exit == True:
                                        wstap_win.destroy()
                                    # If your confirms exit, quit(code)
                                    else:
                                        pass

                            # Looping the window so its visible to the user
                            wstap_win.mainloop()

                        # Calling the main window to display itself
                        wstap()
                def text_to_handwriting(arg):
                    if arg == 34:
                        # =====================================
                        # All the modules needed are imported.
                        import pywhatkit as pp
                        import tkinter.messagebox
                        from PIL import Image
                        # =====================================

                        # ==============================================================
                        # A subroutine has been created to run the window

                        def text_to_handwriting():
                            # Declare the window
                            wifi_speed_testing_window = tk.Tk()
                            # Give the window a title
                            wifi_speed_testing_window.title("Text To Handwriting")
                            # Geomtry for the window (widthxheight)
                            wifi_speed_testing_window.geometry("400x200")
                            # Making the window semi-trasnparent
                            wifi_speed_testing_window.attributes("-alpha", 0.6)
                            # Removing the top buttons off the window
                            wifi_speed_testing_window.overrideredirect(False)
                            # Adding a background for the window
                            wifi_speed_testing_window.config(bg="black")

                            # Declaring a label
                            l_one_speed_testing = Label(wifi_speed_testing_window, text="Text:")
                            # Placing the label in a specific spot (x = 0,y= 0)
                            l_one_speed_testing.place(x=0, y=0)

                            # Declaring an entry for the user to type input
                            e_one_speed_testing = Entry(wifi_speed_testing_window)
                            # Placing the input in a specific spot (x=33,y=0)
                            e_one_speed_testing.place(x=33, y=0)

                            # Declaring a second label
                            l_two_speed_testing = Label(wifi_speed_testing_window,text="Name:")
                            # Placing the label in a specifc spot (x=166,y=0)
                            l_two_speed_testing.place(x=166, y=0)

                            # Declaring a second entry
                            e_two_speed_testing = Entry(wifi_speed_testing_window)
                            # Placing the entry in a specifc spot (x=210,y=0)
                            e_two_speed_testing.place(x=210, y=0)

                            # Declaring a button and assigning a subroutine to the button
                            b_one_speed_testing = Button(wifi_speed_testing_window,text="Submit", command=lambda: create_writing(1))
                            # Placing the button in a specifc spot (x=0,y=25)
                            b_one_speed_testing.place(x=0, y=25)

                            # Declaring a button and assining a subroutine to the button
                            b_three_speed_testing = Button(wifi_speed_testing_window,text="Exit", command=lambda: exit(2))
                            # Placing the button in a specific spot (x=0,y=50)
                            b_three_speed_testing.place(x=0, y=50)

                            # ==============================================================
                            # Declaring a subroutine for exiting the application
                            def exit(arg):
                                if arg == 2:
                                    # Asks the user if they want to exit
                                    ask_speed_testing = tkinter.messagebox.askyesno("Notification",
                                                                                    "Are you sure you want to exit? ")
                                    if ask_speed_testing == True:
                                        quit()
                                    else:
                                        pass

                            # Declaring a subroutine to convert the text to handwritng
                            def create_writing(arg):
                                if arg == 1:
                                    # Getting input from entry 1
                                    x_speed_testing = str(e_one_speed_testing.get())
                                    # Getting input from entry 2
                                    y_speed_testing = str(e_two_speed_testing.get())
                                    # Converting the the text to handwriting
                                    pp.text_to_handwriting(f"{str(x_speed_testing)}",
                                                           f"C:/Users/pmoot/Pictures/PythonProjectPur/{str(y_speed_testing)}.png")
                                    # Notifiying the user that the image for the handwriting has been created
                                    tkinter.messagebox.showinfo("Notification", "Image has been created")
                                    # Opening the image containing the handwriting
                                    img_speed_testing = Image.open(
                                        f"C:/Users/pmoot/Pictures/PythonProjectPur/{str(y_speed_testing)}.png")
                                    # Showing and opening the image
                                    img_speed_testing.show()

                            # ==============================================================
                            # Looping the window so the user can use it for a prolonged period of time
                            wifi_speed_testing_window.mainloop()

                        # Declaring the subroutine to execute the code within the subroutine
                        text_to_handwriting()

                win_2.mainloop()
            open_other_win()

    b_seven = Button(text="Exit", command=lambda:exit_application_two(10))
    b_seven.place(x="", y="175", width="150")
    b_seven.config(bg="#28231D", foreground="red", font='bold')

    def exit_application_two(arg):
        if arg == 10:
            ask = tkinter.messagebox.askyesno("Notification", "Confirm Exit")

            if ask == True:
                engine.say("Exiting Application, Have a great day!")
                quit()

            else:
                pass

    b_eight = Button(text="Shutdown (PC)", command=lambda:shutdown_pc(2))
    b_eight.place(x="", y="200", width="150")
    b_eight.config(bg="#28231D", foreground="red", font=('bold'))

    def shutdown_pc(arg):
        if arg == 2:
            os.system("shutdown /s /t 1")

    win.mainloop()

def requirements_all():
    req_win = tk.Tk()
    req_win.title("Requirements Download")
    req_win.geometry("150x33")
    req_win.config(bg="black")
    req_win.attributes("-alpha",0.7)
    req_win.overrideredirect(True)

    req_b = Button(req_win,text="Download Reqruiements",command=lambda:download_req(56))
    req_b.config(bg="yellow",fg="black")
    req_b.pack()

    def download_req(arg):
        if arg == 56:
            os.system("pip install tk")
            os.system("pip install pyttsx3")
            os.system("pip install SpeechRecognition")
            os.system("pip install Pillow")
            os.system("pip install pypng")
            os.system("pip install pyqrcode")
            os.system("pip install pywhatkit")
            os.system("pip install SpeedTest")
            os.system("pip install python-barcode")
            os.system("pip install pipwin")
            os.system("pipwin install pyaudio")
            print("finished")
            tkinter.messagebox.showinfo("Notification","Successfully Downloaded All Reqruiements")
            req_win.destroy()
            main_win()


    req_win.mainloop()
requirements_all()