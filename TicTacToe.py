from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import messagebox
from PIL import Image, ImageTk

start_window = Tk()
start_window.title("TicTacToe by RSP")
start_window.geometry("600x600+60+60")
start_window.config(bg='#4287f5')

img = Image.open(r"C:\Users\Rahul Roy\PycharmProjects\GIT\Games\Tic Tac Toe\ttt_logo.png")
resized_image = img.resize((210, 130), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
render = ImageTk.PhotoImage(resized_image)
img = Label(start_window, image=render)
img.place(x=190, y=240)

x = 1
moves_remaining = 9
x_value = []
o_value = []


def play_():

    def start():
        game_window = Toplevel(start_window)
        game_window.title("TicTacToe by RSP")
        game_window.geometry("600x600+60+60")
        game_window.config(bg='#4287f5')
        start_window.deiconify()

        def turn():
            if x in [1, 3, 5, 7, 9]:
                user_turn = Label(game_window, text="Player X's move",
                                  font=('Times New Roman', 16), fg='#d63031')
                user_turn.place(x=200, y=550)
            else:
                user_turn = Label(game_window, text="Player O's move",
                                  font=('Times New Roman', 16), fg='#d63031')
                user_turn.place(x=200, y=550)

        turn()

        def clear_value():
            global x, moves_remaining, x_value, o_value
            game_window.destroy()
            x = 1
            moves_remaining = 9
            x_value.clear()
            o_value.clear()

        def restart(val):
            # global x, moves_remaining,x_value, o_value
            if val == 'X':
                answer = askyesno(title='Play Again',
                                  message='Player X wins!!!\nDo You want to Play Again?')
                print(answer)
                if answer:
                    clear_value()

                    start()
                else:
                    clear_value()
                    # play_()
                    messagebox.showinfo(title="Greetings from RSP!", message=" Thank You for playing this game")

            elif val == 'O':
                answer = askyesno(title='Play Again',
                                  message='Player O wins!!!\nDo You want to Play Again?')
                print(answer)
                if answer:
                    clear_value()
                    start()
                else:
                    clear_value()
                    # play_()
                    messagebox.showinfo(title="Greetings from RSP!", message=" Thank You for playing this game")
            else:
                answer = askyesno(title='Play Again',
                                  message='OHH NOO! Its a Tie\nDo You want to Play Again?')
                if answer == 'yes':
                    clear_value()
                    start()
                else:
                    clear_value()
                    # play_()
                    messagebox.showinfo(title="Greetings from RSP!", message=" Thank You for playing this game")

        def check_winner():
            x_win_1 = ['1', '2', '3']
            x_win_2 = ['1', '4', '7']
            x_win_3 = ['1', '5', '9']
            x_win_4 = ['2', '5', '8']
            x_win_5 = ['3', '6', '9']
            x_win_6 = ['4', '5', '6']
            x_win_7 = ['7', '8', '9']
            x_win_8 = ['3', '5', '7']

            o_win_1 = ['1', '2', '3']
            o_win_2 = ['1', '4', '7']
            o_win_3 = ['1', '5', '9']
            o_win_4 = ['2', '5', '8']
            o_win_5 = ['3', '6', '9']
            o_win_6 = ['4', '5', '6']
            o_win_7 = ['7', '8', '9']
            o_win_8 = ['3', '5', '7']

            # print("x", x_value)
            # print("o", o_value)
            if all(item in x_value for item in x_win_1) or \
                    all(item in x_value for item in x_win_2) or \
                    all(item in x_value for item in x_win_3) or \
                    all(item in x_value for item in x_win_4) or \
                    all(item in x_value for item in x_win_5) or \
                    all(item in x_value for item in x_win_6) or \
                    all(item in x_value for item in x_win_7) or \
                    all(item in x_value for item in x_win_8):
                print("x wins")
                restart('X')
                game_window.withdraw()
                start_window.deiconify()

            elif all(item in o_value for item in o_win_1) or \
                    all(item in o_value for item in o_win_2) or \
                    all(item in o_value for item in o_win_3) or \
                    all(item in o_value for item in o_win_4) or \
                    all(item in o_value for item in o_win_5) or \
                    all(item in o_value for item in o_win_6) or \
                    all(item in o_value for item in o_win_7) or \
                    all(item in o_value for item in o_win_8):
                print("O wins")
                restart('O')
                game_window.withdraw()
                start_window.deiconify()

            else:
                if moves_remaining == 0:
                    print("Ties")
                    restart('no')
                    game_window.withdraw()
                    start_window.deiconify()

        def clicked(button_no, name):
            global x, moves_remaining
            if x in [1, 3, 5, 7, 9]:
                button_no['text'] = "X"
                x_value.append(name)
                x_value.sort()
                # print(x_value)
                moves_remaining -= 1
                check_winner()
            else:
                button_no['text'] = "O"
                o_value.append(name)
                o_value.sort()
                # print(o_value)
                moves_remaining -= 1
                check_winner()

            # print(f"You clicked {name}")
            button_no['state'] = 'disabled'
            button_no['fg'] = 'yellow'
            button_no['bg'] = '#b2bec3'
            x += 1
            turn()

        first = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(first, "1"))
        first.place(x=100, y=50)
        second = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(second, "2"))
        second.place(x=215, y=50)
        third = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(third, "3"))
        third.place(x=330, y=50)
        fourth = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(fourth, "4"))
        fourth.place(x=100, y=211)
        fifth = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(fifth, "5"))
        fifth.place(x=215, y=211)
        sixth = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(sixth, "6"))
        sixth.place(x=330, y=211)
        seventh = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(seventh, "7"))
        seventh.place(x=100, y=372)
        eighth = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(eighth, "8"))
        eighth.place(x=215, y=372)
        ninth = Button(game_window, bg='#dfe6e9', height=10, width=15, command=lambda: clicked(ninth, "9"))
        ninth.place(x=330, y=372)

        game_window.mainloop()

    play_button = Button(start_window, text="LETS PLAY", command=start,
                         font=('Terminal', 20), bg='#2d3436', fg='#abbbd4')
    play_button.place(x=210, y=400)


play_()
start_window.mainloop()
