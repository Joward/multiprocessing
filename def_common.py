list_run = set()

def def_run(cmd_type, *args):
    test = {}
    test['cmd_type'] = cmd_type
    test['cmd_opt'] = list(args)
    list_run.append(test)