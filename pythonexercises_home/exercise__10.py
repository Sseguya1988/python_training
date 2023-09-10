# Exercise 10: Access the nested key increment from the following dictionary
emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}
# Use a for loop to access Key in dict
for key, value in emp_dict.items():
    print(key)
