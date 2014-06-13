

# Formats number values into dollar currency
# e.g. 123690 is changed to $123,690M
def format_currency(value):
    return "${:,}M".format(value)

def round_value(value):
    return round(value)

