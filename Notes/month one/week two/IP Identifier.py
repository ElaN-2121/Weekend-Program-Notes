import ipaddress

def check_ip(ip):
    try:
        # Validate IP
        ip_obj = ipaddress.IPv4Address(ip)
        pring(f"\nIP Address: {ip}")

        # Private or public?
        if ip_obj.is_private:
            print("Type: Private")
        else:
            print("Types: Public")

        # Class Determination
        first_octate = int(ip.split('.')[0])
        
        if 1<= first_octate <= 126:
            ip_class = "A"
            subnet = "/8"

        elif 128 <= first_octet <= 191:
            ip_class = "B"
            subnet = "/16"

        elif 192 <= first_octet <= 223:
            ip_class = "C"
            subnet = "/24"

        elif 224 <= first_octet <= 239:
            ip_class = "D (Multicast)"
            subnet = "N/A"

        elif 240 <= first_octet <= 255:
            ip_class = "E (Experimental)"
            subnet = "N/A"

        else:
            ip_class = "Unknown"
            subnet = "N/A"

        print(f"Class: {ip_class}")
        print(f"The subnet is: {subnet}")
        

    except ipaddress.AddressValueError:
        print("It is invalid IP Address!")


if __name__ == "__main__":
    user_ip = input("Enter an IP address to be tested: ")
    check_ip(user_ip)
