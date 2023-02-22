#   1-masala
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QTableWidget,QTableWidgetItem,QTextEdit
from PyQt5.QtGui import QFont
import mysql.connector, sys
app=QApplication(sys.argv)
class Window1(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Telegram Chat")
        self.setGeometry(100,100,800,600)
        self.win2=Window2()
        
        self.start()
        self.show()
        

    def font(self,ob,x,y):
        ob.setFont(QFont("Times",20))
        ob.move(x,y)

    def start(self):
        login=QLabel("Login: ",self)
        self.font(login,50,200)
        password=QLabel("Password: ",self)
        self.font(password,50,260)
        self.log=QLineEdit(self)
        self.log.setPlaceholderText("Enter your login")
        self.font(self.log,220,200)
        self.passw=QLineEdit(self)
        self.passw.setPlaceholderText("Enter your password")
        self.font(self.passw,220,260)

        ok=QPushButton("OK",self)
        self.font(ok,450,320)
        ok.clicked.connect(self.Signin)


    def Signin(self):
        '''a1=self.log.text()
        a2=self.passw.text()
        self.win2.cur.execute("INSERT INTO Telegram (user,password) VALUES(%s,%s)",(a1,a2))
        self.win2.mydb.commit()'''
        self.win2.show()

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="TelegramChat"
        )
        self.cur=self.mydb.cursor()
        self.setWindowTitle("Second Window")
        self.setGeometry(100,100,800,600)
        self.createDB()
        self.start2()

    def createDB(self):
        self.cur.execute("CREATE DATABASE IF NOT EXISTS TelegramChat")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Telegram(user VARCHAR(50),password VARCHAR(20), intext TEXT, outtext TEXT)")
        self.mydb.commit()

    def start2(self):
        whom=QLabel("Whom: ",self)
        whom.setFont(QFont("Times",15))
        whom.move(50,50)
        self.who=QLineEdit(self)
        c=win1.log.text()
        if self.who.text() != "":
            self.who.setPlaceholderText("Enter reciever's")
        else:
            self.who.setText()
        self.who.setFont(QFont("Times",15))
        self.who.move(170,50)

        input=QLabel("INPUT ",self)
        input.setFont(QFont("Times",15))
        input.move(150,150)
        self.text1=QTextEdit(self)
        self.text1.setFont(QFont("Times",15))
        self.text1.move(50,200)

        output=QLabel("OUTPUT ",self)
        output.setFont(QFont("Times",15))
        output.move(500,150)
        self.text2=QTextEdit(self)
        self.text2.setFont(QFont("Times",15))
        self.text2.move(400,200)

        send=QPushButton("Send",self)
        send.setFont(QFont("Times",15))
        send.move(200,400)
        send.clicked.connect(self.closeit)

    def closeit(self):
        a1=win1.log.text()
        a2=win1.passw.text()
        a3=self.text1.toPlainText()
        a4=self.text2.toPlainText()
        self.cur.execute("INSERT INTO Telegram (user,password,intext,outtext) VALUES(%s,%s,%s,%s)",(a1,a2,a3,a4))
        self.mydb.commit()
        win1.log.setText(self.who.text())
        win1.passw.clear()
        self.text2.setText(a3)
        self.text1.clear()
        self.who.clear()
        self.close()
win1=Window1()
sys.exit(app.exec_())
