ret = list()
n = 3
def process(n, numOpen, numClose, str, ret):
    # termination check
    if numOpen == n and numClose == n:
        ret.append(str)
        return
    # recurse next
    if numOpen < n:
        process(n, numOpen + 1, numClose, str + "(", ret)  # add open bracket
    if numClose < numOpen:
        process(n, numOpen, numClose + 1, str + ")", ret)  # add close bracket

process(n, 0, 0, "", ret)  # recurse
print(ret) 