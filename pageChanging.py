import tkinter as tk
from PIL import Image,ImageTk
import os
pictures = {'আ': 'ah1.jpg', 'অ': 'oha1.jpg', 'ই': 'i1.jpg','এ':'ae1.jpg','ে':'aec1.jpg','া':'ahc1.jpg','ব':'b1.jpg','ঃ':'bsro1.jpg','চ':'cha1.jpg',
            'ছ':'chha1.jpg','ঁ':'chndro1.jpg','ড':'da1.jpg','দ':'dda14.jpg','ধ':'ddha4.jpg','ঢ':'dha14.jpg','ঞ':'eio1.jpg','ফ':'fa14.jpg','গ':'ga13.jpg',
            'ঘ':'gha1.jpg','হ':'ha1.jpg','ি':'ic1.jpg','জ':'ja1.jpg','ঝ':'jha1.jpg','ক':'k1.jpg','খ':'kha1.jpg','ল':'la1.jpg','ম':'ma1.jpg','ন':'na1.jpg'
            ,'ও':'o1.jpg','ো':'oc1.jpg','ঐ':'oi1.jpg','ৌ':'oic1.jpg','ং':'onsor1.jpg','ঔ':'ou1.jpg','ৈ':'ouc1.jpg','প':'pa1.jpg','র':'rri1.jpg',
            'ৃ':'rric1.jpg','শ':'sa1.jpg',' ':'space1.jpg','ট':'ta1.jpg','ঠ':'tha1.jpg','ত':'tta1.jpg','থ':'ttha1.jpg','উ':'u1.jpg','ু':'uc1.jpg','ঙ':'umo13.jpg'}
message = ''
fields = 'Last Name', 'First Name', 'Job', 'Country'
LARGE_FONT = ("Verdana", 12)
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Normal People to D&M",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="D&M to Normal People",
                            command=lambda: self.ret2())
        button2.pack()

    def ret2(self):
        os.system("python classify_webcam.py")


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.labelText = tk.Label(self, text="Normal People to D&M")
        self.labelText.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()

        button3 = tk.Button(self, text="Translate",
                            command=lambda: self.ret())
        button3.pack()
    def ret(self):
        message = self.entry.get()
        print(message)
        self.photos = []
        self.cv = tk.Canvas(self)
        self.cv.pack()
        for letter in message:
            filename = pictures[letter]
            im = Image.open(filename)
            im = im.resize((50, 50), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(im)
            self.photos.append(photo)
        i = 0
        j = 0
        for photo in self.photos:
            self.cv.create_image(5 + i, 5 + j, image=photo, anchor='nw')
            i += 100
            if i % 1000 == 0:
                j += 105
                i = 0
app = SeaofBTCapp()
app.title("One Hand Bangla Sign Language")
app.mainloop()