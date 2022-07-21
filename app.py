import streamlit as st
import pandas as pd
import numpy as np

#Setting the page configuration to wide mode
st.set_page_config(layout="wide")

# Giving an interesting name to our app


def display_single_record(df1):
    col1,col2,col3=st.columns([1,3,2])
    with col1:
       #Gender
        st.subheader("Gender")
        s=df1['GENDER']

        if(s[0]=='M'):
            st.text("Male")
        else:
            st.text("Female")

        #Age
        st.subheader("Age")
        st.text(f"{df1['AGE'][0]} Years")

        #Admission Date
        st.subheader("Admission Date")
        st.text(f"{df1['ADM_DATE'][0]}")

        #Discharge Date

        st.subheader("Discharge Date")
        st.text(f"{df1['DIS_DATE'][0]} ")

        #Blood group , weight and height

        st.subheader("Blood Type")
        b=str(df1["INV"].values[0])
        #Blood group   -   B positive
        st.write(b.split("-")[1])

    with col2:
        st.subheader("Proc")
        st.info(str(df1['PROC'].values[0]))

        st.subheader("Note type")
        st.write(df1['NOTE_TYPE'].values[0])

        st.subheader("History")
        st.warning(df1['HISTORY'].values[0])

        st.subheader("Past Surgery")
        sg=str(df1['PAST_SURG'].values[0])
        if(sg=="nan"):
            st.write("None")
        else:
            st.write(sg)



    with col3:
        #Diagnosis
        st.subheader("Diagnosis")
        st.success(df1['DIAG'].values[0])

        #Hospital course
        st.subheader("Hospital Course")
        st.error(df1['HOSPITAL_COURSE'].values[0])




df = pd.read_excel('DATA_SEARCH_SAMPLE.xls')

side=st.sidebar
sd=side.selectbox("Portal",['Patient','Management'])
if(sd=='Patient'):
    st.title("Patient Portal")
    st.text("Check your reports")
    pat_id = st.text_input("Patient Id", value="ZYNNGCDHBD")
    df1 = df.loc[df['PAT_ID'] == pat_id]
    if (len(df1) > 0):
        display_single_record(df1)
    else:
        #if df1 has 0 rows
        st.error("No record")

else:
    st.title("Hospital Management")
    st.subheader("Authenticate to continue")
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")

    username_dummy=["rick@gmail.com","ron@yahoo.com","tara@gmail.com","saketsingh2@gmail.com"]

    password_dummy=["2345","6578","1234","4567"]

    b=-99


    for i in range(0,len(username_dummy),1):
        if(username==username_dummy[i]):
            if(password==password_dummy[i]):
                st.success("Permission Granted")
                b=1
                break
    if(b!=1):
        st.error("Permission Denied")

    else:
        # s=st.checkbox("Show sample of records")
        # if(s):
        #     st.write(df.sample(10))
        st.header("Filter by Admission Date")
        col1,col2=st.columns(2)
        with col1:
            from_date=st.date_input("From")
        with col2:
            to_date = st.date_input("To")
        df['ADM_DATE'] = pd.to_datetime(df['ADM_DATE']).dt.date
        df_filter_adm=df.loc[(df['ADM_DATE']>from_date)&(df['ADM_DATE']<to_date)]
        st.write(df_filter_adm)

        #Hlw to do the same for discharge date
        st.header("Filter by Discharge Date")
        col1,col2=st.columns(2)
        with col1:
            from_date=st.date_input("From",key=2)
        with col2:
            to_date = st.date_input("To",key=3)
        df['DIS_DATE'] = pd.to_datetime(df['DIS_DATE']).dt.date
        df_filter_dis=df.loc[(df['DIS_DATE']>from_date)&(df['DIS_DATE']<to_date)]
        st.write(df_filter_dis)

        # to crate another section
        # -- we can sort the excel file by date( admission date and discharge date)

        #To create a filter based on to and from
        #Filter based on the diagnosis

        st.header("Filter by Diagnosis")
        search=st.text_input("Search")
        diag_list=df['DIAG']
        for i in range(0,len(diag_list)):
            f=str(diag_list[i]).find(search)
            if(f!=-1):
                st.write(df.iloc[[i]])
