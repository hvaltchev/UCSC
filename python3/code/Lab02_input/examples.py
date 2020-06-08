#!/usr/bin/env python3
"""
Some example f-strings.
""" 
the_float = 12.345
print(f'float: f"{{the_float}}" \t\t\t\t= |{the_float}|')
print(f'float: f"{{the_float:.2}}" \t\t\t= |{the_float:.2}|')
print(f'money: f"${{the_float:.2f}}" \t\t\t= ${the_float:.2f}')
print(f'float: f"{{the_float:+10.2f}}"'
      f' \t\t\t= |{the_float:+10.2f}|')
print(f'float: f"{{the_float:<10.2f}}"'
      f' \t\t\t= |{the_float:<10.2f}|')
print()
the_int = 12
print(f'int: f"{{the_int}}" \t\t\t\t= |{the_int}|')
print(f'hex: f"{{the_int:#X}}" \t\t\t\t= |{the_int:#X}|')
print()
the_string = "Croque Monsieur"
print(f'str: f"{{the_string}}" \t\t\t\t= |{the_string}|')
print(f'str: f"{{the_string:<20}}" \t\t\t= |{the_string:<20}|')
print(f'str: f"{{the_string:^20}}" \t\t\t= |{the_string:^20}|')
print(f'str: f"{{the_string:*>20}}" \t\t\t= |{the_string:*>20}|')
print(f'str: f"{{the_string:2}}" \t\t\t\t= |{the_string:2}|')
print(f'str: f"{{the_string:.2}}" \t\t\t\t= |{the_string:.2}|')
print(f'unicode: f"{{165:c}}" \t\t\t\t= |{165:c}|')
print()
short_str = "XO"
print(f'str: f"{{short_str * 2:^{{3*len(short_str)}}}}"'
      f' \t= |{short_str * 2:^{3*len(short_str)}}|')
