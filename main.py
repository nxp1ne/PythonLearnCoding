y = [2, 3, 5, 10 ,10, 10, 7, 2, 2, 2, 5, 4, 3, 3]
def bts(x, y):
    y = [2, 3, 5, 10 ,10, 10, 7, 2, 2, 2, 5, 4, 3, 3]
    x = len(y)
    return(sum(y) / x)

z = bts(x=len(y), y=[2, 3, 5, 10 ,10, 10, 7, 2, 2, 2, 5, 4, 3, 3])
print(z)

# task 2
text = "крутой текст, вот прям уверен, вот прям на все тысячи процентов. r"
def func():
    print(text.count(','))
func()

# Day 2
import tkinter as tk

def tapping(event):
    klavisha = event.keysym
    label.config(text=canvas.coords(oval))
    speed = 45
    if klavisha == "Up":
        canvas.move(oval, 0, -speed)
    elif klavisha == "Down":
        canvas.move(oval, 0, speed)
    elif klavisha == "Left":
        canvas.move(oval, -speed, 0)
    elif klavisha == "Right":
        canvas.move(oval, speed, 0)


windowz = tk.Tk()
canvas = tk.Canvas(windowz, bg='#9400A3', width=1920, height=1080)
label = tk.Label(windowz, text='Sigma Gaming 2004', font=100)
oval = canvas.create_oval([300, 300], [100, 100], fill='red')
line = canvas.create_line((10, 10), (10,1000), fill='black')
line = canvas.create_line((10, 10), (100,10), fill='black')

label.pack()
canvas.pack()
windowz.bind("<KeyPress>", tapping)
windowz.mainloop()
