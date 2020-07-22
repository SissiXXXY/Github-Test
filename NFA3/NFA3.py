# import re
import logging


def transit(tbl, currentsta, inp):
    for _input, _output, _next_status in tbl[currentsta]:
        if _input is None or inp == _input:
            logging.info(f"current={currentsta}, input={inp}, output={_output}, next={_next_status}")
            return _next_status, _output
    logging.error(f"can not find next status for current={currentsta} inp={inp} ")
    return None


def run_nfa(tbl, input_s):
    currentlist = [0]
    for c in input_s:
        nextsta_union = set()
        outputp = -2
        logging.debug(f"currentlist={currentlist},c={c}")
        for currentx in currentlist:
            nextstatusl, outputp = transit(tbl, currentx, c)
            nextsta_union = nextsta_union.union(set(nextstatusl))
            logging.debug(f"nextsta_union={nextsta_union}")
            if -1 in nextsta_union and outputp == 1:
                print("TRUE, reached the final state")
                return
        currentlist = nextsta_union
        print(f"output={outputp},next={nextsta_union}") #??????????????????????????????????????????????????????
        '''if -1 in nextsta_union and outputp == 1:
            print("TRUE, reached the final state")
            return'''
    print(f"False, currentstatus={currentlist}, input={c} output={outputp}, nextstatus={nextsta_union}")


'''
def rrun_nfa(tbl, input_s):
    current = 0
    for c in input_s:
        result = transit(tbl, current, c)
        logging.debug(f"current={current} input={c} result={result}")

        if result is None:
            print("Failed")
            return

        next_status, output = result
        if next_status == -1:
            print("reach final status. output=", output)
            return
        current = next_status

    print("not matched, current status=", current)
'''

'''DFA1_table = [{0, 'c', -1, 1},
              {1, 's', -1, 2},
              {2, 'c', -1, 3},
              {3, '1', -1, 4},
              {4, '7', -1, 5},
              {5, '3', 1, 6},
              {0,None,0, 0}]'''

'''NFA1_table = {


    (0, 'c'): [
        (-1, 1)
    ],
    (0, '\0'):[
        (0, -1) #false, jump to the final state
    ],
    (0, None): [
        (-1, 0)
    ],

    (1, 'c'): [
        (-1, 2)
    ],
    (1, None): [
        (-1, 0)
    ],
    (2, 'd'): [
        (-1, 3)
    ],
    (2, None): [
        (-1, 0)
    ],
    (3, 'e'): [
        (-1, 4)
    ],
    (3, None):[
        (-1, 0)
    ],
    (4, '\0'):[
        (1, -1) #'code' at the end, true, final state
    ],
    (4, None):[
        (-1, 0) #string not finish, 'code' is not at the end, back to first state
    ],
    (-1, None):[
        (-1, -1)
    ]
}'''
NFA1_tbl = {
    0: [
        # (['\0'], 0, 0),  # false, jump to the final state ！！！！！problem here
        (['c', None], -1, [1, 0])

        # (['c'],-1,[1])
        # ([None],-1,[0])

    ],
    1: [
        (['o', None], -1, [2, 0])
    ],
    2: [
        (['d', None], -1, [3, 0])
    ],
    3: [
        (['e', None], -1, [4, 0])
    ],
    4: [
        (['\0'], 1, [-1]),  # 'code' at the end, true, final state
        ([None], -1, [0])
    ],
    -1: [
        ([None], -1, [-1])
    ]
}
NFA2_table = {
    0: [
        ('g', -1, 1),
        (None, -1, 0)
    ],
    1: [
        ('o', 1, 2),
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

NFA3_table = {
    0: [
        ('a', -1, [0, 1]),
        ('g', -1, [0, 3]),
        ('h', -1, [0, 5]),
        ('i', -1, [0, 7]),
        ('o', -1, [0, 9]),
        ('s', -1, [0, 11]),
        ('t', -1, [0, 13]),
        ('w', -1, [0, 15]),
        ('n', -1, [0, 17]),
        (None, -1, [0])
    ],
    1: [
        ('a', -1, [1, 2]),
        (None, -1, [1])
    ],
    2: [
        (None, 1, [-1])
    ],
    3: [
        ('g', -1, [3, 4]),
        (None, -1, [3])
    ],
    4: [
        (None, 1, [-1])
    ],
    5: [
        ('h', -1, [5, 6]),
        (None, -1, [5])
    ],
    6: [
        (None, 1, [-1])
    ],
    7: [
        ('i', -1, [7, 8]),
        (None, -1, [7])
    ],
    8: [
        (None, 1, [-1])
    ],
    9: [
        ('o', -1, [9, 10]),
        (None, -1, [9]),
    ],
    10: [
        (None, 1, [-1])
    ],
    11: [
        ('s', -1, [11, 12]),
        (None, -1, [11])
    ],
    12: [
        (None, 1, [-1])
    ],
    13: [
        ('t', -1, [13, 14]),
        (None, -1, [13])
    ],
    14: [
        (None, 1, [-1])
    ],
    15: [
        ('w', -1, [15, 16]),
        (None, -1, [15])
    ],
    16: [
        (None, 1, [-1])
    ],
    17: [
        ('n', -1, [17, 18]),
        (None, -1, [17])
    ],
    18: [
        ('n', -1, [18, 19]),
        (None, -1, [18])
    ],
    19: [
        (None, 1, [-1])
    ],
    -1: [
        (None, 1, -1)
    ]
}

'''[{0, '0', -1, 1},
              {0, '1', -1, 0},
              {0, '\0', 1, 2},
              {1, '0', -1, 0},
              {1, '1', -1, 1},
              {1, '\0', 0, 2}]'''

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("start")

    run_nfa(NFA3_table, "annn\0")
    # run_dfa(DFA2_table, "catcc")
    # run_dfa(DFA3_table, "1000\0")
    # r = re.compile(r"[Hh][Tt][Tt][Pp][Ss]?://")
    # print(r.match("HtTPs://asdf.com"))
