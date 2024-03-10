import qrcode 

from PIL import Image

qr=qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6,
    border=5
)

data="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="white")
img.save('qrcode.png')
 
import qrcode
import tkinter as tk
import datetime

win= tk.Tk()
win.title('interface')
win.geometry('400x200')

win.config(bg='yellow')



optionlist=(
    'png',
    'svg',
    )   

def qrgenerate():
    text=entry.get()
    site=text
    val=formatoption.get()
    url=qrcode.make(site)
    saveas=datetime.datetime.now().strftime('%Y-%m-%D-%H:%M:%S')
    if val=='.png':
        url.png('QR'+ saveas + '.png', scale =8)
    elif val =='.svg':
        url.svg('QR'+ saveas + '.svg', scale=8)
    label = tk.Label(win, text='SUCCESS!', bg= 'black' , fg='#00ff00')   
    label.grid(row=4,column=1)



label= tk.Label(win, text='generate qr code for: ' ,bg="black",fg="white")
label.grid(row=0,column=0)

entry= tk.Entry(win) 
entry.grid (row=0,column=1)


optiondisplay= tk.Label(win, text='choose format')
optiondisplay.grid(row=1,column=0)

formatoption= tk.StringVar(win)
formatoption.set(optionlist[0])

opt=tk.OptionMenu(win,formatoption,*optionlist)
opt.config(width=6,height=0 ,font=('courier 10',12))  
opt.grid(row=1,column=1)

qrbutton=tk.Button(win, text='generate qr code', bg='black',fg='white',font='courier 10',command=qrgenerate)
qrbutton.grid(row=2,column=1 )

quitbutton = tk.Button(win , text= 'exit app' ,bg='white',fg= 'black', command =win.quit)
quitbutton.grid(row=5 , column=1)


win.mainloop()
