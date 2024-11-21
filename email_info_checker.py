import os
import re
import smtplib
import dns.resolver
from datetime import datetime


def is_email_valid(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def check_email_active(email):
    domain = email.split('@')[1]
    try:
        # Connect to the domain's SMTP server
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(domain)
        server.helo()
        response_code, response_message = server.verify(email)
        server.quit()

        if response_code == 250:
            return "Active"
        else:
            return f"Not Active (Response: {response_message}"
    except Exception:
        return "Unable to verify"


def get_email_hosting(email):
    try:
        domain = email.split('@')[1]
        mx_records = dns.resolver.resolve(domain, 'MX')
        sorted_mx_records = sorted(mx_records, key=lambda x: x.preference)
        hosting_provider = str(sorted_mx_records[0].exchange)
        return hosting_provider
    except Exception:
        return "Unknown Hosting Provider"


def process_email(email):
    email_info = {"Email": email}

    # Validate email
    if is_email_valid(email):
        email_info["Validation"] = "Valid"
        email_info["Hosting Provider"] = get_email_hosting(email)
        email_info["Status"] = check_email_active(email)
    else:
        email_info["Validation"] = "Invalid"
        email_info["Hosting Provider"] = "N/A"
        email_info["Status"] = "N/A"

    return email_info


def save_report(results):
    output_file = os.path.join("email_info", f"email_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

    with open(output_file, "w") as f:
        f.write("Email Validation and Hosting Information Report\n")
        f.write("=" * 50 + "\n\n")
        for result in results:
            f.write(f"Email: {result['Email']}\n")
            f.write(f"Validation: {result['Validation']}\n")
            f.write(f"Hosting Provider: {result['Hosting Provider']}\n")
            f.write(f"Status: {result['Status']}\n")
            f.write("-" * 50 + "\n")

    print(f"Report saved to: {output_file}")


def main():
    os.makedirs("email_info", exist_ok=True)

    # Making the script working in a loop until the user will not end the job
    while True:
        print("Enter a single email or a comma-separated list of emails (type 'q' for exit): ")
        user_input = input("Email(s): ").strip()

        # Ending the job
        if user_input.lower() == 'q':
            print("Finishing the job. Good Bye!")
            break

        emails = [email.strip() for email in user_input.split(",")]
        results = []

        for email in emails:
            results.append(process_email(email))

        # Save the report right after it was created
        save_report(results)


if __name__ == "__main__":
    main()
