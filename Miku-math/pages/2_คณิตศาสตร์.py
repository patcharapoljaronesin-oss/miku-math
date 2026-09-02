import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="สูตร",
        options=["ผลต่างกำลังสอง", "กำลังสองสมบูรณ์", "สูตรกำลังสอง(Quadratic Formula)"],
        icons=["1-circle", "2-circle"],
        menu_icon="calculator"
    )
if selected == "ผลต่างกำลังสอง":

    st.title("*ผลต่างกำลังสอง*")

    x = st.text_input("ใส่ค่า $x$")
    y = st.text_input("ใส่ค่า $y$")

    if x != "" and y != "":
        x = int(x)
        y = int(y)
        st.markdown(f"ผลลัพธ์: ({x}+{y})({x}-{y})")
if selected == "กำลังสองสมบูรณ์":

    st.title("*กำลังสองสมบูรณ์*")

    x = st.text_input("ใส่ค่า $x$")
    y = st.text_input("ใส่ค่า $y$")
    if x != "" and y != "":
        x = int(x)
        y = int(y)
        ans1 = f"{x}**2 + {2*x*y} + {y}**2"
        ans2 = f"{x}**2 - {2*x*y} + {y}**2"
        st.text(f"ผลลัพธ์จากสูตร (x+y)**2: {ans1}")
        st.text(f"เท่ากับ {(x**2) + (2*x*y) + (y**2)}")
        st.text("")
        st.text(f"ผลลัพธ์จากสูตร (x-y)**2: {ans2}")
        st.text(f"เท่ากับ {(x**2) - (2*x*y) + (y**2)}")
if selected == "สูตรกำลังสอง(Quadratic Formula)":

    st.title("*สูตรกำลังสอง(Quadratic Formula)*")

    a = st.text_input("a:")
    b = st.text_input("b:")
    c = st.text_input("c:")

    if a != "" and b != "" and c != "":
        a = int(a)
        b = int(b)
        c = int(c)
        Discriminant = (b**2) - (4*a*c)

        def equation(a,b,c):
            sqrt = np.sqrt((b**2) - (4*a*c))
            try:
                CheckSqrt = str(int(sqrt))
            except ValueError:
                CheckSqrt = str((sqrt))
            print(sqrt)
            print("เป็นทศนิยม")
            if "." in CheckSqrt and Discriminant >= 0:
                st.text(f"-({b}) ± sqrt({Discriminant}) / {2*a}")

            elif Discriminant > 0:
                if ((-1 * b) + sqrt) % (2*a) == 0:
                   st.text(f"{int(((-1 * b) + sqrt) / (2*a))}  , {int(((-1 * b) - sqrt) / (2*a))}")
                else:         
                   st.text(f"{int((-1 * b) + sqrt)} / {2*a} , {int((-1 * b) - sqrt)} / {2*a}")

            elif Discriminant == 0:
                if ((-1 * b) + sqrt) % (2*a) == 0:
                   st.text(f"{int((-1 * b) / (2*a))}")
                else:         
                    st.text(f"{int((-1 * b))} / {2*a}")

            elif Discriminant < 0:
                st.text("ไม่มีคำตอบเป็นจำนวนจริง")

        equation(a,b,c)
