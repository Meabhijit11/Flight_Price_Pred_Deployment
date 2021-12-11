from flask import Flask, request, render_template
import pickle as pk
import numpy as np

# Flask constructor
application = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@application.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        Total_Stops = request.form.get("Total_Stops")
        # getting input with name = lname in HTML form
        Month = request.form.get("Month")
        Day = request.form.get("Day")
        Dep_hour = request.form.get("Dep_hour")
        Dep_min = request.form.get("Dep_min")
        Duration_hours = request.form.get("Duration_hours")
        Duration_mins = request.form.get("Duration_mins")
        Arrival_hr = request.form.get("Arrival_hr")
        Arrival_min = request.form.get("Arrival_min")
        Airline = request.form.get("Airline")
        Source = request.form.get("Source")
        Destination = request.form.get("Destination")

        filename = 'flight_price_rf.pk'
        loaded_model = pk.load(open(filename, 'rb'))
        if Source == "Chennai":
            ch = 1
            de = 0
            kol = 0
            mum = 0
        elif Source == 'Delhi':
            ch = 0
            de = 1
            kol = 0
            mum = 0
        elif Source == 'Kolkata':
            ch = 0
            de = 0
            kol = 1
            mum = 0
        else:
            ch = 0
            de = 0
            kol = 0
            mum = 1

        if Destination == "Cochin":
            coc=1;
            delhi=0;
            hy=0;
            kolk=0;
            nd=0;
        elif Destination == "Delhi":
            coc=0;
            delhi=1;
            hy=0;
            kolk=0;
            nd=0;
        elif Destination == "Hyderabad":
            coc=0;
            delhi=0;
            hy=1;
            kolk=0;
            nd=0;
        elif Destination== "Kolkata":
            coc=0;
            delhi=0;
            hy=0;
            kolk=1;
            nd=0;
        else:
            coc=0;
            delhi=0;
            hy=0;
            kolk=0;
            nd=1;

        if Airline == "Air India":
            air=1;
            ga=0;
            ig=0;
            ja=0;
            jab=0;
            mul=0;
            mulp=0;
            sj=0;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline == "GoAir":
            air=0;
            ga=1;
            ig=0;
            ja=0;
            jab=0;
            mul=0;
            mulp=0;
            sj=0;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline == "IndiGo":
            air=0;
            ga=0;
            ig=1;
            ja=0;
            jab=0;
            mul=0;
            mulp=0;
            sj=0;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline== "Jet Airways":
            air=0;
            ga=0;
            ig=0;
            ja=1;
            jab=0;
            mul=0;
            mulp=0;
            sj=0;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline == "Jet Airways Business":
            air=0;
            ga=0;
            ig=0;
            ja=0;
            jab=1;
            mul=0;
            mulp=0;
            sj=0;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline == "Multiple carriers":
            air=0;
            ga=0;
            ig=0;
            ja=0;
            jab=0;
            mul=1;
            mulp=0;
            sj=0;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline== "Multiple carriers Premium economy":
            air=0;
            ga=0;
            ig=0;
            ja=0;
            jab=0;
            mul=0;
            mulp=1;
            sj=0;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline== "SpiceJet":
            air=0;
            ga=0;
            ig=0;
            ja=0;
            jab=0;
            mul=0;
            mulp=0;
            sj=1;
            tj=0;
            vi=0;
            vpe=0;
        elif Airline== "Trujet":
            air=0;
            ga=0;
            ig=0;
            ja=0;
            jab=0;
            mul=0;
            mulp=0;
            sj=0;
            tj=1;
            vi=0;
            vpe=0;
        elif Airline== "Vistara":
            air=0;
            ga=0;
            ig=0;
            ja=0;
            jab=0;
            mul=0;
            mulp=0;
            sj=0;
            tj=0;
            vi=1;
            vpe=0;
        else:
            air=0;
            ga=0;
            ig=0;
            ja=0;
            jab=0;
            mul=0;
            mulp=0;
            sj=0;
            tj=0;
            vi=0;
            vpe=1;

        predictionresult = loaded_model.predict([[Total_Stops,Month,Day,Dep_hour,Dep_min,Duration_hours,Duration_mins,Arrival_hr,Arrival_min,air,ga,ig,ja,jab,mul,mulp,sj,tj,vi,vpe,ch,de,kol,mum,coc,delhi,hy,kolk,nd]])
        # print("Prediction is ",predictionresult)
        return "Flight Price Prediction is " + str(np.round(predictionresult[0],decimals=2)) + "  Rupees"
    return render_template("index.html")


if __name__ == '__main__':
    application.run(debug=True)

# int(np(predictionresult[0]))