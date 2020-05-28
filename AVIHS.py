# Import Libraries
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from email.message import EmailMessage
import datetime as datetime
import smtplib
import imghdr
import seaborn as sns
import cv2
import os
import streamlit as st
import altair as alt


# Main function
def main():

    # Create Sidebar
    st.sidebar.title("Avihs Technologies")
    st.sidebar.subheader("Analytics/Automation Platform")
    sdbar_select = st.sidebar.radio("What service do you want to use today",
                                    ["Internet Leased Line", "Email Automation", "Whatsap Automation"])

    # ILL Landing page
    if sdbar_select == "Internet Leased Line":
        st.title("Howdy!! Welcome to ILL Analytics World")
        img = mpimg.imread("Avihs1.jpg")
        st.image(img, width=700)

    # Upload the file
        data = st.file_uploader("Upload the file", type=["csv", "txt", "xls"])
        if data is not None:
            df = pd.read_csv(data)
            if st.checkbox("Check if database is loaded"):
                if st.dataframe(df.head()):
                    st.success("Loading Suceess")

                df['FAN Creation Date'] = pd.to_datetime(
                    df['FAN Creation Date'], format='%Y-%m-%d %H:%M:%S')
                df = df.sort_values(by='FAN Creation Date', ascending=False)
                df_new = df[df["Point A City"] == "BANGALORE"]
                df_new = df_new[df["Location"] != "BANGALORE"]
                df_new["Bandwidth"] = df_new["Bandwidth"].str.replace(
                    "Mbps", "")
                if st.checkbox("Fetch Probable Leads"):
                    number = st.slider(
                        "How many latest enties required?", 1, len(df_new))
                    st.dataframe(df_new.head(number))

                    if st.checkbox("Top Company names based on Bandwidth"):
                        st.info(
                            "These leads are published based on high Bandwidth requirements")
                        number = st.number_input(
                            "Choose the count you want to view", 1, len(df_new))
                        top_ten = df_new.head(number)
                        top_ten = top_ten[["Company Name", "Bandwidth"]]
                        top_ten['Bandwidth'] = pd.to_numeric(
                            top_ten["Bandwidth"])
                        top_ten.sort_values(
                            by="Bandwidth", ascending=False, inplace=True)
                        top_ten.reset_index(drop=True, inplace=True)

                        # alt.Chart(top_ten).mark_bar().encode(
                        #     x='Bandwidth', y='Company Name')
                        # st.altair_chart(alt.Chart(top_ten).mark_bar().encode(
                        #     x=alt.X('Bandwidth'), y='Company Name'), sort=None)

                        st.altair_chart(alt.Chart(top_ten).mark_bar().encode(
                            x='Bandwidth',
                            y=alt.Y('Company Name', sort='-x')
                        ))
                        st.dataframe(top_ten)

                        # Download file
                        # import base64

                        # def get_table_download_link(df):
                        #     csv = df.to_csv('final.csv', index=False)
                        #     b64 = base64.b64encode(csv.encode()).decode()
                        #     href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'

                        # st.markdown(get_table_download_link(
                        #     dt), unsafe_allow_html=True)

    if sdbar_select == "Email Automation":
        st.title("Hi! Welcome to Email Automation Center")
        img = mpimg.imread("Avihs2.jpg")
        st.image(img, width=700)
        if st.checkbox("Insert Email Id's"):
            contacts = st.text_area("")
            if st.button("Send Email"):
                msg = EmailMessage()
                msg['Subject'] = "This an automated email"
                msg['From'] = 'lohith.udemy@gmail.com'
                msg['To'] = ", ".join(contacts)
                msg.set_content("This is the body of an email")

                # For pdf create lst on similar line
                files = ['Avihs1.jpg', 'waymo_car.jpg']

                for file in files:
                    with open('Avihs1.jpg', 'rb') as f:
                        file_data = f.read()
                        # No need of file_type for pdf
                        file_type = imghdr.what(f.name)
                        file_name = f.name

                        # For pdf, maintype="application" & subtype='octet-stream'
                        msg.add_attachment(file_data, maintype='image',
                                           subtype=file_type, filename=file_name)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login('lohith.udemy@gmail.com', 'SSingapore123')
                    smtp.send_message(msg)

    if sdbar_select == "Whatsap Automation":
        st.title("Hello!! Welcome to Whatsap Automation")
        img = mpimg.imread("Avihs3.jpg")
        st.image(img, width=700)

        st.text_area("Enter phone numbers")
        st.button("Send")

        # import webbrowser
        # import time
        # import pyautogui as gui

        # interval = 2
        # position = 1022, 231
        # numbers = {917025674097, 919048525224}

        # message = "Automated message"

        # for i in numbers:
        #     url = 'https://wa.me/{}?text={}'.format(i, message)
        #     webbrowser.open(url)
        #     time.sleep(3)
        #     gui.click(position)
        #     time.sleep(3)
        #     gui.press('enter')
        #     time.sleep(interval)


if __name__ == '__main__':
    main()
