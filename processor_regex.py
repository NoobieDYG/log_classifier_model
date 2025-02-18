import re
def classify_with_regex(log_message):
    regex_patterns={
        r"User User\d+ logged (in|out).":"User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern,log_message,re.IGNORECASE):
            return label
    return None
if __name__ == "__main__":
    log_messages = [
        "User User123 logged in.",
        "Backup started at 12:00 AM.",
        "Backup completed successfully.",
        "System updated to version 1.2.3.",
        "File report.pdf uploaded successfully by user User456.",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user Admin.",
        "Account with ID 789 created by User123."
    ]

    for message in log_messages:
        classification = classify_with_regex(message)
        print(f"Log Message: {message} -> Classification: {classification}")
