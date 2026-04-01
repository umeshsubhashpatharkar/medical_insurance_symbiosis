import pickle
import json
import config
import numpy as np


class MedicalInsurance():
    def __init__(self,age,gender,children,smoker,bmi,region):
        self.age = age  # 57
        self.gender = gender # female
        self.children = children # 5
        self.smoker = smoker
        self.bmi = bmi
        self.region = region  # northeast

    
    def load_model(self):
        ################ read model ####################
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file) 
        ################ read project data ####################
        with open(config.JSON_FILE_PATH,"r") as file:
             self.json_data = json.load(file)

        ################ scalar model ####################
        with open(config.STD_FILE_PATH,"rb") as file:
             self.std_scalar_model = pickle.load(file)


    def get_predicted_charges(self):
        # call model and project data using user defined function
        self.load_model()
    
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.json_data["gender"][self.gender]     # female =1
        test_array[1] = self.children
        test_array[2] = self.json_data["smoker"][self.smoker]     # yes =1,no=0
        region_index = self.json_data["columns"].index(self.region)
        test_array[region_index] = 1
        test_array[7] = (0 if self.age < 19 else 
                        1 if 19<= self.age < 31 else
                        2 if 31<= self.age <46 else
                        3 if 46<= self.age <61 else
                        4 )
        test_array[8] = (0 if self.bmi <= 18.5 else 
                        1 if 18.5< self.bmi <= 24.5 else
                        2 if 24.5< self.bmi <= 30.5 else
                        3  )
        # std_array = self.std_scalar_model.transform([test_array]) # it must be 2 D
        pred_charges = self.model.predict([test_array]) # this already in 1D  so added EXTRA 1 D
        
        return pred_charges