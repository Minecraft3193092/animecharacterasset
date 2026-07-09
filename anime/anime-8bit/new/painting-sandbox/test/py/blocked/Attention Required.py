import tkinter as tk

root = tk.Tk()
root.title('Attention Required!')
root.geometry('500x500')

name = 'test'

block_headline = tk.Label(root,text='Sorry, you have been blocked',font=('Arial',20))
unable_to_access = tk.Label(root,text=f'You are unable to access {name}',font=('Arial',15))

block_headline.pack()
unable_to_access.pack()

root.mainloop()