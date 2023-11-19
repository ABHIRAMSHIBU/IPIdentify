import sys
try:
    from ip_identify import IPIdentify
except ModuleNotFoundError:
    print("IPIdentify not found, install it by using pip install 'https://github.com/ABHIRAMSHIBU/IPIdentify/archive/refs/heads/develop.zip'")
    sys.exit(-1)

ipaddress = input("Enter IPv4 address:")

enquiry = IPIdentify.IPEnquire(ipaddress)
print("ISP of ",ipaddress," is:",IPIdentify.IPLocation.getISP(enquiry))
