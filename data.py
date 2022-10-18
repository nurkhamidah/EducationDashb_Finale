import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

## Define Country
G20_OECD = ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 
       'Japan', 'Korea', 'Mexico', 'Russia', 'Saudi Arabia', 'South Africa', 'Türkiye', 'Turkey', 'United Kingdom', 
       'United States', 'European Union', 'Austria', 'Belgium', 'Canada', 'Chile', 'Czech Republic', 'Denmark', 'Estonia', 
       'Finland', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Portugal', 'Slovak Republic', 'Slovakia', 'Slovenia',
       'Spain', 'Sweden', 'Switzerland', 'Malaysia', 'Singapore', 'Myanmar', 'Thailand', 'Brunei Darussalam', 'Viet Nam', 'Philippines',
       'Timor Leste', 'Cambodia']

EU = ['AUT', 'BEL', 'BGR','HRV', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE', 'GBR']
G20 = ['ARG', 'AUS', 'AUT', 'BEL', 'BGR', 'BRA', 'CAN', 'CHN', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'HRV', 'IND', 'IDN', 'ITA', 'IRL', 'ITA', 'LVA', 'LTU', 'JPN', 'KOR', 'LUX', 'MEX', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'RUS', 'SAU', 'SVK', 'SVN', 'ESP', 'SWE', 'ZAF', 'TUR', 'GBR', 'USA', 'OED']

OECD =['AUS', 'AUT', 'BEL', 'CAN', 'CHE', 'DEU', 'DNK', 'ESP', 'FIN', 'FRA', 'GBR', 'GRC', 'IRE', 'ISL', 'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NOR', 'NZL', 'PRT', 'SWE', 'TUR', 'USA', 'OED']
ASEAN = ['BRN', 'KHM', 'IDN', 'LAO', 'MYS', 'MMR', 'PHL', 'SGP', 'THA', 'VNM', 'OED']

# DEFINE COLOR
other = '#8E8D8A'
point = '#E85A4F'
bg = '#EAE7DC'

## PISA 

pisa_read = pd.read_csv('https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/pisa_read.csv', sep=";")
pisa_read['color'] = other
pisa_read['color'][pisa_read['country_id']=='IDN'] = point


## IQ

IQ = pd.read_csv('https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/IQ.csv', sep=";")
IQ['color'] = other
IQ['color'][IQ['country_id']=='IDN'] = point
iq_score = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/199countries_iqscore.csv", sep=",")


## GOV SPENDING

gov_spending192 = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/192countries_govexpend.csv", sep=",")
gov_spending39 = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/39countries_govspendonedu.csv", sep=",")

gov_spending192['color'] = other
gov_spending192['color'][gov_spending192['country_id']=='IDN'] = point


## SALARY

salary = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/39countries_salary.csv")
all_data = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/39countries_alldata.csv", sep=",")

all_data['salary'][all_data['country_id'] == 'SWE'] = 37000
salary_use = all_data
salary_use = salary_use.sort_values('salary', ascending=False)
salary_top = salary_use.sort_values('salary', ascending=True).tail(5)
salary_low = salary_use.sort_values('salary', ascending=True).head(5)

salidx_top = px.bar(salary_top, 
                    y='country_name', 
                    x='salary', 
                    orientation='h',
                    color='country_index',
                    range_color=[0.5,1],
                    width=500)
salidx_low = px.bar(salary_low, 
                    y='country_name', 
                    x='salary', 
                    orientation='h',
                    color='country_index',
                    range_color=[0.5,1],
                    width=500)
salidx_low.update_traces(customdata=salary_low['country_index'],
                         hovertemplate='Country: %{y}<br>'+
                                        'Teacher Salary: %{x}'+'USD'+'<br>'+
                                        'Index: %{customdata}'+'%'+
                                        '<extra></extra>')
salidx_top.update_traces(customdata=salary_top['country_index'],
                         hovertemplate='Country: %{y}<br>'+
                                        'Teacher Salary: %{x}'+'USD'+'<br>'+
                                        'Index: %{customdata}'+'%'+
                                        '<extra></extra>')

# Change the bar mode
salidx_top.update_layout(barmode='group',
                      title={
                        'text': '5 NEGARA PENDAPATAN TERTINGGI DI DUNIA (USD/Year)'
                        },
                      yaxis_title="Country",
                      legend=dict(
                        yanchor='top',
                        y=1.2,
                        xanchor='right',
                        x=0.99
                  ))
salidx_low.update_layout(barmode='group',
                      title={
                        'text': '5 NEGARA PENDAPATAN TERENDAH DI DUNIA (USD/Year)'
                        },
                      yaxis_title="Country",
                      legend=dict(
                        yanchor='top',
                        y=1.2,
                        xanchor='right',
                        x=0.99
                  ))

## REG

all_data['ratio'] = all_data['expenditure_percapita']/all_data['salary']
y = all_data['country_index']
X = all_data[['salary', 'net_user','reading_mean']]

data = all_data[['country_id', 'country_name', 'net_user', 'salary', 'reading_mean', 'country_index']]
data2 = data[['net_user', 'salary', 'reading_mean', 'country_index']]

corr = data2.corr()

cor = go.Figure()
cor.add_trace(go.Heatmap(z=corr.values,
                         x=corr.index.values,
                         y=corr.columns.values,
                         colorscale='rdbu',
                         zmin=-1, zmax=1,
                         text=corr.values.astype(str),
                         texttemplate="%{text:.2f}",
                         textfont={"size":16},
                         hovertemplate='X: %{x}<br>'+'Y: %{y}<br>'+
                         "Correlation: %{text:.2f}<br>"+'<extra></extra>'))

cor.update_layout(height=600,
                  width=600,
                  title={
                      'text': 'KORELASI ANTAR VARIABEL'
                  })

model = LinearRegression()
model.fit(X, y)
model_r2 = model.score(X, y)

X2 = sm.add_constant(X)
models = sm.OLS(y,X2)
summary = models.fit().summary()

## ASSUMPTIONS

def calculate_residuals(model, features, label):
    """
    Creates predictions on the features with the model and calculates residuals
    """
    predictions = model.predict(features)
    df_results = pd.DataFrame({'Actual': label, 'Predicted': predictions})
    df_results['Residuals'] = abs(df_results['Actual']) - abs(df_results['Predicted'])
    
    return df_results

def linear_assumption(model, features, label):
    """
    Linearity: Assumes that there is a linear relationship between the predictors and
               the response variable. If not, either a quadratic term or another
               algorithm should be used.
    """
    print('Assumption 1: Linear Relationship between the Target and the Feature', '\n')
        
    print('Checking with a scatter plot of actual vs. predicted.',
           'Predictions should follow the diagonal line.')
    
    # Calculating residuals for the plot
    df_results = calculate_residuals(model, features, label)
    
    # Plotting the actual vs predicted values
    sns.lmplot(x='Actual', y='Predicted', data=df_results, fit_reg=False, height=5)
        
    # Plotting the diagonal line
    line_coords = np.arange(df_results.min().min(), df_results.max().max())
    plt.plot(line_coords, line_coords,  # X and y points
             color='darkorange', linestyle='--')
    plt.title('Actual vs. Predicted')
    plt.show()
    
def normal_errors_assumption(model, features, label, p_value_thresh=0.05):
    """
    Normality: Assumes that the error terms are normally distributed. If they are not,
    nonlinear transformations of variables may solve this.
               
    This assumption being violated primarily causes issues with the confidence intervals
    """
    from statsmodels.stats.diagnostic import normal_ad
    print('Assumption 2: The error terms are normally distributed', '\n')
    
    # Calculating residuals for the Anderson-Darling test
    df_results = calculate_residuals(model, features, label)
    
    print('Using the Anderson-Darling test for normal distribution')

    # Performing the test on the residuals
    p_value = normal_ad(df_results['Residuals'])[1]
    print('p-value from the test - below 0.05 generally means non-normal:', p_value)
    
    # Reporting the normality of the residuals
    if p_value < p_value_thresh:
        print('Residuals are not normally distributed')
    else:
        print('Residuals are normally distributed')
    
    # Plotting the residuals distribution
    plt.subplots(figsize=(12, 6))
    plt.title('Distribution of Residuals')
    sns.distplot(df_results['Residuals'])
    plt.show()
    
    print()
    if p_value > p_value_thresh:
        print('Assumption satisfied')
    else:
        print('Assumption not satisfied')
        print()
        print('Confidence intervals will likely be affected')
        print('Try performing nonlinear transformations on variables')
        
def multicollinearity_assumption(model, features, label):
    """
    Multicollinearity: Assumes that predictors are not correlated with each other. If there is
                       correlation among the predictors, then either remove prepdictors with high
                       Variance Inflation Factor (VIF) values or perform dimensionality reduction
                           
                       This assumption being violated causes issues with interpretability of the 
                       coefficients and the standard errors of the coefficients.
    """
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    print('Assumption 3: Little to no multicollinearity among predictors')
        
    # Plotting the heatmap
    plt.figure(figsize = (10,8))
    sns.heatmap(pd.DataFrame(features, columns=features.columns).corr(), annot=True)
    plt.title('Correlation of Variables')
    plt.show()
        
    print('Variance Inflation Factors (VIF)')
    print('> 10: An indication that multicollinearity may be present')
    print('> 100: Certain multicollinearity among the variables')
    print('-------------------------------------')
       
    # Gathering the VIF for each variable
    VIF = [variance_inflation_factor(features, i) for i in range(0,len(features.columns))]
    for idx, vif in enumerate(VIF):
        print('{0}: {1}'.format(features.columns[idx], vif))
        
    # Gathering and printing total cases of possible or definite multicollinearity
    possible_multicollinearity = sum([1 for vif in VIF if vif > 10])
    definite_multicollinearity = sum([1 for vif in VIF if vif > 100])
    print()
    print('{0} cases of possible multicollinearity'.format(possible_multicollinearity))
    print('{0} cases of definite multicollinearity'.format(definite_multicollinearity))
    print()

    if definite_multicollinearity == 0:
        if possible_multicollinearity == 0:
            print('Assumption satisfied')
        else:
            print('Assumption possibly satisfied')
            print()
            print('Coefficient interpretability may be problematic')
            print('Consider removing variables with a high Variance Inflation Factor (VIF)')

    else:
        print('Assumption not satisfied')
        print()
        print('Coefficient interpretability will be problematic')
        print('Consider removing variables with a high Variance Inflation Factor (VIF)')
        
def autocorrelation_assumption(model, features, label):
    """
    Autocorrelation: Assumes that there is no autocorrelation in the residuals. If there is
                     autocorrelation, then there is a pattern that is not explained due to
                     the current value being dependent on the previous value.
                     This may be resolved by adding a lag variable of either the dependent
                     variable or some of the predictors.
    """
    from statsmodels.stats.stattools import durbin_watson
    print('Assumption 4: No Autocorrelation', '\n')
    
    # Calculating residuals for the Durbin Watson-tests
    df_results = calculate_residuals(model, features, label)

    print('\nPerforming Durbin-Watson Test')
    print('Values of 1.5 < d < 2.5 generally show that there is no autocorrelation in the data')
    print('0 to 2< is positive autocorrelation')
    print('>2 to 4 is negative autocorrelation')
    print('-------------------------------------')
    durbinWatson = durbin_watson(df_results['Residuals'])
    print('Durbin-Watson:', durbinWatson)
    if durbinWatson < 1.5:
        print('Signs of positive autocorrelation', '\n')
        print('Assumption not satisfied')
    elif durbinWatson > 2.5:
        print('Signs of negative autocorrelation', '\n')
        print('Assumption not satisfied')
    else:
        print('Little to no autocorrelation', '\n')
        print('Assumption satisfied')
        
def homoscedasticity_assumption(model, features, label):
    """
    Homoscedasticity: Assumes that the errors exhibit constant variance
    """
    print('Assumption 5: Homoscedasticity of Error Terms', '\n')
    
    print('Residuals should have relative constant variance')
        
    # Calculating residuals for the plot
    df_results = calculate_residuals(model, features, label)

    # Plotting the residuals
    plt.subplots(figsize=(12, 6))
    ax = plt.subplot(111)  # To remove spines
    plt.scatter(x=df_results.index, y=df_results.Residuals, alpha=0.5)
    plt.plot(np.repeat(0, df_results.index.max()), color='darkorange', linestyle='--')
    ax.spines['right'].set_visible(False)  # Removing the right spine
    ax.spines['top'].set_visible(False)  # Removing the top spine
    plt.title('Residuals')
    plt.show()  
    
linearity = linear_assumption(model, X, y)
normality = normal_errors_assumption(model, X, y)
multicollinearity = multicollinearity_assumption(model, X, y)
autocorrelation = autocorrelation_assumption(model, X, y)
homoscedascity = homoscedasticity_assumption(model, X, y)
