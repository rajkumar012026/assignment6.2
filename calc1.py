import tkinter as tk
first_number = None
second_number = None
operator = None
#click function
def btn_click(value):

   global first_number
   global second_number
   global operator
   if value == "Clear":
        user_input.delete(0, 'end')
        first_number = None
        second_number = None
        operator = None
   elif value in ["+","-","x","/"]:
        operator = value
        first_number = user_input.get()
        user_input.delete(0, 'end')
   elif value == "=":
       second_number = user_input.get()
       if first_number and operator:
           num1 = float(first_number)
           num2 = float(second_number)

           if operator == "+": res = num1 + num2
           elif operator == "-": res = num1 - num2
           elif operator == "x": res = num1 * num2
           elif operator == "/": res = num1 / num2

           user_input.delete(0, 'end')
           user_input.insert(0, str(res))
           first_number = None

   else:

       current_number = user_input.get()
       user_input.delete(0, 'end')
       user_input.insert(0, str(current_number) + str(value))

root = tk.Tk()
root.title("Calculator")
#cus_font = tf.Font(family='Helvetica', size=20, weight='bold')
user_input = tk.Entry(width=26, font = "arial",justify='right')
user_input.grid(row=0, column=0, columnspan=4)
# list of buttons
data = [[1, 2, 3, 4], [5, 6, 7, 8],[9, 0, ".", "Clear"],["+","-","x","/"],["="]]
for i in data: # Display of buttons
    for j in i:
        if len(i) == 1: #to adjust the button
            btn = tk.Button(root, width=5, height=3, text=j, command=lambda v=j: btn_click(v))
            btn.grid(row=data.index(i)+1, column=(i.index(j))*2, padx=2, pady=2,columnspan=4,sticky="nsew")
        else:
            btn = tk.Button(root, width=5, height=3, text=j, command=lambda v=j: btn_click(v))
            btn.grid(row=data.index(i)+1, column=i.index(j), padx=2, pady=2,columnspan=1,sticky="nsew")
root.mainloop()
