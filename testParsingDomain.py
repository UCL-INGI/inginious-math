from parsingDomain import is_interval, is_integer, compareDomains, expandSet, expandInterval, expandExclu, is_set, is_simpleInterval, is_intervalExclu

succeededCount = 0
failedCount = 0

def unitTest(fun, arg, expected):
    global failedCount
    global succeededCount

    result = fun(arg)
    if result[0] == expected:
        succeededCount += 1
        print("Test succeeded:", end="")
    else:
        failedCount += 1
        print("Test FAILED", end="")

    if result[0] == False:
        print(" " + result[1] + " ( {} )".format(arg))
    else:
        print(" ( {} )".format(arg))

def unitTest2(result, expected):
    global failedCount
    global succeededCount

    if result[0] == expected:
        succeededCount += 1
        print("Test succeeded:", end="")
    else:
        failedCount += 1
        print("Test FAILED", end="")

    if result[0] == False:
        print(" " + result[1])
    else:
        print()

def unitTestSimple(actual, expected):
    global failedCount
    global succeededCount

    if actual == expected:
        succeededCount += 1
        print("Test succeeded")
    else:
        failedCount += 1
        print("Test FAILED")

print("Test of 'is_integer'\n")

unitTest(is_integer, "-144", True)
unitTest(is_integer, "144", True)
unitTest(is_integer, "144.3", False)
unitTest(is_integer, "144.3.1", False)
unitTest(is_integer, "abc", False)
unitTest(is_integer, "11aa", False)
unitTest(is_integer, "aa11", False)
unitTest(is_integer, "0", True)
unitTest(is_integer, "a", False)
unitTest(is_integer, "+inf", True)
unitTest(is_integer, "-inf", True)
unitTest(is_integer, "+inf3", False)

print("\nTest of 'is_interval'\n")

unitTest(is_interval, "]-4;-1]U{1}U[2;4]", True)
unitTest(is_interval, "]-4;-1]U{1}U[2,4]", False)
unitTest(is_interval, "]-4;-1]U{1}U[2;4", False)
unitTest(is_interval, "]-4;1;-1]U{1}U[2;4]", False)
unitTest(is_interval, "{1}", True)
unitTest(is_interval, "]abc;-1]U{1}U[2;4]", False)
unitTest(is_interval, "]-4;-1]U{1}UU[2;4]", False)
unitTest(is_interval, "", False)
unitTest(is_interval, "12", False)
unitTest(is_interval, "[2]", False)
unitTest(is_interval, "[3;2]", False)
unitTest(is_interval, "[3;3]", False)
unitTest(is_interval, "{0;1;2;3}", True)
unitTest(is_interval, "{0;2;a;3}", False)
unitTest(is_interval, "[0;2]\{1}", True)
unitTest(is_interval, "[0;2]\{3}", False)
unitTest(is_interval, "[0;2;3]\{1}", False)
unitTest(is_interval, "[0;2]\{a}", False)
unitTest(is_interval, "{}", True)
unitTest(is_interval, "{0}u{1}", True)
unitTest(is_interval, "R", True)
unitTest(is_interval, "R\{0}", True)
unitTest(is_interval, "[0;+inf[", True)
unitTest(is_interval, "]-inf;+inf[", True)
unitTest(is_interval, "]-inf;0[", True)
unitTest(is_interval, "]+inf;+inf[", False)
unitTest(is_interval, "]-inf;-inf[", False)
unitTest(is_interval, "]-10;-inf[", False)
unitTest(is_interval, "]+inf;1[", False)
unitTest(is_interval, "[-inf;1[", False)
unitTest(is_interval, "[1;+inf]", False)
unitTest(is_interval, "]inf;inf[", False)
unitTest(is_interval, "]inf;1[", False)
unitTest(is_interval, "[1;inf]", False)
unitTest(is_interval, "[0;inf[", True)

print("\nTest of 'compareDomains'\n")

unitTest2(compareDomains("[1;2]", "[2;3]U[1;2]"), False)
unitTest2(compareDomains("[2;3]U[1;2]", "[1;2]"), False)
unitTest2(compareDomains("[2;3]U[1;2]", "[1;2]U[2;3]"), True)
unitTest2(compareDomains(" [ 1 ; 2 ] ", "[1;2]"), True)
unitTest2(compareDomains("[-2;10]\{3;5;7} U [11;12[", "[11;12[ U [-2;3[U]3;5[U]5;7[U]7;10]"), True)
unitTest2(compareDomains("[-2;10]\{3;5;10} U [11;12[", "[11;12[ U [-2;3[U]3;5[U]5;7[U]7;10]"), False)
unitTest2(compareDomains("R\{0}", "]-inf;0[U]0;+inf["), True)
unitTest2(compareDomains("]-inf;inf[", "]-inf;+inf["), True)
unitTest2(compareDomains("{0}u{1}", "{0}U{1}"), True)
unitTest2(compareDomains("R", "R"), True)
unitTest2(compareDomains("R", "]-inf ; +inf["), True)

print("\nTest of 'expandSet'\n")

unitTestSimple(expandSet("{0;1;2}"), "{0}U{1}U{2}")
unitTestSimple(expandSet("{0}"), "{0}")

print("\nTest of 'expandExclu'\n")

unitTestSimple(expandExclu("[2;5]\{3;4}"), "[2;3[U]3;4[U]4;5]")
unitTestSimple(expandExclu("R\{0}"), "]-inf;0[U]0;inf[")

print("\nTest of 'expandInterval'\n")

unitTestSimple(expandInterval("{0;1;2}"), "{0}U{1}U{2}")
unitTestSimple(expandInterval("[2;5]\{3;4}"), "[2;3[U]3;4[U]4;5]")
unitTestSimple(expandInterval("[2;5]\{3;4}U{0;1;2}"), "[2;3[U]3;4[U]4;5]U{0}U{1}U{2}")

print("\nTest of 'is_set'\n")

unitTest(is_set, "{1;2;3", False)
unitTest(is_set, "{1;2;3}", True)
unitTest(is_set, "1;2;3", False)
unitTest(is_set, "{a;2;3}", False)

print("\nTest of 'is_simpleInterval'\n")

unitTest(is_simpleInterval, "[2;3;4]", False)
unitTest(is_simpleInterval, "[4;3]", False)
unitTest(is_simpleInterval, "[3;4}", False)
unitTest(is_simpleInterval, "[a;b]", False)
unitTest(is_simpleInterval, "[1,2]", False)
unitTest(is_simpleInterval, "[1;10]", True)

print("\nTest of 'is_intervalExclu'\n")

unitTest(is_intervalExclu, "[2;3]\{4}", False)
unitTest(is_intervalExclu, "[2;3]\{1}", False)
unitTest(is_intervalExclu, "[2;8]\{3}\{4}", False)
unitTest(is_intervalExclu, "[4;2]\{3}", False)
unitTest(is_intervalExclu, "[2;3]\{3}", False)

print("\n\nNumber of tests succeeded: {}/{}".format(succeededCount,succeededCount+failedCount))
print("Number of tests failed: {}/{}".format(failedCount, failedCount+succeededCount))
