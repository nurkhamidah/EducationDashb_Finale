from email.errors import InvalidMultipartContentTransferEncodingDefect
from turtle import width
from data import *
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Capstone Project Mida",
    page_icon="👋",
    layout='wide',
)


st.title('Kualitas Pendidikan Rendah, Bagaimana Indonesia Mengatasinya?')
st.caption('Meneliti seberapa jauh perjalanan kualitas pendiidkan Indonesia berdasarkan beberapa indikator, dan sejauh mana ketertinggalan Indonesia dibandingkan negara lain.')

st.image("https://cdn.pixabay.com/photo/2014/11/20/20/40/nelson-mandela-539834_1280.jpg")
st.caption("Source: Pixabay/ben_kerckx-69781")

st.markdown('<div style="text-align: justify">Seorang mantan presiden Afrika Selatan sekaligus pejuang hak bagi rakyat kulit hitam, Nelson Mandela, pernah berkata bahwa <i>“Education is the most powerful weapon to change the world”</i>. Pendidikan adalah senjata paling ampuh untuk mengubah dunia.</div>', unsafe_allow_html=True)
''

st.markdown('<h5 style="text-align: justify">Memangnya, sejauh apa pentingnya pendidikan dan seberapa besar dunia bisa berubah karena pendidikan?</h5>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify">Mencontoh dari Jepang, sejak 1868 Jepang sudah berusaha memajukan masyarakatnya di bidang pendidikan melalui pendirian Departemen Pendidikan, pengaturan sistem pendidikan, dan berbagai pelatihan bagi guru baik sebelum maupun setelah perang dunia II. Walaupun melalui berbagai kendala, Jepang kini mampu menunjukkan eksistensinya sebagai negara dengan sumber daya manusia terbaik di dunia.</div>', unsafe_allow_html=True)
" "

m1, m2, m3, m4 = st.columns([1,1,1,1])
with m1:
    st.metric(label='1945s Atomic Bomb Damage', value='78 schools')
with m2:
    st.metric(label='1960s HS Enrollment', value="60%", delta='+20%')
with m3:
    st.metric(label='1960s Univs Enrollment', value="30%", delta='+20%')
with m4:
    st.metric(label='2021s Nobel Awards', value='29 nobels')
st.caption('Source: [Hiroshima for Peace](https://hiroshimaforpeace.com/en/fukkoheiwakenkyu/vol1/1-52)', unsafe_allow_html=True)
" "

st.markdown('<h4 style="text-align: justify">Lalu, bagaimana dengan anak-anak Jepang saat ini?</h4>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify"><i>Ulster Institute</i> pada tahun 2019 melalui artikelnya yang berjudul <b><i>The Intelligence of Nations</i></b> meneliti mengenai skor rata-rata IQ dari 199 negara di dunia. Selaras dengan pemaparan sebelumnya, bahwa negara yang menduduki peringkat pertama adalah Jepang dengan skor rata-rata IQ sebesar 106.48.</div>', unsafe_allow_html=True)
" " 

drop, plot = st.columns([1, 3])
vars = ['EU', 'OECD', 'G20', 'ASEAN', 'TOP 10', 'LOW 10']
with drop:
    var = st.selectbox('Pilih Kelompok:', vars)
    st.markdown('<div style="text-align: justify">Bisa terlihat pada tabel, bahwa di negara ASEAN sendiri, Indonesia masuk sebagai negara dengan rata-rata IQ terendah. Di antara negara-negara G20, rata-rata IQ Indonesia berada di urutan keempat terbawah, di atas 3 negara lainnya: Saudi Arabia, India, dan Afrika Selatan.</div>', unsafe_allow_html=True)
with plot:
    if var == 'EU':
        iq_score_use = IQ[IQ['country_id'].isin(EU)].sort_values('iq', ascending=False)
    elif var == 'OECD':
        iq_score_use = IQ[IQ['country_id'].isin(OECD)].sort_values('iq', ascending=False)
    elif var == 'ASEAN':
        iq_score_use = IQ[IQ['country_id'].isin(ASEAN)].sort_values('iq', ascending=False)
    elif var == 'TOP 10':
        iq_score_use = IQ.sort_values('iq', ascending=False).head(10)
    elif var == 'LOW 10':
        iq_score_use = IQ.sort_values('iq', ascending=False).tail(10)
    else:
        iq_score_use = IQ[IQ['country_id'].isin(G20)].sort_values('iq', ascending=False)
    iq = go.Figure()
    iq.add_trace(go.Scatter(
        x=iq_score_use['country_name'],
        y=iq_score_use['iq'],
        mode='markers',
        customdata=iq_score_use['rank'],
        hovertemplate='Country: %{x}<br>'+
        'Score: %{y}<br>'+ 'Rank: %{customdata} <br>'+
        '<extra></extra>',
        marker={'color':iq_score_use['color'],
                'size':10}
    ))
    iq.update_layout(
        title={
            'text': 'IQ SCORE '+var+' COUNTRIES'
            },
        xaxis=dict(
            title=var+' Country',
            tickmode='linear'),
        yaxis_title='IQ Score'
    )
    st.plotly_chart(iq)
st.caption('Source: [World Population Review](https://worldpopulationreview.com/country-rankings/average-iq-by-country)', unsafe_allow_html=True)
" "
        
st.markdown('<div style="text-align: justify">Sebuah program pengukur kualitas pendidikan, PISA (Program for International Student Assessment), melakukan asesmen kualitas pendidikan dengan mengevaluasi performa akademik pelajar sekolah berusia 15 tahun. Selain matematika dan sains, PISA mengukur kompetensi membaca siswa di mana para siswa diharapkan tidak hanya mampu membaca, lebih jauh siswa diharapkan mampu memahami dan memperluas makna dari apa yang dibaca secara kritis.</div>', unsafe_allow_html=True)
" "

me0, me1, me2 , me3, me4, me5= st.columns([0.5,1,1,1,1,0.5])
me1.metric("Jepang", 503.86, round(503.86-515.96,2))
me2.metric("Amerika Serikat", 505.35, round(505.35-496.94,2))
me3.metric("Indonesia", 370.97, round(370.97-397.26,2))
me4.metric("China", 524.28, round(524.28-526.68,2))
st.caption('Source: [National Center for Education Statistics](https://nces.ed.gov/surveys/pisa/idepisa/dataset.aspx)', unsafe_allow_html=True)


" "

v2, plot2 = st.columns([1, 2])
vars2 = ['EU ', 'OECD ', 'G20 ', 'ASEAN ', 'TOP 10 ', 'LOW 10 ']
with v2:
    var2 = st.selectbox('Pilih Kelompok:', vars2)
    st.markdown('<div style="text-align: justify">Hasil asesmen PISA ini menjadi penting untuk mengukur seberapa baik kualitas pendidikan suatu negara. Hasil skor PISA yang rendah (masuk 10 peringkat terbawah dari 79 negara) menunjukkan bahwa siswa Indonesia tidak mempunyai <i>basic skills</i> yang nanti akan dibutuhkan di masa depan, seperti <i>problem solving capability </i> melalui <i>critical thinking</i>. Lebih jauh, dengan kualitas SDM yang rendah tentu Indonesia memiliki banyak PR ketika di era Masyarakat Ekonomi ASEAN (MEA), di mana tenaga kerja bebas lintas negara.</div>', unsafe_allow_html=True)
with plot2:
    if var2 == 'EU ':
        pisa_read_use = pisa_read[pisa_read['country_id'].isin(EU)].sort_values('read', ascending=False)
    elif var2 == 'OECD ':
        pisa_read_use = pisa_read[pisa_read['country_id'].isin(OECD)].sort_values('read', ascending=False)
    elif var2 == 'ASEAN ':
        pisa_read_use = pisa_read[pisa_read['country_id'].isin(ASEAN)].sort_values('read', ascending=False)
    elif var2 == 'TOP 10 ':
        pisa_read_use = pisa_read.sort_values('read', ascending=False).head(10)
    elif var2 == 'LOW 10 ':
        pisa_read_use = pisa_read.sort_values('read', ascending=False).tail(10)
    else:
        pisa_read_use = pisa_read[pisa_read['country_id'].isin(G20)].sort_values('read', ascending=False)
    rd = go.Figure()
    rd.add_trace(go.Bar(
        x=pisa_read_use['country_name'],
        y=pisa_read_use['read'],
        name='Reading Skill',
        orientation='v',
        marker=dict(
            color=pisa_read_use['color']
        ),
        width=0.5,
        hovertemplate='Country: %{x}<br>'+
            'Reading Score: %{y}<br>'+
            '<extra></extra>',
    ))
    rd.update_layout(
        title={
            'text': 'PISA READING SCORE '+var2+' COUNTRIES'
            },
        xaxis=dict(
            title=var2+' Country',
            tickmode='linear'),
        yaxis_title='PISA Score'
    )
    st.plotly_chart(rd)
    st.caption('Source: [National Center for Education Statistics](https://nces.ed.gov/surveys/pisa/idepisa/dataset.aspx)', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify">Padahal, banyak anak jenius Indonesia yang bersinar di mancanegara dan kerap mewakili Indonesia memenangkan berbagai ajang kompetensi kecerdasan tingkat internasional. Kerap kali anak Indonesia turut meraih berbagai prestasi yang tidak kalah gemilang.</div>', unsafe_allow_html=True)


with st.container():
    met1, met2, met, met3, met4 = st.columns([1,1,1,1,1])
    met.metric("Gold Medals", 8)
    met2.metric("Silver Medals", 20)
    met1.write('<div style="text-align:left"><b>PRESTASI ANAK INDONESIA DALAM SETAHUN TERAKHIR</b></div>', unsafe_allow_html=True)
    met1.caption('Source: [Berbagai Sumber](https://www.detik.com/)')
    met3.metric("Bronze Medals", 22)
    met4.metric("Honorable Mentions", 3)
" "
st.markdown('<h5 style="text-align: justify">Lalu, kembali lagi ke pertanyaan, bagaimana bisa Indonesia memiliki kualitas pendidikan yang rendah ketika pada kenyataannya anak Indonesia kerap kali berprestasi di tingkat internasional?</h5>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify">Pengeluaran suatu negara dalam pengembangan pendidikan juga dapat dijadikan suatu indikasi apakah negara itu fokus dalam pengembangan pendidikannya atau tidak. Pemerintah Indonesia menggelontorkan hampir 20% dari total APBN. Hal ini bisa dibilang besar mengingat GDP Indonesia pada tahun 2021 sebesar Rp2,784.4 T. Berarti, sebanyak lebih dari 560 Triliun dikeluarkan oleh pemerintah untuk membangun pendidikan.</div>', unsafe_allow_html=True)

v3, plot3 = st.columns([1, 3])
vars3 = [' EU ', ' OECD ', ' G20 ', ' ASEAN ', ' TOP 10 ', ' LOW 10 ']
with v3:
    var3 = st.selectbox('Pilih Kelompok:', vars3)
    st.markdown('<div style="text-align: justify">Sebaliknya, jika di antara negara-negara G20 Indonesia memiliki rata-rata IQ terendah, pengeluaran pemerintah Indonesia untuk pendidikan termasuk besar dan menempati urutan kedua. Hal yang sama juga terjadi di ASEAN di mana Indonesia menempati negara kedua dengan pengeluaran pemerintah untuk pendidikan terbesar, yakni 19.153% dari GDP.</div>', unsafe_allow_html=True)
with plot3:
    if var3 == ' EU ':
        govs = gov_spending192[gov_spending192['country_id'].isin(EU)].sort_values('percent_total_expenditure', ascending=False)
    elif var3 == ' OECD ':
        govs = gov_spending192[gov_spending192['country_id'].isin(OECD)].sort_values('percent_total_expenditure', ascending=False)
    elif var3 == ' ASEAN ':
        govs = gov_spending192[gov_spending192['country_id'].isin(ASEAN)].sort_values('percent_total_expenditure', ascending=False)
    elif var3 == ' TOP 10 ':
        govs = gov_spending192.sort_values('percent_total_expenditure', ascending=False).head(10)
    elif var3 == ' LOW 10 ':
        govs = gov_spending192.sort_values('percent_total_expenditure', ascending=False).tail(10)
    else:
        govs = gov_spending192[gov_spending192['country_id'].isin(G20)].sort_values('percent_total_expenditure', ascending=False)
    gv = go.Figure()
    gv.add_trace(go.Bar(
        x=govs['country_name'],
        y=govs['percent_total_expenditure'],
        name='Percent Expenditure',
        orientation='v',
        marker=dict(
            color=govs['color'],
        ),
        width=0.5,
        customdata=govs['latest_year'],
        hovertemplate='Country: %{x}<br>'+
            'Expenditure %{y}'+'% <br>'+
            'Year: %{customdata} <br>'+
            '<extra></extra>',
    ))
    gv.update_layout(
        title={
            'text': 'GOVERNMENT EXPENDITURE OF GDP '+var3+' COUNTRIES'
            },
        xaxis=dict(
            title=var3+' Country',
            tickmode='linear'),
        yaxis_title="Percent Expenditure"
    )
    st.plotly_chart(gv)
    st.caption('Source: [World Bank](https://data.worldbank.org/indicator/SE.XPD.TOTL.GB.ZS)', unsafe_allow_html=True)

st.markdown('<h5 style="text-align: justify">Jadi, apa yang menjadi penyebab kualitas pendidikan Indonesia rendah?</h5>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify">Lizabeth Pisani, salah seorang jurnalis Reuters, menulis satu buku berjudul <b><i>Indonesia Etc: Exploring the Improbable Nation (2013)</i></b>, salah satu buku yang mendapat banyak pengakuan di dunia internasional. Dalam buku itu, Pisani menyoroti bagaimana kualitas pendidikan Indonesia utamanya dilihat dari skor PISA-nya. Pisani memaparkan berdasarkan hasil analisisnya bahwa kualitas pendidikan Indonesia yang rendah bisa disebabkan dari beberapa faktor, antara lain:</div>', unsafe_allow_html=True)
" "
c1, c2, c3, c4, c5 = st.columns([1,1,1,1,1])
c1.markdown('<div style="text-align: center"><b>Anggaran besar. tidak terserap optimal.</b></div>', unsafe_allow_html=True)
c2.markdown('<div style="text-align: center"><b>Kualitas guru rendah akibat minim passion mengajar.</b></div>', unsafe_allow_html=True)
c3.markdown('<div style="text-align: center"><b>Banyak kasus guru membolos.</b></div>', unsafe_allow_html=True)
c4.markdown('<div style="text-align: center"><b>Tidak ada sistem reward bagi guru inovatif.</b></div>', unsafe_allow_html=True)
c5.markdown('<div style="text-align: center"><b>Sistem pendidikan yang tidak mendorong siswa berpikir kritis.</b></div>', unsafe_allow_html=True)
" "

# p1, p2, p3 = st.columns([1,1,1])
# with p1:
#     st.metric("Kenaikan gaji guru", "10%", "0.15 points*")
#     st.caption("*) Skor Matematika dan Bahasa Inggris")
#     st.caption("Source: [Garcia & Han, 2022](https://journals.sagepub.com/doi/epub/10.1177/21582440221082138)")
# with p3:
#     st.metric('Performa siswa', "28%", "Gaji guru per jam")

st.markdown('<div style="text-align: justify">Lizabeth Pisani, salah seorang jurnalis Reuters, menulis satu buku berjudul <b><i>Pemaparan Pisani dalam bukunya memang ada benarnya. Salah satu yang perlu disoroti adalah anggaran yang tidak terserap dan passion guru dalam mengajar yang rendah.</div>', unsafe_allow_html=True)

g1, g2, g3 = st.columns([1,1,1])
with g1:
    st.metric('Gaji Guru per bulan', 'Rp2,7 juta', '-Rp 0,2 jt*')
    st.caption('*) dari rata-rata pendapatan pekerja nasional Indonesia')
    st.caption('Source: [KBR.id](https://kbr.id/nasional/01-2020/bps__gaji_guru_dan_petani_di_bawah_rata_rata_nasional/101947.html)')
    


c1, text1 = st.columns([2, 1])
with c1:
    st.plotly_chart(sal_top)
c2, text2 = st.columns([1, 2])
with c2:
    st.plotly_chart(sal_low)

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

st.write(summary2)
st.write(" ")

"Diperoleh bahwa gaji tidak berkontribusi signifikan dalam menjelaskan indeks kualitas pendidikan, namun memiliki korelasi positif. Sementara konektivitas internet dan skor PISA sangat menjelaskan besaran indeks pendidikan. Sebanyak 65% keragaman indeks pendidikan ditentukan oleh dua faktor ini, sementara 35% sisanya ditentukan variabel lain yang tidak dimasukkan dalam analisis. Hal ini mengindikasikan bahwa suatu negara dengan kualitas pendidikan tinggi, salah duanya ditentukan oleh kualitas siswa yang tinggi dan dibersamai dengan konektivitas digital yang canggih. Untuk memperbaiki kualitas pendidikan Indonesia, berdasarkan analisis ini, Indonesia perlu fokus pada bagaimana sistem pendidikannya mampu menghasilkan kualitas SDM yang berkualitas dan mampu berpikir kritis, serta memperbaiki infrastruktur digital dan memperluas konektivitas internetnya agar seluruh siswa di Indonesia mampu melihat dunia lebih luas melalui internet."

"Masih banyak pekerjaan rumah Indonesia dalam memperbaiki kualitas pendidikannya, mengingat saat ini peringkat indikator pendidikan Indonesia masih rendah. Namun bukan berarti tidak mungkin jika terus diusahakan. "


