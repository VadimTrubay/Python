#calculator
import numexpr

expr = input("Введите математическую операцию: ")
result = numexpr.evaluate(expr)
print(f"Результат: {result}")

input()
