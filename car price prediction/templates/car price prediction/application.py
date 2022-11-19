from flask import Flask,render_template
import pandas as pd
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open("LRModel.pkl", "rb"))
dataset=pd.read_csv("orderedcarset2.csv")
@app.route('/')

def index():
    car_name=sorted(dataset['name'].unique())
    years =sorted(dataset['year'].unique(), reverse=True)
    fuel_type =sorted(dataset['fuel'].unique())
    seller =sorted(dataset['seller_type'].unique())
    trans=sorted(dataset['transmission'].unique())
    owner_type=sorted(dataset['owner'].unique())

    name.insert(0, 'select name')
    return render_template('frontindex.html',car_name=name, years=year, fuel_type=fuel, seller=seller_type,trans=transmission, owner_type=owner)

@app.route('/predict',methods=['POST'])
def predict():

    car_name=request.form.get('name')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    seller=request.form.get('seller_type')
    trans=request.form.get('transmission')
    owner=request.form.get('owner')
    driven=request.form.get('km_driven')


    prediction=model.predict(pd.DataFrame(columns=['name', 'year', 'fuel_type', 'seller_type' , 'transmission' , 'owner', 'km_driven'],
                              data=np.array([car_name,year,fuel_type,seller,trans,owner,driven])))

    return str(np.round(prediction[0],2))


if __name__=='__main__':
    app.run(debug=True)