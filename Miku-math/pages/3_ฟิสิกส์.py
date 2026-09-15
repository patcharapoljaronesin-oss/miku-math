import streamlit as st
import numpy as np
import random
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="สูตร",
        options=["สูตรการเคลื่อนที่แนวตรง"],
        icons=["1-circle", "2-circle", "3-circle", "4-circle", "5-circle"],
        menu_icon="calculator"
    )
if selected == "สูตรการเคลื่อนที่แนวตรง":
    inputCounter = 0
    check = True

    st.title("**สูตรการเคลื่อนที่แนวตรง**")
    st.markdown("**<span style='color:red;'>**หมายเหตุ: ใส่ได้แค่ 3 ค่าเท่านั้น**</span>**", unsafe_allow_html=True)
                      
    var = [
        st.text_input("ใส่ค่า $s$(ระยะทาง)",placeholder="ตัวเลข หากไม่มีค่าปล่อยว่าง"), #s
        st.text_input("ใส่ค่า $t$(เวลา)",placeholder="ตัวเลข หากไม่มีค่าปล่อยว่าง"), #t
        st.text_input("ใส่ค่า $u$(ควาวเร็วเริ่มต้น)",placeholder="ตัวเลข หากไม่มีค่าปล่อยว่าง"), #u
        st.text_input("ใส่ค่า $v$(ความเร็วสุดท้าย)",placeholder="ตัวเลข หากไม่มีค่าปล่อยว่าง"), #v
        st.text_input("ใส่ค่า $a$(ความเร่ง)",placeholder="ตัวเลข หากไม่มีค่าปล่อยว่าง") #a
    ]
    for i in var:
        if i != "":
            try:
                float(i)
                inputCounter += 1
            except ValueError:
                st.error("โปรดใส่ตัวเลข")
                check = False
    if inputCounter > 3:
        check = False
        st.error("โปรดใส่แค่ 3 ค่า")

    if check == True and inputCounter == 3:
        if var[0] != "":
            s = float(var[0])
        else:
            s = None
        if var[1] != "":
            t = float(var[1])
        else:
            t = None
        if var[2] != "":
            u = float(var[2])
        else:
            u = None
        if var[3] != "":
            v = float(var[3])
        else:
            v = None
        if var[4] != "":
            a = float(var[4])
        else:
            a = None
            
        # v = u + at
        # s = ut - 1/2at²
        if t != None and u != None and a != None:
            st.markdown("$v = u + at$")
            st.markdown(f"$v =$ {u + (a * t)} $m/s$")
            st.markdown("")
            st.markdown("$s = ut + ½at²$")
            st.markdown(f"$s =$ {(u * t) + ((0.5) * a * (t**2))} $m$")
            st.markdown("")
        # s = ((u + v)/2) * t
        # a = (v - u) / t
        elif t != None and u != None and v != None:
            st.markdown("$s = [(u + v) / 2] * t$")
            st.markdown(f"$s =$ {((u + v) / 2) * t} $m$")
            st.markdown("")
            st.markdown("$a = (v - u) / t$")
            st.markdown(f"$a =$ {(v - u) / t} $m/s²$")
        # s = vt - 1/2at²
        elif v != None and t != None and a != None:
            st.markdown("$s = vt - ½at²$")
            st.markdown(f"$s =$ {(v * t) - ((0.5) * a * (t**2))} $m$")
        # v² = u² + as
        # t = (-u ± √(u² + 2as)) / a
        elif u != None and a != None and s != None:
            st.markdown("$v² = u² + as$")
            st.markdown(f"$v² =$ {(u**2) + (a * s)} $m/s$")
            st.markdown("")
            st.markdown("$t = (-u ± √(u² + 2as)) / a$")
            st.markdown(f"$t =$ {((-1 * u) + np.sqrt(u**2 + (2 * a * s))) / a} $s$")
            st.markdown(f"$t =$ {((-1 * u) - np.sqrt(u**2 + (2 * a * s))) / a} $s$")
        # a = (2(s-ut))/t²
        elif s != None and t != None and u != None:
            st.markdown("$a = (2(s - ut)) / t²$")
            st.markdown(f"$a =$ {(2*(s - (u * t))) / (t**2)} $m/s²$")
        # a = (2(s-vt))/t²
        elif s != None and t != None and v != None:
            st.markdown("$a = s/vt + 2/t²$")
            st.markdown(f"$a =$ {(2*(s - (v * t))) / (t**2)} $m/s²$")
        # a = (v² - u²)/2s
        # t = 2s / (u + v)
        elif v != None and u != None and s != None:
            st.markdown("$a = (v² - u²) / 2s$")
            st.markdown(f"$a =$ {(v**2 - u**2) / (2*s)} $m/s²$")
            st.markdown("")
            st.markdown("$t = 2s / (u + v)$")
            st.markdown(f"$t =$ {(2 * s) / (u + v)} $s$")
        #t = (v-u)/a
        elif u != None and v != None and a != None:
            st.markdown("$t = (v-u)/a$")
            st.markdown(f"$t =$ {(v-u)/a} $s$")
st.image("https://preview.redd.it/chibi-miku-v0-4dv4gsxdbikf1.jpeg?width=1080&crop=smart&auto=webp&s=31848bea76b2db81d0d9a4228d5e14af558ee061", width=3)
