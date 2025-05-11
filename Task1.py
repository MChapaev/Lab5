import re
# Validation
def is_valid_ipv4(ip: str) -> bool:
    pattern = re.compile(r'''
        ^
        (?:
          (?:25[0-5]|
          2[0-4][0-9]|
          1[0-9]{2}|
          [1-9]?[0-9])
          \.
        ){3}
        (?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])
        $
    ''', re.VERBOSE)
    return bool(pattern.match(ip))


def validate_ipv4(ip: str) -> str:
    if not is_valid_ipv4(ip):
        raise ValueError(f"Invalid IP-address: {ip}")
    return ip


# Main
if __name__ == "__main__":
    print(validate_ipv4("192.168.0.1"))
    # print(validate_ipv4("1920.168.0.1")) # Will raise an error
