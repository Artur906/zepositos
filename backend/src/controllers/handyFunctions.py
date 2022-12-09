
def has_id(payload):
    try:
        payload['id']
    except:
        return False
    return True