import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # read data from file 
    df=pd.read_csv("epa-sea-level.csv")
    y= df["CISRO Adjusted Sea Level"]
    x= df["Year"]

    #create a scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    #create first line of best fit
    res=linregress(x,y)
    x_pred = pd.Series([i for i in range(1880,2050)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred,y_pred,"r")

    #create second line of best fit
    new_df= df.loc[df['Year'] >=2000]
    new_x= new_df['Year']
    new_y=new_df['CISRO Adjusted Sea Level']
    res_2= linregress(new_x,new_y)
    x_pred2= pd.Series([i for i in range(2000,2050)])
    y_pred2= res_2.slope*x_pred2 + res_2.intercept
    plt.plot(x_pred2,y_pred2,'green')


    # add labels and title 
    ax.set_xlabel('Year')
    ax.set_ylabel('CISRO Adjusted Sea Level')
    ax.set_title('rise in sea level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()