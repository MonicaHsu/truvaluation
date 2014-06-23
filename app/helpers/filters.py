

# Formats number values into dollar currency
# e.g. 123690 is changed to $123,690M
def format_currency(value):
	return "${:,}".format(int(round((value),-4)))

def format_percent(value):
	return round((value),-2)
