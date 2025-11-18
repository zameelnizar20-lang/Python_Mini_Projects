from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation, getcontext

# Set Decimal precision high enough for currency math
getcontext().prec = 28

def get_rates_manual():
    """
    Return exchange rates relative to USD (USD = 1).
    Example meaning: rates['EUR'] = 0.92 means 1 USD = 0.92 EUR
    """
    return {
        "USD": Decimal("1.0"),
        "EUR": Decimal("0.92"),   # example: 1 USD = 0.92 EUR
        "INR": Decimal("83.50"),  # example: 1 USD = 83.50 INR
    }

def get_rates_api():
    """
    OPTIONAL: placeholder for API-based rates.
    Implementation would:
      - call an API (e.g., exchangeratesapi.io, openexchangerates, etc.)
      - parse JSON, convert floats to Decimal
      - return a dict with the same shape as get_rates_manual()
    Separated so network code is not mixed with conversion logic.
    """
    raise NotImplementedError("Add API integration here if you want live rates.")

def validate_currency(currency: str, rates: dict):
    """Return currency uppercased if valid, else raise ValueError."""
    code = currency.strip().upper()
    if code not in rates:
        raise ValueError(f"Unsupported currency '{currency}'. Supported: {', '.join(sorted(rates.keys()))}")
    return code

def parse_amount(amount_str: str) -> Decimal:
    """
    Parse a user input amount string into Decimal.
    Accepts: "1,234.56", " 1000 ", "500"
    Raises ValueError for invalid or negative amounts.
    """
    cleaned = amount_str.replace(",", "").strip()
    try:
        value = Decimal(cleaned)
    except InvalidOperation:
        raise ValueError(f"Invalid numeric amount: '{amount_str}'")
    if value < 0:
        raise ValueError("Amount must be non-negative.")
    return value

def convert_currency(amount: Decimal, from_curr: str, to_curr: str, rates: dict) -> Decimal:
    """
    Convert amount from `from_curr` to `to_curr` using rates dict (relative to USD).
    Steps:
      1. Convert from `from_curr` to USD: amount_in_usd = amount / rate[from_curr]
      2. Convert USD to `to_curr`: converted = amount_in_usd * rate[to_curr]
    Using Decimal ensures accurate arithmetic for money.
    """
    from_code = from_curr.upper()
    to_code = to_curr.upper()
    # validate (assumes caller validated, but safe to check)
    if from_code not in rates or to_code not in rates:
        raise ValueError("Currency not supported.")
    # If from_curr == to_curr, return same amount
    if from_code == to_code:
        return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

    # Step 1: convert from `from_curr` to USD (base)
    rate_from = rates[from_code]
    amount_in_usd = amount / rate_from

    # Step 2: convert USD to `to_curr`
    rate_to = rates[to_code]
    converted = amount_in_usd * rate_to

    # Round to 2 decimal places (common for currencies)
    return converted.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

def format_amount(amount: Decimal, currency: str) -> str:
    """Return formatted string like '123.45 USD'."""
    return f"{amount:.2f} {currency.upper()}"

def run_converter():
    """
    Simple CLI run function. Reads input from user, runs conversion, prints result.
    Keeps UI logic out of conversion functions for testability.
    """
    rates = get_rates_manual()
    print("Supported currencies:", ", ".join(sorted(rates.keys())))
    try:
        amt_str = input("Enter amount: ").strip()
        from_curr = input("From currency (code, e.g. USD): ").strip()
        to_curr = input("To currency (code, e.g. EUR): ").strip()

        amount = parse_amount(amt_str)
        from_code = validate_currency(from_curr, rates)
        to_code = validate_currency(to_curr, rates)

        result = convert_currency(amount, from_code, to_code, rates)
        print(f"{format_amount(amount, from_code)} = {format_amount(result, to_code)}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    run_converter()
