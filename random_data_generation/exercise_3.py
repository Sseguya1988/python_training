# Exercise 3: Generate 6 digit random secure OTP
import secrets
# to generate a 6 digit OPT
otp = secrets.randbelow(10**6)
# ensure OTP has six digits, with leading zeros if necessary
otp_string = f"{otp:06}"
print(f"The required 6-digit OTP is : {otp}")

