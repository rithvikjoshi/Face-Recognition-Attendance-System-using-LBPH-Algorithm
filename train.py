from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x720+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Train Data Set", font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=50,width=1420,height=45)

        img_top=Image.open(r"img\facialrecognition.png")
        img_top=img_top.resize((1366,305),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=95,width=1366,height=305)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classfier,cursor="hand2", font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=380,width=1366,height=60)


        img_bottom=Image.open(r"img\facialrecognition.png")
        img_bottom=img_bottom.resize((1420,305),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1420,height=305)

    def train_classfier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grag scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifer.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Traning Data set Completed")



        





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()