from data import *
import streamlit as st

st.set_page_config(
    page_title="Capstone Project Mida",
    page_icon="👋",
    layout='wide',
)

st.markdown(f"""
            <style>
                body {{
                    max-width: 80%
                }}
            </style>
            """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center"><b>Kualitas Pendidikan Rendah, Bagaimana Indonesia Mengatasinya?</b></h1>', unsafe_allow_html=True)
st.caption('<div style="text-align:center">Nur Khamidah</div>', unsafe_allow_html=True)
" "
st.caption('<div style="text-align:justify">Meneliti seberapa jauh perjalanan kualitas pendidikan Indonesia berdasarkan beberapa indikator, dan sejauh mana ketertinggalan Indonesia dibandingkan negara lain.</div>', unsafe_allow_html=True)

" "
i1, i2, i3 = st.columns([1,3,1])
with i2:
    st.image("https://cdn.pixabay.com/photo/2014/11/20/20/40/nelson-mandela-539834_1280.jpg", width=700)
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

drop, plot = st.columns([1, 2])
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
        yaxis_title='IQ Score')
    
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
        yaxis_title='PISA Score',
    )
    st.plotly_chart(rd)
    st.caption('Source: [National Center for Education Statistics](https://nces.ed.gov/surveys/pisa/idepisa/dataset.aspx)', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify">Padahal, banyak anak jenius Indonesia yang bersinar di mancanegara dan kerap mewakili Indonesia memenangkan berbagai ajang kompetensi kecerdasan tingkat internasional. Kerap kali anak Indonesia turut meraih berbagai prestasi yang tidak kalah gemilang.</div>', unsafe_allow_html=True)
" "
st.write('<div style="text-align:center"><b>PRESTASI ANAK INDONESIA DALAM SETAHUN TERAKHIR</b></div>', unsafe_allow_html=True)
" "
with st.container():
    met1, met2, met3, met4 = st.columns([1,1,1,1])
    met1.metric("Gold Medals", 8)
    met2.metric("Silver Medals", 20)
    met3.metric("Bronze Medals", 22)
    met4.metric("Honorable Mentions", 3)
st.caption('Source: [Berbagai Sumber](https://www.detik.com/)')
" "
st.markdown('<h5 style="text-align: justify">Lalu, kembali lagi ke pertanyaan, bagaimana bisa Indonesia memiliki kualitas pendidikan yang rendah ketika pada kenyataannya anak Indonesia kerap kali berprestasi di tingkat internasional?</h5>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify">Pengeluaran suatu negara dalam pengembangan pendidikan juga dapat dijadikan suatu indikasi apakah negara itu fokus dalam pengembangan pendidikannya atau tidak. Pemerintah Indonesia menggelontorkan hampir 20% dari total APBN. Hal ini bisa dibilang besar mengingat GDP Indonesia pada tahun 2021 sebesar Rp2,784.4 T. Berarti, sebanyak lebih dari 560 Triliun dikeluarkan oleh pemerintah untuk membangun pendidikan.</div>', unsafe_allow_html=True)

v3, plot3 = st.columns([1, 2])
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
            'text': 'PRESENTASE PENGELUARAN PEMERINTAH UNTUK PENDIDIKAN '+var3+' COUNTRIES'
            },
        xaxis=dict(
            title=var3+' Country',
            tickmode='linear'),
        yaxis_title="Percent Expenditure")
    st.plotly_chart(gv)
    st.caption('Source: [World Bank](https://data.worldbank.org/indicator/SE.XPD.TOTL.GB.ZS)', unsafe_allow_html=True)
" "
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

st.markdown('<div style="text-align:justify">Dalam tulisan ini, disoroti mengenai pemaparan Pisani terutama pada kesejahteraan guru yang masih harus menjadi perhatian serius bagi pemerintah. Data menunjukkan bahwa kesejahteraan guru di Indonesia masih rendah, dengan rata-rata gaji yang terbilang lebih kecil daripada gaji guru di negara lain di dunia.</div>', unsafe_allow_html=True)
" "
    
with st.expander('Hasil Analisis Regresi', expanded=True):
    g1, g2, g3 = st.columns([1,1,1])
    with g1:
        st.metric("Jumlah Guru Honorer di Indonesia", '48%*', delta=None)
        st.caption('*) Dari total sebanyak 2,923,758 guru di Indonesia')
        st.caption('Source: [Katadata, 2022](https://databoks.katadata.co.id/datapublish/2022/01/12/52-guru-di-indonesia-berstatus-pns)')
    with g2:
        st.metric("Guru Millenial di Indonesia", "29.29%*")
        st.caption('*) Berusia rentang 30-39 tahun, merupakan mayoritas usia guru di Indonesia.')
        st.caption("Source: [Katadata, 2021](https://databoks.katadata.co.id/datapublish/2022/01/11/mayoritas-guru-di-indonesia-generasi-milenial)")
    with g3:
        st.metric('Gaji Guru per bulan', 'Rp2,7 juta')
        st.caption('Lebih rendah Rp0.2 jt dari rata-rata pendapatan pekerja nasional Indonesia')
        st.caption('Source: [KBR.id](https://kbr.id/nasional/01-2020/bps__gaji_guru_dan_petani_di_bawah_rata_rata_nasional/101947.html)')
" "

st.markdown('<div style="text-align:justify">Untuk memvalidasi temuan ini, data berikut dipaparkan untuk menunjukkan bahwa dari 39 negara yang diteliti, Indonesia berada pada 5 negara dengan gaji guru terendah di dunia. </div>', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1])
with c1:
    st.plotly_chart(salidx_top)
with c2:
    st.plotly_chart(salidx_low)
st.caption('Source: [Etateach, 2021](https://etateach.com/teacher-salaries-around-the-world.html)', unsafe_allow_html=True)

st.markdown('<div style="text-align:justify">Diperoleh bahwa negara dengan gaji guru dalam US Dollar adalah Swiss, Australia, Luxembourg, Jerman, dan Kanada. Sebagaimana yang dipaparkan di atas, negara-negara ini memberikan kualitas pendidikan yang setara dengan gaji gurunya. Rata-rata indeks kualitas pendidikan mereka berada di angka 0.8 hingga mendekati 1. Sementara negara dengan gaji terendah dari 39 negara yang diteliti, mayoritas (4 dari 5) memiliki skor indeks kualitas pendidikan yang menengah ke bawah. </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:justify">Untuk memperjelas temuan, dilakukan analisis korelasi dan regresi untuk variabel-variabel di atas dan beebrapa variabel tambahan seperti proporsi pengguna internet suatu negara untuk mengetahui apakah konektivitas infrastruktur berbasis teknologi juga memengaruhi kualitas pendiidikan suatu negara, dengan data sebagai berikut:</div>', unsafe_allow_html=True)

with st.expander('Data Faktor-faktor yang Memengaruhi Kualitas Pendidikan', expanded=False):
    x1, x2, x3 = st.columns([1,3,1])
    with x2:
        st.dataframe(data)
        st.caption('Source: [National Center for Education Statistics](https://nces.ed.gov/surveys/pisa/idepisa/dataset.aspx), [World Bank Data](https://data.worldbank.org/indicator/IT.NET.USER.ZS), [United Nations](https://rankedex.com/society-rankings/education-index), and [Etateach, 2021](https://etateach.com/teacher-salaries-around-the-world.html)')

" "
st.markdown('<div style="text-align:justify">Korelasi antar variabel dapat dijelaskan dalam <i>heatmap</i> berikut.</div>', unsafe_allow_html=True)
w1, w2, w3 = st.columns([1,3,1])
with w2:
    st.plotly_chart(cor)

" "

st.markdown('<div style="Berdasarkan analisis regresi dengan data di atas, diperoleh hasil analisis sebagai berikut:</div>', unsafe_allow_html=True)

" "
r1, r2, r3, r4 = st.columns([1,1,1,1])
with r1:
    st.metric("Gaji Guru", "30.7%", 0.0000005)
    st.caption('Gaji guru menaikkan indeks kualitas pendidikan walaupun tidak signifikan*, tetapi secara individu, gaji guru berkontribusi pada 30.7% keragaman nilai indeks kualitas pendidikan.')
with r2:
    st.metric("Proporsi Pengguna Internet", "57.7%**", 0.005)
    st.caption('Proporsi pengguna internet suatu negara menaikkan indeks kualitas pendidikan secara signifikan** baik secara individu atau bersama dengan variabel lain.  Secara individu, proporsi pengguna internet berkontribusi pada 57.7% keragaman nilai indeks kualitas pendidikan.')
with r3:
    st.metric("Skor Membaca PISA", "32.8%**", 0.0006)
    st.caption('Skor membaca PISA suatu negara menaikkan indeks kualitas pendidikan secara signifikan** baik secara individu atau bersama dengan variabel lain.  Secara individu, skor membaca PISA berkontribusi pada 32.8% keragaman nilai indeks kualitas pendidikan.')
with r4:
    st.metric("Keseluruhan Variabel", "63.8%**")
    st.caption('Gaji guru, proporsi pengguna internet, dan skor membaca PISA secara bersama menaikkan indeks secara signifikan** dengan keragaman yang dijelaskan sebesar 63.8%. Proporsi pengguna internet dan skor membaca PISA berpengaruh secara signifikan terhadap indeks kualitas pendidikan.')
st.caption('''*) Pada level signifikansi 5%.
           **) Pada level signifikansi 1%.''')

st.markdown('<div style="text-align:justify">Diperoleh bahwa gaji tidak berkontribusi signifikan dalam menjelaskan indeks kualitas pendidikan, namun memiliki korelasi positif. Sementara konektivitas internet dan skor PISA sangat menjelaskan besaran indeks pendidikan.</div>', unsafe_allow_html=True)
" "
st.markdown('<h5 style="text-align:justify">Apa insight dan rekomendasi berdasarkan paparan sebelumnya?</h5>', unsafe_allow_html=True)

st.markdown('<div style="text-align:justify">Diperoleh bahwa gaji tidak berkontribusi signifikan dalam menjelaskan indeks kualitas pendidikan, namun memiliki korelasi positif. Sementara konektivitas internet dan skor PISA sangat menjelaskan besaran indeks pendidikan. Hal ini mengindikasikan bahwa suatu negara dengan kualitas pendidikan tinggi, salah duanya ditentukan oleh kualitas siswa yang tinggi dan dibersamai dengan konektivitas digital yang canggih.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:justify">Untuk memperbaiki kualitas pendidikan Indonesia, berdasarkan analisis ini, Indonesia perlu fokus pada bagaimana sistem pendidikannya mampu menghasilkan kualitas SDM yang berkualitas dan mampu berpikir kritis, serta memperbaiki infrastruktur digital dan memperluas konektivitas internetnya agar seluruh siswa di Indonesia mampu melihat dunia lebih luas melalui internet.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:justify">Walaupun gaji guru tidak berpengaruh langsung secara signifikan, tetapi melihat korelasinya yang cukup besar (>50%) dengan indeks kualitas pendidikan, menunjukkan bahwa secara tidak langsun variabel ini berpengaruh. Diperlukan perhatian khusus dari pemerintah terhadap kesejahteraan guru yang secara tidak langsung akan berpengaruh pada perbaikan kualitas pendidikan Indonesia di masa depan.</div>', unsafe_allow_html=True)

