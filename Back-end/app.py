from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:1234@localhost:5432/Web"
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from principal import CarsModel
from app import db
    
@app.route("/")
def saludo():
    return "Programacion Web"

@app.route('/cars', methods=["GET"])
def handle_car():   
    cars=CarsModel.query.all()
    results=[
        {
            "id":car.id,
            "name":car.name,
            "model":car.model,
            "doors":car.doors
    }
    for car in cars]
    return {"count": len(results), "cars":results}

@app.route('/carsPost', methods=["POST"])
def post_car():
    if(request.is_json):
        data=request.get_json()
        print(data)
        new_car=CarsModel(name=data['name'],model=data['model'],doors=data['doors'])
        db.session.add(new_car)
        db.session.commit()
        # Close the scoped session to commit the changes
        db.session.close()

        return {"message":"nuevo carrito creado"}
    else:
        return{"message_error":"error"}
    
@app.route('/carsPut/<int:car_id>', methods=["PUT"])
def put_car(car_id):
    if request.is_json:
        data = request.get_json()
        car = CarsModel.query.get(car_id)

        if car is not None:
            car.name = data['name']
            car.model = data['model']
            car.doors = data['doors']

            db.session.commit()

            return {'message': 'carrito actualizado'}
        else:
            return {'message_error': 'carrito no encontrado, intenta con otro valor'}
    else:
        return {'message_error': 'error'}