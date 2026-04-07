def test_import_is_palindrome():
    try:
        from is_palindrome import is_palindrome
        assert callable(is_palindrome), "is_palindrome not callable"
    except ImportError as error:
        assert False, error

def test_int_type_word_is_palindrome():
    try:
        from is_palindrome import is_palindrome
        is_palindrome(1234)
    except TypeError as error:
        assert False, error

def test_list_type_word_is_palindrome():
    try:
        from is_palindrome import is_palindrome
        is_palindrome([1,2,3,4])
    except TypeError as error:
        assert False, error

def test_bool_type_word_is_palindrome():
    try:
        from is_palindrome import is_palindrome
        is_palindrome(False)
    except TypeError as error:
        assert False, error

def test_a_is_palindrome():
    from is_palindrome import is_palindrome
    is_palindrome_result = is_palindrome("a")
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_empty_string_is_palindrome():
    from is_palindrome import is_palindrome
    is_palindrome_result = is_palindrome("")
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

if __name__ == '__main__':
    for test in (
        test_import_is_palindrome,
        test_int_type_word_is_palindrome,
        test_list_type_word_is_palindrome,
        test_bool_type_word_is_palindrome,
        test_empty_string_is_palindrome,
        test_a_is_palindrome
        
    ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)