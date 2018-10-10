from __future__ import print_function

from itertools import chain, combinations, product

params_methodHeaders = [
    ['"jsonrpc":"2.0"', '"jsonrpc": ""', '"jsonrpc":"True"',
     '"jsonrpc": null', '"jsonrpc":1', '"jsonrpc":0.0000000001',
     '"jsonrpc":"String"']
    ,
    ['"method":"loginUser"', '"method":""', '"method":"True"', '"method":null', '"method":1', '"method":0.0000000001',
     '"method":"String"']
    , ['"id":"loginUser"', '"id":""', '"id":"True"', '"id":null', '"id":1', '"id":0.0000000001', '"id":"String"']
    , [
        '"params":{"email": "user@mail.domain", "hash": "5c60fead1d0596dd725be08f481b4a8f", "uiType": "Web", "locale": "en_US"'
        ,
        '"params":{"email": "user@mail.domain", "hash": "5c60fead1d0596dd725be08f481b4a8f", "uiType": "Desktop", "locale": "en_US"'
        ,
        '"params":{"email": "user@mail.domain", "hash": "5c60fead1d0596dd725be08f481b4a8f", "uiType": "Android", "locale": "en_US"'
        ,
        '"params":{"email": "user@mail.domain", "hash": "5c60fead1d0596dd725be08f481b4a8f", "uiType": "iOS", "locale": "en_US"'
    ]
]


def pairwise_generator(*sequences):
    unseen = set(chain.from_iterable(product(*i) for i in combinations(sequences, 2)))
    for path in product(*sequences):
        common_pairs = set(combinations(path, 2)) & unseen
        if common_pairs:
            yield path
            unseen.difference_update(common_pairs)


def get_all_pairs_result(parameters, is_pairs=True):
    lst = []
    n_lst = []
    if is_pairs:
        result_list = list(pairwise_generator(*parameters))
        print(len(result_list))
    else:
        result_list = list(product(*parameters))
        print(len(result_list))
    for tpl in result_list:
        result_ = ''
        for i in tpl:
            if result_ == '':
                result_ = result_ + i
            else:
                result_ = '{},{}'.format(result_, i)
        lst.append(result_)
    print(lst)
    for i in lst:
        str = '{}{}{}'.format('{"request": {', i, '}},"response": {"id": "loginUser","error": {},"result": {}}}')
        n_lst.append(str)
    s = ',\n'.join(n_lst)
    # print('['+ s + ']')
    print('[' + s + ']')
    return lst


if __name__ == '__main__':
    result = get_all_pairs_result(params_methodHeaders)
