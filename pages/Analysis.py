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
from streamlit_extras.dataframe_explorer import dataframe_explorer
from ss import df ,df15 ,df16 , df17 , df18 ,df19 , df20 , df21 ,df22
st.set_page_config(page_title='player evaluation', page_icon='⚽️', layout='wide', initial_sidebar_state='auto')
def add_vertical_space(num_lines: int = 5):
    """Add vertical space to your Streamlit app."""
    for _ in range(num_lines):
        st.write("")


df15 = pd.read_csv("F:\AI corse\\final project\sources\players_15.csv")
df16 = pd.read_csv("F:\AI corse\\final project\sources\players_16.csv")
df17 = pd.read_csv("F:\AI corse\\final project\sources\players_17.csv")
df18 = pd.read_csv("F:\AI corse\\final project\sources\players_18.csv")
df19 = pd.read_csv("F:\AI corse\\final project\sources\players_19.csv")
df20 = pd.read_csv("F:\AI corse\\final project\sources\players_20.csv")
df21 = pd.read_csv("F:\AI corse\\final project\sources\players_21.csv")
df22 = pd.read_csv("F:\AI corse\\final project\sources\players_22.csv")
df =pd.concat([df15,df16,df17,df18,df19,df20,df21,df22])
df.shape
df.reset_index(inplace =True)
df.drop('index' , axis = 1 , inplace= True)
df = df.drop(['player_face_url','club_logo_url','club_flag_url','nation_logo_url','nation_flag_url','sofifa_id', 'player_url', 
              'dob','club_loaned_from' , 'body_type'] , axis=1)


filterd_df = dataframe_explorer(df)
st.dataframe(filterd_df )

from streamlit_extras.mention import mention

mention(
    label="classification report",
    icon= '🖨',  # Some icons are available... like Streamlit!
    url= "https://drive.google.com/file/d/1mIoED6cjH5HGLCrA5qULrYKzvEnmdFd9/view?usp=share_link" ,
)



year = st.selectbox('Please select a year', ['--','2015', '2016', '2017',"2018" , "2019" , "2020" , '2021' , "2022"])

if year == '2015' :
    st.title("2015")
    top_clubs = df15.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df15[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df15[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df15[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df15[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df15[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))

elif year == '2016' :
    st.title("2016")
    top_clubs = df16.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df16[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df16[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df16[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df16[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df16[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))
   

elif year == '2017' :
    st.title("2017")
    top_clubs = df17.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df17[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df17[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df17[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df17[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df17[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))
elif year == '2018' :
    st.title("2018")
    top_clubs = df18.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df18[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df18[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df18[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df18[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df18[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))
elif year == '2019' :
    st.title("2019")
    top_clubs = df19.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df19[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df19[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df19[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df19[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df19[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))
elif year == '2020' :
    st.title("2020")
    top_clubs = df20.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df20[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df20[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df20[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df20[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df20[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))
elif year == '2021' :
    st.title("2021")
    top_clubs = df21.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df21[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df21[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df21[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df21[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df21[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))
elif year == '2022' :
    st.title("2022")
    top_clubs = df22.groupby(['club_name']).overall.mean().sort_values(ascending  = False)[:20]
    st.plotly_chart(px.bar( top_clubs,  x= top_clubs.index , y = top_clubs.values , color_discrete_sequence = ['blue'] , title= "Top 20 club overall "  ))
    add_vertical_space()
    add_vertical_space()
    top_players = df22[['short_name', 'overall']][:20]
    st.plotly_chart(px.bar( top_players,  x= "short_name" , y = "overall" , color_discrete_sequence = ['blue'] , title= "Top 20 player overall"  ))
    add_vertical_space()
    add_vertical_space()
    potential = df22[['short_name', "potential"]].sort_values(by = ['potential'], ascending = False)[:20]
    st.plotly_chart(px.bar( potential,  x= "short_name" , y = "potential" , color_discrete_sequence = ['blue'] , title= "Top 20 player potental "  ))
    add_vertical_space()
    add_vertical_space()
    top_league_wage= df22[['league_name', 'wage_eur']].groupby('league_name').count().sort_values(by='wage_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_wage ,color_discrete_sequence = ['blue'] , title= "Top 20 league wages"))
    add_vertical_space()
    add_vertical_space()
    top_league_value= df22[['league_name', 'value_eur']].groupby('league_name').count().sort_values(by='value_eur' ,ascending= False)[0:20]
    st.plotly_chart(px.bar(top_league_value ,color_discrete_sequence = ['blue'] , title= " Top 20 league value"))
    add_vertical_space()
    add_vertical_space()
    average_age = df22[['league_name', 'age']].groupby('league_name').mean().sort_values(by=["age"] ,ascending= False)[0:20]
    st.plotly_chart(px.bar(average_age ,color_discrete_sequence = ['blue']))
    

elif year == '--':
    pass
















#df15 = pd.read_csv("F:\AI corse\\final project\sources\players_15.csv")
#filterd_df = dataframe_explorer(df15)
#st.dataframe(filterd_df )
