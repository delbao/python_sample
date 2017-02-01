import traceback

def another_function():
    lumberstack()

def lumberstack():
    print "stack trace is ..."
    traceback.print_stack()
    print repr(traceback.extract_stack())
    print repr(traceback.format_stack())

if __name__ == '__main__':
    another_function()
