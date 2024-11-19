import base64
import email
from email import policy
from email.parser import BytesParser

# Load the .eml file
with open("your_email.eml", "rb") as eml_file:
    msg = BytesParser(policy=policy.default).parse(eml_file)

# Find all attachments
for part in msg.iter_attachments():
    filename = part.get_filename()
    if filename:
        # Decode and save the attachment
        with open(filename, "wb") as file:
            file.write(part.get_payload(decode=True))
        print(f"Extracted: {filename}")
    else:
        # If no filename, handle inline content or skip
        print("No filename found for an attachment.")
