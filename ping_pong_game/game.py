# Resolution of screen is  1280 x 720
# Importing tkinter,time and os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep, time
import os
home_dir = os.path.expanduser('~')
# Making the path for the images to be used in the gameplay
desktop_dir = os.path.join(home_dir, 'Desktop')


window = Tk()

window.title("Game")
score = 0
value_some = 0
player = 0
game_frame = Frame(window)  # Creating a frame within the window
game_frame.pack()
my_game = ttk.Treeview(game_frame)
window.resizable(False, False)  # Makes the window not resizable
file = open('leaderboard.txt', 'r')
leaderboard = [line.replace('\n', '') for line in file.readlines()]
points = 0
my_game['columns'] = ('player_rank', 'player_name',
                      'player_city', 'player_age')


# Makes the window of 1280 x 720 resolution
window.minsize(width=1280, height=720)


def welcome():  # Main Menu

    def login():
        label1.destroy()
        buttona.destroy()
        buttonb.destroy()
        buttonc.destroy()
        buttond.destroy()
        # Initialize the Login Page
        label2 = Label(window,  text="LOGIN", font=(
            "Comic Sans MS", '38'), fg="white", bg="#079af0")
        label2.place(relx=.5, rely=.1, anchor=CENTER)
        label3 = Label(
            window, text="Enter Initials:", font=(
                "Comic Sans MS", '38'), fg="white", bg="#079af0")
        label3.place(relx=.5, rely=.2, anchor=CENTER)
        text = Text(bg="white", height=3, width=75, fg="black")
        text.place(relx=.5, rely=.4, anchor=CENTER)

        def choice():
            label2.destroy()
            label3.destroy()

            button2.destroy()
            # Initiale the Preferences Page
            initials = text.get("1.0", 'end-1c')
            text.destroy()
            label4 = Label(
                window, text="Choose Your Preferences below,  "+initials, font=(
                    "Comic Sans MS", '38'), fg="white", bg="#079af0")
            label4.place(relx=.5, rely=.2, anchor=CENTER)

            def keys():
                # Function for when player chooses to play up and down keys
                canvas = Canvas(window, width=1280, height=720)
                checker = -1
                img_intro = ImageTk.PhotoImage(
                    Image.open("sky copy.png").resize((1280, 720)))
                canvas.create_image(10, 10, anchor=NW,
                                    image=img_intro, tags="image_intro")
                coordinates_of_ball = [200, 10, 230, 40]
                oval = canvas.create_oval(
                    coordinates_of_ball, fill="orange")  # Creates the ball
                upspeed = 8
                sidespeed = 8
                bar1_coors = [10, 10, 30, 100]
                bar1 = canvas.create_rectangle(
                    bar1_coors, fill="orange")  # Creates the left bar
                bar2_coors = [1250, 10, 1270, 110]
                # Creates the player controlled bar
                bar2 = canvas.create_rectangle(bar2_coors, fill="orange")
                speed_of_bar1 = 25
                speed_of_bar2 = 25
                back_label.destroy()
                label4.destroy()
                button3.destroy()
                button4.destroy()
                canvas.pack()

                def move_up2(event):
                    # Controls Upwards movement of right bar
                    speed_of_bar2_up = 50
                    yz = canvas.coords(bar2)
                    if yz[1] <= 7:
                        speed_of_bar2_up = 0
                        canvas.move(bar2, 0, speed_of_bar2_up)

                    else:
                        canvas.move(bar2, 0, -speed_of_bar2_up)

                def move_down2(event):
                    # Controls Downwards movement of right bar
                    speed_of_bar2_down = 50
                    yz = canvas.coords(bar2)
                    if yz[3] >= 720:
                        speed_of_bar2_down = 0
                        canvas.move(bar2, 0, speed_of_bar2_down)

                    else:
                        canvas.move(bar2, 0, speed_of_bar2_down)

                def ball_moving():
                    # Controls the complete collission of the gameplay
                    global points
                    list1 = [sidespeed, upspeed]

                    list2 = [sidespeed, upspeed]
                    start = time()
                    counter = 0

                    points = 0
                    with open('./initials.txt', 'w') as saveFilep:

                        saveFilep.write(initials)
                        saveFilep.write("\n")

                    while True:

                        xy1 = canvas.coords(oval)
                        xy2 = canvas.coords(bar2)
                        # Checks if player-controlled bar collides with ball
                        if xy1[1] >= xy2[1] and xy1[3] <= xy2[3]+30:

                            if xy1[2] >= xy2[2]-15:
                                counter += 1
                                list2[0] = list1[0]
                                list1[0] = -1 * list1[0]
                                points += 1
                                points_label = Label(
                                    canvas, text="Point: "+str(points), font=("Comic Sans MS", '38'))  # Updating points
                                points_label.place(x=.1, y=.1)

                                if list1[0] < 0:
                                    list1[0] = list1[0] - 2.5
                                    list2[0] = list2[0] + 2.5
                                elif list1[0] > 0:
                                    list1[0] = list1[0] + 2.5
                                    list2[0] = list2[0] - 2.5

                                else:
                                    list1[0] = list1[0]
                        # Checks if CPU-controlled bar collides with ball
                        if xy1[0] <= 30:
                            list1[0] = -1 * list1[0]

                        if xy1[1] <= 0 or xy1[3] >= 720:
                            list2[1] = list1[1]
                            list1[1] = -1 * list1[1]

                        if xy1[2] >= 1280:
                            stop = time()
                            with open('./player.txt', 'a') as saveFile09:

                                saveFile09.write(initials)
                                saveFile09.write("\n")
                            with open('./score.txt', 'a') as saveFile24:
                                # Game finishes as ball hits right edge
                                saveFile24.write(str(points))
                                saveFile24.write("\n")
                            messagebox.showinfo(
                                title="Game Over", message="This is the amount of seconds you lasted:" + str(round((stop-start), 3)))
                            exit()

                        def imagere(event):
                            # Function to control removal of boss mode image
                            canvas.delete("boss1")

                        def resume(event):
                            # Function to control Resume Key
                            list1[0] = -1*list2[0]
                            list1[1] = -1*list2[1]

                        def pause(event):
                            # Function to control Pause Key
                            list1[0] = 0
                            list1[1] = 0

                        def boss(event):
                            # Function to add boss key Image
                            global img
                            canvas.bind_all('<Key-o>', pause)
                            canvas.bind_all('<Key-O>', pause)
                            canvas.img = ImageTk.PhotoImage(
                                Image.open("work.png").resize((1280, 720)))

                            canvas.create_image(
                                10, 10, anchor=NW, image=canvas.img, tags="boss1")

                        def cheat(event):
                            # Function to add cheat code
                            list1[0] = 10
                            list1[1] = 10

                        def save(event=None):
                            # Function to save gameplay

                            text = ""
                            for i in xy1:
                                text = text + str(i) + " "

                            with open('./oval.txt', 'w') as saveFile:

                                saveFile.write(text)
                            with open('./pref.txt', 'w') as saveFile:

                                saveFile.write("a")
                            with open('./points.txt', 'w') as saveFile10:

                                saveFile10.write(str(points))
                        # To bind respective keys to the function
                        canvas.bind_all('<Key-Up>', move_up2)
                        canvas.bind_all('<Key-Down>', move_down2)
                        canvas.bind_all('<Key-b>', boss)
                        canvas.bind_all('<Key-B>', boss)
                        canvas.bind_all('<Key-c>', cheat)
                        canvas.bind_all('<Key-C>', cheat)
                        canvas.bind_all('<Key-p>', pause)
                        canvas.bind_all('<Key-P>', pause)
                        canvas.bind_all('<Key-r>', resume)
                        canvas.bind_all('<Key-R>', resume)
                        canvas.bind_all('<Key-v>', imagere)
                        canvas.bind_all('<Key-V>', imagere)
                        canvas.bind_all('<Key-x>', save)
                        canvas.bind_all('<Key-X>', save)
                        # Moving ball function
                        canvas.move(oval, list1[0], list1[1])

                        canvas.coords(bar1, [10, xy1[1]-30, 30, xy1[3]+30])
                        sleep(0.00002)

                        window.update()

                window.update()
                ball_moving()

            def w_s_key():
                # Function for when player chooses to play with W and S keys
                canvas = Canvas(window, width=1280, height=720)
                checker = -1
                img_intro = ImageTk.PhotoImage(
                    Image.open("sky copy.png").resize((1280, 720)))
                canvas.create_image(10, 10, anchor=NW,
                                    image=img_intro, tags="image_intro")
                coordinates_of_ball = [200, 10, 230, 40]
                oval = canvas.create_oval(
                    coordinates_of_ball, fill="orange")  # Creates the ball
                upspeed = 8
                sidespeed = 8
                bar1_coors = [10, 10, 30, 100]
                # Creates the CPU-controlled bar
                bar1 = canvas.create_rectangle(bar1_coors, fill="orange")
                bar2_coors = [1250, 10, 1270, 110]
                # Creates the player-controlled bar
                bar2 = canvas.create_rectangle(bar2_coors, fill="orange")
                speed_of_bar1 = 25
                speed_of_bar2 = 25
                back_label.destroy()
                label4.destroy()
                button3.destroy()
                button4.destroy()
                canvas.pack()

                def move_up2(event):
                    # Controls Upwards movement of right bar
                    speed_of_bar2_up = 50
                    yz = canvas.coords(bar2)
                    if yz[1] <= 7:
                        speed_of_bar2_up = 0
                        canvas.move(bar2, 0, speed_of_bar2_up)

                    else:
                        canvas.move(bar2, 0, -speed_of_bar2_up)

                def move_down2(event):
                    # Controls Downwards movement of right bar
                    speed_of_bar2_down = 50
                    yz = canvas.coords(bar2)
                    if yz[3] >= 720:
                        speed_of_bar2_down = 0
                        canvas.move(bar2, 0, speed_of_bar2_down)

                    else:
                        canvas.move(bar2, 0, speed_of_bar2_down)

                counter = 0

                def ball_moving():
                    # Controls the complete collission of the gameplay
                    global points

                    list1 = [sidespeed, upspeed]
                    list2 = [sidespeed, upspeed]
                    points = 0
                    value3 = sidespeed
                    points = 0
                    counter = 0
                    start = time()
                    with open('./initials.txt', 'w') as saveFilep:

                        saveFilep.write(initials)
                        saveFilep.write("\n")

                    while True:

                        xy1 = canvas.coords(oval)
                        xy2 = canvas.coords(bar2)
                        # Checks if player-controlled bar collides with ball
                        if xy1[1] >= xy2[1] and xy1[3] <= xy2[3]+30:
                            if xy1[2] >= xy2[2]-15:
                                counter += 1
                                list1[0] = -1 * list1[0]
                                points += 1
                                points_label = Label(
                                    canvas, text="Point: "+str(points), font=("Comic Sans MS", '38'))
                                points_label.place(x=.1, y=.1)

                                if list1[0] < 0:
                                    list1[0] = list1[0] - 2.5
                                    list2[0] = list1[0]
                                elif list1[0] > 0:
                                    list1[0] = list1[0] + 2.5
                                    list2[0] = list1[0]

                                else:
                                    list1[0] = list1[0]
                        # Checks if CPU-controlled bar collides with ball
                        if xy1[0] <= 30:
                            list1[0] = -1 * list1[0]

                        if xy1[1] <= 0 or xy1[3] >= 720:
                            list2[1] = list1[1]
                            list1[1] = -1 * list1[1]

                        if xy1[2] >= 1280:  # Game gets over when ball hits the right edge
                            stop = time()
                            with open('./player.txt', 'a') as saveFile47:

                                saveFile47.write(initials)
                                saveFile47.write("\n")
                            with open('./score.txt', 'a') as saveFileu:

                                saveFileu.write(str(points))
                                saveFileu.write("\n")

                            messagebox.showinfo(
                                title="Game Over", message="This is the amount of seconds you lasted:" + str(round((stop-start), 3)))
                            text = ""

                            with open('./oval.txt', 'w') as saveFilel:

                                saveFilel.write("x")
                                exit()
                            exit()

                        def imagere(event):
                            # Function to control removal of boss mode image
                            canvas.delete("boss2")

                        def resume(event):
                            # Function to control resume key
                            list1[0] = list2[0]
                            list1[1] = list2[1]

                        def pause(event):
                            # Function to control pause key
                            list1[0] = 0
                            list1[1] = 0

                        def boss(event):
                            # Function to control create boss mode image
                            global img1
                            canvas.bind_all('<Key-o>', pause)
                            canvas.bind_all('<Key-O>', pause)
                            img1 = ImageTk.PhotoImage(
                                Image.open("work.png").resize((1280, 720)))

                            canvas.create_image(
                                10, 10, anchor=NW, image=img1, tags="boss2")

                        def cheat(event):
                            # Function to control cheat key
                            list1[0] = 10
                            list1[1] = 10

                        def save(event=None):
                            # Function to control save key
                            text = ""

                            for i in xy1:
                                text = text + str(i) + " "
                            print(text)
                            with open('./oval.txt', 'w') as saveFile56:

                                saveFile56.write(text)
                            with open('./pref.txt', 'w') as saveFile678:

                                saveFile678.write("w")
                            with open('./points.txt', 'w') as saveFile10:

                                saveFile10.write(str(points))
                                exit()

                        # Binds keys with specific function
                        canvas.bind_all('<Key-w>', move_up2)
                        canvas.bind_all('<Key-s>', move_down2)
                        canvas.bind_all('<Key-W>', move_up2)
                        canvas.bind_all('<Key-S>', move_down2)
                        canvas.bind_all('<Key-c>', cheat)
                        canvas.bind_all('<Key-C>', cheat)
                        canvas.bind_all('<Key-p>', pause)
                        canvas.bind_all('<Key-P>', pause)
                        canvas.bind_all('<Key-r>', resume)
                        canvas.bind_all('<Key-R>', resume)
                        canvas.bind_all('<Key-b>', boss)
                        canvas.bind_all('<Key-B>', boss)
                        canvas.bind_all('<Key-v>', imagere)
                        canvas.bind_all('<Key-V>', imagere)
                        canvas.bind_all('<Key-X>', save)
                        canvas.bind_all('<Key-x>', save)
                        canvas.move(oval, list1[0], list1[1])
                        canvas.coords(bar1, [10, xy1[1]-30, 30, xy1[3]+30])
                        sleep(0.00002)

                        window.update()

                window.update()
                ball_moving()
            # Makes the prefrence buttons
            button3 = Button(
                window, text="Play with Up and Down Keys", font=(
                    "Comic Sans MS", '38'), fg="black", bg="#403937",  command=keys)
            button3.place(relx=.5, rely=.4, anchor=CENTER)
            button4 = Button(
                window, text="Play with W and S Keys", font=(
                    "Comic Sans MS", '38'), fg="black", bg="#403937",  command=w_s_key)
            button4.place(relx=.5, rely=.5, anchor=CENTER)

        button2 = Button(window, text="Continue", font=(
            "Comic Sans MS", '38'), fg="black", bg="#403937", command=choice)
        button2.place(relx=.5, rely=.5, anchor=CENTER)

    global imag1
    # Background image for menu,login,leaderboard,prefrences
    imag1 = PhotoImage(file="moon.png")
    back_label = Label(image=imag1)
    back_label.place(x=0, y=0, relwidth=1, relheight=1)
    # Functions to create a hover effect when hovering over button

    def button_hover1(event):
        buttona["bg"] = "black"
        buttona["fg"] = "orange"

    def button_hover2(event):
        buttonb["bg"] = "black"
        buttonb["fg"] = "orange"

    def button_hover3(event):
        buttonc["bg"] = "black"
        buttonc["fg"] = "orange"

    def button_hover4(event):
        buttond["bg"] = "black"
        buttond["fg"] = "orange"

    def button_leave1(event):
        buttona["bg"] = "black"
        buttona["fg"] = "black"

    def button_leave2(event):
        buttonb["bg"] = "black"
        buttonb["fg"] = "black"

    def button_leave3(event):
        buttonc["bg"] = "black"
        buttonc["fg"] = "black"

    def button_leave4(event):
        buttond["bg"] = "black"
        buttond["fg"] = "black"

    window.configure(bg="black")

    def escape(event):
        exit()
    # Function to run saved game

    def load():
        paragraph = open('oval.txt', 'r')
        paragraph2 = open('pref.txt', 'r')

        count = 0
        list_of_coordinates = paragraph.read()
        word = paragraph2.read()
        paragraph.close()
        paragraph2.close()
        # Checks if function was actually saved
        if list_of_coordinates == 'x':
            label1.destroy()
            buttona.destroy()
            buttonb.destroy()
            buttonc.destroy()
            buttond.destroy()
            load_label = Label(window, text="No Game was previously saved", font=(
                "Comic Sans MS", '38'), fg="white")
            load_label.place(relx=.5, rely=.405, anchor=CENTER)
            buttone = Button(window, bg='gray', text="Back", font=(
                "Comic Sans MS", '38'), fg="black", command=welcome)
            buttone.place(relx=.1, rely=.1, anchor=S)

        else:
            paragraph3 = open('initials.txt', 'r')
            name1 = paragraph3.read()
            paragraph3.close()
            list1 = list_of_coordinates.split()
            list2 = []
            for i in list1:
                num = float(i)
                list2.append(num)
            # Checks if game was controlled by arrows
            if word == 'a':

                def keys():
                    # Function when the game is used to control by arrows
                    canvas = Canvas(window, width=1280, height=720)
                    checker = -1
                    img_intro = ImageTk.PhotoImage(
                        Image.open("sky copy.png").resize((1280, 720)))
                    canvas.create_image(10, 10, anchor=NW,
                                        image=img_intro, tags="image_intro")
                    coordinates_of_ball = [200, 10, 230, 40]
                    oval = canvas.create_oval(
                        list2, fill="orange")  # Creates the ball
                    upspeed = 8
                    sidespeed = 8
                    bar1_coors = [10, 10, 30, 100]
                    # Creates the CPU-controlled bar
                    bar1 = canvas.create_rectangle(bar1_coors, fill="orange")
                    bar2_coors = [1250, 10, 1270, 110]
                    # Creates the player-controleld bar
                    bar2 = canvas.create_rectangle(bar2_coors, fill="orange")
                    speed_of_bar1 = 25
                    speed_of_bar2 = 25
                    back_label.destroy()

                    canvas.pack()

                    def move_up2(event):
                      # Used to control the upwards movement of player-controlled bar
                        speed_of_bar2_up = 50
                        yz = canvas.coords(bar2)
                        if yz[1] <= 7:
                            speed_of_bar2_up = 0
                            canvas.move(bar2, 0, speed_of_bar2_up)

                        else:
                            canvas.move(bar2, 0, -speed_of_bar2_up)

                    def move_down2(event):
                        # Used to control the downwards movement of player-controlled bar
                        speed_of_bar2_down = 50
                        yz = canvas.coords(bar2)
                        if yz[3] >= 720:
                            speed_of_bar2_down = 0
                            canvas.move(bar2, 0, speed_of_bar2_down)

                        else:
                            canvas.move(bar2, 0, speed_of_bar2_down)

                    def ball_moving():
                        # Controls the collision detection of the game-play

                        list1 = [sidespeed, upspeed]

                        list2 = [sidespeed, upspeed]
                        start = time()
                        counter = 0
                        with open('./points.txt', 'r') as saveFile5:
                            points = int(saveFile5.read())

                        while True:

                            xy1 = canvas.coords(oval)
                            xy2 = canvas.coords(bar2)
                            # Checks if ball collides with player-controlled bar
                            if xy1[1] >= xy2[1] and xy1[3] <= xy2[3]+30:
                                if xy1[2] >= xy2[2]-15:
                                    points += 1
                                    points_label = Label(
                                        canvas, text="Point: "+str(points), font=("Comic Sans MS", '38'))
                                    points_label.place(x=.1, y=.1)
                                    counter += 1
                                    list1[0] = -1 * list1[0]

                                    if list1[0] < 0:
                                        list1[0] = list1[0] - 2.5
                                        list2[0] = list1[0]
                                    elif list1[0] > 0:
                                        list1[0] = list1[0] + 2.5
                                        list2[0] = list1[0]

                                    else:
                                        list1[0] = list1[0]
                            # Checks if ball collides with CPU-controlled bar
                            if xy1[0] <= 30:
                                list1[0] = -1 * list1[0]

                            if xy1[1] <= 0 or xy1[3] >= 720:
                                list2[1] = list1[1]
                                list1[1] = -1 * list1[1]

                            if xy1[2] >= 1280:
                                stop = time()
                                with open('./player.txt', 'a') as saveFile4:
                                    saveFile4.write(name1)
                                    saveFile4.write("\n")
                                with open('./score.txt', 'a') as saveFile5:

                                    saveFile5.write(str(points))
                                    saveFile5.write("\n")
                                # Checks if ball hits the right edge
                                messagebox.showinfo(
                                    title="Game Over", message="This is the amount of seconds you lasted:" + str(round((stop-start), 3)))
                                text = ""

                                with open('./oval.txt', 'w') as saveFile:

                                    saveFile.write("x")
                                    exit()

                            def imagere(event):
                                # Function to control removal of boss mode image
                                canvas.delete("boss1")

                            def resume(event):
                                # Function to control resume key
                                list1[0] = list2[0]
                                list1[1] = list2[1]

                            def pause(event):
                                # Function to control pause
                                list1[0] = 0
                                list1[1] = 0

                            def boss(event):
                                # Function to control addition of boss mode image
                                global img
                                canvas.bind_all('<Key-o>', pause)
                                canvas.bind_all('<Key-O>', pause)
                                canvas.img = ImageTk.PhotoImage(
                                    Image.open("work.png").resize((1280, 720)))

                                canvas.create_image(
                                    10, 10, anchor=NW, image=canvas.img, tags="boss1")

                            def cheat(event):
                                # Function to control cheat key
                                list1[0] = 10
                                list1[1] = 10

                            def save(event):
                                # Function to control the ssave key of the gameplay

                                for i in xy1:
                                    text = text + str(i) + " "
                                with open('./oval.txt', 'w') as saveFile976:

                                    saveFile976.write(text)
                                paragraph2 = open('pref.txt', 'w')
                                paragraph2.write('a')
                                paragraph2.close()
                                exit()
                            # Binds the keys with the respective functions
                            canvas.bind_all('<Key-Up>', move_up2)
                            canvas.bind_all('<Key-Down>', move_down2)
                            canvas.bind_all('<Key-b>', boss)
                            canvas.bind_all('<Key-B>', boss)
                            canvas.bind_all('<Key-c>', cheat)
                            canvas.bind_all('<Key-C>', cheat)
                            canvas.bind_all('<Key-p>', pause)
                            canvas.bind_all('<Key-P>', pause)
                            canvas.bind_all('<Key-r>', resume)
                            canvas.bind_all('<Key-R>', resume)
                            canvas.bind_all('<Key-v>', imagere)
                            canvas.bind_all('<Key-V>', imagere)
                            canvas.bind_all('<Key-x>', save)
                            canvas.bind_all('<Key-X>', save)

                            canvas.move(oval, list1[0], list1[1])

                            canvas.coords(bar1, [10, xy1[1]-30, 30, xy1[3]+30])
                            sleep(0.00002)

                            window.update()

                    window.update()
                    ball_moving()
                keys()
            elif word == 'w':
                # Called when the game being played was using W and S keys
                def w_s_key():
                    canvas = Canvas(window, width=1280, height=720)
                    checker = -1
                    img_intro = ImageTk.PhotoImage(
                        Image.open("sky copy.png").resize((1280, 720)))
                    canvas.create_image(10, 10, anchor=NW,
                                        image=img_intro, tags="image_intro")
                    coordinates_of_ball = [200, 10, 230, 40]
                    oval = canvas.create_oval(
                        coordinates_of_ball, fill="orange")  # Creates ball
                    upspeed = 8
                    sidespeed = 8
                    bar1_coors = [10, 10, 30, 100]
                    # Creates CPU-controlled bar
                    bar1 = canvas.create_rectangle(bar1_coors, fill="orange")
                    bar2_coors = [1250, 10, 1270, 110]
                    # Creates Plauyer-controlled bar
                    bar2 = canvas.create_rectangle(bar2_coors, fill="orange")
                    speed_of_bar1 = 25
                    speed_of_bar2 = 25
                    back_label.destroy()

                    canvas.pack()

                    def move_up2(event):
                        # Controls the upward movement of the player-controlled bar
                        speed_of_bar2_up = 50
                        yz = canvas.coords(bar2)
                        if yz[1] <= 7:
                            speed_of_bar2_up = 0
                            canvas.move(bar2, 0, speed_of_bar2_up)

                        else:
                            canvas.move(bar2, 0, -speed_of_bar2_up)

                    def move_down2(event):
                     # Controls the downward movement of the player-controlled bar

                        speed_of_bar2_down = 50
                        yz = canvas.coords(bar2)
                        if yz[3] >= 720:
                            speed_of_bar2_down = 0
                            canvas.move(bar2, 0, speed_of_bar2_down)

                        else:
                            canvas.move(bar2, 0, speed_of_bar2_down)

                    counter = 0

                    def ball_moving():
                        # Controls the collision detection of the game-play

                        list1 = [sidespeed, upspeed]
                        list2 = [sidespeed, upspeed]
                        points = 0
                        value3 = sidespeed
                        with open('./points.txt', 'r') as saveFile5:
                            points = int(saveFile5.read())

                        counter = 0
                        start = time()

                        while True:

                            xy1 = canvas.coords(oval)
                            xy2 = canvas.coords(bar2)
                            # Checks if the ball is hit by player controlled bar
                            if xy1[1] >= xy2[1] and xy1[3] <= xy2[3]+30:
                                if xy1[2] >= xy2[2]-15:
                                    points += 1
                                    points_label = Label(
                                        canvas, text="Point: "+str(points), font=("Comic Sans MS", '38'))
                                    points_label.place(x=.1, y=.1)
                                    counter += 1
                                    list1[0] = -1 * list1[0]

                                    if list1[0] < 0:
                                        list1[0] = list1[0] - 2.5
                                        list2[0] = list1[0]
                                    elif list1[0] > 0:
                                        list1[0] = list1[0] + 2.5
                                        list2[0] = list1[0]

                                    else:
                                        list1[0] = list1[0]
                            # Checks if ball hits the CPU-controlled bar
                            if xy1[0] <= 30:
                                list1[0] = -1 * list1[0]

                            if xy1[1] <= 0 or xy1[3] >= 720:
                                list2[1] = list1[1]
                                list1[1] = -1 * list1[1]

                            if xy1[2] >= 1280:
                                stop = time()
                                with open('./player.txt', 'a') as saveFile4:

                                    saveFile4.write(name1)
                                    saveFile4.write("\n")
                                with open('./score.txt', 'a') as saveFile5:

                                    saveFile5.write(str(points))
                                    saveFile5.write("\n")
                                # Game ends when the balls hits the right edge
                                messagebox.showinfo(
                                    title="Game Over", message="This is the amount of seconds you lasted:" + str(round((stop-start), 3)))
                                text = ""

                                with open('./oval.txt', 'w') as saveFile99:

                                    saveFile99.write("x")
                                    exit()

                            def imagere(event):
                                # Controls the image removal of boss-key

                                canvas.delete("boss2")

                            def resume(event):
                                # Controls the resume key

                                list1[0] = list2[0]
                                list1[1] = list2[1]

                            def pause(event):
                                # Controls the pause key

                                list1[0] = 0
                                list1[1] = 0

                            def boss(event):
                                # Controls the image addition of boss-key
                                global img1
                                canvas.bind_all('<Key-o>', pause)
                                canvas.bind_all('<Key-O>', pause)
                                img1 = ImageTk.PhotoImage(
                                    Image.open("work.png").resize((1280, 720)))

                                canvas.create_image(
                                    10, 10, anchor=NW, image=img1, tags="boss2")

                            def cheat(event):
                                # Controls the cheat key
                                list1[0] = 10
                                list1[1] = 10

                            def save(event=None):
                                # Controls the save key

                                text = ""

                                for i in xy1:
                                    text = text + str(i) + " "
                                print(text)
                                with open('./oval.txt', 'w') as saveFile78:

                                    saveFile78.write(text)
                                with open('./pref.txt', 'w') as saveFile6:

                                    saveFile6.write("w")
                            # Binds the keys with the appropriate functions
                            canvas.bind_all('<Key-w>', move_up2)
                            canvas.bind_all('<Key-s>', move_down2)
                            canvas.bind_all('<Key-W>', move_up2)
                            canvas.bind_all('<Key-S>', move_down2)
                            canvas.bind_all('<Key-c>', cheat)
                            canvas.bind_all('<Key-C>', cheat)
                            canvas.bind_all('<Key-p>', pause)
                            canvas.bind_all('<Key-P>', pause)
                            canvas.bind_all('<Key-r>', resume)
                            canvas.bind_all('<Key-R>', resume)
                            canvas.bind_all('<Key-b>', boss)
                            canvas.bind_all('<Key-B>', boss)
                            canvas.bind_all('<Key-v>', imagere)
                            canvas.bind_all('<Key-V>', imagere)
                            canvas.bind_all('<Key-X>', save)
                            canvas.bind_all('<Key-x>', save)
                            canvas.move(oval, list1[0], list1[1])
                            canvas.coords(bar1, [10, xy1[1]-30, 30, xy1[3]+30])
                            sleep(0.00002)

                            window.update()
                    window.update()
                    ball_moving()
                w_s_key()

    def lead(event=None):
        # Creates the leader board
        label1.destroy()
        buttona.destroy()
        buttonb.destroy()
        buttonc.destroy()
        buttond.destroy()

        score_list = open("new_score.txt") . read() . splitlines()
        player_list = open("new_player.txt") . read() . splitlines()
        list_lead = [[]]
        # Sorting the 2 single-dimension lists into a single 2-D list
        list_lead = [list(items) for items in zip(score_list, player_list)]
        # Sorting the leaderboard list
        list_lead.sort(key=lambda value: value[0])
        sorted_player = []
        sorted_score = []
        # Putting the single 2-d list into two single-dimension lists
        for i in range(len(list_lead)):
            sorted_score.append(list_lead[i][0])
            sorted_player.append(list_lead[i][1])

        # Creates the header texts
        back = Button(window, height=2, width=10, text='Main Menu',
                      command=welcome, font=('Open Sans', 14, "bold"))
        back . place(relx=.05, rely=.05, anchor=CENTER)
        t1 = Label(window, text='Players:', font=(
            'Open Sans', 24, "bold"), bg='#079af0')
        t1 . place(relx=.2, rely=.2, anchor=CENTER)
        add = 0
        if len(sorted_player) > 5:
            length = 5
        else:
            length = len(sorted_player)
        i = length-1
        while i >= 0:
            # Prints the list of sorted player names
            t2 = Label(window, text=sorted_player[i], font=(
                'Open Sans', 24, "bold"), bg='#079af0')
            valuex = .2
            valuey = .3 + add
            t2 . place(relx=valuex, rely=valuey, anchor=CENTER)
            add = add + 0.1
            i = i-1
        t3 = Label(window, text='Scores:', font=(
            'Open Sans', 24, "bold"), bg='#079af0')
        t3 . place(relx=.3, rely=.2, anchor=CENTER)
        j = length-1
        add = 0
        while j >= 0:
            # Prints the list of sorted player scores
            t2 = Label(window, text=sorted_score[j], font=(
                'Open Sans', 24, "bold"), bg='#079af0')
            valuex = .3
            valuey = .3 + add
            t2 . place(relx=valuex, rely=valuey, anchor=CENTER)
            add = add + 0.1
            j = j-1
        # Prints the highest scorer and highest score respectively
        t4 = Label(window, text='Highest Scorer', font=(
            'Open Sans', 24, "bold"), bg='#079af0')
        t4 . place(relx=.5, rely=.2, anchor=CENTER)
        t5 = Label(window, text=sorted_player[length-1],
                   font=('Open Sans', 24, "bold"), bg='#079af0')
        t5 . place(relx=.5, rely=.3, anchor=CENTER)
        t6 = Label(window, text='Highest Score', font=(
            'Open Sans', 24, "bold"), bg='#079af0')
        t6 . place(relx=.7, rely=.2, anchor=CENTER)
        t7 = Label(window, text=sorted_score[length-1],
                   font=('Open Sans', 24, "bold"), bg='#079af0')
        t7 . place(relx=.7, rely=.3, anchor=CENTER)
    # Text and buttons for the Main Menu
    label1 = Label(window,  text="PONG", font=(
        "Comic Sans MS", '38'), fg="white", bg="#079af0")
    label1.place(relx=.5, rely=.1, anchor=CENTER)
    buttona = Button(window,  text="        Start        ", relief=SUNKEN, font=(
        "Comic Sans MS", '38'), fg="black", command=login)
    buttona.place(relx=.5, rely=.405, anchor=CENTER)
    buttonb = Button(window, bg='#403937', text="   Leaderboard  ", font=(
        "Comic Sans MS", '38'), fg="black", command=lead)
    buttonb.place(relx=.5, rely=.5, anchor=CENTER)
    with open('new_score.txt', 'w') as file:
        file.write("")
    with open('new_player.txt', 'w') as file:
        file.write("")
    with open('score.txt', 'r') as file:
        for line2 in file:
            if not line2.isspace():
                with open('new_score.txt', 'a') as file2:
                    file2.write(line2)
                    print(2)
    with open('player.txt', 'r') as file:
        for line2 in file:
            if not line2.isspace():
                with open('new_player.txt', 'a') as file2:
                    file2.write(line2)
    buttonc = Button(window, bg='#403937', text="         Load         ", font=(
        "Comic Sans MS", '38'), fg="black", command=load)
    buttonc.place(relx=.5, rely=.64, anchor=S)
    buttond = Button(window, bg='#403937', text="         Exit          ", font=(
        "Comic Sans MS", '38'), fg="black", command=lambda: exit())
    buttond.place(relx=.5, rely=.735, anchor=S)
    # Binds the buttons to the respective functions
    buttona.bind("<Enter>", button_hover1)
    buttonb.bind("<Enter>", button_hover2)
    buttonc.bind("<Enter>", button_hover3)
    buttond.bind("<Enter>", button_hover4)
    buttona.bind("<Leave>", button_leave1)
    buttonb.bind("<Leave>", button_leave2)
    buttonc.bind("<Leave>", button_leave3)
    buttond.bind("<Leave>", button_leave4)


welcome()


window.mainloop()  # Creating the main loop
