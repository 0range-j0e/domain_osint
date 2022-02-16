import os

# Perform OSINT on a given domain name using whois, dig and nslookup. Output results to a file with a name of your choosing.


# User provides URL.
print("Perform OSINT on a given domain using WHOIS, dig, and nslookup.")
url = input("Choose domain: ")

# User provides filename for system command outputs.
filename = input("Choose filename: ")

# Print status to terminal.
print(f"Performing queries on {url}\n")

# Add header to WHOIS information section of file for readability.
os.system(f"""echo '[+] WHOIS information:\\n\\n' | tee -a {filename}""")

# Perform WHOIS with -H parameter that hides legal disclaimer for readability.
os.system(f"whois -H {url} | tee -a {filename}")

# Add header to dig information section of file for readability.
os.system(f"""echo '\\n\\n [+] dig information:\\n\\n' | tee -a {filename}""")

# Perform dig with standard settings.
os.system(f"dig {url} | tee -a {filename}")

# Add header to nslookup information section of file for readability.
os.system(f"""echo '\\n\\n [+] nslookup information:\\n\\n' | tee -a {filename}""")

# Perform nslookup with standard settings.
os.system(f"nslookup {url} | tee -a {filename}")
