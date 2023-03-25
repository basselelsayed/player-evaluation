# importing libraries
### https://www.goal.com/en/news/fifa-player-ratings-explained-how-are-the-card-number--stats-decided/1hszd2fgr7wgf1n2b2yjdpgynu  ___fifa link introduce how atributes of players taken ###
##https://www.mirror.co.uk/sport/football/news/kevin-de-bruyne-uses-data-23870686
##https://analyticsfc.co.uk/our-team/
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from category_encoders import BinaryEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, OrdinalEncoder , OneHotEncoder
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression

# Read data 
df15 = pd.read_csv("sources/players_15.csv")
df16 = pd.read_csv("sources/players_16.csv")
df17 = pd.read_csv("sources/players_17.csv")
df18 = pd.read_csv("sources/players_18.csv")
df19 = pd.read_csv("sources/players_19.csv")
df20 = pd.read_csv("sources/players_20.csv")
df21 = pd.read_csv("sources/players_21.csv")
df22 = pd.read_csv("sources/players_22.csv")
# Compine the data
df =pd.concat([df15,df16,df17,df18,df19,df20,df21,df22])
df.shape
df.reset_index(inplace =True)
df.drop('index' , axis = 1 , inplace= True)
# Data summary report 

# Data first look
df
df.columns
df.describe()
df.info()
# Clean Data 
### [body_type , player_tags , player_traits] type mmkn nd5lo
#Drop uneccessary columns
df = df.drop(['player_face_url','club_logo_url','club_flag_url','nation_logo_url','nation_flag_url','sofifa_id', 'player_url', 'short_name', 
              'long_name','player_positions','dob','club_team_id','club_loaned_from' ,'nationality_id', 'nationality_id' , 'nation_team_id',
              'body_type' , 'real_face' ,'player_traits' ] , axis=1)
df.shape
#Handle missing data 
## we have to divide the number of columns to show the missing data because they are too uch to appear
## get list of all columns in data frame to divide them
df.columns
## first part of data 
df_prt1 = df[ [ 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'height_cm',
       'weight_kg', 'club_name', 'league_name', 'league_level',
       'club_position', 'club_jersey_number', 'club_joined',
       'club_contract_valid_until', 'nationality_name', 'nation_position',
       'nation_jersey_number', 'preferred_foot', 'weak_foot', 'skill_moves','international_reputation', 'work_rate', 'release_clause_eur',
       'player_tags', 'pace', 'shooting', 'passing']]
## get the number of the missing data (part1)
df_prt1.isnull().sum()
## missin percentage part(1)
df_prt1.isnull().mean()*100
###  i found alot of missing data in following columns[value_eur,wage_eur,club_name,league_name ,league_level ,club_position,club_jersey_number
###    ,club_joined ,club_contract_valid_until,nation_position ,nation_jersey_number,,,] so i will decide how i will handle them {fill , drop }

df["value_eur"].describe()
df_prt1.drop(df_prt1[df_prt1["value_eur"].isnull()].index , axis= 0 , inplace= True)
## we cant fill the missing the data so we will drop the null rows /  Note :there is a big difference between median and mean (squide data)
df.drop(df[df["value_eur"].isnull()].index , axis = 0 ,inplace =True  ) 
df_prt1.drop(df_prt1[df_prt1["value_eur"].isnull()].index , axis = 0  ) 
df_prt1.isnull().sum()
## handle missing in player_tags 
df.player_tags.value_counts()

## i cant fill the misiing columns so i have to drop the column
df.drop("player_tags" , axis = 1 , inplace = True)
## i cant fill the misiing columns so i have to drop the column
df_prt1.drop("player_tags" , axis = 1 , inplace = True)

df_prt1.isnull().sum()
## we cant fill the columns so we will drop 
df.drop(['nation_jersey_number', "nation_position"] , axis = 1 , inplace=True) 
df_prt1.drop(['nation_jersey_number', "nation_position"] , axis = 1 , inplace=True) 
df_prt1.isnull().sum()
##############################################################################################################################################################################################
## handle release_clause_eur
df.release_clause_eur.describe()
df.release_clause_eur.mean()
## i can fill the release clauss with mean values

# df.release_clause_eur.fillna(df.release_clause_eur.mean() , inplace= True)
df_prt1.release_clause_eur.fillna(df.release_clause_eur.mean() , inplace= True)
df_prt1.isnull().sum()
##############################################################################################################################################################################################
df_prt1.isnull().sum()
#################################################################################################################################################################################################
## haandle pace , shooting ,passing
df.shooting.describe()
df.pace.describe()
df.passing.describe()
# df.pace.fillna(df.pace.mean() , inplace= True)
# df.shooting.fillna(df.shooting.mean() , inplace= True)
# df.passing.fillna(df.passing.mean() , inplace= True)
df_prt1.pace.fillna(df.pace.mean() , inplace= True)
df_prt1.shooting.fillna(df.shooting.mean() , inplace= True)
df_prt1 .passing.fillna(df.passing.mean() , inplace= True)
df_prt1.isnull().sum()
################################################################################################################################################################################################
## handle clube joined
df.club_joined.describe()
df[df['club_joined'].isnull()]
df.drop(df[df['club_joined'].isnull()].index , axis = 0 , inplace =True)

df_prt1.drop(df_prt1[df_prt1['club_joined'].isnull()].index , axis = 0 , inplace =True)
df_prt1.isnull().sum()
df.drop(df[df['league_level'].isnull()].index , axis = 0 , inplace = True )
df_prt1.drop(df_prt1[df_prt1['league_level'].isnull()].index , axis = 0 , inplace = True )
## part2 of data 
df_prt2 = df[['dribbling', 'defending',
       'physic', 'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power','power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions','mentality_positioning', 'mentality_vision', 'mentality_penalties']]
## get the number of the missing data part(2)
df_prt2.isnull().sum()
### missin percentage 
df_prt2.isnull().mean()*100
## HANDLE DRIPLING , DEFENDING , PHYSIC
df.dribbling.describe()
df.defending.describe()
df.physic.describe()
#df.dribbling.fillna(df.dribbling.mean() , axis = 0 , inplace =True)
df_prt2.dribbling.fillna(df_prt2.dribbling.mean() , axis = 0 , inplace =True)
# df.defending.fillna(df.defending.mean() , axis = 0 , inplace =True)
df_prt2.defending.fillna(df_prt2.defending.mean() , axis = 0 , inplace =True)
#  df.physic.fillna(df.physic.mean() , axis = 0 , inplace =True)
df_prt2.physic.fillna(df_prt2.physic.mean() , axis = 0 , inplace =True)
df_prt2.isnull().sum()
## data part(3)
df_prt3 = df[['mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed',
       'ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram','lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm']]
df_prt3.isnull().sum()
df_prt3.isnull().mean()*100
df.mentality_composure.describe()
# df.mentality_composure.fillna(df.mentality_composure.mean() , axis = 0 , inplace =True)
df_prt3.mentality_composure.fillna(df_prt3.mentality_composure.mean() , axis = 0 , inplace =True)
 # df.goalkeeping_speed .fillna(df.goalkeeping_speed .mean() , axis = 0 , inplace =True)
df_prt3.goalkeeping_speed .fillna(df_prt3.goalkeeping_speed .mean() , axis = 0 , inplace =True)
df_prt3.isnull().sum()
df_prt4 = df[['cdm', 'rdm', 'rwb', 'lb',
       'lcb', 'cb', 'rcb', 'rb', 'gk']]
df_prt4.isnull().sum()
## now after i handled all the missing data we will start to explore data and start feautre engineering process
## feture engineering
df.columns
## i can extract new feature (loyality ) as it indicate how many year did player stay in club and if it will make a difference in the value or not 
df.club_joined = df.club_joined.astype('datetime64[ns]')
df.club_joined = df.club_joined.dt.year
df['loyality'] = df.club_contract_valid_until - df.club_joined
df.drop(["club_contract_valid_until" ,"club_joined" ]  , axis = 1 , inplace = True  )
df.loyality.describe()
df.work_rate.value_counts()
#handle last 10 columns as they nedd to remove + from numbers
df.select_dtypes('O').info()
df_prt1
###############################################################################################################################################################################

###############################################################################################################################################################################
# split data 
"""df.drop(['ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram',
       'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb',
       'lcb', 'cb', 'rcb', 'rb', 'gk' , 'league_name', 'nationality_name' ,'release_clause_eur' ,'work_rate'] , axis = 1 , inplace=True)
       """
df.shape
x= df.drop('value_eur' , axis = 1 )
y = df['value_eur']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
## cross validation
#x_full_train , x_test2 ,y_full_train , y_test2 = train_test_split(x, y, test_size=0.2, random_state=42)
# x_train, x_test, y_train, y_test = train_test_split(x_full_train, y_full_train, test_size=0.2, random_state=42)
# 
x_train.shape
x_train.isnull().sum()[50:57]
x_train.isnull().sum()[19:27]
x_train.pace.fillna(x_train.pace.mean() , inplace= True)
x_train.shooting.fillna(x_train.shooting.mean() , inplace= True)
x_train.passing.fillna(x_train.passing.mean() , inplace= True)
x_train.dribbling.fillna(x_train.dribbling.mean() , axis = 0 , inplace =True)
x_train.defending.fillna(x_train.defending.mean() , axis = 0 , inplace =True)
x_train.physic.fillna(x_train.physic.mean() , axis = 0 , inplace =True)
x_train.mentality_composure.fillna(x_train.mentality_composure.mean() , axis = 0 , inplace =True)
x_train.goalkeeping_speed .fillna(x_train.goalkeeping_speed .mean() , axis = 0 , inplace =True)
x_train.release_clause_eur.fillna(x_train.release_clause_eur.mean() , inplace= True)
x_test.pace.fillna(x_train.pace.mean() , inplace= True)
x_test.shooting.fillna(x_train.shooting.mean() , inplace= True)
x_test.passing.fillna(x_train.passing.mean() , inplace= True)
x_test.dribbling.fillna(x_train.dribbling.mean() , axis = 0 , inplace =True)
x_test.defending.fillna(x_train.defending.mean() , axis = 0 , inplace =True)
x_test.physic.fillna(x_train.physic.mean() , axis = 0 , inplace =True)
x_test.mentality_composure.fillna(x_train.mentality_composure.mean() , axis = 0 , inplace =True)
x_test.goalkeeping_speed .fillna(x_train.goalkeeping_speed .mean() , axis = 0 , inplace =True)
x_test.release_clause_eur.fillna(x_train.release_clause_eur.mean() , inplace= True)
"""x_test2.pace.fillna(x_train.pace.mean() , inplace= True)
x_test2.shooting.fillna(x_train.shooting.mean() , inplace= True)
x_test2.passing.fillna(x_train.passing.mean() , inplace= True)
x_test2.dribbling.fillna(x_train.dribbling.mean() , axis = 0 , inplace =True)
x_test2.defending.fillna(x_train.defending.mean() , axis = 0 , inplace =True)
x_test2.physic.fillna(x_train.physic.mean() , axis = 0 , inplace =True)
x_test2.mentality_composure.fillna(x_train.mentality_composure.mean() , axis = 0 , inplace =True)
x_test2.goalkeeping_speed .fillna(x_train.goalkeeping_speed .mean() , axis = 0 , inplace =True)
#x_test2.release_clause_eur.fillna(x_train.release_clause_eur.mean() , inplace= True)
"""
l = ['ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram',
       'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb',
       'lcb', 'cb', 'rcb', 'rb', 'gk']
for i in l :
    x_train[i] = x_train[i].str.split("+").str[0]

for i in l :
   x_train[i] = x_train[i].str.split("-").str[0]
for i in l :
   x_test[i] = x_test[i].str.split("+").str[0]
for i in l :
    x_test[i] = x_test[i].str.split("-").str[0]
# for i in l :
   #x_test2[i] = x_test2[i].str.split("+").str[0]
#for i in l :
  #  x_test2[i] = x_test2[i].str.split("-").str[0]
x_train
# this function constructed to show if any columns have a nan value after spliting the data 

for i in l :
    if x_train[i].isnull().sum() == 0 :
        pass
    else :
        print( i  , "has nan value")

##   i will fill the missing value in [lw,lf,cf,cf .... ] with mean but i dont have the mean because Not all values are int so i cant use df.lw.mean() so i replaced the NAN values with 0 
## then i will calculate the mean of all wanted columns then i fill the nan values with 
##df.lw.mean() == 54
##df.lf.mean() == 54
##df.cf.mean() == 54
##df.rf.mean() == 54
##df.rw.mean() == 54
##df.gk.mean() == 19
x_train.lw.fillna('54', axis = 0 , inplace = True)
x_train.lf.fillna('54', axis = 0 , inplace = True)
x_train.cf.fillna('54', axis = 0 , inplace = True)
x_train.rf.fillna('54', axis = 0 , inplace = True)
x_train.rw.fillna('54', axis = 0 , inplace = True)
x_train.gk.fillna('19', axis = 0 , inplace = True)
x_test.lw.fillna('54', axis = 0 , inplace = True)
x_test.lf.fillna('54', axis = 0 , inplace = True)
x_test.cf.fillna('54', axis = 0 , inplace = True)
x_test.rf.fillna('54', axis = 0 , inplace = True)
x_test.rw.fillna('54', axis = 0 , inplace = True)
x_test.gk.fillna('19', axis = 0 , inplace = True)
'''x_test2.lw.fillna('54', axis = 0 , inplace = True)
x_test2.lf.fillna('54', axis = 0 , inplace = True)
x_test2.cf.fillna('54', axis = 0 , inplace = True)
x_test2.rf.fillna('54', axis = 0 , inplace = True)
x_test2.rw.fillna('54', axis = 0 , inplace = True)
x_test2.gk.fillna('19', axis = 0 , inplace = True)
'''
for i in l :
   x_train[i]= x_train[i].astype(int)
for i in l :
   x_test[i]= x_test[i].astype(int)
 #for i in l :
   #x_test2[i]= x_test2[i].astype(int)
x_train.info()
x_train.select_dtypes("O").info()
x_train.drop('club_name' , axis = 1 , inplace= True)
x_test.drop('club_name' , axis = 1 , inplace= True)
#x_test2.drop('club_name' , axis = 1 , inplace= True)
x_train.head()
x_test
# Handle categorical data 
encoder = BinaryEncoder(cols=[  'league_name', 'nationality_name' ,'release_clause_eur' ,'work_rate' ,'club_position'  , 'preferred_foot'])
x_train=encoder.fit_transform(x_train)
x_test=encoder.transform(x_test)
# x_test2=encoder.transform(x_test2)
## Scaling data 
scaler = MinMaxScaler()
numerical_cols = list(x_train.select_dtypes(include=['int64', 'float64','int32']).columns)
x_train[numerical_cols] = scaler.fit_transform(x_train[numerical_cols])
x_test[numerical_cols] = scaler.transform(x_test[numerical_cols])
# x_test2[numerical_cols] = scaler.transform(x_test2[numerical_cols])
x_train.head()
x_test.head()
x_train.isnull().sum()
px.histogram(y_train)

