import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
from form import ContactForm
import requests
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
 'db': 'hospice',
'host': 'localhost',
'port': 27017
}
db = MongoEngine()
db.init_app(app)


class h(db.Document):
    
    name = db.StringField()
    age=db.IntField()
    gender=db.StringField()
    location =db.StringField()
    phone =db.IntField()
    schedule =db.StringField()
  
    def to_json(self):
        return {
                
                "name": self.name,
                "age":self.age,
                'gender':self.gender,
                'location':self.location,
                'phone':self.phone,
                'schedule':self.schedule,
                
                }


@app.route('/', methods=['POST'])
def create_record():
 
    record = json.loads(request.data)
    c = h(
                
                name=record['name'],
                age=record['age'],
                gender=record['gender'],
                location=record['location'],
                phone=record['phone'],
                schedule=record['schedule'],
                
                )
    c.save()
    return jsonify(c.to_json())
'''
@app.route('/')
def start():
    render_template("add.html")
'''
@app.route('/add',methods=['GET','POST'])
def add():
 form = ContactForm()  
 if request.method=="GET":
   return render_template("add.html",form=form)
 else:
      x={
            
            "name":request.form['name'],
            'age':request.form['age'],
            'gender':request.form['gender'],
            'location':request.form['location'],
            'phone':request.form['phone'],
            'schedule':request.form['schedule'],
   
         }
      
      y=json.dumps(x)
    
      response = requests.post(url="http://127.0.0.1:5000/",data=y)
      #loaded_json = json.loads(x)
      
      return render_template('x.html',a=x)
 
if __name__ == '__main__': 
 app.run(debug = True)