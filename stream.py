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

## PISA 
pisa_score = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/79countries_rankedpisa.csv", sep=",")
pisa_score_sum = pisa_score
pisa_score_sum['sum_all'] = pisa_score_sum['reading']+pisa_score_sum['math']+pisa_score_sum['science']
pisa_score_sum = pisa_score_sum.sort_values('sum_all', ascending=False)
pisa_score_use = pisa_score[pisa_score.country_name.isin(G20_OECD)].sort_values('sum_all', ascending=False)

pisa = go.Figure()
pisa.add_trace(go.Bar(
    x=pisa_score_use['country_name'],
    y=pisa_score_use['reading'],
    name='Reading',
    orientation='v',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    ),
    customdata=pisa_score_use['rank_reading'],
    hovertemplate='Country: %{x}<br>'+
        'Reading Score: %{y}<br>'+
        'Reading Rank: %{customdata} <br>'+
        '<extra></extra>',
))
pisa.add_trace(go.Bar(
    x=pisa_score_use['country_name'],
    y=pisa_score_use['math'],
    name='Math',
    orientation='v',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    ),
    customdata=pisa_score_use['rank_math'],
    hovertemplate='Country: %{x}<br>'+
        'Math Score: %{y}<br>'+
        'Math Rank: %{customdata} <br>'+
        '<extra></extra>',
))
pisa.add_trace(go.Bar(
    x=pisa_score_use['country_name'],
    y=pisa_score_use['science'],
    name='Science',
    orientation='v',
    marker=dict(
        color='rgba(187, 38, 8, 0.6)',
        line=dict(color='rgba(58, 79, 80, 1.0)', width=3)
    ),
    customdata=pisa_score_use['rank_science'],
    hovertemplate='Country: %{x}<br>'+
        'Science Score: %{y}<br>'+
        'Science Rank: %{customdata} <br>'+
        '<extra></extra>',
))

pisa.update_layout(barmode='stack')

## IQ

iq_score = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/199countries_iqscore.csv", sep=",")

iq_score_use = iq_score[iq_score.country.isin(G20_OECD)].sort_values('iq', ascending=False)
iq_score_use.rename({'Unnamed: 0':'rank'}, axis=1, inplace=True)

iq = go.Figure()
iq.add_trace(go.Scatter(
    x=iq_score_use['country'],
    y=iq_score_use['iq'],
    mode='markers',
    customdata=iq_score_use['rank'],
    hovertemplate='Country: %{x}<br>'+
    'Score: %{y}<br>'+ 'Rank: %{customdata}<br>'+
    '<extra></extra>'
))

## GOV SPENDING

gov_spending192 = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/192countries_govexpend.csv", sep=",")
gov_spending39 = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/39countries_govspendonedu.csv", sep=",")

gov = go.Figure()
gov.add_trace(go.Bar(
    x=gov_spending39['country_name'],
    y=gov_spending39['gov_expenditure'],
    orientation='v',
    marker=dict(
        color='rgba(187, 138, 68, 0.6)',
        line=dict(color='rgba(58, 79, 80, 1.0)', width=3)
    ),
    hovertemplate='Country: %{x}<br>'+
        'Expenditure: %{y}'+'%'+'<br>'+
        '<extra></extra>',
))

## SALARY

salary = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/39countries_salary.csv")
salary['salary'][salary['country_id'] == 'SWE'] = 37000
salary_use = salary
salary_use['ratio'] = salary_use['expenditure_percapita']/salary_use['salary']
salary_use = salary_use.sort_values('salary', ascending=False)

sal = go.Figure(data=[
    go.Bar(name='Salary (Year) in USD', 
           x=salary_use['country_name'], 
           y=salary_use['salary'],
           hovertemplate='Country: %{x}<br>'+
           'Salary: %{y}'+'USD'+'<br>'+
           '<extra></extra>',
           ),
    go.Bar(name='Expenditure Percapita', 
           x=salary_use['country_name'], 
           y=salary_use['expenditure_percapita'],
           customdata=salary_use['ratio'].round(2),
           hovertemplate='Country: %{x}<br>'+
           'Expenditure Percapita: %{y}'+'USD'+'<br>'+
           'Ratio: %{customdata}'+'%'+
           '<extra></extra>',
           )],
                )
# Change the bar mode
sal.update_layout(barmode='group',
                  legend=dict(
                      yanchor='top',
                      y=0.99,
                      xanchor='right',
                      x=0.99
                  ))

## ALL

all_data = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/39countries_alldata.csv", sep=",")

## REG

cor = px.imshow(all_data.corr('pearson'))
all_data['ratio'] = all_data['expenditure_percapita']/all_data['salary']
y = all_data['country_index']
X = all_data[['salary', 'net_user','reading_mean', 'math_mean', 'science_mean']]

X2 = sm.add_constant(X)
res = sm.OLS(y, X2).fit()
summary = res.summary()

model = LinearRegression()
model.fit(X, y)
model_r2 = model.score(X, y)

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
    
## FIX MULT

X['pisa'] = (X['math_mean']+X['reading_mean']+X['science_mean'])/3
X_new = X[['salary', 'pisa', 'net_user']]

model_2 = LinearRegression()
model_2.fit(X_new, y)
model2_r2 = model_2.score(X_new, y)

multicollinearity2 = multicollinearity_assumption(model_2, X_new, y)
linearity2 = linear_assumption(model_2, X_new, y)

X2_new = sm.add_constant(X_new)
res2 = sm.OLS(y, X2_new).fit()
summary2 = res2.summary()

x = X_new['salary']
y2 = X_new['pisa']
x2 = sm.add_constant(x)
res3 = sm.OLS(y2, x2).fit()
summary3 = res3.summary()

## EDU GAP

# edu_gap = pd.read_csv("https://raw.githubusercontent.com/nurkhamidah/Education_Dashboard/master/34provinces_edugap.csv", sep=",")
# edu_gap['prov_name'].replace('D.K.I. Jakarta', 'Jakarta Raya', inplace=True)
# edu_gap['prov_name'].replace('D.I. Yogyakarta', 'Yogyakarta', inplace=True)
# edu_gap['prov_name'].replace('Kepulauan Bangka Belitung', 'Bangka Belitung', inplace=True)
# edu_gap['ratio'] = edu_gap['rata_lama_sekolah']/edu_gap['angka_hls']


# geojson2 = requests.get(
#     "https://raw.githubusercontent.com/bimaputra1/School_Partitipation_Rates_with_GeoPandas/master/gadm36_IDN_1.json"
# ).json()


# # dataframe with columns referenced in question
# df = pd.DataFrame(
#     {"Column": pd.json_normalize(geojson2["features"])["properties.NAME_1"]}
# ).assign(Columnnext=lambda d: d["Column"].str.len())

# fig8 = go.Figure(
#     data=go.Choropleth(
#         geojson=geojson2,
#         locations=df["Column"],  # Spatial coordinates
#         featureidkey="properties.NAME_1",
#         z=edu_gap["ratio"],  # Data to be color-coded
#         colorscale="Reds",
#         colorbar_title="Ratio",
#     )
# )
# fig8.update_geos(fitbounds="locations", visible=False)


import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Capstone Project Mida",
    page_icon="👋",
)

st.title('Kualitas Pendidikan Rendah, Bagaimana Indonesia Mengatasinya?')
st.caption('Meneliti seberapa jauh perjalanan kualitas pendiidkan Indonesia berdasarkan beberapa indikator, dan sejauh mana ketertinggalan Indonesia dibandingkan negara lain.')


st.image("https://cdn.pixabay.com/photo/2014/11/20/20/40/nelson-mandela-539834_1280.jpg")
st.caption("Source: Pixabay/ben_kerckx-69781")

"Seorang mantan presiden Afrika Selatan sekaligus pejuang hak bagi rakyat kulit hitam, Nelson Mandela, pernah berkata bahwa  “Education is the most powerful weapon to change the world”. Pendidikan adalah senjata paling ampuh untuk mengubah dunia."

st.subheader("Memangnya, sejauh apa pentingnya pendidikan dan seberapa besar dunia bisa berubah karena pendidikan?")

"Sebelum dan selama perang dunia II, Kota Hiroshima, Jepang, menjadi kota pusat pendidikan barat. Sejak 1868, Jepang sudah berusaha memajukan masyarakatnya melalui pendidikan sejak zaman modern melalui pendirian Departemen Pendidikan, pengaturan sistem pendidikan, dan berbagai pelatihan bagi guru. Hal ini menunjukkan bagaimana pentingnya pendidikan bagi Jepang kala itu. Namun setelah pengeboman yang terjadi oleh Amerika Serikat pada 6 Agustus 1945, Hiroshima luluh oleh bom atom tersebut. Singkat cerita, sebagaimana dilansir dari Hiroshima for Global Peace <https://hiroshimaforpeace.com/en/fukkoheiwakenkyu/vol1/1-52/>, kesadaran untuk membangkitkan kembali semangat pendidikan di Jepang sedemikian rupa muncul yang bertujuan membangun pola pikir rasional dan ilmiah generasi mudanya tidak mudah disesatkan di masa depan. "

"Dan nyata, benar bahwa melalui kebijakan dan langkah besar dalam memajukan pendidikan tersebut, saat ini Jepang menjadi negara maju dan terlihat dari banyaknya pemenang Nobel asal Jepang dari berbagai bidang sebanyak 22 orang. Dapat dikatakan, melalui sistem pendidikan Jepang yang fokus mengembangkan kualitas masing-masing individu sesuai minat dan keahliannya masing-masing, Jepang terbukti mampu menghasilkan SDM unggul dan berkualitas, baik di tingkat Asia maupun dunia."

"Lalu, bagaimana dengan anak-anak Jepang saat ini?"

"Ulster Institute pada tahun 2019 melalui artikelnya yang berjudul 'The Intelligence of Nations' meneliti mengenai skor rata-rata IQ dari 199 negara di dunia. Selaras dengan pemaparan sebelumnya, bahwa negara yang menduduki peringkat pertama adalah Jepang dengan skor rata-rata IQ sebesar 106.48." 

st.plotly_chart(iq)

"Mengukur kualitas pendidikan suatu negara adalah dengan melihat siswanya. Selain melalui skor IQ rata-rata, cara lain untuk mengukur seberapa jauh kualitas pendidikan di suatu negara adalah dengan PISA (Program for International Student Assessment). Program ini melakukan asesmen kualitas pendidikan dengan mengukur performa akademik pelajar sekolah berusia 15 tahun. Bidang yang diteliti adalah matematika, sains, dan kemampuan membaca. Dilaksanakan setiap tahun dan diawali tahun 2000, pelaksanaan PISA tahun 2018 dilaksanakan oleh 78 negara di dunia. Asesmen kompetensi matematika menguji bagaimana siswa memecahkan masalah dengan konteks di dunia nyata, sementara tes sains menguji kompetensi untuk menjelaskan fenomena secara ilmiah, mengevaluasi dan merancang penyelidikan ilmiah, dan menafsirkan data dan bukti secara ilmiah. Kemudian, PISA mengukur kompetensi membaca siswa di mana para siswa diharapkan tidak hanya mampu membaca, lebih jauh siswa diharapkan mampu memahami, merenungkan, mengkonstruksi, dan memperluas makna dari apa yang dibaca serta terlibat dengan teks tertulis untuk mencapai tujuannya, mengembangkan pengetahuan dan potensi seseorang, dan berpartisipasi dalam masyarakat. Jepang kali ini juga menunjukkan kualiitasnya. Dalam asesmen PISA, Jepang menduduki peringkat 6 untuk matematika dan sains, serta 15 untuk membaca dari 78 negara yang diteliti." 

"Hasil asesmen PISA ini menjadi penting untuk mengukur seberapa baik kualitas pendidikan suatu negara. Hasil skor PISA yang rendah menunjukkan bahwa siswa Indonesia tidak mempunyai basic skills yang nanti akan dibutuhkan di masa depan, seperti problem solving capability melalui critical thinking. Lebih jauh, dengan kualitas SDM yang rendah tentu Indonesia memiliki banyak PR ketika di era Masyarakat Ekonomi ASEAN (MEA), di mana tenaga kerja bebas lintas negara."

st.subheader("Lalu Bagaimana dengan Indonesia?")

"Kualitas Indonesia masih jauh untuk dikatakan sempurna. Berdasarkan nilai IQ, Indonesia berada di peringkat 130 dari 199 negara atau peringkat kedua terbawah dari 12 negara-negara Asia Tenggara. Skor PISA Indonesia juga terbilang rendah, di bawah rata-rata dunia. Indonesia berada di peringkat 72 untuk kompetensi matematika, 71 untuk kompetensi sains, dan 73 untuk kompetensi membaca. Dari sini terlihat bhawa negara kita masih jauh tertinggal dibandingkan Jepang apalagi negara-negara maju lainnya seperti China yang berada di peringkat 1, dan negara tetangga Singapura di peringkat 2."

st.plotly_chart(pisa)

"Padahal, banyak anak jenius Indonesia yang bersinar di mancanegara dan kerap mewakili Indonesia memenangkan berbagai ajang kompetensi kecerdasan tingkat internasional. Kerap kali anak Indonesia turut meraih berbagai prestasi yang tidak kalah gemilang. Dilansir dari voi.id, Indonesia memenangkan 6 medali di ajang International Mathematical Olympiad (IMO) 2022 in Oslo, Norway. Dalam kesempatan tersebut, Andrew Daniel Janong dari SMAK 5 Penabur Jakarta, menerima Honorable Mention Award dan Rafael Kristoforus Yanto dari SMAK Penabur Gading Serpong medali silver. Total dari kesempatan tersebut, ada 6 medali yang diraih oleh anak Indonesia. Tentu masih banyak lagi prestasi anak Indonesia yang belum sempat disebutkan di tulisan ini."

"Lalu, kembali lagi ke pertanyaan, bagaimana bisa Indonesia memiliki kualitas pendidikan yang rendah ketika pada kenyataannya anak Indonesia kerap kali berprestasi di kancah internasional?"

"Pengeluaran suatu negara dalam pengembangan pendidikan juga dapat dijadikan suatu indikasi apakah negara itu fokus dalam pengembangan pendidikannya atau tidak. Namun, pemerintah Indonesia menggelontorkan hampir 20% dari total GDP atau Gross Domestic Product (Statista, 2021). Hal ini bisa dibilang besar mengingat GDP Indonesia pada tahun 2021 sebesar Rp16,970.8 T. Berarti, sebanyak lebih dari 3000 Triliun dikeluarkan oleh pemerintah untuk membangun pendidikan."

st.plotly_chart(gov)

st.subheader("Lalu, apa yang menjadi penyebab kualitas pendidikan Indonesia rendah?")

"Lizabeth Pisani, salah seorang jurnalis Reuters, menulis satu buku berjudul “Indonesia Etc: Exploring the Improbable Nation” (2013), salah satu buku yang mendapat banyak pengakuan di dunia internasional. Dalam buku itu, Pisani menyoroti bagaimana kualitas pendidikan Indonesia utamanya dilihat dari skor PISA-nya. Pisani memaparkan berdasarkan hasil analisisnya bahwa kualitas pendidikan Indonesia yang rendah bisa disebabkan dari beberapa faktor, antara lain: anggaran besar yang tidak terserap secara optimal untuk pendidikan, kualitas guru yang masih rendah yang salah satu sebabnya adalah passion mengajar rendah, banyak guru yang kerap mangkir atau membolos, tidak ada sistem semacam reward bagi guru yang inovatif, serta sistem pendidikan yang tidak mendorong siswanya dalam berpikir kritis."

"Pemaparan Pisani dalam bukunya memang ada benarnya. Salah satu yang penulis soroti adalah anggaran yang tidak terserap dan passion guru dalam mengajar yang rendah. Sebagaimana penelitian oleh Rosmanida dkk (2022) dengan judul 'The Effect of Salary Amount on Teachers' Performance' yang menyoroti rendahnya gaji guru mempengaruhi performa dalam mengajar di kelas akibat fokusnya yang terpecah untuk menggeluti usaha sampingan. Selain itu, hasil yang sama juga dipaparkan oleh Arain dkk (2014) di mana gaji guru memiliki relasi positif dengan performa siswa yang dinilai dari skor PISA-nya. Kemudian, terdapat penelitian oleh Kalikulla (2017) yang berjudul 'Pengaruh Kesejahteraan Guru, Motivasi Kerja dan Kompetensi Guru Terhadap Kinerja Guru' dengan studi kasus SMK di Kabupaten Sumba Barat menyatakan hasil yang signifikan terkait pengaruh kesejahteraan guru terhadap kinerja guru. Dari sini dapat diperoleh satu gambaran kecil bahwa bagaimana negara menghargai jasa gurunya akan menentukan bagaimana performa guru yang lebih jauh berimplikasi pada kualitas pendidikan melalui performa siswa."

st.plotly_chart(sal)

"Tahun 2018, United Nations Educational, Scientific, and Cultural Organization (UNESCO) merilis indeks pengembangan manusia (Human Development Index), di mana, salah satu komponennya adalah Education Index atau indeks pendidikan. Indeks Pendidikan ini diukur dengan menggabungkan rata-rata tahun sekolah untuk orang dewasa dengan tahun sekolah yang diharapkan untuk anak-anak, masing-masing menerima bobot 50%. Kemudian, penulis melakukan analisis terkait faktor penentu indeks pendidikan berdasarkan faktor yang dipaparkan oleh Pisani dalam bukunya. Dalam hal ini, akan dicoba untuk meneliti bagaimana pengaruh skor PISA dan besaran gaji guru, serta dengan tambahan variabel proporsi penduduk yang mengakses intenret di suatu negara terhadap besaran indeks pendidikan. Penambahan variabel presentase akses internet dimaksudkan untuk mengetahui apakah konektivitas secara digital juga memengaruhi bagaimana pendidikan di suatu negara, mengingat teknologi berkembang sangat cepat dan memungkinkan siswa dengan internet mampu mengakses ilmu pengetahuan dan teknologi yang berkembang di seluruh dunia secara up to date. Data disajikan dalam tabel berikut."

data = all_data[['country_id', 'country_name', 'net_user', 'salary', 'reading_mean', 'math_mean', 'science_mean', 'country_index']]
st.dataframe(data)

"Dengan korelasi sesuai plot sebagai berikut:"

drop, plot = st.columns([1, 3])
vars = ['gov_expenditure', 'reading_mean', 'math_mean', 'science_mean', 'salary', 'net_user', 'expected_school', 'years_school']
with drop:
    var = st.selectbox('Pilih Korelasi:', vars)
    st.plotly_chart(px.scatter(all_data, x=var, y = 'country_index'))

"Berdasarkan analisis regresi dengan data di atas, diperoleh hasil analisis sebagai berikut:"

st.write(summary3)
st.write(" ")

"Diperoleh bahwa gaji tidak berkontribusi signifikan dalam menjelaskan indeks kualitas pendidikan, namun memiliki korelasi positif. Sementara konektivitas internet dan skor PISA sangat menjelaskan besaran indeks pendidikan. Sebanyak 65% keragaman indeks pendidikan ditentukan oleh dua faktor ini, sementara 35% sisanya ditentukan variabel lain yang tidak dimasukkan dalam analisis. Hal ini mengindikasikan bahwa suatu negara dengan kualitas pendidikan tinggi, salah duanya ditentukan oleh kualitas siswa yang tinggi dan dibersamai dengan konektivitas digital yang canggih. Untuk memperbaiki kualitas pendidikan Indonesia, berdasarkan analisis ini, Indonesia perlu fokus pada bagaimana sistem pendidikannya mampu menghasilkan kualitas SDM yang berkualitas dan mampu berpikir kritis, serta memperbaiki infrastruktur digital dan memperluas konektivitas internetnya agar seluruh siswa di Indonesia mampu melihat dunia lebih luas melalui internet."

"Masih banyak pekerjaan rumah Indonesia dalam memperbaiki kualitas pendidikannya, mengingat saat ini peringkat indikator pendidikan Indonesia masih rendah. Namun bukan berarti tidak mungkin jika terus diusahakan. "


