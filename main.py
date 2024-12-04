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
    ["TSLA", "AUR", "LAZR"],                                   # Transportation
    ["COHR", "GEV", "SOUN", "ALAB", "ISRG",                    # Added
     "AVAV", "PEGA", "UPST", "PRCT", "AI", "PLTR",
     "VRT", "NET", "PATH", "UPST", "SERV", "APLD", "ARM",
     "HPAI", "TER", "SYNA", "AMBA", "SYM", "MYO", "REKR",
     "AIRE", "IOT", "DE", "OSS", "MBOT", "VRSSF", "CYN",
     "AITX", "TREIF", "NMTC", "PKKFF", "FOBIF", "IBM",
     "NFLX", "EKSO", "AIGFF", "ATIXF", "OTRK", "NEXCF",
     "AIMLF", "HAPBF", "DTMXF", "SNPS", "AICOF", "KVYO",
     "KITT", "QGSI", "ORCL", "POET"]                          
]

# Companies to exclude based on activities for example
exclusions = ["EXAI"]

def filter_tickers(tickers, exclusions):
    """Filters out the tickers present in exclusions."""
    return [
        [ticker for ticker in row if ticker not in exclusions] 
        for row in tickers
    ]

# Apply filtering function
filtered_ai_tickers = filter_tickers(ai_tickers, exclusions)

# Calculate the number of included and excluded tickers
total_tickers = sum(len(row) for row in ai_tickers)
included_count = sum(len(row) for row in filtered_ai_tickers)
excluded_count = total_tickers - included_count

# Output results
print("\nNumber of tickers included:", included_count)
print("Number of tickers excluded:", excluded_count)