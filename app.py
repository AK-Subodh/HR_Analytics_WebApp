import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.preprocessing  import RobustScaler

#filename='scaling_input.pkl'
model = pickle.load(open('voting_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    if request.method == "POST":

        # Number of trainings
        no_trainings = request.form["no_of_trainings"]
        no_trainings=int(no_trainings)

         #Average Training Score
        score_trainings = request.form["avg_training_score"]
        score_trainings=int(score_trainings)

         #Length of Service
        service_length = request.form["length_of_service"]
        service_length=int(service_length)

        #Reegion
        region = request.form["region"]
        region=int(region)
        d = {}
        for x in range(1, 35):
            d["region_region_{0}".format(x)] = 0
        d["region_region_{0}".format(region)]=1
        


        # Previous Year Rating
        rating=request.form['previous_yr_rating']
        if(rating=="5.0"):
            previous_year_rating=5.0
        elif(rating=="4.0"):
            previous_year_rating=4.0
        elif(rating=="3.0"):
            previous_year_rating=3.0
        elif(rating=="2.0"):
            previous_year_rating=2.0
        elif(rating=="1.0"):
            previous_year_rating=1.0
        else:
            previous_year_rating=0.0

        #KPIs met
        kpi=int(request.form['kpi_met'])
        #if(kpi=="1"):
        #    kpi=1
        #elif(kpi=="0"):
        #    kpi=0

        #Awards won
        awards=int(request.form['awards_won'])
        #if(awards=="1"):
         #   awards=1
        #elif(awards=="0"):
         #   awards=0

        #Department
        department=request.form['department']
        if(department=="analytics"):
            department="Analytics"
        elif(department=="finance"):
            department="Finance"
        elif(department=="hr"):
            department="HR"
        elif(department=="legal"):
            department="Legal"
        elif(department=="operations"):
            department="Operations"
        elif(department=="procurement"):
            department="Procurement"
        elif(department=="r&d"):
            department="R_and_D"
        elif(department=="sales&marketing"):
            department="Sales_Marketing"
        elif(department=="technology"):
            department="Technology"
        d1 = {}
        l1=["Analytics","Finance","HR","Legal","Operations","Procurement","R_and_D","Sales_Marketing","Technology"]
        for x in l1:
            d1["department_{0}".format(x)] = 0
        d1["department_{0}".format(department)]=1
        

         #Education
        education=request.form['education']
        if(education=="bachelors"):
            education="Bachelor"
        elif(education=="below_secondary"):
            education="Below_secondary"
        elif(education=="masters&above"):
            education="Master"
        d2 = {}
        l2=["Bachelor","Below_secondary","Master"]
        for x in l2:
            d2["education_{0}".format(x)] = 0
        d2["education_{0}".format(education)]=1
        print('d2:',d2)


         #Recruitment
        recruitment=request.form['recruitment']
        if(recruitment=="referred"):
            recruitment="referred"
        elif(recruitment=="sourcing"):
            recruitment="sourcing"
        elif(recruitment=="other"):
            recruitment="other"
        d3 = {}
        l3=["referred","sourcing","other"]
        for x in l3:
            d3["recruitment_channel_{0}".format(x)] = 0
        d3["recruitment_channel_{0}".format(recruitment)]=1

        
         #Age bin
        age=request.form['age']
        if(age=="20"):
            age="20"
        elif(age=="30"):
            age="30"
        elif(age=="40"):
            age="40"
        d4 = {}
        l4=["20","30","40"]
        for x in l4:
            d4["age_{0}".format(x)] = 0
        d4["age_{0}".format(age)]=1

         #Gender
        gender=request.form['gender']
        if(gender=="m"):
            gender="m"
        elif(gender=="f"):
            gender="f"
        d5 = {}
        l5=["m","f"]
        for x in l5:
            d5["gender_{0}".format(x)] = 0
        d5["gender_{0}".format(gender)]=1
    
        no_of_trainings=no_trainings
        previous_year_rating=previous_year_rating
        length_of_service=service_length
        kpi=kpi
        awards=awards
        avg_training_score=score_trainings
        department_Analytics= d1['department_Analytics']
        department_Finance= d1['department_Finance']
        department_HR=d1['department_HR']
        department_Legal=d1['department_Legal']
        department_Operations=d1['department_Operations']
        department_Procurement=d1['department_Procurement']
        department_R_and_D=d1['department_R_and_D']
        department_Sales_Marketing=d1['department_Sales_Marketing']
        department_Technology=d1['department_Technology']
        education_Bachelor=d2['education_Bachelor']
        education_Below_secondary=d2['education_Below_secondary']
        education_Master=d2['education_Master']
        gender_f=d5['gender_f']
        gender_m=d5['gender_m']
        recruitment_channel_other=d3['recruitment_channel_other']
        recruitment_channel_referred=d3['recruitment_channel_referred']
        recruitment_channel_sourcing=d3['recruitment_channel_sourcing']
        age_20=d4['age_20']
        age_30=d4['age_30']
        age_40=d4['age_40']
        region_region_1=d['region_region_1']
        region_region_2=d['region_region_2']
        region_region_3=d['region_region_3']
        region_region_4=d['region_region_4']
        region_region_5=d['region_region_5']
        region_region_6=d['region_region_6']
        region_region_7=d['region_region_7']
        region_region_8=d['region_region_8']
        region_region_9=d['region_region_9']
        region_region_10=d['region_region_10']
        region_region_11=d['region_region_11']
        region_region_12=d['region_region_12']
        region_region_13=d['region_region_13']
        region_region_14=d['region_region_14']
        region_region_15=d['region_region_15']
        region_region_16=d['region_region_16']
        region_region_17=d['region_region_17']
        region_region_18=d['region_region_18']
        region_region_19=d['region_region_19']
        region_region_20=d['region_region_20']
        region_region_21=d['region_region_21']
        region_region_22=d['region_region_22']
        region_region_23=d['region_region_23']
        region_region_24=d['region_region_24']
        region_region_25=d['region_region_25']
        region_region_26=d['region_region_26']
        region_region_27=d['region_region_27']
        region_region_28=d['region_region_28']
        region_region_29=d['region_region_29']
        region_region_30=d['region_region_30']
        region_region_31=d['region_region_31']
        region_region_32=d['region_region_32']
        region_region_33=d['region_region_33']
        region_region_34=d['region_region_34']

        inp_l=np.array([[no_of_trainings, previous_year_rating, length_of_service, kpi,
        awards, avg_training_score, department_Analytics,
        department_Finance, department_HR, department_Legal,
        department_Operations, department_Procurement, department_R_and_D,
        department_Sales_Marketing, department_Technology,
        region_region_1, region_region_10, region_region_11,
        region_region_12, region_region_13, region_region_14,
        region_region_15, region_region_16, region_region_17,
        region_region_18, region_region_19, region_region_2,
        region_region_20, region_region_21, region_region_22,
        region_region_23, region_region_24, region_region_25,
        region_region_26, region_region_27, region_region_28,
        region_region_29, region_region_3,region_region_30,
        region_region_31, region_region_32, region_region_33,
        region_region_34, region_region_4, region_region_5,
        region_region_6,region_region_7, region_region_8,
        region_region_9, education_Bachelor, education_Below_secondary,
        education_Master, gender_f,gender_m, recruitment_channel_other,
        recruitment_channel_referred, recruitment_channel_sourcing,
        age_20, age_30, age_40]])

       
        print(inp_l)
        t=np.array([[3,5,5,1,0,89,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1]])
        predictions=model.predict_proba(inp_l)[:,1]
        print('Predictions: ',predictions)
        my_prediction=int(round(predictions[0]))

        return render_template('result.html', prediction=my_prediction)



if __name__ == "__main__":
    #from scaling_input import scaling_input
    app.run(debug=True)