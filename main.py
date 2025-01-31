import streamlit as st
from evaluation_helper import print_proper_output,predict

st.title("Car Evaluation App")

st.header("This app helps you to evaluate your car condition depending on various paramters",divider="red")

row1 = st.columns(3)
row2 = st.columns(3)


with row1[0]:
    buying = st.selectbox("Choose Your Buying Price",options=["vhigh","high","med","low"])
with row1[1]:
    maint = st.selectbox("Choose maintainence cost",options=["vhigh","high","med","low"])
with row1[2]:
    doors = st.selectbox("Enter number of doors", options=[2,3,4,"5more"])

with row2[0]:
    persons = st.selectbox("Enter number of occupancy in car", options=[2,4,"more"])
with row2[1]:
    lug_boot = st.selectbox("Enter Bootspace in your car", options=["small","med","big"])
with row2[2]:
    safety = st.selectbox('Choose safety features', options=["low","med","high"])


input_dict = {
    "buying" : buying,
    "maint" : maint,
    "doors" : doors,
    "persons" : persons,
    "lug_boot" : lug_boot,
    "safety" : safety,
}


# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    output = print_proper_output(prediction)
    st.success(f'Predicted Condition of your car: {output}')
    st.balloons()

st.sidebar.title("App Information")
st.sidebar.markdown("---")
st.sidebar.info("A simple ML-powered car condition prediction app.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
