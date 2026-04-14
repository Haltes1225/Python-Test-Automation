from is_palindrome import is_palindrome

def test_import_is_palindrome():
    try:
        from is_palindrome import is_palindrome
        assert callable(is_palindrome), "is_palindrome not callable"
    except ImportError as error:
        assert False, error

def test_int_type_word_is_palindrome():
    try:
        is_palindrome(1234)
        assert False, "TypeError expected"
    except TypeError:
        pass
    
def test_float_type_word_is_palindrome():
    try:
        is_palindrome(123.884999)
        assert False, "TypeError expected"
    except TypeError:
        pass

def test_list_type_word_is_palindrome():
    try:
        is_palindrome([1,2,3,4])
        assert False, "TypeError expected"
    except TypeError:
        pass

def test_bool_type_word_is_palindrome():
    try:
        is_palindrome(False)
        assert False, "TypeError expected"
    except TypeError:
        pass

def test_None_palindrome():
    try:
        is_palindrome(None)
        assert False, "TypeError expected"
    except TypeError:
        pass

def test_empty_string_is_palindrome():
    is_palindrome_result = is_palindrome("")
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_a_is_palindrome():
    is_palindrome_result = is_palindrome("a")
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_1001xa_is_palindrome():
    is_palindrome_result = is_palindrome("a"*1001)
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_kajak_is_palindrome():
    is_palindrome_result = is_palindrome("kajak")
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_alamakota_is_palindrome():
    string = "Ala ma kota"
    is_palindrome_result = is_palindrome(string)
    assert is_palindrome_result == False, f"Expected False, got {is_palindrome_result}"      

def test_case_sensitivity_is_palindrome():
    is_palindrome_result = is_palindrome("aaaAAA")
    assert is_palindrome_result == False, f"Expected False, got {is_palindrome_result}"

def test_special_characters_is_palindrome():
    string = "~!@#$%^&*()_+}{,./;'][=-]"
    string = string + string[::-1]
    is_palindrome_result = is_palindrome(string)
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_even_length_string_is_palindrome():
    string = "jdbdfjwkkivkkeo47888::<<>::L!@ŚRGGASaqcfeeEGTV46902d2xffgy"*2
    string = string + string[::-1]
    is_palindrome_result = is_palindrome(string)
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_uneven_length_string_is_palindrome():
    string = "nsbnrPDPevjh2kC224><<?'{e{}ee}||\pol||e==-23+fvfeeevllababababa"*2
    string = string + "ć" + string[::-1]
    is_palindrome_result = is_palindrome(string)
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"

def test_lorem_ipsum_is_palindrome():
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ante eu quam elementum aliquam non efficitur mi. Fusce pulvinar elit eget lorem rhoncus vehicula. Maecenas pretium in mi in feugiat. Sed mattis ante quis erat volutpat ultricies. Morbi turpis felis, laoreet vel sem a, lobortis pulvinar nulla. Sed placerat, erat quis blandit rhoncus, ante nisi aliquam justo, ac finibus nisl odio vitae risus. Cras in rhoncus massa. Sed et aliquam dui. Pellentesque ornare ultrices arcu in euismod. "
    is_palindrome_result = is_palindrome(string)
    assert is_palindrome_result == False, f"Expected False, got {is_palindrome_result}" 

def test_palindromised_lorem_ipsum_is_palindrome():
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ante eu quam elementum aliquam non efficitur mi. Fusce pulvinar elit eget lorem rhoncus vehicula. Maecenas pretium in mi in feugiat. Sed mattis ante quis erat volutpat ultricies. Morbi turpis felis, laoreet vel sem a, lobortis pulvinar nulla. Sed placerat, erat quis blandit rhoncus, ante nisi aliquam justo, ac finibus nisl odio vitae risus. Cras in rhoncus massa. Sed et aliquam dui. Pellentesque ornare ultrices arcu in euismod. "
    string = string + string[::-1]
    is_palindrome_result = is_palindrome(string)
    assert is_palindrome_result == True, f"Expected True, got {is_palindrome_result}"    

if __name__ == '__main__':
    for test in (
        test_import_is_palindrome,
        test_int_type_word_is_palindrome,
        test_float_type_word_is_palindrome,
        test_list_type_word_is_palindrome,
        test_bool_type_word_is_palindrome,
        test_empty_string_is_palindrome,
        test_None_palindrome,
        test_a_is_palindrome,
        test_case_sensitivity_is_palindrome,
        test_special_characters_is_palindrome,
        test_1001xa_is_palindrome,
        test_kajak_is_palindrome,
        test_alamakota_is_palindrome,
        test_even_length_string_is_palindrome,
        test_uneven_length_string_is_palindrome,
        test_lorem_ipsum_is_palindrome,
        test_palindromised_lorem_ipsum_is_palindrome
        
    ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)