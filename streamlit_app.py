from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location="below"):

    # generate descending order of pincodes (based on # of aadhaar generated)
    # let user pick # of top records to show (= n)
    # plot bar graph with # of aadhaar generated for top n pincodes

    num = st.slider("Number of top pincodes to show", 1, 10, 5)

    # df = pd.read_csv("../datasets/Aadhaar.csv")
    # import os

    # print(os.getcwd())

    df = pd.read_csv("datasets/Aadhaar-small-cleaned.csv")

    # grain check: check if the grain is at pincode level
    total_pincode_count = df["Pin Code"].unique().size  # 17103
    total_count = len(df.index)  # 222281

    # so clearly not at pincode level. let's group it and aggregate
    data = (
        df.groupby("Pin Code")["Aadhaar generated"]
        .sum()
        .sort_values(ascending=False, ignore_index=True)
    )
    data = data.head(num)
    # print(data)

    st.write(f"Total Count: {total_count}")
    st.write(f"Total Pincode Count: {total_pincode_count}")

    st.bar_chart(
        data,
        x_label="pincodes",
        y_label="# of Aadhaars generated",
    )
    # st.altair_chart(
    #     alt.Chart(pd.DataFrame(data), height=500, width=500)
    #     .mark_circle(color="#0068c9", opacity=0.5)
    #     .encode(x="x:Q", y="y:Q")
    # )
