from tkinter import *

window = Tk()
window.config(background = "coral1")
window.title("Fruit Baskets: Fruit Shop")
window.geometry("670x400")

orange_price= 25
apple_price = 20

def order_calculations ():
    orange_number = int(entry_oranges.get())
    apple_number = int(entry_apple.get())
    price_total = int(apple_number * apple_price) + int(orange_number * orange_price)
    your_total = Label(window,
                       text="\n"f"Your purchase costs ₱{price_total}"".",
                       bg= "coral1",
                       font = ("Times", 15))
    your_total.pack()

greetings_one = Label(window, text= "Welcome to Fruit Baskets!", 
                      font = ("Times", 20),
                      bg= "coral1")
greetings_two = Label(window, text = "How may I help you?""\n",
                       bg = "coral1",
                       font = ("Arial", 12))
greetings_one.pack()
greetings_two.pack()

menu = Button(window, text= "Available Items for Today:""\n\n""Oranges -------- ₱25""\n\n""Apples ---------- ₱20",
              font = ("Times", 15),
              bg = "chartreuse3",
              fg = "black" )
menu.pack()

frame_label = Frame(window, bg = "coral1")
frame_label.pack()

frame_button = Frame(window, bg = "coral1")
frame_button.pack()

orange_quantity_label = Label(frame_label, 
                              text = "\n""Type below the number of oranges""\n"" you would like to purchase:",
                              font = ("TIMES", 12),
                              bg="coral1")
entry_oranges = Entry(frame_button, justify = CENTER, bg = "orange", fg = "black")
orange_quantity_label.grid(row = 0, column = 0, padx = 20)
entry_oranges.grid(row = 0, column = 2, padx = 35)

apple_quantity_label = Label(frame_label, 
                              text = "\n""Type below the number of apples ""\n""you would like to purchase:",
                              font = ("TIMES", 12),
                              bg = "coral1")
entry_apple = Entry(frame_button, justify = CENTER, bg = "red", fg = "black")
apple_quantity_label.grid(row = 0, column = 3, padx = 20)
entry_apple.grid(row = 0, column = 5, padx = 40)

order_button = Button(window, text ="Click to Order",
                      font = ("Times", 10),
                      bg = "cadetblue3",
                      fg = "black",
                      command = order_calculations)
order_button.pack()

window.mainloop()
