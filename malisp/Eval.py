from . import Types
from . import Reader
from . import Core

def apply(f, args, env):

    if isinstance(args[0], Reader.MalData):
        args[0] = args[0].data

    if isinstance(args[1], Reader.MalData):
        args[1] = args[1].data
    
    return f(args[0], args[1])

def eval_ast(arg, env):
    if type(arg) == list:
        buffer = []
        for node in arg:
            buffer.append(Core.int_eval(node, env))

        return buffer
    else:
        if isinstance(arg, Reader.MalData) and arg.data_type == 'SYM':
            #if arg.data in env.data:
            return env.get(arg.data)
        else:
            return arg