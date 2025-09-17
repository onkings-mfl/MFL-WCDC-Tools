# $language = "Python3"
# $interface = "1.0"
import urllib.re
import sys
import ssl

# GitHub raw script URL
url = "https://raw.githubusercontent.com/onkings-mfl/MFL-WCDC-Tools/refs/heads/dev/SecureCrt-Tools/crt_login.py"

try:
    # Check for and retrieve the csv_path argument from SecureCRT
    if crt.Arguments.Count > 0:
        custom_csv_path = crt.Arguments.GetArg(0).strip()
    else:
        custom_csv_path = None
    
    with urllib.request.urlopen(url) as response:
        code = response.read().decode('utf-8')
    
    exec(code)
except Exception as e:
    crt.Dialog.MessageBox(f"Error fetching or executing script: {str(e)}")