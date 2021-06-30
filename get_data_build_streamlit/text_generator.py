import streamlit as st
from textgenrnn import textgenrnn


st.set_page_config(page_icon="assets/favicon.ico",
                   layout='wide')
st.title('Bob Dylan Lyrics Generator')

st.markdown("Create new lyrics based on Bob Dylan Style")

def text_generator():
    textgen = textgenrnn()
    textgen.train_from_file('lyrics/dylan.txt', num_epochs=5)

    results_data = textgen.generate(25, temperature=0.5, return_as_list=True)
    for text in results_data:
        st.text(text)

if __name__ == '__main__':
    text_generator()
