import streamlit as st
import pandas as pd
#Display text
st.text('Welcome to  africa data School.')

#Display string formatted as Markdown.
st.markdown('showing markdown **_really_ cool**.')

#Display mathematical expressions formatted as LaTeX.
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

#  (st.write) This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it

#example 1
st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
 }))


