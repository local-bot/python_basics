#! /usr/bin/env python3

price = 49

txt = "For only %.2f dollars!" % (price)

print(txt)

txt2 = f"For only {price:.2f} dollars!"
print(txt2)