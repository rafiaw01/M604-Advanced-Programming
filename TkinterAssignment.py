# Student Name : Awais Rafi
#Instructor Name : William Morrison
#Submission Date : September 21,2023


##############################################################################
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import Image, ImageTk
from tkinter import Text

df = pd.read_csv(
    r"C:\Users\USER\Desktop\Renewable Energy\renewable electricity by country - US states  renewable electricity.csv")
pd.set_option('display.max_columns', None)
print(df)

#####################################################################################
window = tk.Tk()
window.configure()
window.title("Solar Buddy")
window.geometry("1200x1000")
fig, ax = plt.subplots()
plt.grid()

#####################################################################################
solar_image = Image.open(r"C:\Users\USER\Desktop\Renewable Energy\Solar Panel.webp")
obj = ImageTk.PhotoImage(solar_image)

lbl_1 = tk.Label(image=obj)
lbl_1.image=obj

lbl_1.pack()

frame = tk.Frame(window)
label = tk.Label(text="Solar Power Generated")
label.config(font=("Arial"))
label.pack()
frame.pack()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

####################################################################################
def plotting():
    x = df['US STATE'].head(10)
    y = df['renewables'].head(10)
    plt.figure(figsize=(12, 12))
    plt.figure(figsize=(12, 12))
    ax.plot(x, y)
    canvas.draw()

#Exception Handling Test
try:
    print(dff)
except:
    print("dff is not defined")

######################################################


def solar_power_calculation(solar_plate,solar_power):
    return solar_plate * solar_power


#################################################################################
b = tk.Button(window, text="Press to Graph", command=plotting,fg='red',bg='yellow')
b.pack()

toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X)

window.mainloop()
