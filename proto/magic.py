def fixdocstring(func):

    func.__doc__ = func.__doc__.replace('<arg_a>', 'a: a very common argument')
    #(This is just an example, other string formatting methods can be used as well.)
    return func

    list_params

@fixdocstring
def test(a):
    '''
    Arguments:
    <arg_a>
    '''
    pass
