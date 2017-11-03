# print("First Demo")
def demo_string():
    stra = 'hello worlD'
    print(stra.capitalize())
    print(stra.replace('worlD', 'qiaoweiba'))
    strb = '   \n\rhello qiaoweiba \r\n'
    print(1, strb.lstrip())
    print(2, strb.rstrip())
    strc = 'hello w'
    print(3, strc.startswith('helo'))
    print(4, strc.startswith('hel'))
    print(5, strc.endswith('x'))
    print(6, stra+strb+strc)
    print(7, stra + strb + strc)
    print(len(strc))


def demo_operation():
    print(1, 1+2+2, 2*5, 2**5)
    print(2, True, False)


def demo_buildinfunction():
    print(1, max(2, 1), min(5, 2))
    print(2, abs(-2))
    print(3, list(range(1, 10, 3)), range(1, 3, 10))
    print(4, dir(list))
    print(5, chr(97), ord('a'))


def demo_controlflow():
    # continue, break, pass
    for i in range(0, 10, 2):
        if i < 5:
            continue
        print(1, i)
        if i == 6:
            break
if __name__ == '__main__':
    # print('hello qiaoweiba')
    # comment
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    demo_controlflow()
