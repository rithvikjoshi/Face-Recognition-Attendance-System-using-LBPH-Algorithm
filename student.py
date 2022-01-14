from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import importlib
from email_validator import validate_email, EmailNotValidError



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x720+0+0")
        self.root.title("Face Recognition System") 


        #variables
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_year=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_usn=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_search=StringVar()
        self.var_searchtxt=StringVar()


        #image1
        img=Image.open(r"img\header.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=130)

        #bg image
        img3=Image.open(r"img\stud.jpg")
        img3=img3.resize((1365,620),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1365,height=620)

        title_lbl=Label(bg_img,text="Student Registration", font=("time new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1365,height=52)


        #mainframe
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1330,height=550)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=520)

        img_left=Image.open(r"img\student.jpg")
        img_left=img_left.resize((645,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=645,height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=640,height=100)

        #department
        dep_label=Label(current_course_frame,text="Department : ",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=5)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select department","MCA","MBA","Mtech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year : ",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=2,padx=2,pady=5)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select year","2018-21","2019-22","2020-22")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semister : ",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=0,padx=2,pady=5)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select semester","Sem - 1","Sem - 2","Sem - 3","Sem - 4","Sem - 5","Sem - 6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)


        #Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Studnet Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=240,width=640,height=250)
        
        #studentid
        studentID_label=Label(class_student_frame,text="StudentID : ",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=15,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student name
        studentName_label=Label(class_student_frame,text="Student Name : ",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=15,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #USN
        rool_no_label=Label(class_student_frame,text="USN : ",font=("times new roman",12,"bold"),bg="white")
        rool_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        rool_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_usn,width=15,font=("times new roman",12,"bold"))
        rool_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Gender
        gender_label=Label(class_student_frame,text="Gender : ",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,width=13,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #email
        email_label=Label(class_student_frame,text="Email : ",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #phone
        phone_label=Label(class_student_frame,text="Phone : ",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_student_frame,text="Address : ",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        #Teacher
        teacher_label=Label(class_student_frame,text="Teacher Name : ",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)


        #buttons
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=160,width=635,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=195,width=635,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)


        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Database Information",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=630,height=520)


        img_right=Image.open(r"img\smart-attendance.jpg")
        img_right=img_right.resize((620,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=620,height=130) 

        #search
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=620,height=70)

        #search bar
        search_label=Label(search_frame,text="Search by : ",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","id","usn")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky =W)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_searchtxt,width=12,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",command=self.search_data,width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",command=self.show_data,width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4) 

        #table
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=620,height=280)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","sem","year","id","name","usn","gender","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Depatment")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("usn",text="USN")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="EmailID")
        self.student_table.heading("phone",text="Mobile")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("usn",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

    #function dec
    def add_data(self):
        self.letter()
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_gender.get()=="Select gender" or self.var_sem.get()=="Select semester" or self.var_year.get()=="Select year" or self.var_usn.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_usn.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()                                                                                               
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    #fetch data from mysql
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_sem.set(data[1]),
        self.var_year.set(data[2]),
        self.var_id.set(data[3]),
        self.var_name.set(data[4]),
        self.var_usn.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_address.set(data[9]),
        self.var_teacher.set(data[10]),
        self.var_radio1.set(data[11])


    #update database
    def update_data(self):
        self.letter()
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student data?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,sem=%s,year=%s,name=%s,usn=%s,gender=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where id=%s",(
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_usn.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_id.get()                                                                                              
                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #delete data in mysql
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Success","Student data deleted successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
    #reset button
    def reset_data(self):
        self.var_dep.set("Select department")
        self.var_sem.set("Select semister")
        self.var_year.set("Select year")
        self.var_id.set("")
        self.var_name.set("")
        self.var_usn.set("")
        self.var_gender.set("Select gender")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #search details in table    
    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_search.get())+" LIKE '%"+str(self.var_searchtxt.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #Show all values
    def show_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()         
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("",END,values=i)
            if rows==None:
                messagebox.showerror("Error","Data Not Found",parent=self.root)
                conn.commit()
        conn.close()




    #take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="atte",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,sem=%s,year=%s,name=%s,usn=%s,gender=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where id=%s",(
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_usn.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_id.get()==id+1                                                                                            
                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined on face

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scalling factor=1.3
                    #minimun neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or  int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed succesfully!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 
        
    
    def letter(self):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        sel = self.var_name.get()
        num = self.var_phone.get()
        email = self.var_email.get()
        if not sel.isalpha():
            messagebox.showerror('Only letters in name','Only letters are allowed!')
            importlib.reload(module)
        if not num.isdigit():
            messagebox.showerror('Only numbers in mobile','Only numbers are allowed!')
            importlib.reload(module)
        if len(num)!=10:
            messagebox.showerror('Invaild mobile no.','Provide 10 digits only!')
            importlib.reload(module)

        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError as e:
            messagebox.showerror('Invald email','Enter the correct email format')
            importlib.reload(module)  
        # if(validate_email(email)):
        #     messagebox.showerror('Invald email','Enter the correct email format')
        #     importlib.reload(module)




        

                    



                    
                

        

        










        












if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()