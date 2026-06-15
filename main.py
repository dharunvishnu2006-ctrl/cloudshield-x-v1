from src.log_reader import read_logs
from src.ip_detector import detect_suspicious_ips
from src.alert_system import raise_alerts
from src.report_generator import generate_report

logs = read_logs("data/sample_server.log")
suspicious = detect_suspicious_ips(logs)
alerts = raise_alerts(suspicious)
print("Alerts:", alerts)

report_path = generate_report(suspicious)
print("Report saved to:", report_path)