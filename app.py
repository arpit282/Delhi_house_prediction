from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()


app = Flask(__name__)
model = pickle.load(open("random_forest_regression_model.pkl","rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/houseprediction",methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':

        area = request.form["Area"]
        persqft = request.form["persqft"]

        bhk = request.form["BHK"]
        if(bhk == "2"):
            BHK_2 = 1
            BHK_3 = 0
            BHK_4 = 0
            BHK_5 = 0
            BHK_6 = 0
            BHK_7 = 0

        elif(bhk == "3"):
            BHK_2 = 0
            BHK_3 = 1
            BHK_4 = 0
            BHK_5 = 0
            BHK_6 = 0
            BHK_7 = 0

        elif(bhk == "4"):
            BHK_2 = 0
            BHK_3 = 0
            BHK_4 = 1
            BHK_5 = 0
            BHK_6 = 0
            BHK_7 = 0

        elif(bhk == "5"):
            BHK_2 = 0
            BHK_3 = 0
            BHK_4 = 0
            BHK_5 = 1
            BHK_6 = 0
            BHK_7 = 0

        elif(bhk == "6"):
            BHK_2 = 0
            BHK_3 = 0
            BHK_4 = 0
            BHK_5 = 0
            BHK_6 = 2
            BHK_7 = 0

        elif(bhk == "7"):
            BHK_2 = 0
            BHK_3 = 0
            BHK_4 = 0
            BHK_5 = 0
            BHK_6 = 0
            BHK_7 = 1

        else:
            BHK_2 = 0
            BHK_3 = 0
            BHK_4 = 0
            BHK_5 = 0
            BHK_6 = 0
            BHK_7 = 0


        bath = request.form["Bathroom"]
        if(bath == "2"):
            bathroom_2 = 1
            bathroom_3 = 0
            bathroom_4 = 0
            bathroom_5 = 0
            bathroom_6 = 0
            bathroom_7 = 0

        elif(bath == "3"):
            bathroom_2 = 0
            bathroom_3 = 1
            bathroom_4 = 0
            bathroom_5 = 0
            bathroom_6 = 0
            bathroom_7 = 0

        elif(bath == "4"):
            bathroom_2 = 0
            bathroom_3 = 0
            bathroom_4 = 1
            bathroom_5 = 0
            bathroom_6 = 0
            bathroom_7 = 0

        elif(bath == "5"):
            bathroom_2 = 0
            bathroom_3 = 0
            bathroom_4 = 0
            bathroom_5 = 1
            bathroom_6 = 0
            bathroom_7 = 0

        elif(bath == "6"):
            bathroom_2 = 0
            bathroom_3 = 0
            bathroom_4 = 0
            bathroom_5 = 0
            bathroom_6 = 2
            bathroom_7 = 0

        elif(bath == "7"):
            bathroom_2 = 0
            bathroom_3 = 0
            bathroom_4 = 0
            bathroom_5 = 0
            bathroom_6 = 0
            bathroom_7 = 1

        else:
            bathroom_2 = 0
            bathroom_3 = 0
            bathroom_4 = 0
            bathroom_5 = 0
            bathroom_6 = 0
            bathroom_7 = 0

        furnished = request.form["Furnished"]
        if(furnished == "Unfurnished"):
            un = 1
            semi = 0

        elif(furnished == "Semi Furnished"):
            un = 0
            semi = 1

        else:
            un=0
            semi=0

        parking = request.form["Parking"]
        if (parking == "2"):
            park_2 = 1
            park_3 = 0
            park_4 = 0
            park_5 = 0


        elif (parking == "3"):
            park_2 = 0
            park_3 = 1
            park_4 = 0
            park_5 = 0


        elif (parking == "4"):
            park_2 = 0
            park_3 = 0
            park_4 = 1
            park_5 = 0


        elif (parking == "5"):
            park_2 = 0
            park_3 = 0
            park_4 = 0
            park_5 = 1

        else:
            park_2 = 0
            park_3 = 0
            park_4 = 0
            park_5 = 0


        status = request.form["Status"]
        if(status == "Ready"):
            ready_to_move = 1

        else:
            ready_to_move = 0


        transaction = request.form["Transaction"]
        if(transaction == "Resale"):
            sale = 1

        else:
            sale = 0

        type = request.form["Type"]
        if(type == "Builder"):
            build = 1

        else:
            build = 0





        # Area # Price # Per_Sqft  # BHK_2
        # BHK_3 # BHK_4 # BHK_5 # BHK_6 # BHK_7
        # Bathroom_2 # Bathroom_3 # Bathroom_4
        # Bathroom_5 # Bathroom_6  # Bathroom_7
        # Furnishing_Semi - Furnished # Furnishing_Unfurnished
        # Parking_2 # Parking_3 # Parking_4 # Parking_5 # Status_Ready_to_move
        # Transaction_Resale # Type_Builder_Floor

        x = [[area,persqft,BHK_2,BHK_3,BHK_4,BHK_5,BHK_6,BHK_7,bathroom_2,
              bathroom_3,bathroom_4,bathroom_5,bathroom_6,bathroom_7,semi,un,
              park_2,park_3,park_4,park_5,ready_to_move,sale,build]]



        prediction = model.predict(x)

        price_prediction= round(prediction[0],2)

        return render_template('index.html',pred = "Your House Price Prediction is {}".format(price_prediction))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


