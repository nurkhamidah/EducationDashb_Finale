from data import *
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


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


