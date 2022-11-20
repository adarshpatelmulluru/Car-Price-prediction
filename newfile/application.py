from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
tran=pickle.load(open("trans.pkl","rb"))
dataset = pd.read_csv("orderedcarset2.csv")


@app.route('/', methods=['GET', 'POST'])
def index():
    name = sorted(dataset['name'].unique())
    year = sorted(dataset['year'].unique(), reverse=True)
    fuel_type = sorted(dataset['fuel'].unique())
    seller_type = sorted(dataset['seller_type'].unique())
    transmission = sorted(dataset['transmission'].unique())
    owner = sorted(dataset['owner'].unique())

    name.insert(0, 'select name')
    return render_template('frontindex.html', carname=name, years=year, fuel_type=fuel_type, seller_type=seller_type, transmission=transmission, owner=owner)


@app.route('/predict', methods=['POST'])
def predict():

    car_name = request.form.get('carname')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    seller = request.form.get('seller_type')
    trans = request.form.get('transmission')
    owner = request.form.get('owner')
    driven = request.form.get('km_driven')
    print(car_name, fuel_type, seller, trans, owner, year,driven)
    data=np.array([car_name, fuel_type, seller, trans, owner, int(year),int(driven)])
    t=tran.transform(pd.DataFrame(columns=['name', 'fuel', 'seller_type', 'transmission', 'owner', 'year','km_driven'],data=[data]))
    prediction = model.predict(t)
    print(prediction)

    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)
