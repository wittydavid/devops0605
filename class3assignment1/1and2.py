# There are two options catching an exception
# 1. Catch a "generic" exception
try:
    a = 1 / 0
except BaseException as e:
    print(f"The reason for the exception is (using args) - {e.args}, or (using string) - {e.__str__()}")
# Letting the code run with out an exception allows up to catch the specific exception type
# 2. Catch a "specific" exception
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(f"The reason for the exception is (using args) - {e.args}, or (using string) - {e.__str__()}")
