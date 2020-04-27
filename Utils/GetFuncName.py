from Utils.Logger import log

def get_func_name(testdict):
    testdata = testdict.copy()
    funclist = []
    for i in range(0, len(testdata)):
        key = testdata[i][1]
        func = key + '('
        for j in range(2, len(testdata[i])):
            if testdata[i][j] and testdata[i][j] != 'NA':
                func = func + '"' + testdata[i][j] + '"'+ ','
            else:
                pass
        func = func.strip(',') + ')'
        print(func)
        funclist.append(func)
    return funclist