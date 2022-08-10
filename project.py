#Module
from importlib.util import module_from_spec
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import altair as alt

#Page Title, and modify the icon
image = Image.open('C:\Streamlit\stenv\photo\digi.png')
st.set_page_config(page_title= "Tips Aman Main Facebook Agar Bunda Tetap **_Slay_** :nail_care:", page_icon=image, layout="wide")

#hiding the in-built pop up menu in Streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#Sidebar for the Group Introduction
with st.sidebar:
    st.title("Satu Yang Tak Purnama (Kelompok 14)")
    st.write("Hai **_reader_**, kenalan yuk!")
    st.write("Kita kelompok 14, dari Kelas A program Digitalent Scholarship Kominfo - Women in Tech angkatan kedua. Langsung aja yuk, kita mulai perkenalan dari: ")
    
    st.header("Hanifah")
    image = Image.open('C:\Streamlit\stenv\photo\hanifah.jpg')
    st.image(image, caption='Aku di Universe lain')
    st.write('Wanita single hampir menginjak umur perak, sedang menghadapi midlife crisis.')
    st.write("[Kenal Hanifah lebih dalam>](https://instagram.com/aafhhins)")

    st.header("Anisya Purnamasari")
    image = Image.open("C:\Streamlit\stenv\photo\iron.jpeg")
    st.image(image, caption = "Cita-citaku ingin menjadi orang kaya seperti Tony Stark")
    st.write("Prinsip hidup : Heroes are made by the path they choose, not the powers they are graced with.")
    st.write("[Kenal Anisya lebih dalam>](https:/instagram.com/anisyapurnamasari)")

    st.header("Teti Purnama Sari Rambe")
    image = Image.open("C:\Streamlit\stenv\photo\hijab.jpeg")
    st.image(image, caption = "Aku ditengah jam makan siang kantor")
    st.write("Seperti driver ojek, aku adalah wanita tangguh yang kuat berjalan dibawah teriknya matahari dan derasnya hujan. xixixi")
    st.write("[Kenal Teti lebih dalam>](https:/instagram.com/tetty_purnama)")

    st.write(
        """
        Gimana, udah kenal kan? Kata orang, tak kenal maka tak sayang. Kalau kata kami, sudah kenal maka dukung kami jadi pemenang!!
        """
    )

#--Goes to the Article--
with st.container():
    st.title("Bacaan Ringan Sore Hari : Tips Aman Main Facebook Agar Bunda Tetap **_Slay_** :nail_care:")
    st.caption("Oleh : Satu Yang Tak Purnama - 5 Agustus 2022")


with st.container():
    
    st.markdown("![Alt Text](https://media.giphy.com/media/rjRkXQJBOt0d2/giphy.gif) ![Alt Text](https://media.giphy.com/media/oVCd7vRf5U8vQ8o2NP/giphy.gif)")
    left, middle, right = st.columns(3)
    with middle:
        st.caption("Animasi Logo Facebook")


    
with st.container():
    st.write(
        """
        Teruntuk Bunda yang gemar membaca dan berselancar di Internet. 
        \t Familiar dengan animasi di atas? Yak, ini adalah logo **_Facebook_** yang kemarin **_re-branding_** dengan nama **_Meta_**.
        Dengan jumlah pengguna bulanan Facebook mengungguli beberapa platform populer lainnya seperti Youtube (2,3 milliar), Whatsapp (2 milliar), dan Instagram (2 milliar).
        """
    )

#Bar_Chart Facebook
st.subheader("10 Media Sosial Paling Sering Digunakan di Indonesia")
    

source = pd.DataFrame({
    'Percentage (%)': [88, 84, 82, 79, 56, 50, 50, 35, 34, 29],
    'Social Media' : ['Youtube', 'WhatsApp', 'Facebook', 'Instagram', 'Twitter', 'FB Messenger', 'Line', 'LinkedIn', 'Pinterest', 'WeChat']
})

bar_chart = alt.Chart(source).mark_bar().encode(
    y='Percentage (%)',
    x='Social Media',
)

st. altair_chart(bar_chart, use_container_width=True)

#Back to content
st.write(
    """
    Di Indonesia, Facebook menempati peringkat 3 teratas dalam daftar medsos yang paling sering digunakan oleh penduduk dengan rentang usia 16 hingga 64 tahun.
    Persentase pengguna yang mengakses Facebook sebanyak 82 persen, tepat satu tingkat di bawah WhatsApp (84 persen), dan satu tingkat di atas Instagram (79 persen).
    Sejauh ini, total pengguna aktif medsos Indonesia mencapai 160 juta (59 persen dari total populasi), dengan rata-rata 3 jam 26 menit waktu yang dihabiskan untuk mengakses medsos dalam sehari.

    Peran medsos di era teknologi ini benar-benar luar biasa ya, Bun. Hanya dengan sekali klik, Bunda bisa terhubung dengan teman-teman SMA yang sudah lama tidak terhubung, bahkan Bunda
    bisa beli ini-itu tanpa perlu repot menghadapi panas terik dan macetnya perjalanan.
        
        
    Tapi, tahukah Bunda di balik kemudahannya, ada resiko yang harus diperhatikan loh. Berselancar di Internet, termasuk **_Facebook_** membutuhkan kehati-hatian dikarenakan
    medsos sendiri sangat rawan akan kejahatan yang nama kerennya disebut **_Cybercrime_** yang dapat terjadi dalam sekejap mata, tanpa Bunda tahu siapa pelakunya. Hii serem yaa..
        
    Berikut cerita nyata mengenai kejahatan dunia maya yang terjadi di Indonesia, korbannya adalah Ibu dari teman **_author_** sendiri lho.

    """  
    )

#Case 1
with st.container():
    left, middle, right = st.columns(3)
    with middle :
        image = Image.open("C:\Streamlit\stenv\photo\\lkp.jpeg")
        st.image(image, caption = "Akun yang sudah diambil alih", width = 300)
    st.write("Akun tersebut yang awalnya digunakan sebagai media pemasaran LKP salon milik beliau, sekarang sudah beralih fungsi sebagai penjual **_handphone_** yang jelas-jelas fiktif. Korban kejatahan ini lagi-lagi adalah orang-orang terdekat yang kenal dengan pemilik akun. Bunda hati-hati loh yaa terhadap penipuan yang mengatasnamakan orang-orang terdekat.")
    
    
    st.write("Mari kita ke contoh kasus kedua, apakah Bunda pernah melihat promo seperti ini?")
    left, middle, right = st.columns(3)
    with middle :
        image = Image.open("C:\Streamlit\stenv\photo\kuota.png")
        st.image(image, caption = "Penipuan berkedok jual kuota murah")
    
    st.write("Yak, promo di atas bukanlah akun resmi penjual kuota. Link yang terlampir di foto tersebut adalah link palsu yang nantinya meminta Bunda untuk mengisi data pribadi dan lainnya dengan kedok pengiriman kuota membutuhkan data yang lengkap. Bunda, kami tahu rasa senang melihat tawaran kuota gratis dengan jumlah yang banyak ini. Tapi, alangkah baiknya Bunda jangan mudah tergiur dengan promo seperti ini ya.\nDua gambar di atas tadi merupakan contoh dari sekian banyak modus kejahatan yang terjadi di dunia maya. Gimana, Bun? Mulai risau?")
    
    left, middle, right = st.columns(3)
    with middle :
        st.markdown("![Alt Text](https://media.giphy.com/media/pTkiNqY97QuNxgyjS8/giphy.gif)")
    
    
    st.write(
     """
     
     Sudah-sudah, silahkan tenang, sudahi khawatirnya. Dengan beberapa cerita di atas tadi, kami disini akan memberikan tips dan trick agar Bunda tetap aman dan nyaman bermain sosial media :
    \n 1. Sering-sering update aplikasi secara rutin. Bunda, jangan pelit kuota lho ya, update aplikasi tidak memakan kuota sebanyak saat Bunda nonton drama korea lho.
    
    \n 2. Membuat password yang sulit ditebak, namun Bunda harus tetap ingat. Ayo Bunda, yang passwordnya “cantik123” bisa mulai untuk memikirkan perubahan password-nya ya. Password yang baik terdiri dari kata yang sulit ditebak dan merupakan kombinasi dari angka, simbol, huruf kapital dan kecil.
    """
    )
    st.video("https://www.youtube.com/watch?v=q5DYkzOrz_I&ab_channel=ESET")
 
   
    st.write(
        """3. Sebaiknya kurangi dan hindari posting hal privasi, untuk mencegah pencurian data. Posting foto KTP dan pamer ATM tidak keren sama sekali, Bun.
        \n 4. Jangan mudah percaya dengan harga barang-barang yang dijual murah, pastikan akun yang posting iklan tersebut adalah akun resmi yang biasanya ditandai dengan tanda verified. \t[Agar Tidak Tertipu, Ini Cara Mengetahui Online Shop Abal-Abal>](https://www.kompas.com/tren/read/2021/11/18/190500965/agar-tak-tertipu-ini-cara-mengetahui-online-shop-abal-abal?page=all)
    """)

   
    st. write ("5. Jangan lupa cek kembali link website yang dilampirkan, link asli biasanya akan dapat dibedakan. Salah klik link, bisa berakibat pencurian data. \t[Cek Keamanan Web Melalui Google Transparency>](https://transparencyreport.google.com/safe-browsing/search)")
    left, right = st.columns(2)
    with left :
        image_1 = Image.open("C:\Streamlit\stenv\photo\secure.png")
        st.image(image_1, caption = "Salah satu indikasi situs web aman dan kredibel adalah adanya ikon gembok dan keterangan connection is secured", width= 400)

    with right :
        image_2= Image.open("C:\Streamlit\stenv\photo\english.jpg")
        st.image(image_2, caption = "Website palsu biasanya memiliki tata bahasa yang tidak baik", width= 400)

    st.write("6. Tanyakan kepada keluarga dan orang-orang terdekat yang lebih paham Internet daripada Bunda. Kami sebagai **_author_** sekaligus anak-anak yang melek internet sangat siap untuk membantu mengedukasi orangtua terkait Internet.") 


st.write(
    """Gimana, Bun? Mudah bukan menjaga keamanan data ketika bermain internet.
    **_Author_** berharap sekali dapat mengedukasi Bunda melalui artikel ini.
    Untuk kritik, saran, pertanyaan dan lainnya bisa hubungi kami di menu pop-up sebelah ya. 
    Ciaao~ Maju terus Wanita Indonesia!
    """
    )


left, middle, right = st.columns(3)
with middle :
    st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

#Satisfaction bar
with st.container():
    st.write('Apakah Artikel ini mengedukasi?')
    left, right = st.columns(2)
    with left:
        if st.button("Ya"):
            st.success('Terima kasih, semoga Artikel ini bermanfaat.')

    with right:
        if st.button("Tidak", key="2"):
            st.error('Ooops, mohon hubungi kami untuk kritik dan saran')
            