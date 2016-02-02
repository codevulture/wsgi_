def decorating_func(func):
    def func_wrapper(name):
        name = str(name) + "decorating -----------------",
        func(name)
        print "decorating completed---------"
    return func_wrapper


@decorating_func
def fun(name):
    print "Hi my name is jaivish {0},".format(name)


fun("Jai")
