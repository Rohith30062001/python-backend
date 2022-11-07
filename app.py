import mysql.connector as mysql
from flask import jsonify,Flask,render_template,redirect


id=0

db=mysql.connect(host="localhost",user="admin",password="password",database='employee')
print(db)
cursor=db.cursor()

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Welcome To Employee DB'
    return render_template("home.html")

@app.route('/insert/<employeename>/<employeenumber>/<employeepassword>/<employeeemail>',methods = ['POST', 'GET'])
def insert(employeename,employeenumber,employeepassword,employeeemail):
    #employeename="python"
    #employeenumber="1111111"
    #employeepassword="123456"
    #employeeemail="python@gmail.com"
   
    query="INSERT INTO EMPLOYEETABLE (EMPLOYEENAME,EMPLOYEENUMBER,EMPLOYEEPASSWORD,EMPLOYEEEMAIL) VALUES (%s, %s , %s, %s)"
    values=(employeename,employeenumber,employeepassword,employeeemail)
    cursor.execute(query,values)
    db.commit()
    return redirect("http://127.0.0.1:5000/",code=302)
    return "inserted successfully"

   

@app.route('/dropdatabase')
def dropdatabase():
    query="DROP DATABASE employee"
    cursor.execute(query)
    db.commit()
    return ("The data base is dropped")

@app.route('/dropdatatable')
def droptable():
    query="DROP TABLE EMPLOYEETABLE"
    cursor.execute(query)
    db.commit()
    return ("The data table is dropped")

@app.route('/viewdatatable')
def viewdatatable():
    query="SELECT * FROM EMPLOYEETABLE"
    cursor.execute(query)
    print("SuccessFul")
    rows=cursor.fetchall()
    return jsonify(rows)
    

@app.route('/truncate')
def truncate():
    query="TRUNCATE TABLE EMPLOYEETABLE"
    cursor.execute(query)
    db.commit()
    return "SuccessFulLy Deleted Data In Table"

@app.route('/delete/<int:id>',methods = ['get'])
def delete(id):
    #id=int(input())
    #id=int(input())
    query=f"DELETE FROM EMPLOYEETABLE WHERE ID={id}"
    cursor.execute(query)
    db.commit()
    #return ("SuccessFulLy Deleted Data In Table")
    return redirect("http://127.0.0.1:5000/",code=302)

@app.route('/search/<int:id>',methods = ['POST', 'GET'])
def search(id):
    #id=int(input())
    query=f"SELECT EMPLOYEENAME,EMPLOYEENUMBER,EMPLOYEEPASSWORD,EMPLOYEEEMAIL FROM EMPLOYEETABLE WHERE ID={id}"
    res=cursor.execute(query)
    #print(res)
    rows=cursor.fetchall()
    if rows !=[]:
        return render_template("search.html",data=rows)
    else:
        return '<body style="background-color: rgb(85, 153, 131);"><h2 style="color: red;"><center> Employee Not Found </center></h2></body>'
    #return redirect("http://127.0.0.1:5000/",code=302) 
   


if __name__ == '__main__':
    app.run(debug=True)
