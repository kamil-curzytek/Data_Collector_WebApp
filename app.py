from flask import Flask, render_template, request
from database import Database
from send_email import send_email

#methods to operate with database
database = Database("users.db")
def insert_command(email, height):
    return(database.insert(email,height))

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success/", methods = ['POST']) #HTTP POST request -> when user uploads some data to the server, opposite is GET
def success():
    if request.method == 'POST':
        email = request.form["email_name"]    #we use request method to read key value 'email_name' from form element from index.html
        height = request.form["height"]
        #print(request.form) #printing all dictionary keys with values from form 
        #print(email) #printing email
        #print(height) #printing height
        #print(insert_command(email, height))
        if(insert_command(email,height) == 0): #checking answer from database insert method
            send_email(email, height, database.average()[0], database.average()[1]) #passing arguments from average method
            return render_template("success.html")
        else:
            return render_template("index.html", text = "Email already exists in our database !")


if __name__ == "__main__":
    app.debug=True
    app.run()