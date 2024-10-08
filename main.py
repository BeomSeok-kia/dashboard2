import pandas as pd
import streamlit as st
from data_loader import load_data

def main():
    st.title('대시보드')
    df = load_data()
 # 특정날짜범위선택
    st.subheader("범위를선택하세요")
    df['Date'] = pd.to_datetime(df['Date'])
    start_date = st.date_input("시작일", 
df['Date'].min())
    end_date = st.date_input("종료일", df['Date'].max())
    ranged_df = df[(df['Date'] >=
pd.to_datetime(start_date)) & (df['Date'] <=
pd.to_datetime(end_date))]
    ranged_df = ranged_df.reset_index(drop=True)
st.table(ranged_df)

st.subheader("주가변동차트")
st.line_chart(ranged_df.set_index('Date')['Close'])

if __name__=='__main__':
    main()