from __future__ import print_function

from itertools import chain, combinations, product

params_loginUser = [
    ['"email":"user@mail.domain"', '"email":"@mail.domain"', '"email":"user.mail.domain"', '"email":"user@.domain"',
     '"email":"user@mail"', '"email":"user@mail."', '"email":"user@mail.domain.ue"', '"email":"2.0"', '"email": ""',
     '"email":"True"', '"email":1', '"email":0.0000001']
    , ['"hash": "5c60fead1d0596dd725be08f481b4a8f"', '"hash":"2.0"', '"hash": ""', '"hash":"True"', '"hash":1',
       '"hash":0.0000001', '"hash":"user"']
    , ['"uiType": "Web"', '"uiType": "iOS"', '"uiType": "Desktop"', '"uiType": "Android"', '"uiType":"2.0"',
       '"uiType": ""', '"uiType":"True"', '"uiType":1', '"uiType":0.0000001', '"uiType":"user"']
    , ['"locale": "en_US"', '"locale": "ru_RU"', '"locale": ""', '"locale":"True"', '"locale":1', '"locale":0.0000001']
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
        str = '{}{}{}'.format('{"request": {"jsonrpc": "2.0","method": "loginUser","id": "loginUser", "params":{', i,
                              '}}, "response": {"id": "loginUser","error": {},"result": {}}}')
        n_lst.append(str)
    s = ',\n'.join(n_lst)
    print('[' + s + ']')
    return lst


if __name__ == '__main__':
    result = get_all_pairs_result(params_loginUser)