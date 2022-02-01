# Core packages
from http.client import ImproperConnectionState
from google.protobuf.symbol_database import Default
import streamlit as st
import seaborn as sns
import pandas as pd


# Additional packages


# Fxns


def main():
    """All main code goes here"""

    # Configure page title
    st.set_page_config(
        page_title="Rakuten Radio Analytics",
        page_icon="https://cdn-bnpne.nitrocdn.com/oaKpnkVSVvzIewntLhNHVuPbygaYweqt/assets/static/optimized/rev-89e43b2/wp-content/uploads/2019/12/Rakuten-icon.jpeg",
        initial_sidebar_state="collapsed",
    )

    st.sidebar.title("Tab_1")

    # Working with text
    st.header("Header")
    st.subheader("Subheader")
    st.title("Title")
    st.text("Text")
    st.markdown("Markdown")

    # Working with alerts
    st.success("Success")
    st.warning("Warning")
    st.info("Info")
    st.error("Error")
    st.exception("Exception")

    # Super function
    st.write("# One hashtag")
    st.write("## Two hashtag")
    st.write("### Three hashtag")
    st.write(3 + 2)
    st.help(range)

    # Dataframe display & download
    df = sns.load_dataset("iris")
    st.dataframe(df)

    st.download_button(label="Download file", data=df.to_csv(), mime="text/csv")

    # Columns widget
    col1, col2 = st.columns(2)
    # pass [3,2] if u want to vary size of container
    with col1:
        st.info("Left")
        st.write(
            "end, each comprising two bails balanced on three stumps. The game proceeds when a player on the fielding team, called the bowler,  (propels) the ball from one end of the pitch towards the wicket at the other end. The batting side's players score runs by striking the bowled ball with a bat and running between the wickets, while the bowling side tries to prevent this by keeping the ball within the field and getting it to either wicket, and dismiss each batter (so they are ). Means of dismissal include being bowled, when the ball hits the stumps and dislodges the bails, and by the fielding side either catching a hit ball before it touches the ground, or hitting a wicket with the ball before a "
        )

    with col2:
        st.success("Right")
        st.write(
            "The earliest reference to cricket is in South East England in the mid-16th century. It spread globally with the expansion of the British Empire, with the first international matches in the second half of the 19th century. The game's governing body is the International Cricket Council (ICC), which has over 100 members, twelve of which are full members who play Test matches. The game's rules, the Laws of Cricket, are maintained by Marylebone Cricket Club (MCC) in London. The sport is followed primarily in South Asia, Australasia, the United Kingdom, southern Africa and the West Indies.[1] Women's cricket, which is organised and played separately, has also achieved internat"
        )

    # st.table(df)

    # Dataframe styling
    # include $ symbol
    st.dataframe(df.head(10).style.format({"sepal_length": "${:20,.2f}"}))
    # convert series to lower case
    st.dataframe(df.head(10).style.format({"species": lambda x: x.upper()}))
    # highlight max and min values
    st.dataframe(
        df.head(5)
        .style.highlight_max(color="lightgreen")
        .highlight_min(color="#cd4f39")
    )
    # background gradient
    st.dataframe(df.head(5).style.background_gradient(cmap="Blues"))
    # changing multiple properties
    st.dataframe(
        df.head(10).style.set_properties(
            **{
                "background-color": "black",
                "color": "lawngreen",
                "border-color": "white",
            }
        )
    )
    # bar chart to values
    st.dataframe(
        df.head(5)
        .style.bar(subset=["sepal_length",], color="lightgreen")
        .bar(subset=["sepal_width"], color="#ee1f5f")
        .bar(subset=["petal_length"], color="#FFA07A")
    )
    # highlight null values
    st.dataframe(df.head(5).style.highlight_null(null_color="green"))
    # set value for none with color
    st.dataframe(
        df.head(5).style.set_na_rep("OutofScope").highlight_null(null_color="orange")
    )

    # Apply color based on condition
    # def color_negative_red(value):
    #     if value < 0:
    #         color = 'red'
    #     elif value > 0:
    #         color = 'green'
    #     else:
    #         color = 'black'

    #     return 'color: %s' % color

    # df.style.applymap(color_negative_red, subset=['total_amt_usd_diff','total_amt_usd_pct_diff'])

    # Multiple submit buttons with same name
    name1 = "Lohith"
    name2 = "Supriya"
    if st.button("Submit"):
        st.write(f"Name is {name1}")

    if st.button("Submit", key="nm01"):
        st.write(f"Name is {name2}")

    # Radio buttons
    status = st.radio("Select type", ("type_1", "type_2"))
    if status == "type_1":
        st.success("Great job")
    elif status == "type_2":
        st.warning("Try again")

    # Checkbox
    if st.checkbox("show/hide"):
        st.success("Great job")

    # Expander widget
    if st.expander("Show/hide expander"):
        st.success("Great job")

    # select widget
    lang = ["None", "python", "Julia", "C"]
    lang_slct = st.selectbox("Select language", lang, Default == "None")
    st.write(f"selected language is {lang_slct}")

    # Multiselect widget
    lang_1 = ["None_1", "python_1", "Julia_1", "C_1"]
    lang_slct_1 = st.multiselect("Select language", lang_1, default="None_1")
    st.write(f"selected language is {lang_slct_1}")

    # Slider widget
    st.slider("Age", 1, 100, 10)

    # Images
    st.image(
        "https://mma.prnewswire.com/media/949195/Rakuten_Logo.jpg?p=publish",
        use_column_width=True,
    )

    # Video
    st.video("https://youtu.be/Hd2xpPRE2eo", start_time=1)

    # Text input
    st.text_input("Enter the text")
    st.text_input("Enter the password", type="password")

    st.text_area("Enter the text here", height=100)

    # Number input
    st.number_input("Enter the number", 1, 20, 5)

    # Date and time input
    st.date_input("Select the date")
    st.time_input("Select the time")

    # Color picker
    color = st.color_picker("Pls pick the color")
    st.write(color)

    # File upload single and multiple files
    st.file_uploader("Upload the file here", type=["csv", "xls"])
    st.file_uploader(
        "Upload the file here", type=["csv", "xls"], accept_multiple_files=True
    )

    # Forms
    with st.form(key="Salary_form", clear_on_submit=True):
        cl_1, cl_2, cl_3 = st.columns([3, 2, 1])

        with cl_1:
            years = st.number_input("Enter number of years")

        with cl_2:
            salary = st.number_input("Enter salary")

        with cl_3:
            st.text("Savings")
            submit_vlaue = st.form_submit_button("Submit")

    if submit_vlaue:
        with st.expander("results"):
            savings = [years * salary]
            df = pd.DataFrame({"Total_savings": savings})
            st.dataframe(df.T)

    # Progress bar
    # progress_bar = st.sidebar.progress(0)
    # for i in range(100):
    #     progress_bar.progress(i)
    #     time.sleep(0.05)

    # Append link
    st.write("[Learn More >](https://pythonandvba.com)")

    # Stop the flow of app to debug
    # st.stop()

    # Adding animations
    # import streamlit as st
    # from streamlit_lottie import st_lottie
    # import requests
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # import seaborn as sns

    # def load_lottieurl(url: str):
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return None
    #     return r.json()

    # lottie_penguin = load_lottieurl(
    #     "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json"
    # )
    # st_lottie(lottie_penguin, speed=1.5, width=800, height=400)

    # Pandas profiling

    #     penguin_file = st.file_uploader('Select Your Local Penguins CSV')
    # if penguin_file is not None:
    #      penguins_df = pd.read_csv(penguin_file)
    # else:
    #      penguins_df = pd.read_csv('penguins.csv')
    # sns.set_style('darkgrid')
    # markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
    # fig, ax = plt.subplots()
    # ax = sns.scatterplot(data = penguins_df, x = selected_x_var,
    #   y = selected_y_var, hue = 'species', markers = markers,
    #   style = 'species')
    # plt.xlabel(selected_x_var)
    # plt.ylabel(selected_y_var)
    # plt.title("Scatterplot of Palmer's Penguins")
    # st.pyplot(fig)
    # st.title('Pandas Profiling of Penguin Dataset')
    # penguin_profile = ProfileReport(penguins_df, explorative=True)
    # st_profile_report(penguin_profile)

    # write container and draw line inbetween them
    with st.container():
        st.subheader("Hi, I am Sven :wave:")
        st.title("A Data Analyst From Germany")
        st.write(
            "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
        )
        st.write("[Learn More >](https://pythonandvba.com)")

    with st.container():
        st.write("---")


if __name__ == "__main__":
    main()

