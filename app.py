import streamlit as st
import pandas as pd
import numpy as np
import sklearn as sns
import pickle

Status  = {
"New" : 0,"Ready to move" : 1,"Resale" : 2,"Under Construction" : 3,}

Location  = {
"AGIRIPALLI" : 0,"Ajit Singh Nagar" : 1,"Andhra Prabha Colony Road" : 2,"Ashok Nagar" : 3,"Auto Nagar" : 4,"Ayyappa Nagar" : 5,"Bandar Road" : 6,"Benz Circle" : 7,"Bharathi Nagar" : 8,"Bhavanipuram" : 9,"Chennai Vijayawada Highway" : 10,"Currency Nagar" : 11,"Devi Nagar" : 12,"Edupugallu" : 13,"Enikepadu" : 14,"G Konduru" : 15,"Gandhi Nagar" : 16,"Gannavaram" : 17,"Gollapudi" : 18,"Gollapudi1" : 19,"Gosala" : 20,"Governor Peta" : 21,"Gudavalli" : 22,"Gunadala" : 23,"Guntupalli" : 24,"Guru Nanak Colony" : 25,"Ibrahimpatnam" : 26,"Jaggayyapet" : 27,"Kanchikacherla" : 28,"Kandrika" : 29,"Kanigiri Gurunadham Street" : 30,"Kankipadu" : 31,"Kanuru" : 32,"Kesarapalle" : 33,"Kesarapalli" : 34,"LIC Colony" : 35,"Labbipet" : 36,"Madhuranagar" : 37,"Mangalagiri" : 38,"Milk Factory Road" : 39,"Moghalrajpuram" : 40,"Mylavaram" : 41,"MylavaramKuntamukkalaVellaturuVijayawada Road" : 42,"Nandigama" : 43,"Nidamanuru" : 44,"Nunna" : 45,"Nuzividu" : 46,"Nuzvid Road" : 47,"Nuzvid To Vijayawada Road" : 48,"PNT Colony" : 49,"Pamarru" : 50,"Patamata" : 51,"Payakapuram" : 52,"Pedaogirala" : 53,"Pedapulipaka Tadigadapa Road" : 54,"Penamaluru" : 55,"Poranki" : 56,"Punadipadu" : 57,"Rajarajeswari Peta" : 58,"Rajiv Bhargav Colony" : 59,"Rama Krishna Puram" : 60,"Ramalingeswara Nagar" : 61,"Ramavarapadu" : 62,"Ramavarapadu Ring" : 63,"SURAMPALLI" : 64,"Satyanarayanapuram Main Road" : 65,"Satyaranayana Puram" : 66,"Sri Ramachandra Nagar" : 67,"Srinivasa Nagar Bank Colony" : 68,"Subba Rao Colony 2nd Cross Road" : 69,"Tadepalligudem" : 70,"Tadigadapa" : 71,"Tadigadapa Donka Road" : 72,"Tarapet" : 73,"Telaprolu" : 74,"Tulasi Nagar" : 75,"Vaddeswaram" : 76,"Vidhyadharpuram" : 77,"Vijayawada Airport Road" : 78,"Vijayawada Guntur Highway" : 79,"Vijayawada Machilipatnam Road" : 80,"Vijayawada Nuzvidu Road" : 81,"Vijayawada Road" : 82,"Vuyyuru" : 83,"chinnakakani" : 84,"currency nagar" : 85,"krishnalanka" : 86,"kunchanapalli" : 87,"ramavarappadu" : 88,}

Facing  = {
"East" : 0,"None" : 1,"North" : 2,"NorthEast" : 3,"NorthWest" : 4,"South" : 5,"SouthEast" : 6,"SouthWest" : 7,"West" : 8,}

Type  = {
"Apartment" : 0,"Independent Floor" : 1,"Independent House" : 2,"Residential Plot" : 3,"Studio Apartment" : 4,"Villa" : 5,}


model =pickle.load(open('House_Price.pkl','rb'))

#creating the function to accept inputs and creating an 2d array and predicting the result.

def predict(bedrooms,bathrooms,status,size,location,facing,Types):
    """function to accept the values"""
    selected_location=Location[location]
    selected_status = Status[status]
    selected_facing=Facing[facing]
    selected_type = Type [Types] 

    user_input = np.array([[bedrooms,bathrooms,selected_status,size,selected_location,selected_facing,selected_type]])

    result = model.predict(user_input)[0].round(2)
    return result

if __name__=="__main__":
    st.header("House Price Prediction")
    col1,col2 = st.columns([2,1])
    bedrooms = col1.slider("No. of Bedrooms",max_value=10,min_value=1)
    bathrooms = col1.slider("No. of Bathrooms",max_value=10,min_value=1)
    status = col1.selectbox("Select status:",list(Status.keys()))
    size = col2.number_input("Enter SQFT:",min_value=500,max_value=10000,value=1000,step=500)
    location = col2.selectbox("Select Location:",list(Location.keys()))
    facing = col2.selectbox("Select Facing:",list(Facing.keys()))
    Types = col1.selectbox("Select Type:",list(Type.keys()))
    result = predict(bedrooms,bathrooms,status,size,location,facing,Types)
    submit_button = st.button("Predict")
    if submit_button:
        larger_text=f"<h2 style='color:#ff1111;'>The Predicted Price is: {result} Thousand</h2>"
        st.markdown(larger_text,unsafe_allow_html=True)