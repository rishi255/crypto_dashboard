import altair as alt
import pandas as pd
import streamlit as st

with st.echo(code_location="below"):
    """
    # Welcome to Streamlit!

    This is a simple demo app created by me.

    Dataset used: Aadhaar dataset that contains # of Aadhaar IDs generated at (I think) the Sub-district level (or something similar).
    User Input: # of top pin-codes to show.
    Output: Top n pin-codes where highest number of Aadhaars were generated.
    """

    # generate descending order of pincodes (based on # of aadhaar generated)
    # let user pick # of top records to show (= n)
    # plot bar graph with # of aadhaar generated for top n pincodes

    num = st.slider("Number of top pincodes to show", 1, 10, 5)

    # df = pd.read_csv("../datasets/Aadhaar.csv")
    df = pd.read_csv("datasets/Aadhaar-small-cleaned.csv")

    # grain check: check if the grain is at pincode level
    total_pincode_count = df["Pin Code"].unique().size  # 17103
    total_count = df.shape[0]  # 222281

    # so clearly not at pincode level. let's group it and aggregate df.
    data = (
        df.groupby("Pin Code")["Aadhaar generated"]
        .sum()
        .sort_values(
            ascending=False,
        )
    ).reset_index()
    data = data.head(num)

    st.write(f"Total Count: {total_count}")
    st.write(f"Total Pincode Count: {total_pincode_count}")

    # create altair bar chart
    chart = (
        alt.Chart(data, height=500, width=500)
        .mark_bar()
        .encode(
            x=alt.X(field="Pin Code", type="nominal").sort("-y"), y="Aadhaar generated"
        )
    )

    # write chart to page
    st.altair_chart(chart)
