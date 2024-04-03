# Keylogger with Email Reporting

This Python script serves as a basic keylogger that records key presses on victim system and emails the logged data periodically. It is designed to run in the background and silently capture keystrokes.

## Features
- Captures key presses using the `pynput` library.
- Periodically sends the logged data via email as an attachment.
- Supports Gmail SMTP for sending emails securely.

## Setup Instructions
1. **Install Dependencies:** Make sure you have the necessary dependencies installed. You can install them using pip:

    ```bash
    pip install pynput
    ```

2. **Configure Email Settings:** Update the following variables in the script to match your email configuration:
    - `receiver_email`: Email address where the logs will be sent.
    - `sender_email`: Your email address from which the logs will be sent.
    - `password`: Password for the sender's email account.

3. **Run the Script:** Execute the script using Python or turn to exe:

    ```bash
    python keylogger.py
    ```

4. **Allow Less Secure Apps:** If you're using Gmail, you might need to allow less secure apps to access your account. You can do this in your Google Account settings.

## Notes
- **Security:** Be cautious when using this script, as it can potentially capture sensitive information. Ensure that you have the necessary permissions before running it.
- **Legal Considerations:** Depending on your location and intended use, recording keystrokes without consent may be illegal. Make sure to comply with applicable laws and regulations.
- **Customization:** Feel free to modify the script to suit your specific requirements, such as changing the email service provider or adjusting the logging frequency.

## Disclaimer
This script is provided for educational and informational purposes only. The author is not responsible for any misuse or damage caused by its usage.
