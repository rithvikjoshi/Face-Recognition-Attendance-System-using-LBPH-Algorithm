from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x720+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_usn=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        


    
        #image1
        img=Image.open(r"img\header.jpg")
        img=img.resize((1366,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=200)
        #image2
        # img1=Image.open(r"img\facialrecognition.png")
        # img1=img1.resize((710,200),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=710,y=0,width=710,height=200)

        title_lbl=Label(self.root,text="Attendance Report", font=("time new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=200,width=1366,height=55)



        #mainframe
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=0,y=255,width=1366,height=490)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=670,height=460)

        img_left=Image.open(r"img\student.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=670,height=130)

        #Sub Frame
        attendance_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        attendance_frame.place(x=5,y=135,width=657,height=300)

        #studentid
        studentID_label=Label(attendance_frame,text="StudentID : ",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=15,pady=5,sticky=W)

        studentID_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_id,width=15,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=15,pady=5,sticky=W)


        #USN
        usn_label=Label(attendance_frame,text="USN : ",font=("times new roman",12,"bold"),bg="white")
        usn_label.grid(row=0,column=2,padx=15,pady=5,sticky=W)

        usn_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_usn,width=15,font=("times new roman",12,"bold"))
        usn_entry.grid(row=0,column=3,padx=15,pady=5,sticky=W)


        #Student Name
        student_name_label=Label(attendance_frame,text="Student Name : ",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=15,pady=5,sticky=W)

        student_name_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_name,width=15,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=15,pady=5,sticky=W)


        #Department
        dep_label=Label(attendance_frame,text="Department : ",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=15,pady=5,sticky=W)

        dep_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_dep,width=15,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=15,pady=5,sticky=W)


        #time
        time_label=Label(attendance_frame,text="Time : ",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=15,pady=5,sticky=W)

        time_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_time,width=15,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=15,pady=5,sticky=W)


        #date
        date_label=Label(attendance_frame,text="Date : ",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=15,pady=5,sticky=W)

        date_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_date,width=15,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=15,pady=5,sticky=W)


        #attendance_status
        attendance_status_label=Label(attendance_frame,text="Attendance Status : ",font=("times new roman",12,"bold"),bg="white")
        attendance_status_label.grid(row=5,column=0,padx=15,pady=5,sticky=W)

        attendance_status_combo=ttk.Combobox(attendance_frame,textvariable=self.var_atten_attendance,width=13,font=("times new roman",12,"bold"),state="readonly")
        attendance_status_combo["values"]=("Status","Present","Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=5,column=1,padx=15,pady=5,sticky=W)

        #buttons
        btn_frame=Frame(attendance_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=655,height=35)

        import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",command=self.action,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)




        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=670,height=460)

        #table
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=660,height=435)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","usn","name","dep","time","date","atte"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="ID")
        self.AttendanceReportTable.heading("usn",text="USN")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("atte",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("usn",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("atte",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



    #fetch data


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
        
    #import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    
    #export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is been exported to "+os.path.basename(fln)+" succesfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #get focus from table
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_usn.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    # export upadte
    def action(self):
        id=self.var_atten_id.get()
        usn=self.var_atten_usn.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","USN","Name","Department","Time","Date","Attendance"]))
                dict_writer.writerow({
                "ID":id,
                "USN":usn,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

        

    #reset
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_usn.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()