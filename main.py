import streamlit as st
import webbrowser

# Streamlit page setup
st.set_page_config(page_title="Ethical Hacking Videos", page_icon=":guardsman:", layout="wide")
st.title("🎯 learn Ethical Hacking ")  
st.markdown("### A collection of ethical hacking video resources")
st.markdown("#### Note: This app is for educational purposes only.")

# Video list
videos = [
    {
        "title": "Ethical Hacking Full Course - Learn Ethical Hacking in 9 Hours",
        "url": "https://www.youtube.com/watch?v=3Kq1MIfTWCE"
    },
    {
        "title": "Introduction to Ethical Hacking",
        "url": "https://www.youtube.com/watch?v=KkF-DvDkEfo"
    },
    {
        "title": "Ethical Hacking Tutorial for Beginners",
        "url": "https://www.youtube.com/watch?v=3Kq1MIfTWCE"
    }

]

# Session state to track opened videos
if 'past_links' not in st.session_state:
    st.session_state.past_links = []

# Dropdown to select a video
video_titles = [video["title"] for video in videos]
selected_title = st.selectbox("🎥 Select a video to watch:", video_titles)

# Button to open the video
if st.button("🔗 Open Video in Browser"):
    selected_video = next((video for video in videos if video["title"] == selected_title), None)
    if selected_video:
        webbrowser.open_new_tab(selected_video["url"])
        st.session_state.past_links.append(selected_video)

# Display past opened videos
if st.session_state.past_links:
    st.markdown("### 📜 Previously Opened Videos")
    for vid in st.session_state.past_links:
        st.markdown(f"- [{vid['title']}]({vid['url']})")

st.markdown("### 📜 Disclaimer")
st.markdown("This app is for educational purposes only. The videos provided are for learning and research in ethical hacking.")
st.markdown("Always ensure you have permission to test any system or network before attempting any hacking techniques.")
st.markdown("### 📜 Note")
st.markdown("This app is for educational purposes only. The videos provided are for learning and research in ethical hacking.")
st.markdown("Always ensure you have permission to test any system or network before attempting any hacking techniques.")
st.markdown("### 📜 Note you have this app to do hacking")
st.markdown("### 🛠 Useful Hacking Tools")

tools = {
    "Kali Linux": "https://www.kali.org/",
    "Wireshark": "https://www.wireshark.org/",
    "Metasploit": "https://www.metasploit.com/",
    "Burp Suite": "https://portswigger.net/burp",
    "Nmap": "https://nmap.org/",
    "OWASP ZAP": "https://www.zaproxy.org/",
    "termux": "https://termux.com/",
    "John the Ripper": "https://www.openwall.com/john/",
    "SQLMap": "https://sqlmap.org/",
    "Nikto": "https://cirt.net/Nikto2",

    "Aircrack-ng": "https://www.aircrack-ng.org/",
    }

for name, url in tools.items():
    st.markdown(f"- [{name}]({url})")
st.markdown("### 🛠 Useful Hacking Tools")


st.header("""


⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠃⣠⡞⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠘⣦⡀⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠋⢰⣿⠇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢹⣷⠀⢻⣿⣿⣿⣿
⣿⣿⣿⡿⠋⢰⣼⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣾⠀⠻⣿⣿⣿
⣿⣿⡿⢁⣾⠸⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⡟⢸⣆⠹⣿⣿
⣿⣿⡇⢾⣿⠀⣮⣿⣧⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⣿⣿⡖⢸⣿⡆⣿⣿
⣿⣿⡇⠘⢿⠀⠹⣿⣿⣆⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⣼⣿⡿⠃⣸⡟⠁⣿⣿
⣿⡟⣁⢸⣾⣧⠀⢶⣿⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢁⣾⣿⣿⠆⢀⣿⣿⢀⡙⣿
⣿⢀⣿⡀⠹⣿⣎⠀⢹⣿⣿⣧⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣠⣿⣿⣿⠁⠀⣾⡿⠃⣼⣧⢹
⣿⠀⢿⡷⡈⢿⣿⣎⢀⠙⠿⢿⡏⢆⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⡜⣿⡿⠟⠁⢀⣾⣿⠟⣰⣿⡏⢸
⠋⡀⢻⣷⡐⡀⢩⣿⠀⡀⡈⠲⠷⠈⢷⣦⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣡⣴⠏⢠⡿⠆⡀⠀⢸⣯⠅⠐⣸⣿⠇⡘
⠰⣷⡈⠻⣿⣌⠀⠙⠳⠄⠀⢰⣦⣄⠠⣿⣿⣷⣬⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣩⣴⣾⣿⡇⢀⣤⣶⡀⢀⡴⠟⠁⢀⣴⡿⠋⣰⣷
⣆⢻⣷⠀⠺⣿⣧⠀⠈⠲⡄⠸⠈⣻⣷⣌⠛⢿⣿⣿⣷⣌⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⣴⣿⣿⣿⠿⠋⣴⣿⡟⢸⠁⡴⠛⠀⢀⣾⡿⠂⣴⣿⢋
⣿⡄⣙⣆⠢⠈⢽⣷⠀⠀⣤⣄⠑⢼⣿⣿⠀⠀⢉⠻⠿⣿⣿⣦⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣡⣾⣿⡿⠿⢋⠁⠂⢀⣿⣿⠁⢀⣤⣄⠀⢠⣿⠍⠀⢂⣞⡁⣼
⣿⣷⠈⠻⣷⣌⠢⠘⢿⡀⠈⠿⣷⣦⣉⠻⢥⣂⠀⠀⢶⣦⣽⣿⣿⣆⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣾⣿⣿⣧⣴⠢⠀⠄⣪⠽⠋⣡⣶⣿⠟⠀⣸⠟⡁⢀⣴⡿⠏⢰⣿
⣿⣿⡇⣦⡐⠺⣿⡂⢐⠀⡈⠂⠽⣿⣿⠬⢐⠨⠁⠈⠻⢿⣿⣿⣿⣿⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⠿⠂⠀⠩⢀⠠⢴⣿⡿⠅⠈⡀⠄⠀⣶⡿⠖⣠⡆⣼⣿
⣿⣿⣷⡘⢿⣦⠀⠸⠶⣄⠀⢴⣶⣬⣉⢛⡒⠂⠀⢺⣿⣿⣿⣿⠋⣡⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⠻⣿⣿⣿⣿⠂⠀⠒⣚⣋⣩⣴⣶⠄⢀⡴⠾⠂⢠⣾⠟⣠⣿⣿
⣿⣿⣿⣧⠀⢽⣷⣬⡐⠈⠀⠀⠁⣛⣿⣖⣒⡂⠀⠙⢋⣿⣿⣿⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢸⣿⣿⣏⠙⠁⠀⣒⣒⣾⡿⠓⠁⠀⠈⠀⣠⣴⣿⠅⢀⣿⣿⣿
⣿⣿⣿⣿⣷⣤⡉⠛⣿⣷⣄⠀⠀⠀⣉⣉⣉⠭⠀⠀⢉⣿⢿⣿⣷⣦⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣡⣶⣿⣿⠻⣟⠃⠀⠩⢭⣍⣉⡁⠀⠀⢀⣶⣿⡟⠋⣁⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣭⠃⠠⢾⣿⣿⡿⠿⢒⠠⠀⠁⣾⣿⢿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⣿⣿⣿⠿⡿⡆⠀⠀⠀⠺⠿⣿⣿⣿⣧⠀⢫⣭⣴⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠼⠋⣡⣴⣾⣷⠤⠂⠀⠉⠁⣼⣿⣿⣿⣆⢻⣿⣿⣿⣿⣿⣿⢃⣴⣿⡿⡿⡆⠁⠀⠀⡐⢴⣾⣶⣦⡉⠻⠄⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠉⢿⡟⣡⣾⣶⠊⠀⠀⠙⠃⢿⣿⣿⣦⡙⢿⣿⣿⠟⣡⣾⣿⣿⠇⠁⠁⡀⡈⠲⣿⣦⡙⠿⠏⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⡉⢰⣿⣿⢃⣾⡶⢀⣴⢂⣶⣶⣶⣬⣥⣶⣿⣿⣦⣭⣴⣶⣶⣆⢲⣀⠸⣾⣆⢹⣿⠷⡀⣁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⣒⣀⠘⠩⠃⢘⡙⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⣝⡄⠫⠍⢀⡀⢂⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿









""")


st.markdown("### 🛠 Useful Hacking Tools")

tools = {
    "World Dangerous Hackers Tool Expose": "https://github.com/Cabdulahi/pish",
    "Pish web tool": "https://github.com/Cabdulahi/pish",
    "MITM attack tool": "https://github.com/websploit/websploit",
    "Kill shot pentesting framework": "https://github.com/bahaabdelwahed/killshot",
    "Facebook information gathering": "git clone https://github.com/CiKu370/OSIF.git",
    "Facebook Toolkit + bots, dump private data": "https://github.com/warifp/FacebookToolkit",
    "Facebook cracking tool Fcrack.py": "https://github.com/INDOnimous/FB-Crack-",
    "Facebook and yahoo account cloner": "https://gitlab.com/W1nz0N/fyc.git",
    "Facebook report tool": "git clone https://github.com/IlayTamvan/Report",
    "Facebook BruteForce Tool": "https://github.com/IAmBlackHacker/Facebook-BruteForce",
    "Facebook hacking ASU": "git clone https://github.com/LOoLzeC/ASU",
    "Facebook Downloader": "https://github.com/barba99/facebook-spotify-youtube-descargar",
    "Hack Facebook MBF": "git clone https://github.com/Rizky-ID/autombf",
    "Facebook Repot3": "git clone https://github.com/PangeranAlvins/Repot3",
    "Facebook Information Gathering": "https://github.com/xHak9x/fbi",
    "Facebook Brute with TOR": "https://github.com/thelinuxchoice/facebash",
    "ip camera 📷 hacking": "https://github.com/kancotdiq/ipcs",
    "Termux Lazyscript tool": "https://github.com/TechnicalMujeeb/Termux-Lazyscript",
    "TMscanner Tool": "https://github.com/TechnicalMujeeb/TM-scanner",
    "Trace location with IP": "https://github.com/Rajkumrdusad/IP-Tracer",
    "WPS Wi-Fi hacking tool": "https://github.com/nxxxu/AutoPixieWps",
    "Routersploit - vulnerability scanner and attacker": "https://github.com/reverse-shell/routersploit.git",
    "Local network exploiting tool Zarp": "https://github.com/hatRiot/zar",
    "ip tracker, Device info by link": "https://github.com/lucasfarre/ip-tracker",
    "Ip-Fy IP address information": "https://github.com/T4P4N/IP-FY.git",
    "Wifite Wi-Fi hacking tool": "https://github.com/derv82/wifite",
    "Modern phishing tool hidden eye": "https://github.com/DarkSecDevelopers/HiddenEye",
    "complete phishing tool 32 templates + 1 customizable": "https://github.com/thelinuxchoice/blackeye",
    "social media phishing with shellphish": "https://github.com/thelinuxchoice/shellphish",
    "Advance Phishing OTP Bypass": "https://github.com/Ignitetch/AdvPhishing",
    "Paytm Phishing OTP Bypass": "https://github.com/Ignitetch/Paytm-Phishing",
    "UberEats Phishing OTP Bypass": "https://github.com/Ignitetch/UberEats-Phishing",
    "Whats App Phishing": "https://github.com/Ignitetch/whatsapp-phishing",
    "Zomato Phishing": "https://github.com/Ignitetch/Zomato-Phishing",
    "hotstar OTP Bypass": "https://github.com/Ignitetch/Hotstar-otp-bypass",
    "Ola OTP Bypass": "https://github.com/Ignitetch/ola-otpbypass",
    "Amazon Payment Gateway Phishing": "https://github.com/Ignitetch/Amazon-payment-gateway-phishing"
}

for name, url in tools.items():
    st.markdown(f"- [{name}]({url})")
st.markdown("### 🛠 Useful Hacking Tools")

st.page_links = {
    'Ethical Hacking Videos': 'https://www.youtube.com/playlist?list=PL4cUxeGkcC9gQ0q1a8i3k7a7j6h8x5bq6',
    'Ethical Hacking Resources': 'https://www.udemy.com/course/learn-ethical-hacking-from-scratch/',
    'Ethical Hacking Tutorials': 'https://www.tutorialspoint.com/ethical_hacking/index.htm',
    'Ethical Hacking Books': 'https://www.amazon.com/s?k=ethical+hacking&ref=nb_sb_noss_2'
}

st.markdown("### 📚 Useful Links")
for title, link in st.page_links.items():
    st.markdown(f"- [{title}]({link})")
st.markdown("### 📚 Useful Links"
            )



st.contect_instagram = {
    'Instagram': 'https://www.instagram.com/soloXrespect/',
}

st.bgcolor = "cyan"
st.markdown(
    """
    <style>
    body {
        background-color: cyan;
    }
    </style>
    """,
    unsafe_allow_html=True
)