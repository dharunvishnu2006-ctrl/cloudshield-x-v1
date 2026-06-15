import streamlit as st
from src.scanner import CloudShieldScanner
from src.log_reader import read_logs
from src.ip_detector import detect_suspicious_ips
from src.alert_system import raise_alerts
from src.report_generator import generate_report

st.set_page_config(
    page_title="CloudShield X",
    page_icon="",
    layout="wide"
)

st.title("CloudShield X — Security Log Analyzer")
st.caption("v1 of 6 | CSPM Platform | Built by J. Dharun Vishnu")
st.sidebar.title("CloudShield X")
st.sidebar.caption("CSPM Platform — v1")

page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Analytics", "Reports", "About"]
)

if page == "Dashboard":
    st.subheader("Live Stats")
    col1, col2, col3 = st.columns(3)
    m1 = col1.empty()
    m2 = col2.empty()
    m3 = col3.empty()

    m1.metric("Total Logs Scanned", "0")
    m2.metric("Suspicious IPs", "0")
    m3.metric("Alerts Raised", "0")

    st.divider()
    st.subheader("Upload server Log")
    uploaded_file = st.file_uploader("choose a .log file", type=["log", "txt"])

    if uploaded_file is not None:
        temp_path = "data/uploaded_log.log"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded! Scanning...")
        logs = read_logs(temp_path)
        suspicious = detect_suspicious_ips(logs, threshold=3)
        alerts = raise_alerts(suspicious)
        report_path = generate_report(suspicious)

        st.success(f"Scan Completed! Report saved to: {report_path}")

        m1.metric("Total Logs Scanned", len(logs))
        m2.metric("Suspicious IPs", len(suspicious))
        m3.metric("Alerts Raised", len(alerts))