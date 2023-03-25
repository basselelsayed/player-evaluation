import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from category_encoders import BinaryEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, OrdinalEncoder
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
import streamlit as st 

st.set_page_config(page_title='player evaluation', page_icon='⚽️', layout='wide', initial_sidebar_state='auto')

from streamlit_extras.dataframe_explorer import dataframe_explorer

def add_vertical_space(num_lines: int = 5):
    """Add vertical space to your Streamlit app."""
    for _ in range(num_lines):
        st.write("")





    
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_toggle import st_toggle_switch
from streamlit_extras.no_default_selectbox import selectbox







st.title('AI   🆚  Agents') 
add_vertical_space()


st.image('ping 4.png')
add_vertical_space()

st.caption('''For the last two decades, coaches have been using data science in sports to help improve the performance of their players.

They’ve been leveraging big data to help them make split second on-the-field decisions, and relying on sports analytics to help them sign the “next big thing”.

Referees, meanwhile, now use Video Assistant Technology (VAR) in football to help them make more precise judgments regarding the big decisions, such as penalties, free kicks, and red cards.

And now that AI, and specifically Deep Learning, has got involved, the sports experience is going to change even more.''')#https://www.v7labs.com/blog/ai-in-sport


st.caption(""" Also, players now started to go to AI but why ? , the answer will be \'to see and analyis their performance during the matches'

t is the right answer but the fact is , not only for this reason , but also ,they start to use AI to make it as evaluation for them 
 
 as they want to get rid of agents because not all players like agents , alot of players make their families their agents because they 
 
 cant trust stranger people , no we have to ask a very important question , what is the main problem between the players and their agents
 
 why did they start to think to use AI .Everybody goes to work to make money. Agents are no different. However, there are agents who will force 

 certain situations, purely for financial gain.Agents have been known to force through contracts and transfers for their clients because there is 

 something in it for them. Most of the time that is for financial gain but there are other reasons, like trying to keep important people within football clubs happy for future needs.

 Agents receive fees from the deals that they sort for players and clubs. It is normally a percentage of the amount the player will receive over the length of their contract. 

 here is an example for a problem we face """)

st.caption ("""agent comes with many responsibilities but the main one is to get you the best deals.

They are there to represent you and handle any contract negotiations. They should be advising and guiding 

you through career decisions but also matters off the pitch.""")

st.caption (""" what if there is a replacement ?? . what if there is way to know the best player value according to his attributes

firstly , it will make the player comfortable with the fact of that he is sold or evaluated with the right price ,so no

more of over price or underprice for both team and player second , no need for extra money for doing nothing """)


st.caption("""some of player truly start to use this idea . kevin de pryne player of manchester city start to use this idea 
and make an contract with a company """)





    








#df15 = pd.read_csv("F:\AI corse\\final project\sources\players_15.csv")
#filterd_df = dataframe_explorer(df15)
#st.dataframe(filterd_df )









