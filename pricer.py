from math import log, sqrt, exp, erf

def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def black_scholes_price(
    S: float,      # spot price
    K: float,      # strike
    r: float,      # risk-free rate (annual, contin. comp.)
    sigma: float,  # volatility (annual)
    T: float,      # time to maturity in years
    option_type: str = "call"  # "call" or "put"
) -> float:
    if T <= 0 or sigma <= 0:
        # At expiry or zero vol, the option is just intrinsic value
        if option_type == "call":
            return max(S - K, 0.0)
        elif option_type == "put":
            return max(K - S, 0.0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    if option_type == "call":
        price = S * norm_cdf(d1) - K * exp(-r * T) * norm_cdf(d2)
    elif option_type == "put":
        price = K * exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price

if __name__ == "__main__":
    # Example usage
    S = 100.0   # spot
    K = 150.0   # strike
    r = 0.0415    # 2% risk-free
    sigma = 0.25  # 25% vol
    T = 10.0     # 1 year

    call_price = black_scholes_price(S, K, r, sigma, T, "call")
    put_price  = black_scholes_price(S, K, r, sigma, T, "put")

    print(f"Call price: {call_price:.4f}")
    print(f"Put  price: {put_price:.4f}")
