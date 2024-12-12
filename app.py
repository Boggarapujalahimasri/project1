from flask import Flask,render_template, request, redirect
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient("localhost",27017)
mydb=client["calci"]
results=mydb["amrutha"]
isLoggedIn=False
credentials={
    "bjhimasri26@gmail.com":"hima",
    "amrutha@gmail.com":"ammu"
}
@app.route("/",methods=["GET","POST"])
def homepage():
    global isLoggedIn
    if request.method=="POST":
        log_email = request.form["email"]
        log_password= request.form["password"]
        if(log_email in credentials) and (credentials[log_email]==log_password):
            isLoggedIn = True
            return redirect("/calci")
        else:
            return redirect("/")
    else:
        return render_template("login.html")    

@app.route("/calci",methods=["GET","POST"])

def calculator():
    if request.method=="POST":
        a=int(request.form["num1"])
        opr=request.form["opr"]
        b=int(request.form["num2"])
        if opr=="add": 
            res= f"{a} + {b} is {a+b}"
            results.insert_one({
                "num1":a,"num2":b,"operator":opr,"results":res
            })
            return render_template("index.html",output=res)
        elif opr=="div": 
            res= f"{a} /{b} is {a/b}"
            results.insert_one({
                "num1":a,"num2":b,"operator":opr,"results":res
            })
            return render_template("index.html",output=res)
        elif opr=="sub": 
            res= f"{a} - {b} is {a-b}"
            results.insert_one({
                "num1":a,"num2":b,"operator":opr,"results":res
            })
            return render_template("index.html",output=res)
        elif opr=="mul": 
            res= f"{a} x {b} is {a*b}"
            results.insert_one({
                "num1":a,"num2":b,"operator":opr,"results":res
            })
            return render_template("index.html",output=res)
    else:
        return render_template("index.html")

    
    
app.run(debug=True)