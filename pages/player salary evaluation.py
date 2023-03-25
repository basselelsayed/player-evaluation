from streamlit_extras.dataframe_explorer import dataframe_explorer
import streamlit as st 
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
from xgboost import XGBRegressor
import pickle
from st_keyup import st_keyup
from streamlit_extras.word_importances import format_word_importances
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from ss import x_train , y_train
from ss import x_test , y_test

from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title='player evaluation', page_icon='⚽️', layout='wide', initial_sidebar_state='auto')


def add_vertical_space(num_lines: int = 2):
    """Add vertical space to your Streamlit app."""
    for _ in range(num_lines):
        st.write("")


st.title("Hello 📢")
add_vertical_space()
add_vertical_space()



colored_header(
    label="To evaluate player enter the following :",
    description="Time to make 💲",
    color_name="violet-70",
)
add_vertical_space()
add_vertical_space()
add_vertical_space()

text = "please enter number from 0 to 99"
wrong_messege = format_word_importances(
    words=text.split(),
    importances=(-0.8,-0.8,-0.8,-0.8,-0.8,-0.8,-0.8,),  # fmt: skip
)



text0 = "please enter number from 1 to 5"
wrong_messege1 = format_word_importances(
    words=text0.split(),
    importances=(-0.8,-0.8,-0.8,-0.8,-0.8,-0.8,-0.8,),  # fmt: skip
)




















while  True : 
    overall = st.number_input("player overall from 0 to 99")
    if overall not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(overall)
        break

add_vertical_space()

while  True : 
    potential = st.number_input("player potential from 0 to 99")
    if potential not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(potential)
        break

add_vertical_space()

wage = st.number_input("wage")
st.write(wage)

add_vertical_space()

age = st.number_input("age")
st.write(age)

add_vertical_space()

height = st.number_input("height")
st.write(height)

add_vertical_space()

weight = st.number_input("weight")
st.write(weight)

add_vertical_space()

league_name= selectbox("Select league name", ['Argentina Primera División', 'English League Championship',
       'English Premier League', 'USA Major League Soccer',
       'English League One', 'English League Two', 'Spain Primera Division',
       'French Ligue 1', 'Spanish Segunda División', 'Italian Serie A',
       'German 1. Bundesliga', 'French Ligue 2', 'Turkish Süper Lig',
       'German 2. Bundesliga', 'Portuguese Liga ZON SAGRES', 'Mexican Liga MX',
       'Holland Eredivisie', 'Colombian Liga Postobón',
       'Polish T-Mobile Ekstraklasa', 'Saudi Abdul L. Jameel League',
       'Belgian Jupiler Pro League', 'Swedish Allsvenskan',
       'Japanese J. League Division 1', 'Italian Serie B',
       'Norwegian Eliteserien', 'Chilian Campeonato Nacional',
       'Danish Superliga', 'Korean K League 1', 'German 3. Bundesliga',
       'Scottish Premiership','Austrian Football Bundesliga',
       'Rep. Ireland Airtricity League', 'Campeonato Brasileiro Série A',
       'Swiss Super League', 'Russian Premier League',
       'Australian Hyundai A-League', 'Chinese Super League',
       'Romanian Liga I', 'Greek Super League', 'Ecuadorian Serie A',
       'South African Premier Division', 'Paraguayan Primera División',
       'Liga de Fútbol Profesional Boliviano', 'Czech Republic Gambrinus Liga',
       'Peruvian Primera División', 'Venezuelan Primera División',
       'Uruguayan Primera División', 'Indian Super League',
       'Ukrainian Premier League', 'Finnish Veikkausliiga',
       'Croatian Prva HNL', 'Campeonato Brasileiro Série B',
       'UAE Arabian Gulf League', 'Hungarian Nemzeti Bajnokság I',
       'Cypriot First Division', 'Scottish Championship',
       'English National League'])
st.write(league_name)

add_vertical_space()

while  True : 
    league_level = st.number_input("league level  from 1 to 5")
    if league_level not in range (1,6):
        st.write(wrong_messege1, unsafe_allow_html=True)
        break
    else :
        st.write(league_level)
        break

add_vertical_space()

club_position= selectbox("Select club position", ['SUB', 'RES', 'RCB', 'GK', 'LCB', 'RB', 'LB', 'ST', 'RM', 'LM', 'LCM',
       'RCM', 'CAM', 'LDM', 'RDM', 'RS', 'LS', 'CDM', 'LW', 'RW', 'CB', 'CM',
       'LWB', 'RWB', 'RAM', 'LAM', 'RF', 'LF', 'CF'])
st.write(club_position)

add_vertical_space()

club_jersey_number =st.number_input("club jersey number")
st.write(club_jersey_number)

add_vertical_space()

nationality_name = selectbox("Select nationality name", ['England', 'Spain', 'Germany', 'France', 'Argentina', 'Brazil', 'Italy',
       'Colombia', 'Netherlands', 'Republic of Ireland', 'Sweden', 'Japan',
       'United States', 'Poland', 'Norway', 'Saudi Arabia', 'Mexico',
       'Portugal', 'Chile', 'Denmark', 'Korea Republic', 'Turkey', 'Scotland',
       'Austria', 'Belgium', 'Australia', 'Switzerland', 'China PR', 'Uruguay',
       'Russia', 'Romania', 'Serbia', 'Senegal', 'Wales', 'Croatia', 'Ghana',
       'Nigeria', 'Paraguay', 'Côte d\'Ivoire', 'Greece', 'Venezuela',
       'Northern Ireland', 'Czech Republic', 'Morocco', 'Cameroon', 'Ecuador',
       'South Africa', 'Bosnia and Herzegovina', 'Canada', 'Peru','Slovakia', 'Finland', 'Congo DR', 'Ukraine', 'Algeria', 'Mali',
       'Slovenia', 'Iceland', 'Bolivia', 'Albania', 'Jamaica', 'New Zealand',
       'Kosovo', 'Tunisia', 'Costa Rica', 'Guinea', 'India', 'Hungary',
       'Montenegro', 'Georgia', 'North Macedonia', 'Cape Verde Islands',
       'Bulgaria', 'Congo', 'Israel', 'Gambia', 'Burkina Faso',
       'Guinea Bissau', 'Egypt', 'Honduras', 'Benin', 'Gabon', 'Iran',
       'Panama', 'Angola', 'Curacao', 'Zimbabwe', 'Lithuania', 'Togo', 'Haiti',
       'Sierra Leone', 'Trinidad and Tobago', 'Luxembourg', 'Belarus',
       'Armenia', 'Cyprus', 'Latvia', 'Estonia', 'Comoros', 'Moldova','Kenya', 'Iraq', 'Zambia', 'Suriname', 'Uganda', 'Madagascar',
       'Azerbaijan', 'Equatorial Guinea', 'United Arab Emirates',
       'Antigua and Barbuda', 'Uzbekistan', 'Faroe Islands',
       'Central African Republic', 'Syria', 'Liechtenstein', 'Mozambique',
       'Guyana', 'Mauritania', 'Kazakhstan', 'Philippines', 'Burundi', 'Libya',
       'Liberia', 'El Salvador', 'Montserrat', 'Palestine', 'Cuba', 'Niger',
       'Bermuda', 'Jordan', 'Lebanon', 'Saint Kitts and Nevis', 'Thailand',
       'Grenada', 'Sudan', 'Dominican Republic', 'Guatemala', 'Malta',
       'Korea DPR', 'New Caledonia', 'Namibia', 'Tanzania', 'Afghanistan',
       'Puerto Rico', 'Barbados', 'Ethiopia', 'South Sudan', 'Hong Kong',
       'Chad', 'Gibraltar', 'Guam', 'Eritrea', 'Kuwait', 'Belize', 'Mauritius', 'Indonesia',
       'Saint Lucia', 'Fiji', 'Qatar', 'Chinese Taipei', 'Oman', 'Rwanda',
       'São Tomé e Príncipe', 'Vietnam', 'Kyrgyzstan', 'Nicaragua', 'Aruba',
       'Bahrain', 'Papua New Guinea', 'Malaysia', 'Malawi', 'Andorra',
       'Turkmenistan', 'Somalia', 'Macau', 'Saint Vincent and the Grenadines',
       'San Marino', 'Cambodia', 'Tajikistan', 'Brunei Darussalam',
       'Sri Lanka', 'Swaziland', 'Bhutan'])
st.write(nationality_name)

add_vertical_space()

preferred_foot = selectbox("Select prefered", ['Right', 'Left'])
st.write(preferred_foot)

add_vertical_space()

while  True : 
    weak_foot = st.number_input("player weak_foot  from 1 to 5")
    if weak_foot  not in range (1, 6):
        st.write(wrong_messege1, unsafe_allow_html=True)
        break
    else :
        st.write(weak_foot)
        break


add_vertical_space()
while  True : 
    skill_moves= st.number_input("player skill moves from 1 to 5")
    if skill_moves not in range (1, 6):
        st.write(wrong_messege1, unsafe_allow_html=True)
        break
    else :
        st.write(skill_moves)
        break

add_vertical_space()

while  True : 
    international_reputation= st.number_input("player international reputationfrom 1 to 5")
    if international_reputation not in range (1, 6):
        st.write(wrong_messege1, unsafe_allow_html=True)
        break
    else :
        st.write(international_reputation)
        break

add_vertical_space()

work_rate= selectbox("work rate", ['High/High', 'High/Low', 'High/Medium', 'Low/High', 'Low/Low',
       'Low/Medium', 'Medium/High', 'Medium/Low', 'Medium/Medium'])
st.write(work_rate)

add_vertical_space()

release_clause_eur =st.number_input("release_clause_eur")
st.write(release_clause_eur)


add_vertical_space()

while  True : 
    pace  = st.number_input("player pace  from 0 to 99")
    if pace  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(pace )
        break

add_vertical_space()
while  True : 
    shooting  = st.number_input("player shooting  from 0 to 99")
    if shooting not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(shooting )
        break

add_vertical_space()
while  True : 
    passing = st.number_input("player passing from 0 to 99")
    if passing not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(passing )
        break

add_vertical_space()
while  True : 
    dribbling  = st.number_input("player dribbling  from 0 to 99")
    if dribbling  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(dribbling )
        break

add_vertical_space()
while  True : 
    defending  = st.number_input("player defending  from 0 to 99")
    if defending  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(defending )
        break

add_vertical_space()
while  True : 
    physic  = st.number_input("player physic from 0 to 99")
    if physic  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(physic )
        break

add_vertical_space()
while  True : 
    attacking_crossing  = st.number_input("player attacking_crossing  from 0 to 99")
    if attacking_crossing  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(attacking_crossing )
        break

add_vertical_space()
while  True : 
    attacking_finishing  = st.number_input("player attacking_finishing  from 0 to 99")
    if attacking_finishing not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(attacking_finishing )
        break

add_vertical_space()
while  True : 
    attacking_heading_accuracy  = st.number_input("player attacking_heading_accuracy  from 0 to 99")
    if attacking_heading_accuracy not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(attacking_heading_accuracy )
        break

add_vertical_space()
while  True : 
    attacking_short_passing = st.number_input("player attacking_short_passing from 0 to 99")
    if attacking_short_passing not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(attacking_short_passing )
        break

add_vertical_space()
while  True : 
    attacking_volleys = st.number_input("player attacking_volleys  from 0 to 99")
    if attacking_volleys not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(attacking_volleys )
        break

add_vertical_space()
while  True : 
    skill_dribbling  = st.number_input("player skill_dribbling from 0 to 99")
    if skill_dribbling not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(skill_dribbling)
        break

add_vertical_space()
while  True : 
    skill_curve  = st.number_input("player skill_curve  from 0 to 99")
    if skill_curve  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(skill_curve )
        break

add_vertical_space()
while  True : 
    skill_fk_accuracy  = st.number_input("player skill_fk_accuracy  from 0 to 99")
    if skill_fk_accuracy  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(skill_fk_accuracy )
        break

add_vertical_space()
while  True : 
    skill_long_passing  = st.number_input("player skill_long_passing  from 0 to 99")
    if skill_long_passing  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(skill_long_passing )
        break

add_vertical_space()
while  True : 
    skill_ball_control  = st.number_input("player skill_ball_control  from 0 to 99")
    if skill_ball_control  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(skill_ball_control)
        break

add_vertical_space()
while  True : 
    movement_acceleration = st.number_input("player movement_acceleration from 0 to 99")
    if movement_acceleration  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(movement_acceleration)
        break

add_vertical_space()
while  True : 
    movement_sprint_speed  = st.number_input("player movement_sprint_speed  from 0 to 99")
    if movement_sprint_speed  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(movement_sprint_speed)
        break

add_vertical_space()
while  True : 
    movement_agility  = st.number_input("player movement_agility from 0 to 99")
    if movement_agility  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(movement_agility)
        break

add_vertical_space()
while  True : 
    movement_reactions  = st.number_input("player movement_reactions  from 0 to 99")
    if movement_reactions  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(movement_reactions)
        break

add_vertical_space()
while  True : 
    movement_balance  = st.number_input("player movement_balance  from 0 to 99")
    if movement_balance  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(movement_balance)
        break

add_vertical_space()
while  True : 
    power_shot_power  = st.number_input("player power_shot_power from 0 to 99")
    if power_shot_power  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(power_shot_power)
        break

add_vertical_space()
while  True : 
    power_jumping  = st.number_input("player power_jumping  from 0 to 99")
    if power_jumping  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(power_jumping)
        break

add_vertical_space()
while  True : 
    power_stamina = st.number_input("player power_stamina  from 0 to 99")
    if power_stamina not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(power_stamina)
        break

add_vertical_space()
while  True : 
    power_strength  = st.number_input("player power_strength  from 0 to 99")
    if power_strength  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(power_strength)
        break

add_vertical_space()
while  True : 
    power_long_shots  = st.number_input("player power_long_shots  from 0 to 99")
    if power_long_shots  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(power_long_shots)
        break

add_vertical_space()
while  True : 
    mentality_aggression  = st.number_input("player mentality_aggression from 0 to 99")
    if mentality_aggression  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(mentality_aggression)
        break

add_vertical_space()
while  True : 
    mentality_interceptions = st.number_input("player mentality_interceptions from 0 to 99")
    if mentality_interceptions  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(mentality_interceptions)
        break

add_vertical_space()
while  True : 
    mentality_positioning  = st.number_input("player mentality_positioning  from 0 to 99")
    if mentality_positioning  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(mentality_positioning)
        break

add_vertical_space()
while  True : 
    mentality_vision  = st.number_input("player mentality_vision  from 0 to 99")
    if mentality_vision  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(mentality_vision)
        break

add_vertical_space()
while  True : 
    mentality_penalties  = st.number_input("player mentality_penalties  from 0 to 99")
    if mentality_penalties not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(mentality_penalties)
        break

add_vertical_space()
while  True : 
    mentality_composure  = st.number_input("player mentality_composure from 0 to 99")
    if mentality_composure  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(mentality_composure)
        break

add_vertical_space()
while  True : 
    defending_marking_awareness = st.number_input("player defending_marking_awareness  from 0 to 99")
    if defending_marking_awareness  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(defending_marking_awareness)
        break

add_vertical_space()
while  True : 
    defending_standing_tackle  = st.number_input("player defending_standing_tackle  from 0 to 99")
    if defending_standing_tackle  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(defending_standing_tackle)
        break

add_vertical_space()
while  True : 
    defending_sliding_tackle = st.number_input("player defending_sliding_tackle from 0 to 99")
    if defending_sliding_tackle  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(defending_sliding_tackle)
        break

add_vertical_space()
while  True : 
    goalkeeping_diving = st.number_input("player goalkeeping_diving from 0 to 99")
    if goalkeeping_diving  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(goalkeeping_diving)
        break

add_vertical_space()
while  True : 
    goalkeeping_handling = st.number_input("player goalkeeping_handling from 0 to 99")
    if goalkeeping_handling  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(goalkeeping_handling)
        break

add_vertical_space()
while  True : 
    goalkeeping_kicking  = st.number_input("goalkeeping_kicking from 0 to 99")
    if goalkeeping_kicking  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(goalkeeping_kicking)
        break

add_vertical_space()
while  True : 
    goalkeeping_positioning  = st.number_input("goalkeeping_positioning  from 0 to 99")
    if goalkeeping_positioning  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(goalkeeping_positioning)
        break

add_vertical_space()
while  True : 
    goalkeeping_reflexes = st.number_input("player goalkeeping_reflexes from 0 to 99")
    if goalkeeping_reflexes  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(goalkeeping_reflexes)
        break

add_vertical_space()
while  True : 
    goalkeeping_speed = st.number_input("goalkeeping_speed  from 0 to 99")
    if goalkeeping_speed not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(goalkeeping_speed)
        break


add_vertical_space()
while  True : 
    ls = st.number_input("ls from 0 to 99")
    if ls not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(ls)
        break


add_vertical_space()
while  True : 
    stricker = st.number_input("stricker   from 0 to 99")
    if stricker  not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(stricker )
        break

add_vertical_space()
while  True : 
    rs = st.number_input("rs from 0 to 99")
    if rs not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rs)
        break

add_vertical_space()
while  True : 
    lw = st.number_input("lw  from 0 to 99")
    if lw not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lw)
        break

add_vertical_space()
while  True : 
    lf= st.number_input("lf  from 0 to 99")
    if lf not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lf)
        break

add_vertical_space()
while  True : 
    cf= st.number_input("cf  from 0 to 99")
    if cf not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(cf)
        break

add_vertical_space()
while  True : 
    rf = st.number_input("rf  from 0 to 99")
    if rf not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rf)
        break

add_vertical_space()
while  True : 
    rw = st.number_input("rw  from 0 to 99")
    if rw not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rw)
        break

add_vertical_space()
while  True : 
    lam = st.number_input("lam  from 0 to 99")
    if lam not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lam)
        break

add_vertical_space()
while  True : 
    cam = st.number_input("cam  from 0 to 99")
    if cam not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(cam)
        break

add_vertical_space()
while  True : 
    ram = st.number_input("ram  from 0 to 99")
    if ram not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(ram)
        break

add_vertical_space()
while  True : 
    lm = st.number_input("lm  from 0 to 99")
    if lm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lm)
        break

add_vertical_space()
while  True : 
    lcm = st.number_input("lcm  from 0 to 99")
    if lcm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lcm)
        break

add_vertical_space()
while  True : 
    cm = st.number_input("cm  from 0 to 99")
    if cm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(cm)
        break

add_vertical_space()
while  True : 
    rcm = st.number_input("rcm  from 0 to 99")
    if rcm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rcm)
        break

add_vertical_space()
while  True : 
    rm = st.number_input("rm  from 0 to 99")
    if rm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rm)
        break

add_vertical_space()
while  True : 
    lwb = st.number_input("lwb  from 0 to 99")
    if lwb not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lwb)
        break

add_vertical_space()
while  True : 
    ldm = st.number_input("ldm  from 0 to 99")
    if ldm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(ldm)
        break

add_vertical_space()
while  True : 
    cdm = st.number_input("cdm  from 0 to 99")
    if cdm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(cdm)
        break

add_vertical_space()
while  True : 
    rdm = st.number_input("rdm  from 0 to 99")
    if rdm not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rdm)
        break

add_vertical_space()
while  True : 
    rwb = st.number_input("rwb  from 0 to 99")
    if rwb not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rwb)
        break

add_vertical_space()
while  True : 
    lb = st.number_input("lb  from 0 to 99")
    if lb not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lb)
        break

add_vertical_space()
while  True : 
    lcb = st.number_input("lcb  from 0 to 99")
    if lcb not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(lcb)
        break

add_vertical_space()
while  True : 
    cb = st.number_input("cb  from 0 to 99")
    if cb not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(cb)
        break

add_vertical_space()
while  True : 
    rcb = st.number_input("rcb  from 0 to 99")
    if rcb not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rcb)
        break

add_vertical_space()
while  True : 
    rb = st.number_input("rb  from 0 to 99")
    if rb not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(rb)
        break

add_vertical_space()
while  True : 
    gk = st.number_input("gk  from 0 to 99")
    if gk not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(gk)
        break

add_vertical_space()
while  True : 
    loyality = st.number_input("loyality  from 0 to 99")
    if loyality not in range (0  , 99):
        st.write(wrong_messege, unsafe_allow_html=True)
        break
    else :
        st.write(loyality)
        break

add_vertical_space()
add_vertical_space()
add_vertical_space()








# loading the saved model
#loaded_model_rf = pickle.load(open('trained_model_rf.sav','rb'))
#loaded_model_lr = pickle.load(open('trained_model_lr.sav','rb'))
#trained_model_ridge = pickle.load(open('trained_model_ridge.sav','rb'))
#trained_model_lasso = pickle.load(open('trained_model_lasso.sav','rb'))
#trained_model_knn = pickle.load(open('trained_model_knn.sav','rb'))
#trained_model_svr =pickle.load(open('trained_model_svr.sav','rb'))
trained_model_xgboost =pickle.load(open('./trained_model_xgboost.sav','rb'))

loaded_scaler = pickle.load(open('./scaler.sav','rb'))
loaded_encoder = pickle.load(open('./encoder.sav','rb'))
input_data = { 'overall': [overall], 'potential':[potential], 'wage_eur':[wage], 'age':[age], 'height_cm':[height], 'weight_kg':[weight],
        'league_name' :league_name, 'league_level' : [league_level], 'club_position' : ['CF'],
       'club_jersey_number' : [club_jersey_number], 
       'nationality_name' : nationality_name, 'preferred_foot' : preferred_foot, 'weak_foot': [weak_foot], 'skill_moves' :[skill_moves],
       'international_reputation' : [international_reputation], 'work_rate' : work_rate, 'release_clause_eur': [release_clause_eur], 'pace': [pace],
       'shooting': [shooting], 'passing':[passing], 'dribbling' :[dribbling], 'defending' :[defending], 'physic' : [physic],
       'attacking_crossing' : [attacking_crossing], 'attacking_finishing' : [attacking_finishing],
       'attacking_heading_accuracy' : [attacking_heading_accuracy], 'attacking_short_passing' :[attacking_short_passing],
       'attacking_volleys': [attacking_volleys], 'skill_dribbling' : [skill_dribbling], 'skill_curve': [skill_curve],
       'skill_fk_accuracy' : [skill_fk_accuracy], 'skill_long_passing' : [skill_long_passing], 'skill_ball_control': [skill_ball_control],
       'movement_acceleration' : [movement_acceleration], 'movement_sprint_speed' : [movement_sprint_speed], 'movement_agility': [movement_agility],
       'movement_reactions' : [movement_reactions], 'movement_balance' : [movement_balance], 'power_shot_power' : [power_shot_power],
       'power_jumping' : [power_jumping], 'power_stamina' : [power_stamina], 'power_strength' : [power_strength], 'power_long_shots' : [power_long_shots],
       'mentality_aggression' : [mentality_aggression], 'mentality_interceptions' : [mentality_interceptions],
       'mentality_positioning': [mentality_positioning], 'mentality_vision' : [mentality_vision], 'mentality_penalties' : [mentality_penalties],
       'mentality_composure' : [mentality_composure], 'defending_marking_awareness' : [defending_marking_awareness],
       'defending_standing_tackle' : [defending_standing_tackle], 'defending_sliding_tackle' : [defending_sliding_tackle],
       'goalkeeping_diving' :[goalkeeping_diving], 'goalkeeping_handling' : [goalkeeping_handling], 'goalkeeping_kicking' : [goalkeeping_kicking],
       'goalkeeping_positioning': [goalkeeping_positioning], 'goalkeeping_reflexes' : [goalkeeping_reflexes], 'goalkeeping_speed' : [goalkeeping_speed],
       'ls' : [ls], 'st' : [stricker ], 'rs' : [rs], 'lw' : [lw], 'lf' : [lf], 'cf' : [cf], 'rf' : [rf], 'rw' : [rw], 'lam' : [lam], 'cam' : [cam], 'ram' : [ram],
       'lm' : [lm], 'lcm' : [lcm], 'cm' : [cm], 'rcm' : [rcm], 'rm' : [rm], 'lwb' : [lwb], 'ldm' : [ldm], 'cdm' : [cdm], 'rdm' : [rdm], 'rwb' : [rwb], 'lb' : [lb],
       'lcb' : [lcb], 'cb' : [cb], 'rcb' : [rcb], 'rb' : [rb], 'gk' : [gk], 'loyality' : [loyality] } 

from streamlit_extras.metric_cards import style_metric_cards
x_x = pd.DataFrame.from_dict(input_data)
numerical_cols = list(x_train.select_dtypes(include=['int64', 'float64','int32']).columns)
x_x = loaded_encoder.transform(x_x)
x_x[numerical_cols] = loaded_scaler.transform(x_x[numerical_cols])
if st.button('Predict') :
    
    prediction1 = trained_model_xgboost.predict(x_x)
    accuarcy1 =trained_model_xgboost.score(x_test , y_test) * 100
    

    col1, col2 = st.columns(2)
    col1.metric(label="Price", value=prediction1[0])
    col2.metric(label="Accuracy", value=round(accuarcy1) )
    style_metric_cards()









 
