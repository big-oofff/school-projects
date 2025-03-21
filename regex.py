'''
Write a Python program that:Reads the log file.
Extracts specific information using regular expressions.
Displays errors, warnings, and user activity separately. 
Display errors first, then warnings, then user activity. 
Determine how many times each type of event occurs.Hacker Challenge :  
Allow users to input a date and show only logs from that date
Sample Output
ERRORS:
2025-02-27 14:23:11 - Database connection failed for user admin
2025-02-27 14:30:14 - Failed to open file config.txt

WARNINGS:
2025-02-27 14:27:09 - Disk usage at 90%

USER ACTIVITY:
2025-02-27 14:25:42 - john_doe logged in from 192.168.1.100
2025-02-27 14:35:21 - alice logged out from N/A

'''
import re

d = {"ERRORS": [], "WARNINGS": [], "USER ACTIVITY": []}
log_pattern = re.compile(r"\[(.*?)\] (ERROR|WARNING|INFO): (.*)")

with open('serverlog.txt', 'r') as fhand:
    text = fhand.readlines()
    
    for line in text:
        match = log_pattern.match(line)
        if match:
            timestamp, level, message = match.groups()
            formatted_log = f"{timestamp} - {message}"      
            if level == "ERROR":
                d["ERRORS"].append(formatted_log)
            elif level == "WARNING":
                d["WARNINGS"].append(formatted_log)
            elif level == "INFO":
                d["USER ACTIVITY"].append(formatted_log)

print("\nERRORS:")
print("\n".join(d["ERRORS"]))

print("\nWARNINGS:")
print("\n".join(d["WARNINGS"]))

print("\nUSER ACTIVITY:")
print("\n".join(d["USER ACTIVITY"]))
