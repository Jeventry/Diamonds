import tkinter as tk
import random
import sys

my_win = 0
my_loss = 0

num_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit = ['of Hearts!', 'of Diamonds!', 'of Clubs!', 'of Spades!']



def main(): 
        
        def no():
            window.destroy()
            sys.exit()
            no()
            
        window = tk.Tk()
    
        window.rowconfigure(0, minsize=50, weight=1)
        window.columnconfigure([0, 1, 2], minsize=50, weight=1)
   
        lbl_value = tk.Label(master=window, text="Welcome to Diamond Rush!")
        lbl_value.grid(row=0, column=1)
        lbl_value = tk.Label(text="Get dealt a Face Card or Diamond to win!")
        lbl_value.grid(row=1, column=1)
        lbl_value = tk.Label(master=window, text="Would you like to play?")
        lbl_value.grid(row=2, column=1)

        btn_yes = tk.Button(master=window, text="Yes", command=window.destroy)
        btn_yes.grid(row=3, column=0, sticky="nsew")
    
        btn_no = tk.Button(master=window, text="No", command=no)
        btn_no.grid(row=3, column=2, sticky="nsew")
    
        window.mainloop()
        
        def dealwindow():         
              
                def deal():   
            
                    global my_win, my_loss
                    y = random.choice(suit)
                    x = random.choice(cards)
                        
                    card_value = num_values[x]

                    if(card_value > 9):
                        my_win += 1

                        lbl_result = tk.Label(text=x)
                        lbl_result.grid (row=0, column=1)
                        lbl_result = tk.Label(text=y)
                        lbl_result.grid (row=1, column=1)
                        lbl_result = tk.Label(text="You win!")
                        lbl_result.grid (row=2, column=1)
                        lbl_result = tk.Label(text="Win:%d" % my_win)
                        lbl_result.grid (row=3, column=0)
                        
                    elif(y == 'of Diamonds!'):
                        my_win += 1
                            
                        lbl_result = tk.Label(text=x)
                        lbl_result.grid (row=0, column=1)
                        lbl_result = tk.Label(text=y)
                        lbl_result.grid (row=1, column=1)
                        lbl_result = tk.Label(text="You win!")
                        lbl_result.grid (row=2, column=1)
                        lbl_result = tk.Label(text="Win:%d" % my_win)
                        lbl_result.grid (row=3, column=0)
                            
                    else:
                        my_loss += 1
                            
                        lbl_result = tk.Label(text=x)
                        lbl_result.grid (row=0, column=1)
                        lbl_result = tk.Label(text=y)
                        lbl_result.grid (row=1, column=1)
                        lbl_result = tk.Label(text="You lost!")
                        lbl_result.grid (row=2, column=1)
                        lbl_result = tk.Label(text="Loss:%d" % my_loss)
                        lbl_result.grid (row=3, column=2)
            
                deal()
   
                btn_deal = tk.Button(text="Deal!", command=deal)
                btn_deal.grid(row=6, column=1, sticky="nsew")
            
                window.mainloop()
            
        dealwindow()

        
        
main()
