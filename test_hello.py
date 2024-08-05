from hello import toyou, add, subtract

def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10

def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x

def test_hello_toyou():
    setup_function(test_hello_toyou)
    assert toyou("test") == "hi test", "Failed test_hello_toyou"
    teardown_function(test_hello_toyou)

def test_hello_add():
    setup_function(test_hello_add)
    assert add(test_hello_add.x) == 11, "Failed test_hello_add"
    teardown_function(test_hello_add)

def test_hello_subtract():
    setup_function(test_hello_subtract)
    assert subtract(test_hello_subtract.x) == 9, "Failed test_hello_subtract"
    teardown_function(test_hello_subtract)

# Run the tests
test_hello_toyou()
test_hello_add()
test_hello_subtract()

