
from tkinter import *

window = Tk()
window.config(background = "antiquewhite2")
window.title("Apples Gallore; Apple Shop")
window.geometry("400x500")


apple_price = 25

def prices_calculation ():
    amount_money = int(money_entry.get())
    number_total = (amount_money // apple_price)
    genshin = Label(window, text ="\n"f"With the money you have, you can purchase {number_total} apples.",
                    bg = "antiquewhite2",
                    font = ("Times", 11))
    money_left = (amount_money % apple_price)
    impact = Label(window, text =f"You also have a remaining money of ₱{money_left}",
                   bg = "antiquewhite2",
                   font = ("Times", 11))
    genshin.pack()
    impact.pack()

greetings_one = Label(window, text= "\n""Good Day, Ma'am/Sir!", 
                      font = ("Times", 20),
                      bg= "antiquewhite2")
greetings_two = Label(window, text = "\n""How may I help you today?""\n",
                       bg = "antiquewhite2",
                       font = ("Arial", 12))
greetings_one.pack()
greetings_two.pack()

menu = Button(window, text= "Apple Prices:""\n\n""1 Apple -------- ₱25",
              font = ("Times", 15),
              bg = "crimson",
              fg = "white" )
menu.pack()

advice_one = Label(window, text= "\n""We'll calculate your purchases for you",
                   bg= "antiquewhite2",
                   font = ("Arial", 12))
advice_two = Label(window, text= "Please enter the amount of money you have in the space below:""\n",
                   bg= "antiquewhite2",
                   font = ("Arial", 10))

money_entry = Entry(window, justify = CENTER, bg= "light green")
submit_button = Button(window, text= "Submit",
                       bg = "cornsilk3",
                       command = prices_calculation)
advice_one.pack()
advice_two.pack()      
money_entry.pack()
submit_button.pack()


window.mainloop()
