import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="สูตร",
        options=["ผลต่างกำลังสอง", "กำลังสองสมบูรณ์"],
        icons=["1-circle", "2-circle"],
        menu_icon="calculator"
    )
if selected == "ผลต่างกำลังสอง":

    st.title("*ผลต่างกำลังสอง*")

    x = int(st.text_input("ใส่ค่า $x$"))
    y = int(st.text_input("ใส่ค่า $y$"))

    if x != "" and y != "":
        st.markdown(f"ผลลัพธ์: ({x}+{y})({x}-{y})")
if selected == "กำลังสองสมบูรณ์":

    st.title("*กำลังสองสมบูรณ์*")

    x = int(st.text_input("ใส่ค่า $x$"))
    y = int(st.text_input("ใส่ค่า $y$"))
    if x != "" and y != "":
        ans1 = f"{x}**2 + {2*x*y} + {y}**2"
        ans2 = f"{x}**2 - {2*x*y} + {y}**2"
        st.text(f"ผลลัพธ์จากสูตร (x+y)**2: {ans1}")
        st.text(f"เท่ากับ {(x**2) + (2*x*y) + (y**2)}")
        st.text("")
        st.text(f"ผลลัพธ์จากสูตร (x-y)**2: {ans2}")
        st.text(f"เท่ากับ {(x**2) - (2*x*y) + (y**2)}")

