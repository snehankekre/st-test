import streamlit as st

"Hello! Let's create an error:"

3 / 0


"# st.metric prototype"


def metric(label, value, change, format_large_value=False):
    """Shows a big metric symbol with a label and a change indicator."""

    # Define CSS styles.
    value_style = "font-size: calc(1.15rem + 1.2vw); font-weight: 500;"
    change_style = "font-size: 1.1rem; font-weight: 500; color: {};"

    # Write label.
    st.caption(label.upper())

    # Determine if change is positive or negative.
    if change[0] == "-":
        change = "▼ " + change[1:].strip()
        change_style = change_style.format("#ff4b4b")
    elif change[0] == "+":
        change = "▲ " + change[1:].strip()
        change_style = change_style.format("#09ab3b")
    else:
        change = "▲ " + change.strip()
        change_style = change_style.format("#09ab3b")

    # Show as in the format 1.0k if value is >1000.
    if format_large_value:
        try:
            value = value  # format_large_number(value)
        except ValueError:
            pass  # probably a string

    # Write value and change.
    st.write(
        f'<div style="margin-top: -1.3rem; margin-bottom: -0.1rem; {value_style}">{value}</div> <div style="{change_style}">{change}</div>',
        unsafe_allow_html=True,
    )


col1, col2, col3, col4, col5 = st.beta_columns(5)
with col1:
    metric(
        "Viewers",
        "∅",
        change="-123",
    )

with col2:
    metric(
        "Developers",
        "––",
        change="13%",
    )
with col3:
    metric(
        "Developers",
        "--",
        change="13%",
    )
with col4:
    metric(
        "Developers",
        "—",
        change="13%",
    )
