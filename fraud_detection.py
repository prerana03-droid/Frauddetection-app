import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Fraud_detection_model.pkl")


st.title("Fraud Detection Prediction app")

st.markdown("Enter the transaction details and click the predict button")

st.divider()

transaction_type = st.selectbox("Transaction type",["PAYMENT","TRANSFER","CASH_OUT","CASH_IN","DEBIT"])
amount = st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Reciever)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Reciever)", min_value=0.0, value=0.0)

#st.write("Model type:", type(model))

if st.button("Predict"):
    # Prepare input data as DataFrame
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

# Run prediction
    prediction = model.predict(input_data)[0]
    print(input_data)
    print(prediction)

    # Display result
    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("🚨 This transaction **may be fraudulent**.")
    else:
        st.success("✅ This transaction looks **legitimate**.")

