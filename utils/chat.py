import base64

def to_base32(x: str) -> str:
    """Encode string to base32 without padding."""
    string_bytes = x.encode('utf-8')
    base32_encoded = base64.b32encode(string_bytes)
    return base32_encoded.decode('utf-8').rstrip('=')

def base32_to_original(base32_string: str) -> str:
    """Decode base32 string that may not have padding."""
    # Add padding back if needed
    missing_padding = len(base32_string) % 8
    if missing_padding:
        base32_string += '=' * (8 - missing_padding)

    base32_bytes = base32_string.encode('utf-8')
    decoded_bytes = base64.b32decode(base32_bytes)
    return decoded_bytes.decode('utf-8')