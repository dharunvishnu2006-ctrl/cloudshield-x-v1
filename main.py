from src.log_reader import read_logs

logs = read_logs("data/sample_server.log")
print(logs)

from src.log_reader import read_logs
from src.ip_detector import detect_suspicious_ips

logs = read_logs("data/sample_server.log")
suspicious = detect_suspicious_ips(logs)
print(suspicious)

from src.log_reader import read_logs
from src.ip_detector import detect_suspicious_ips
from src.alert_system import raise_alerts

logs = read_logs("data/sample_server.log")
suspicious = detect_suspicious_ips(logs)
alerts = raise_alerts(suspicious)
print("Alerts:", alerts)