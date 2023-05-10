def remove_duplicate_emails(email_list):
    unique_emails = set()
    for email in email_list:
        unique_emails.add(email.lower())
    print("Unique email addresses:")
    for email in unique_emails:
        print(email)
