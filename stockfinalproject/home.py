import streamlit as st

st.set_page_config(
    page_title = "Home"
)

st.title(":green[Stock Price Predication Projects]")
st.sidebar.success("Select a demo above.")
st.sidebar.markdown("# :blue[Company name]")
st.sidebar.markdown("## :green[Banana SoftInfoTech]")

url = "https://bananasit.com"
st.sidebar.markdown(f"{url}")

def main():
    st.write('Welcome to the Stock Price Prediction Projects! The project aim to :gray["visualize historical stock data, explore technical indicators, and predict future stock prices using machine learning models."]')


    st.header(':blue[Features:]')
    st.markdown("""
    - **:red[Visualize Data:]** Explore historical stock price data using interactive charts.
    - **:red[Technical Indicators:]** View various technical indicators such as Bollinger Bands, MACD, RSI, etc.
    - **:red[Predictions:]** Predict future stock prices using machine learning models.
    """)
    
    st.header(':blue[How to Use:]')
    st.markdown("""
    1. **:red[Select Stock Symbol:]** Enter the stock symbol of the company you're interested in.
    2. **:red[Choose Date Range:]** Select the date range for which you want to analyze the stock data.
    3. **:red[Explore Visualizations:]** Visualize historical data and technical indicators.
    4. **:red[Make Predictions:]** Choose a machine learning model and predict future stock prices.
    """)

    st.markdown("""
                    ## :blue[Author:]
                    ### Khusbu Champaneria""")
    st.image("pages\WhatsApp Image 2024-03-17 at 9.57.56 PM.jpeg", width=200)

    st.write("I was created by :red[stock price projects]  by under guidance of :red[Dr.Rona Panchal].")
    st.write("I would like to thank :red[Dr.Ronak panchal]  for her valuable guidance and support throughout the project.")

    


if __name__ == '__main__':
    main()






