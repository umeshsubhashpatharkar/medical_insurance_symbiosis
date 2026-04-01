from flask import Flask,render_template,jsonify,request
import config
from Medical_Insurance.utils import MedicalInsurance
import numpy as np

########## initialization of flask
app = Flask(__name__)

######## home api ################
@app.route("/")
def get_homeapi():
    return "we are in HOME API"
    # return render_template("medical_insurance.html")

@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance_charges():
    if request.method == "POST":
        print("we are in POST METHOD")
        data = request.form
        print("data is \n",data)
        gender = data["gender"] # female
        smoker = data["Smoker"]
        children = int(data["children"]) # 5
        region = data["region"]  # northeast
        age = eval(data["age"])  # 57
        bmi = eval(data["bmi"])
        print("age,gender,children,smoker,bmi,region",age,gender,children,smoker,bmi,region)
        ## calling MedicalInsurance class
        med_charges = MedicalInsurance(age,gender,children,smoker,bmi,region)
        charges = med_charges.get_predicted_charges()
        return jsonify({"Result":f"Predicted medical insurnace charges are {np.around(charges[0],2)}"})
    
    
    



if __name__ == "__main__":
    app.run()

