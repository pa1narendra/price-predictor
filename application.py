from flask import Flask,request,render_template
import numpy as np
import pickle

#loading the model pickle file
model=pickle.load(open('House_Price.pkl','rb'))

application = Flask(__name__)

Status  = {
"New" : 0,"Ready to move" : 1,"Resale" : 2,"Under Construction" : 3,}

Location  = {
"AGIRIPALLI" : 0,"Ajit Singh Nagar" : 1,"Andhra Prabha Colony Road" : 2,"Ashok Nagar" : 3,"Auto Nagar" : 4,"Ayyappa Nagar" : 5,"Bandar Road" : 6,"Benz Circle" : 7,"Bharathi Nagar" : 8,"Bhavanipuram" : 9,"Chennai Vijayawada Highway" : 10,"Currency Nagar" : 11,"Devi Nagar" : 12,"Edupugallu" : 13,"Enikepadu" : 14,"G Konduru" : 15,"Gandhi Nagar" : 16,"Gannavaram" : 17,"Gollapudi" : 18,"Gollapudi1" : 19,"Gosala" : 20,"Governor Peta" : 21,"Gudavalli" : 22,"Gunadala" : 23,"Guntupalli" : 24,"Guru Nanak Colony" : 25,"Ibrahimpatnam" : 26,"Jaggayyapet" : 27,"Kanchikacherla" : 28,"Kandrika" : 29,"Kanigiri Gurunadham Street" : 30,"Kankipadu" : 31,"Kanuru" : 32,"Kesarapalle" : 33,"Kesarapalli" : 34,"LIC Colony" : 35,"Labbipet" : 36,"Madhuranagar" : 37,"Mangalagiri" : 38,"Milk Factory Road" : 39,"Moghalrajpuram" : 40,"Mylavaram" : 41,"MylavaramKuntamukkalaVellaturuVijayawada Road" : 42,"Nandigama" : 43,"Nidamanuru" : 44,"Nunna" : 45,"Nuzividu" : 46,"Nuzvid Road" : 47,"Nuzvid To Vijayawada Road" : 48,"PNT Colony" : 49,"Pamarru" : 50,"Patamata" : 51,"Payakapuram" : 52,"Pedaogirala" : 53,"Pedapulipaka Tadigadapa Road" : 54,"Penamaluru" : 55,"Poranki" : 56,"Punadipadu" : 57,"Rajarajeswari Peta" : 58,"Rajiv Bhargav Colony" : 59,"Rama Krishna Puram" : 60,"Ramalingeswara Nagar" : 61,"Ramavarapadu" : 62,"Ramavarapadu Ring" : 63,"SURAMPALLI" : 64,"Satyanarayanapuram Main Road" : 65,"Satyaranayana Puram" : 66,"Sri Ramachandra Nagar" : 67,"Srinivasa Nagar Bank Colony" : 68,"Subba Rao Colony 2nd Cross Road" : 69,"Tadepalligudem" : 70,"Tadigadapa" : 71,"Tadigadapa Donka Road" : 72,"Tarapet" : 73,"Telaprolu" : 74,"Tulasi Nagar" : 75,"Vaddeswaram" : 76,"Vidhyadharpuram" : 77,"Vijayawada Airport Road" : 78,"Vijayawada Guntur Highway" : 79,"Vijayawada Machilipatnam Road" : 80,"Vijayawada Nuzvidu Road" : 81,"Vijayawada Road" : 82,"Vuyyuru" : 83,"chinnakakani" : 84,"currency nagar" : 85,"krishnalanka" : 86,"kunchanapalli" : 87,"ramavarappadu" : 88,}

Facing  = {
"East" : 0,"None" : 1,"North" : 2,"NorthEast" : 3,"NorthWest" : 4,"South" : 5,"SouthEast" : 6,"SouthWest" : 7,"West" : 8,}

Type  = {
"Apartment" : 0,"Independent Floor" : 1,"Independent House" : 2,"Residential Plot" : 3,"Studio Apartment" : 4,"Villa" : 5,}

def predict(bedrooms,bathrooms,status,size,location,facing,Types):
    """Function to accept the values"""
    selected_location = int(location)
    selected_status = int(status)
    selected_facing = int(facing)
    selected_type = int(Types)
    user_input=np.array([[bedrooms,bathrooms,selected_status,size,selected_location,selected_facing,selected_type]])
    result=model.predict(user_input)[0].round(2)
    return result

@application.route('/')
def index():
    return render_template('index.html',Status=Status,Location=Location,Facing=Facing,Type=Type)

@application.route('/predict',methods=['post'])
def result():
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    status = int(request.form['status'])
    size = int(request.form['area'])
    location = int(request.form['location'])
    facing = int(request.form['facing'])
    Types = int(request.form['type'])

    user_input=np.array([[bedrooms,bathrooms,status,size,location,facing,Types]])
    result=model.predict(user_input)[0].round(2)
    return render_template('index.html',prediction=result,Status=Status,Location=Location,Facing=Facing,Type=Type)

if __name__=="__main__":
    application.run(use_reloader=True,debug=True)