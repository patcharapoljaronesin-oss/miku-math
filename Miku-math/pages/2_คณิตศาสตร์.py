import streamlit as st
import numpy as np
import random
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="สูตร",
        options=["ผลต่างกำลังสอง", "กำลังสองสมบูรณ์", "สูตรกำลังสอง(Quadratic Formula)", "ผลบวก/ลบกำลังสาม", "กำลังสามสมบูรณ์"],
        icons=["1-circle", "2-circle", "3-circle", "4-circle", "5-circle"],
        menu_icon="calculator"
    )
if selected == "ผลต่างกำลังสอง":

    st.title("*ผลต่างกำลังสอง*")

    x = st.text_input("ใส่ค่า $x$")
    y = st.text_input("ใส่ค่า $y$")

    if x != "" and y != "":
        st.text(f"ผลลัพธ์: ({x}+{y})({x}-{y})")

if selected == "กำลังสองสมบูรณ์":

    st.title("*กำลังสองสมบูรณ์*")

    x = st.text_input("ใส่ค่า $x$")
    y = st.text_input("ใส่ค่า $y$")

    if x != "" and y != "":
        try:
            x = int(x)
            y = int(y)
            ans1 = f"{x}**2 + {2*x*y} + {y}**2"
            ans2 = f"{x}**2 - {2*x*y} + {y}**2"
            st.text(f"ผลลัพธ์จากสูตร (x+y)**2: {ans1}")
            st.text(f"เท่ากับ {(x**2) + (2*x*y) + (y**2)}")
            st.text("")
            st.text(f"ผลลัพธ์จากสูตร (x-y)**2: {ans2}")
            st.text(f"เท่ากับ {(x**2) - (2* x*y) + (y**2)}") 
        except ValueError:
            try:
                x = int(x)
                ans1 = f"{x}**2 + ({2*x})({y}) + ({y})**2"
                ans2 = f"{x}**2 - ({2*x})({y}) + ({y})**2"
                st.text(f"ผลลัพธ์จากสูตร (x+y)**2: {ans1}")
                st.text(f"เท่ากับ {(x**2)} + ({2*x})({y}) + ({y})**2")
                st.markdown("")
                st.text(f"ผลลัพธ์จากสูตร (x-y)**2: {ans2}")
                st.text(f"เท่ากับ {(x**2)} + ({2*x})({y}) + ({y})**2") 
            except ValueError:
                try:
                    y = int(y)
                    ans1 = f"({x})**2 + ({2*y})({x}) + {y}**2"
                    ans2 = f"({x})**2 - ({2*y})({x}) + {y}**2"
                    st.text(f"ผลลัพธ์จากสูตร (x+y)**2: {ans1}")
                    st.text(f"เท่ากับ ({x})**2 + ({2*y})({x}) + {y**2}")
                    st.markdown("")
                    st.text(f"ผลลัพธ์จากสูตร (x-y)**2: {ans2}")
                    st.text(f"เท่ากับ ({x})**2 - ({2*y})({x}) + {y**2}")
                except ValueError:
                    ans1 = f"{x}**2 + {2}{x}{y} + {y}**2"
                    ans2 = f"{x}**2 - {2}{x}{y} + {y}**2"
                    st.text(f"ผลลัพธ์จากสูตร (x+y)**2: {ans1}")
                    st.text(f"เท่ากับ ({x})**2 + ({2})({x})({y}) + ({y})**2")
                    st.markdown("")
                    st.text(f"ผลลัพธ์จากสูตร (x-y)**2: {ans2}")
                    st.text(f"เท่ากับ ({x})**2 - ({2})({x})({y}) + ({y})**2")   

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
            CheckSqrt = str(sqrt)

            print(sqrt)
            print("เป็นทศนิยม")
            if "." in CheckSqrt and CheckSqrt[CheckSqrt.index(".")+2] and Discriminant >= 0:
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

if selected == "ผลบวก/ลบกำลังสาม":
    st.title("*ผลบวก/ลบกำลังสาม*")

    x = st.text_input("ใส่ค่า $x$")
    y = st.text_input("ใส่ค่า $y$")

    if x != "" and y != "":
        try:
            x = int(x)
            y = int(y)
            st.header("*ผลบวกกำลังสาม*")
            st.text(f"ผลลัพธ์: ({x}+{y})({x**2}-{x*y}+{y**2})")
            st.markdown("")
            st.header("*ผลต่างกำลังสาม*")
            st.text(f"ผลลัพธ์: ({x}-{y})({x**2}+{x*y}-{y**2})") 
        except ValueError:
            try:
                x = int(x)
                st.header("*ผลบวกกำลังสาม*")
                st.text(f"ผลลัพธ์: ({x}+{y})({x**2}-({x})({y})+({y})**2)")
                st.markdown("")
                st.header("*ผลต่างกำลังสาม*")
                st.text(f"ผลลัพธ์: ({x}-{y})({x**2}+({x})({y})-({y})**2)")
            except ValueError:
                try:
                    y = int(y)
                    st.header("*ผลบวกกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x}+{y})(({x})**2-({x})({y})+{y**2})")
                    st.markdown("")
                    st.header("*ผลต่างกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x}-{y})(({x})**2+({x})({y})-{y**2})")
                except ValueError:
                    st.header("*ผลบวกกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x}+{y})(({x})**2-({x})({y})+({y})**2)")
                    st.markdown("")
                    st.header("*ผลต่างกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x}-{y})(({x})**2+({x})({y})-({y})**2)")

if selected == "กำลังสามสมบูรณ์":
    st.title("*ผลบวก/ลบกำลังสาม*")

    x = st.text_input("ใส่ค่า $x$")
    y = st.text_input("ใส่ค่า $y$")

    if x != "" and y != "":
        try:
            x = int(x)
            y = int(y)
            st.header("*ผลบวกกำลังสาม*")
            st.text(f"ผลลัพธ์: {x**3} + {3*(x**2)*y} + {3*x*(y**2)} + {y**3} = {(x**3) - (3*(x**2)*y) + (3*x*(b**2)) - (y**3)}") 
            st.markdown("")
            st.header("*ผลต่างกำลังสาม*")
            st.text(f"ผลลัพธ์: {x**3} - {3*(x**2)*y} + {3*x*(y**2)} - {y**3} = {(x**3) - (3*(x**2)*y) + (3*x*(b**2)) - (y**3)}") 
        except ValueError:
            try:
                x = int(x)
                st.header("*ผลบวกกำลังสาม*")
                st.text(f"ผลลัพธ์: {x**3} + ({3*(x**2)})({y}) + ({3*x})({y})**2 + ({y})**3")
                st.markdown("")
                st.header("*ผลต่างกำลังสาม*")
                st.text(f"ผลลัพธ์: {x**3} - ({3*(x**2)})({y}) + ({3*x})({y})**2 - ({y})**3")
            except ValueError:
                try:
                    y = int(y)
                    st.header("*ผลบวกกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x})**3 + ({3*y})({x})**2 + ({3*(y**2)})({x}) + {y**3}")
                    st.markdown("")
                    st.header("*ผลต่างกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x})**3 - ({3*y})({x})**2 + ({3*(y**2)})({x}) - {y**3}")
                except ValueError:
                    st.header("*ผลบวกกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x})**3 + ({3})({y})({x})**2 + ({3})({x})({y})**2 + ({y})**3")
                    st.markdown("")
                    st.header("*ผลต่างกำลังสาม*")
                    st.text(f"ผลลัพธ์: ({x})**3 - ({3})({y})({x})**2 + ({3})({x})({y})**2 - ({y})**3")
