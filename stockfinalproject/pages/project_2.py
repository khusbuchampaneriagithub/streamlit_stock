# Link here :
#https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt
 
import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
import pandas as pd
import ta
#App title
st.markdown('''
# :green[Stock Price Information Using Machine Learning]
Shown are the stock price dat for query companies!

**Credits**\n
-App built by :blue[Khusbu Champaneria] \n
-Built in :blue[Python] using :blue[streamlit] , :blue[yfinance] , :blue[pandas] , :blue[cufflinks] and  :blue[datetime.]
 ''')
st.write('---')

#sidebar
st.sidebar.subheader("Query Parameters")
start_date=st.sidebar.date_input("Start Date",datetime.date(2023,11,4))
end_date=st.sidebar.date_input("End Date",datetime.date(2024,1,5))

# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date,) #get the historical prices for this ticker
#st.info(tickerDf)

#Ticker information
#string_logo = '<img src=%s>' % tickerData.info['logo_url']
#st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)


# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

pricing_data,fundamental_data, news=st.tabs(["Pricing_data","Fundamental_data","Top 10 news"])

with pricing_data:
    st.header("Price Movements")
    tickerDf1=tickerDf
    tickerDf1['% Change']= tickerDf['Close'] / tickerDf['Close'].shift(1)-1
    tickerDf1.dropna(inplace=True) 
    st.write(tickerDf)
    annual_return=tickerDf1['% Change'].mean()*252*100
    st.write("Annual Return is",annual_return,'%')
    stdev = np.std(tickerDf1['% Change'])*np.sqrt(252)
    st.write('Standard duration is',stdev*100,"%")
    st.write("Risk Close. Return is",annual_return/(stdev*100))

from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    st.write("Fundamental")
    key="GH5883864ZSNUUNA"
    fd=FundamentalData(key,output_format="pandas") 
    st.subheader("Balance sheet")
    balance_sheet = fd.get_balance_sheet_annual(tickerSymbol)[0]
    bs = balance_sheet.T[2:]
    bs.columns=list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader("Income Statement")
    income_statement = fd.get_income_statement_annual(tickerSymbol)[0]
    is1=income_statement.T[2:]
    is1.columns=list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader("Cash Flow Statement")
    cash_flow = fd.get_cash_flow_annual(tickerSymbol)[0]
    cf=cash_flow.T[2:]
    cf.columns=list(cash_flow.T.iloc[0])
    st.write(cf)
    

from stocknews import StockNews
with news:
    st.header("News of " + string_name)
    sn = StockNews([tickerSymbol], save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
            st.subheader(f'News {i+1}')
            st.write(df_news['published'][i])
            st.write(df_news['title'][i])
            st.write(df_news['summary'][i])
            title_sentiment = df_news['sentiment_title'][i]
            st.write(f'Title Sentiment: {title_sentiment}')
            news_sentiment = df_news['sentiment_summary'][i]
            st.write(f"News Sentiment: {news_sentiment}")



