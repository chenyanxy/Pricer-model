# Pricer-model
It computes the fair value of a European option using the Black–Scholes formula.

The script first defines a small function to calculate the normal cumulative distribution, which is needed for the Black–Scholes equations. Then it defines the main pricing function, which takes the market inputs—spot, strike, interest rate, volatility and time to maturity—and converts them into the two core quantities of the model, d1 and d2. These measure how far the option is in- or out-of-the-money once uncertainty and time are accounted for.

With d1 and d2, the function applies the standard closed-form formula: a call is valued as the discounted probability-weighted payoff of finishing above the strike, and a put as the opposite. If maturity or volatility is zero, the code simply returns the intrinsic value because there is no randomness left.

The bottom part of the script is only a runnable example: it sets some numbers, calls the pricing function for both call and put, and prints the results.
