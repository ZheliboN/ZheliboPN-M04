# Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции divide из модулей fake_math и true_math,
# назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён, при помощи оператора as.
from fake_math import divide as div_fake
from true_math import divide as div_true

result1 = div_fake(69, 3)
result2 = div_fake(3, 0)
result3 = div_true(49, 7)
result4 = div_true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
