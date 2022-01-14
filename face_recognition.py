from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime







class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1420x720+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition", font=("time new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1420,height=55)

        #1st Image
        img_top=Image.open(r"img\face_detector1.jpg")
        img_top=img_top.resize((710,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=710,height=700)

        #2nd Image
        img_bottom=Image.open(r"img\mob.jpg")
        img_bottom=img_bottom.resize((710,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=710,y=55,width=710,height=700)

        #button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2", font=("time new roman",15,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=270,y=620,width=180,height=40)



    #Ateendance
    def mark_attendance(self,i,r,n,d):
        with open("attend.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



    #Face Recognition
    def face_recog(self):
        def draw_boundray(img,classifer,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifer.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select usn from student where id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                my_cursor.execute("select id from student where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>60:
                    cv2.putText(img,f"Id :{d}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"USN :{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name :{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep :{i}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(d,r,n,i)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifer.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()










if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()