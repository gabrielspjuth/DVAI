# Original matrix with potential exclusions
ai_tickers = [
    ["NVDA", "MSFT", "GOOGL", "META", "AMZN", "AMD", "AAPL"],  # Major Tech Companies
    ["CRM", "NOW", "ADBE", "PLTR", "PATH", "SNOW", "WDAY"],    # Software and Cloud
    ["INTC", "TSM", "AVGO", "MU", "ASML", "MRVL", "KLAC"],     # Semiconductors
    ["CGNX", "ROK", "TER", "IRBT"],                            # Robotics
    ["AI", "BBAI", "RXRX", "AYX", "DDOG"],                     # Analytics
    ["TTD", "U", "RBLX", "SSTK"],                              # Entertainment
    ["EXAI", "TEM", "RBOT"],                                   # Healthcare
    ["SOUN", "GFAI", "KSCP", "MDAI"],                          # Smaller Innovators
    ["PANW", "CRWD", "ZS"],                                    # Cybersecurity
    ["TSLA", "AUR", "LAZR"]                                    # Transportation
]

# Companies to exclude based on activities
exclusions = ["RXRX"]  # Example of drug-related companies, adjust as needed

# Create a new matrix excluding unwanted stocks
filtered_ai_tickers = [[ticker for ticker in row if ticker not in exclusions] for row in ai_tickers]

# Printing the filtered matrix
for row in filtered_ai_tickers:
    print(row)