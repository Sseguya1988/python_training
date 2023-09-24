# Function to compute the sum of the series
def compute_series_sum(n):
    series_sum = 0
    term = 2  # Initialize the first term
    for i in range(n):
        series_sum += term
        term = term * 10 + 2  # Generate the next term
    return series_sum

# Input the number of terms (n) from the user
n = int(input("Enter the number of terms in the series: "))

# Calculate and print the sum of the series
series_sum = compute_series_sum(n)
print(f"The sum of the series is: {series_sum}")
