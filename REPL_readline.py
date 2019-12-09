import os
import sys
import readline as sys_readline

history_loaded = False
histfile = os.path.expanduser("~/.mylisp_history.log")

def readline(prompt="user> "):
    global history_loaded
    if not history_loaded:
        history_loaded = True
        try:
            with open(histfile, "r") as hf:
                for line in hf.readlines():
                    sys_readline.add_history(line.rstrip("\r\n"))
                    pass
        except IOError:
            pass

    try:
        line = input(prompt)
        sys_readline.add_history(line)
        with open(histfile, "a") as hf:
            hf.write(line + "\n")
    except IOError:
        pass
    except EOFError:
        return None
    return line