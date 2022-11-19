from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)
car=pd.read_csv("orderedcarset2.csv")
@app.route('/')

def index():
    carname=sorted(car['name'].unique())
    year =sorted(car['year'].unique(), reverse=True)
    fuel_type =sorted(car['fuel'].unique())
    seller_type =sorted(car['seller_type'].unique())
    transmission=sorted(car['transmission'].unique())
    owner=sorted(car['owner'].unique())
    return render_template('frontindex.html',carname=name, years=year, fuel_type=fuel, seller_type=seller_type,transmission=transmission, owner=owner)


if __name__=='__main__':
    app.run(debug=True)