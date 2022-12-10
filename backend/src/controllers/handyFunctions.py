
def has_field(payload, field):
    try:
        payload[field]
    except:
        return False
    return True