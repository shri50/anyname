from flask import Flask,render_template,request
import numpy as np
import pickle 

model = pickle.load(open('model1.pkl','rb'))

app = Flask('__name__')


@app.route('/')
def base():

    
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def placement():
    """ Prediction logic for student placement """
    cgpa = float(request.form.get('cgpa_index'))
    iq = int(request.form.get('iq_index'))
    profile_score = int(request.form.get('profile_score_index'))
    


   

    result = model.predict(np.array([cgpa,iq,profile_score]).reshape(1,3))
    # print(result)


    if result[0] == 1:
        final_result = "Student Placed"
    else:
        final_result ="Not Placed"


    return render_template('index.html',prediction = final_result )

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)