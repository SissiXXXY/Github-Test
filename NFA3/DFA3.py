# import re


def transit(tbl, currentsta, inp):
    for _input, _output, _next_status in tbl[currentsta]:
        if _input is None or _input == inp:
            print(f"current={currentsta}, input={inp}, output={_output}, next={_next_status}")
            return _next_status, _output
    return None


def run_dfa(tbl, input_s):
    current = 0
    for c in input_s:
        result = transit(tbl, current, c)

        if result is None:
            print("Failed")
            return

        next_status, output = result
        if next_status == -1:
            print("reach final status. output=", output)
            return
        current = next_status

    print("not matched, current status=", current)


'''DFA1_table = [{0, 'c', -1, 1},
              {1, 's', -1, 2},
              {2, 'c', -1, 3},
              {3, '1', -1, 4},
              {4, '7', -1, 5},
              {5, '3', 1, 6},
              {0,None,0, 0}]'''

DFA1_table = {
    0: [
        ('c', -1, 1),
        (None, 0, 0),
    ],
    1: [
        ('s', -1, 2),
        (None, 0, 1)
    ],
    2: [
        ('c', -1, 3),
        (None, 0, 2)
    ],
    3: [
        ('1', -1, 4),
        (None, 0, 3)
    ],
    4: [
        ('7', -1, 5),
        (None, 0, 4)
    ],
    5: [
        ('3', 1, -1),
        (None, 0, 5)
    ],
    -1: [
        (None, -1, -1)
    ]
}

DFA2_table = {
    0: [
        ('c', -1, 1),
        (None, 0, -1)
    ],
    1: [
        ('a', -1, 2),
        (None, 0, -1)
    ],
    2: [
        ('t', 1, -1),
        (None, 0, -1)
    ],
    -1: [
        (None, -1, -1)
    ]
}

DFA3_table = {
    0: [('0', -1, 1),
        ('1', -1, 0),
        ('\0', 1, -1),
        (None, 0, -1)],
    1: [('0', -1, 0),
        ('1', -1, 1),
        ('\0', 0, -1),
        (None, 0, -1)]
}

'''[{0, '0', -1, 1},
              {0, '1', -1, 0},
              {0, '\0', 1, 2},
              {1, '0', -1, 0},
              {1, '1', -1, 1},
              {1, '\0', 0, 2}]'''

if __name__ == '__main__':
    run_dfa(DFA1_table, "csc173")
    run_dfa(DFA2_table, "catcc")
    run_dfa(DFA3_table, "1000\0")
    # r = re.compile(r"[Hh][Tt][Tt][Pp][Ss]?://")
    # print(r.match("HtTPs://asdf.com"))
