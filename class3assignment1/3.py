# Unfortunately this code is illegal
# Looking at the error we get we can see that there is a syntax error
# Hovering with the mouse over the red line shows us that the block requires a specific structure

# try_stmt  ::=  try1_stmt | try2_stmt
# try1_stmt ::=  "try" ":" suite                                        <-
#                ("except" [expression ["as" identifier]] ":" suite)+   <-
#                ["else" ":" suite]
#                ["finally" ":" suite]
# try2_stmt ::=  "try" ":" suite
#                "finally" ":" suite

# try:
#     x = 1
# finally:
#     print(“finally”)

# As you can see the try block expects a structure like this

x = 1
try:  # <- must
    print(x)
except BaseException as e:  # <- must
    print(f"Something went wrong {e}")
else:  # <- optional - code is executed if no errors were raised
    print("If everything is OK")
finally:  # <- optional - code is executed regardless if the try block raises an error or not
    print("I'm going to run anyway")
