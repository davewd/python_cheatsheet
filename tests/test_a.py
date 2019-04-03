import python_cheatsheet.a as a

def test_PublicFn() :
    assert a.public_fn_with_googley_docstring("test") == 0

if __name__ == "__main__" :
    unittest.main(verbosity=2, exit=False);

