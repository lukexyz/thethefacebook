nimport streamlit as st
from PIL import Image

st.image(Image.open('media/facemash_header.JPG'))

 
p1, p2, p3 = st.columns((6,1,6))

p1.image(Image.open('media/zuckerburg_white.png'))
p1.button('Choice 1')

p2.write("or")
p3.image(Image.open('media/jefferson.jpg'))

p3.button('Choice 2')

st.write("All credit to Mark Zuckerberg")
