from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

hello = Flask(__name__)

hello.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
hello.config["SQLAlchemy_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(hello)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title= db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@hello.route("/",methods=['GET','POST'])
def Home():
    if request.method=="POST":
        title=request.form['title']
        desc=request.form['desc']

        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
        # print(allTodo)
    
    return render_template('index.html' , allTodo=allTodo)

 

@hello.route("/delete/<int:sno>")
def Delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit() 
    return redirect('/')  

if __name__ == "__main__":  
    hello.run(debug=False)
