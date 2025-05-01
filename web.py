import streamlit as st
import pandas as pd
import numpy as np




import streamlit as st

# Change the background color using CSS in markdown
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;  /* Light blue background */
    }
    </style>
    """, unsafe_allow_html=True
)

# Add some content to see the effect



st.title("🎯 Learn Ethical Hacking")
st.markdown("### A collection of ethical hacking video resources")
st.markdown("#### Note: This app is for educational purposes only.")
st.markdown("### 📜 Disclaimer")
st.markdown("This app is for educational purposes only. The videos provided are for learning and research in ethical hacking.")
st.markdown("Always ensure you have permission to test any system or network before attempting any hacking techniques.")
st.markdown("### 📜 Note")
st.markdown("This app is for educational purposes only. The videos provided are for learning and research in ethical hacking.")
st.markdown("Always ensure you have permission to test any system or network before attempting any hacking techniques.")
st.markdown("### 📜 Note you have this app to do hacking"
            
            )




st.markdown("### 🛠 Useful Hacking software")

st.markdown("1. [Kali Linux](https://www.kali.org/) - A Debian-based Linux distribution aimed at advanced Penetration Testing and Security Auditing.")
st.markdown("2. [Wireshark](https://www.wireshark.org/) - A network protocol analyzer that lets you capture and interactively browse the traffic on a computer network.")
st.markdown("3. [Metasploit](https://www.metasploit.com/) - A penetration testing framework that makes hacking simple.")
st.markdown("4. [Burp Suite](https://portswigger.net/burp) - A platform for security testing of web applications.")
st.markdown("5. [Nmap](https://nmap.org/) - A network discovery and security auditing tool.")
st.markdown("6. [OWASP ZAP](https://www.zaproxy.org/) - An open-source web application security scanner.")
st.markdown("7. [Termux](https://termux.com/) - A terminal emulator and Linux environment app for Android.")
st.markdown("8. [Aircrack-ng](https://www.aircrack-ng.org/) - A suite of tools to assess the security of WiFi networks.")
st.markdown("9. [John the Ripper](https://www.openwall.com/john/) - A fast password cracker.")
st.markdown("10. [SQLMap](https://sqlmap.org/) - An open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities.")
st.markdown("11. [Nikto](https://cirt.net/Nikto2) - A web server scanner which performs comprehensive tests against web servers for multiple items.")









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


for tool, link in tools.items():
    st.markdown(f"- [{tool}]({link})")

st.markdown("### 🛠 for contact us ")
import streamlit as st

st.title("Follow on Instagram")

# Simple clickable link
st.markdown("[👉 Visit @soloXrespect on Instagram](https://www.instagram.com/soloXrespect/)")

st.markdown("### 🛠 for contact us ")





ascii_art = r"""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠉⣉⣉⣉⣉⣉⣉⣉⡩⠙⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢋⣡⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⣉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⢡⣾⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⣆⠙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠃⣴⣿⣿⣿⡿⠛⠁⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⠙⠿⣿⣿⣿⣷⡀⠻⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢁⣾⣿⠟⢁⡾⠁⢀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠹⣆⠙⣿⣿⡄⠹⣿⣿⣿⣿
⣿⣿⡿⢁⣾⡿⡏⠀⣼⣁⡴⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⣿⡆⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢳⣄⣹⡀⠘⡿⣿⡄⠹⣿⣿⣿
⣿⣿⠁⣾⡟⢹⡇⢠⠟⠉⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠙⢇⠀⣿⠹⣿⡀⢻⣿⣿
⣿⡇⢸⣿⠂⢸⡇⠀⣠⡞⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⣦⡀⠀⣿⠀⢿⣧⠀⣿⣿
⢿⠀⣾⣿⠀⢸⣧⠞⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠙⢦⣿⠀⢸⣿⡄⢸⣿
⡇⢠⣿⢻⡄⠘⠁⢀⡴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠋⠀⣶⢻⡇⠀⣿
⡁⢸⡏⠘⣇⠀⢰⡟⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣿⣬⡉⣉⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⣦⠀⢠⡏⢘⣿⠀⣿
⠇⢸⣏⠀⢹⣆⠟⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠉⠀⢰⣿⣟⡅⣝⣿⣿⠀⠈⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠘⣇⣾⠁⢸⣿⠀⣿
⠀⢸⣿⡄⠈⣿⠀⢀⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢺⣿⣿⡇⢻⣿⣿⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢹⠏⠀⣾⣿⠀⣿
⡇⠘⣿⢷⡀⠈⠀⣼⠏⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠸⣿⡿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠇⢿⡀⠘⠀⣼⢿⡇⠀⣿
⣿⠀⢿⡈⠻⣆⠀⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⢠⡾⠋⣸⠃⢸⣿
⣿⡇⢸⣧⠀⠈⢷⡏⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡏⠀⢘⣷⠋⠀⣰⡟⠀⣿⣿
⣿⣿⡀⢻⣧⡀⠀⠙⠀⠐⣧⠹⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⢱⡇⠀⠜⠁⢀⣰⣿⠁⣸⣿⣿
⣿⣿⣷⡈⢿⡙⠳⣤⣀⠀⢿⡀⠹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠀⢾⠃⢀⣠⠶⠋⣽⠃⣰⣿⣿⣿
⣿⣿⣿⣷⡈⢷⣄⠀⠉⠛⢾⣇⠀⠹⣞⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠁⢠⣿⠞⠋⠁⢀⣾⠋⣰⣿⣿⣿⣿
⣿⣿⣿⣿⣷⡀⠻⣷⡦⣀⡀⠈⠃⠀⠙⣆⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡞⠁⠀⠉⠀⣀⡤⣶⡿⠁⣰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣆⠘⢿⣌⠙⠳⠶⠦⣤⣼⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣯⣤⣴⠶⠶⠛⢉⣾⠏⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣦⣤⣀⣀⣀⣀⣠⣤⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣦⣠⣤⣀⣀⣀⣀⣠⣤⣾⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡉⠻⣦⣉⠙⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⢉⣩⠾⠋⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠉⠻⢶⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶⣶⣶⣶⠞⠋⢁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣈⡙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠋⣉⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
         
    
      .·¨'`;        ,.·´¨;\                   ,.,   '                   ,. - .,                              _  °        ,.-·.                ,.         ,·´'; '            ,.-·^*ª'` ·,        
     ';   ;'\       ';   ;::\                ;´   '· .,             ,·'´ ,. - ,   ';\           ,.·,       :´¨   ;\        /    ;'\'         ;'´*´ ,'\       ,'  ';'\°        .·´ ,·'´:¯'`·,  '\‘     
     ;   ;::'\      ,'   ;::';             .´  .-,    ';\       ,·´  .'´\:::::;'   ;:'\ '      ,'   ,'\     .'´ ,·´::'\      ;    ;:::\        ;    ';::\      ;  ;::'\      ,´  ,'\:::::::::\,.·\'    
     ;  ;::_';,. ,.'   ;:::';°           /   /:\:';   ;:'\'    /  ,'´::::'\;:-/   ,' ::;  '    ;'  ,'::\ .·' .·´::::::;'    ';    ;::::;'      ;      '\;'      ;  ;:::;     /   /:::\;·'´¯'`·;\:::\°  
   .'     ,. -·~-·,   ;:::'; '         ,'  ,'::::'\';  ;::';  ,'   ;':::::;'´ ';   /\::;' '      ;  ;::·´ .·´:::::::;·´      ;   ;::::;      ,'  ,'`\   \      ;  ;:::;    ;   ;:::;'          '\;:·´  
   ';   ;'\::::::::;  '/::::;       ,.-·'  '·~^*'´¨,  ';::;  ;   ;:::::;   '\*'´\::\'  °     ';  '´   ;´::::::;·´         ';  ;'::::;       ;  ;::;'\  '\    ;  ;:::;    ';   ;::/      ,·´¯';  °    
    ;  ';:;\;::-··;  ;::::;        ':,  ,·:²*´¨¯'`;  ;::';  ';   ';::::';    '\::'\/.'        ;  ;'\   '\::;·´             ;  ';:::';       ;  ;:::;  '\  '\ ,'  ;:::;'    ';   '·;'   ,.·´,    ;'\      
    ':,.·´\;'    ;' ,' :::/  '       ,'  / \::::::::';  ;::';   \    '·:;:'_ ,. -·'´.·´\‘     ;  ;:\:'·.  '·., ,.·';'        ';  ;::::;'     ,' ,'::;'     '\   ¨ ,'\::;'     \'·.    `'´,.·:´';   ;::\'    
     \:::::\    \·.'::::;         ,' ,'::::\·²*'´¨¯':,'\:;     '\:` ·  .,.  -·:´::::::\'    ;_;::'\::`·._,.·'´:\'         \*´\:::;‘     ;.'\::;        \`*´\::\; °     '\::\¯::::::::';   ;::'; ‘  
       \;:·´     \:\::';          \`¨\:::/          \::\'       \:::::::\:::::::;:·'´'     \::'\:;' '·::\::\:::::'\         '\::\:;'      \:::\'          '\:::\:' '         `·:\:::;:·´';.·´\::;'     
                  `·\;'            '\::\;'            '\;'  '       `· :;::\;::-·´           '\::\     `·'\::\;:·'´'           `*´‘         \:'             `*´'‚               ¯      \::::\;'‚     
                     '               `¨'                                                     ¯          ¯'                                                                         '\:·´'       
"""
st.title("💻 Hacker ASCII Art")
st.code(ascii_art, language="text")



st.markdown("### 🛠 some vedios of youtube to lear it ")
st.markdown("#### 1. [Hacking with Python](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 2. [Python for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 3. [Python for Beginners](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 4. [Python for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 5. [Python for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 6. [Python for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 7. [Python for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 8. [Python for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 9. [Python for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 10. [Python for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 11. [Python for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 12. [Python for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 13. [Python for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 14. [Python for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 15. [Python for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 16. [Python for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 17. [Python for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")

st.markdown("### 🛠 some vedios of youtube to learn hacking with kali linux ")
st.markdown("#### 1. [Hacking with Kali Linux](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 2. [Kali Linux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 3. [Kali Linux for Beginners](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 4. [Kali Linux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 5. [Kali Linux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 6. [Kali Linux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 7. [Kali Linux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 8. [Kali Linux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 9. [Kali Linux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 10. [Kali Linux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 11. [Kali Linux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 12. [Kali Linux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 13. [Kali Linux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 14. [Kali Linux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 15. [Kali Linux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 16. [Kali Linux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 17. [Kali Linux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")


st.markdown("### 🛠 some vedios of youtube to learn hacking with metasploit ")
st.markdown("#### 1. [Hacking with Metasploit](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 2. [Metasploit for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 3. [Metasploit for Beginners](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 4. [Metasploit for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 5. [Metasploit for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 6. [Metasploit for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 7. [Metasploit for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 8. [Metasploit for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 9. [Metasploit for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 10. [Metasploit for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 11. [Metasploit for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 12. [Metasploit for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)") 
st.markdown("#### 13. [Metasploit for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 14. [Metasploit for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 15. [Metasploit for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 16. [Metasploit for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 17. [Metasploit for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 18. [Metasploit for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 19. [Metasploit for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 20. [Metasploit for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 21. [Metasploit for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 22. [Metasploit for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")

st.markdown("#### some best youtube vedios to lear with termux")
st.markdown("#### 1. [Hacking with Termux](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 2. [Termux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 3. [Termux for Beginners](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 4. [Termux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 5. [Termux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 6. [Termux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 7. [Termux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 8. [Termux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 9. [Termux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 10. [Termux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 11. [Termux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 12. [Termux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")

st.markdown("#### 13. [Termux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 14. [Termux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 15. [Termux for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 16. [Termux for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 17. [Termux for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")


st.markdown("#### to learninfg hacking with other tools")
st.markdown("#### 1. [Hacking with Other Tools](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 2. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 3. [Other Tools for Beginners](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 4. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 5. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 6. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 7. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 8. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 9. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 10. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 11. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 12. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 13. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 14. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 15. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 16. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 17. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 18. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 19. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 20. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 21. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 22. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 23. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 24. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 25. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 26. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 27. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 28. [Other Tools for Cyber Security](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 29. [Other Tools for Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 30. [Other Tools for Ethical Hacking](https://www.youtube.com/watch?v=3x2v0g4X8aE)")



st.markdown("#### about darkweb ")


st.text("""
            
            [![What is the Dark Web? Tor, Onion & the ...](https://images.openai.com/thumbnails/534be346497090ce9073f473717ee8a8.jpeg)](https://www.thesslstore.com/blog/what-is-the-dark-web/)
The dark web is a segment of the internet that remains hidden from traditional search engines and requires specialized tools, such as the Tor browser, to access. Unlike the surface web, which is readily accessible and indexed by search engines, the dark web is intentionally concealed to provide users with a high degree of anonymity and privacy. This hidden layer of the internet is part of the larger deep web, which encompasses all web content not indexed by standard search engines, including private databases and password-protected sites.

### Structure and Access

The dark web is characterized by its use of encrypted networks and specialized software that anonymize users' identities and activities. One of the most prominent tools for accessing the dark web is Tor (The Onion Router), which routes internet traffic through a series of volunteer-operated servers, or nodes, to obscure the user's location and usage. This multi-layered encryption process ensures that both the user's identity and the content they access remain private.

Websites on the dark web typically use the ".onion" domain suffix, indicating that they are part of the Tor network. These sites are not accessible through standard web browsers like Chrome or Firefox; instead, users must employ the Tor browser or similar tools designed for this purpose.

### Uses and Applications

The dark web serves a variety of purposes, ranging from the facilitation of illegal activities to the support of privacy and free speech. On the illicit side, it has been associated with markets for illegal goods and services, including drugs, weapons, and stolen data. These marketplaces often operate similarly to legitimate e-commerce platforms, allowing users to buy and sell items anonymously, frequently using cryptocurrencies like Bitcoin to further obscure transactions.

However, the dark web also provides a vital space for legitimate activities. It offers a platform for individuals in oppressive regimes to communicate securely and access information without fear of censorship or surveillance. Journalists, whistleblowers, and activists use the dark web to share information and documents that might be suppressed or lead to retaliation if exposed through conventional channels.

### Legal and Ethical Considerations

While accessing the dark web itself is not illegal, engaging in unlawful activities within it is subject to the same legal repercussions as similar actions on the surface web. Law enforcement agencies across the globe monitor the dark web for illegal activities, and individuals found engaging in such activities can face serious legal consequences.

The ethical implications of the dark web are complex. On one hand, it serves as a tool for privacy and free expression, which are fundamental rights in many societies. On the other hand, it can facilitate harmful activities that are difficult to regulate due to the anonymity it provides.

### Security Risks

Navigating the dark web comes with inherent risks. The anonymity it offers can be exploited by cybercriminals to distribute malware, conduct phishing attacks, or engage in other malicious activities. Users may encounter sites that attempt to steal personal information or infect their devices with harmful software. Therefore, individuals accessing the dark web should exercise caution, use robust security measures, and be aware of the potential dangers.

### Conclusion

The dark web is a multifaceted component of the internet that plays a significant role in the digital landscape. It is a double-edged sword: while it can be a haven for privacy and free speech, it also harbors illegal activities that pose challenges to law enforcement and cybersecurity. Understanding the dark web's structure, uses, and risks is essential for navigating this hidden part of the internet safely and responsibly.'
""")


st.markdown("### 🛠 some vedios of youtube to learn darkweb")
st.markdown("#### 1. [Dark Web: What is it?](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 2. [Dark Web: How to Access it Safely](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 3. [Dark Web: Risks and Dangers](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 4. [Dark Web: Myths and Facts](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 5. [Dark Web: How to Stay Safe](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 6. [Dark Web: How to Protect Yourself](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 7. [Dark Web: How to Use it Safely](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 8. [Dark Web: How to Avoid Scams](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 9. [Dark Web: How to Avoid Scams](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 10. [Dark Web: How to Avoid Scams](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 11. [Dark Web: How to Avoid Scams](https://www.youtube.com/watch?v=3x2v0g4X8aE)")

st.markdown("#### some hindi vedios on darkweb")
st.markdown("#### 1. [Dark Web: What is it?](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 2. [Dark Web: How to Access it Safely](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 3. [Dark Web: Risks and Dangers](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 4. [Dark Web: Myths and Facts](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 5. [Dark Web: How to Stay Safe](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 6. [Dark Web: How to Protect Yourself](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 7. [Dark Web: How to Use it Safely](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 8. [Dark Web: How to Avoid Scams](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 9. [Dark Web: How to Avoid Scams](https://www.youtube.com/watch?v=3x2v0g4X8aE)")
st.markdown("#### 10. [Dark Web: How to Avoid Scams](https://www.youtube.com/watch?v=3x2v0g4X8aE)")


st.markdown("#### some links to visit darkweb seftly with.onion browser")

st.text("""
[![Five Things to Know About the Dark Web ...](https://images.openai.com/thumbnails/97efa6152f0021f6448dbe85daf3669b.jpeg)](https://www.peraton.com/news/five-things-to-know-about-the-dark-web/)
Accessing the dark web requires caution and a clear understanding of its purpose and risks. While it hosts both legitimate and illicit content, it's crucial to approach it responsibly. Here are 18 dark web websites that are known for their legitimate services, such as privacy tools, research archives, and secure communication platforms: ([What is the Dark Web? | ESET](https://www.eset.com/uk/about/newsroom/blog/dark-web/?utm_source=chatgpt.com))

1. **ProPublica** – An independent, non-profit newsroom offering investigative journalism.
2. **The Intercept** – Provides news and analysis on politics, technology, and national security.
3. **SecureDrop** – A platform for whistleblowers to securely submit documents to journalists.
4. **Ahmia** – A search engine that indexes .onion sites, making it easier to find content on the dark web.
5. **Torch** – One of the oldest search engines on the dark web, known for its vast index of onion sites.
6. **DuckDuckGo** – A privacy-focused search engine that can be accessed on the dark web.
7. **Sci-Hub** – Provides access to millions of scientific papers, challenging the paywalls of academic publishers.
8. **The Hidden Wiki** – A directory of dark web links, including forums, marketplaces, and services.
9. **Daniel** – A large directory of .onion sites, offering a wide range of resources.
10. **Mail2Tor** – A secure and encrypted email service provider on the dark web.
11. **ProtonMail** – A secure email service known for its strong encryption and privacy features.
12. **ZeroBin** – A pastebin service that provides end-to-end encryption, ensuring that only the intended recipient can read the content.
13. **Facebook** – The official mirror website of Facebook, facilitating anonymous access to the platform.
14. **Haystak** – A search engine with a vast index of dark web pages, offering both free and premium versions.
15. **Smartmixer** – A blockchain-based tool that allows you to mix cryptocurrencies to enhance privacy.
16. **Archetyp Market** – A darknet marketplace known for its focus on privacy and security.
17. **Distributed Denial of Secrets (DDoSecrets)** – A transparency collective that publishes data leaks in the public interest.
18. **The Pirate Bay** – A popular torrent site that can also be accessed on the dark web. ([best dark web sites 2024](https://dark-website.com/best-dark-web-sites-2024/?utm_source=chatgpt.com), [Best Dark Websites You Should Explore in 2024](https://forestvpn.com/blog/internet-privacy/best-dark-websites-2024/?utm_source=chatgpt.com), [best dark web sites 2024](https://darkmarketlists.com/best-dark-web-sites-2024/?utm_source=chatgpt.com), [25 Best Dark Web Sites For 2024 With Direct Access Links - TechInShorts](https://techinshorts.com/25-best-dark-web-sites-for-2024-with-direct-access-links/?utm_source=chatgpt.com), [Distributed Denial of Secrets](https://en.wikipedia.org/wiki/Distributed_Denial_of_Secrets?utm_source=chatgpt.com))

**Important Note:** While these sites have legitimate purposes, the dark web can also host illegal activities. Always exercise caution, use a secure and anonymous browser like Tor, and consider using a VPN. Ensure you're complying with all local laws and regulations when accessing any part of the internet. 
          
  """)


st.title("want to give review about thiss app")



import streamlit as st
import datetime
import json

st.title("📝 Leave a Review for My App!")

# Review input form
with st.form("review_form"):
    name = st.text_input("Your Name")
    review = st.text_area("Your Review")
    submit = st.form_submit_button("Submit")

# Save review to file (optional)
if submit:
    timestamp = datetime.datetime.now().isoformat()
    review_data = {
        "timestamp": timestamp,
        "name": name,
        "review": review
    }

    # You can also send this to a server, database, or email
    with open("reviews.json", "a") as f:
        f.write(json.dumps(review_data) + "\n")

    st.success("✅ Thank you for your feedback!")

    # Simulate sending to Instagram by prompting the user to DM
    st.markdown("📩 Please DM your feedback to my Instagram: [@soloXrespect](https://www.instagram.com/soloXrespect/)")
