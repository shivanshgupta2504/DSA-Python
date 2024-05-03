head = {
    'value': 1,
    'next': {
        'value': 2,
        'next': {
            'value': 3,
            'next': None
        }
    }
}

print(head['next']['next']['value'])