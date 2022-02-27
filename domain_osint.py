import os
import argparse


''' Perform OSINT on a given domain name using whois, dig and nslookup. Output results to a file with a name of your choosing (optional). '''
__author__ = "Orange-Joe"
__copyright__ = "Orange-Joe"
__version__ =  "1.0"


parser = argparse.ArgumentParser(description="Perform OSINT on a given domain name using WHOIS, dig and nslookup. Output results to a file (optional).")
parser.add_argument("domain", type=str, help="Domain to research")
parser.add_argument("-f", "--filename", type=str, help="Choose filename to store output (default is domain name)")
parser.add_argument("-s", "--separate", action="store_true", 
                    help="Separate WHOIS, dig, and nslookup outputs to separate files (ex: filename_dig, filename_whois, etc)")
args = parser.parse_args()

if args.filename is None:
    args.filename = args.domain

# Check if designated filename(s) exists in current directory.
if args.separate:
    while (args.filename + "_whois") in os.listdir():
        user_input = input(f"[!] Output files for filename {args.filename} exist in current directory. Overwrite files? (Y\\N)")
        if user_input.lower() == 'y':
            os.system(f"rm {args.filename}_whois {args.filename}_dig {args.filename}_nslookup")
            break
        elif user_input.lower() == 'n':
            args.filename = input("Choose new file name ")
        else:
            print(f"Aborting {__file__}")
            quit()   

else:          
    while args.filename in os.listdir():
        user_input = input(f"[!] {args.filename} exists in current directory. Overwrite file? (Y\\N)")
        if user_input.lower() == 'y':
            os.system(f"rm {args.filename}")
            print(f"[!] Original {args.filename} removed. Creating new file.")
            break
        elif user_input.lower() == 'n':
            args.filename = input("Choose new file name ")
        else:
            print(f"Aborting {__file__}")
            quit()




# Print status to terminal.
print(f"[+] Running {__file__}")
print(f"[+] Performing queries on {args.domain}\n")


# WHOIS
if args.separate:
    # Add header to WHOIS information section of file for readability.
    os.system(f"""echo '[+] WHOIS information:\\n\\n' | tee -a {args.filename}_whois""")
    # Perform WHOIS with -H parameter that hides legal disclaimer for readability.
    os.system(f"whois -H {args.domain} | tee -a {args.filename}_whois")

else:
    # Add header to WHOIS information section of file for readability.
    os.system(f"""echo '[+] WHOIS information:\\n\\n' | tee -a {args.filename}""")
    # Perform WHOIS with -H parameter that hides legal disclaimer for readability.
    os.system(f"whois -H {args.domain} | tee -a {args.filename}")


# dig 
if args.separate:
    # Add header to dig information section of file for readability.
    os.system(f"""echo '\\n\\n [+] dig information:\\n\\n' | tee -a {args.filename}_dig""")
    # Perform dig with standard settings.
    os.system(f"dig {args.domain} | tee -a {args.filename}_dig")

else:
    # Add header to dig information section of file for readability.
    os.system(f"""echo '\\n\\n [+] dig information:\\n\\n' | tee -a {args.filename}""")
    # Perform dig with standard settings.
    os.system(f"dig {args.domain} | tee -a {args.filename}")


# nslookup 
if args.separate:
    # Add header to nslookup information section of file for readability.
    os.system(f"""echo '\\n\\n [+] nslookup information:\\n\\n' | tee -a {args.filename}_nslookup""")
    # Perform nslookup with standard settings.
    os.system(f"nslookup {args.domain} | tee -a {args.filename}_nslookup")

else:
    # Add header to nslookup information section of file for readability.
    os.system(f"""echo '\\n\\n [+] nslookup information:\\n\\n' | tee -a {args.filename}""")
    # Perform nslookup with standard settings.
    os.system(f"nslookup {args.domain} | tee -a {args.filename}")


# Notify user where output is stored.
if args.separate:
    print(f"[+] Outputs stored in {os.getcwd()}/{args.filename}_whois, {os.getcwd()}/{args.filename}_dig, {os.getcwd()}/{args.filename}_nslookup")

else:
    print(f"[+] Output stored in {os.getcwd()}/{args.filename}")
