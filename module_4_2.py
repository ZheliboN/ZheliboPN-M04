def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
inner_function()
# inner_function() - внутри функции test_function, вызов напрямую из программы невозможен, т.е. вне области видимости
