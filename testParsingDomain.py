from parsingDomain import is_subset, is_integer

def unitTest(fun, arg, expected):
    result = fun(arg)
    if result[0] == expected:
        print("Test succeeded:", end="")
    else:
        print("Test FAILED", end="")

    if result[0] == False:
        print(" " + result[1] + " ( {} )".format(arg))
    else:
        print(" ( {} )".format(arg))


unitTest(is_integer, "-144", True)
unitTest(is_integer, "144", True)
unitTest(is_integer, "144.3", False)
unitTest(is_integer, "144.3.1", False)
unitTest(is_integer, "abc", False)
unitTest(is_integer, "11aa", False)
unitTest(is_integer, "aa11", False)
unitTest(is_integer, "0", True)


unitTest(is_subset, "]-4;-1]U{1}U[2;4]", True)
unitTest(is_subset, "]-4;-1]U{1}U[2,4]", False)
unitTest(is_subset, "]-4;-1]U{1}U[2;4", False)
unitTest(is_subset, "]-4;1;-1]U{1}U[2;4]", False)
unitTest(is_subset, "{1}", True)
unitTest(is_subset, "]abc;-1]U{1}U[2;4]", False)
unitTest(is_subset, "]-4;-1]U{1}UU[2;4]", False)
unitTest(is_subset, "", False)
unitTest(is_subset, "12", False)
unitTest(is_subset, "[2]", False)
unitTest(is_subset, "[3;2]", False)
unitTest(is_subset, "[3;3]", False)
