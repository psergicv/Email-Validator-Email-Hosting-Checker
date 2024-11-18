# Email Validator & Hosting Checker

## Overview
This Python script validates email addresses, checks their hosting provider, and verifies activity status. Results are saved in a beautifully formatted text file.

## Features
- Validate email format.
- Check hosting provider using DNS MX records.
- Verify email activity (SMTP-based).
- Save detailed results in a structured report.

## Requirements
- Python 3.7+
- Required libraries:
  ```
  pip install dnspython
  ```

## Usage
1. Clone this repository:
```
git clone https://github.com/psergicv/Email-Validator-Email-Hosting-Checker.git
cd Email-Validator-Email-Hosting-Checker
```

2. Run the script:
```
python email_info_checker.py
```

3. Follow the prompts to input single or multiple emails.


## Example Output
The results are saved in the email_info folder as a .txt report.

## Contribution
Feel free to fork this repository, open issues, or submit pull requests!

## License
This project is licensed under the MIT License. See LICENSE for details.
