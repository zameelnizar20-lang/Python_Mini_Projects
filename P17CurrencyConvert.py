from decimal import Decimal , getcontext , InvalidOperation , ROUND_HALF_EVEN

getcontext().prec=28

def manual_rates():
    """
    Return exchange rates relative to USD (USD = 1).
    Example meaning: rates['EUR'] = 0.92 means 1 USD = 0.92 EUR
    """
    return{
        "USD" : Decimal("1"),
        "INR" : Decimal("0.92"),
        "EUR" : Decimal("83.50")
    }

def curr_validity_check(curruncy : str , rates : dict):
    code = curruncy.strip().upper()

    if not code in rates:
        raise ValueError(f"Unsupported currency '{curruncy}'. Supported: {', '.join(sorted(rates.keys()))}")
    return code

def amount_validity_check(amt_str : str):

    cleaned = amt_str.replace(",","").strip()

    try:
        value = Decimal(cleaned)
    
    except InvalidOperation:
        raise ValueError(f"Invalid numeric amount: '{amt_str}'")
    
    if value <0:
        raise ValueError("Amount must be non-negative.")
    return value
    
def convert_currency(amount : Decimal , fr_curr : str , to_crr : str , rates : dict):

    from_code = fr_curr.upper()
    to_code =  to_crr.upper()
    

    if from_code not in rates or to_code not in rates:
        raise ValueError ("Currency not supported.")
    
    if from_code == to_code:
        return amount.quantize(Decimal("0.01"),rounding=ROUND_HALF_EVEN)
    

    rate_from = rates[from_code]
    final_amount  = amount/ rate_from

    rate_to = rates[to_code]
    converted = final_amount * rate_to

    return converted.quantize(Decimal("0.01"),rounding=ROUND_HALF_EVEN)


def final_print(amount, curruncy):
    return f"{amount:.2f} : {curruncy.upper()}"
    
    


def run_converter():
    """
    Simple CLI run function. Reads input from user, runs conversion, prints result.
    Keeps UI logic out of conversion functions for testability.
    """

    rates = manual_rates()

    print("Avalible Curuncy list : ", ", ".join(sorted(rates.keys())))

    try:
        amt_str = input("Please Enter the ammount : ").strip()
        fr_curr = input("From currency (code, e.g. USD): ").strip()
        to_crr = input("To currency (code, e.g. INR): ").strip()

        amount = amount_validity_check(amt_str)
        from_code = curr_validity_check(fr_curr,rates)
        to_code = curr_validity_check(to_crr,rates)

        result = convert_currency(amount,fr_curr,to_crr,rates)
        print(f"{final_print(amount,from_code)} = {final_print(result,to_code)}")
    
    except Exception as e:
        print("Error",e)



if __name__=='__main__':
    run_converter()
        


