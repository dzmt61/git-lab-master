def process_payment(amount):
    if amount <= 0:
        raise ValueError("Amount must be > 0!")
    return True