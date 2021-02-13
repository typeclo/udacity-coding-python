def get_foo():
    response = input('Say "foo"!\n')
    if response != 'foo':
        get_foo()

get_foo()
