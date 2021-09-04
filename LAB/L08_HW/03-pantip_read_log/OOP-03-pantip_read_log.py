class FakeDataFrame(object):
    """
    Gay
    """

    def __init__(self, __file_name: str or None = None,  __key: str = 'uid') -> None:
        if isinstance(__file_name, str):

            self.read_csv(__file_name, __key)

    def __to_dict__(self, __file_text: str, __key):

        if isinstance(__file_text, str):

            self.columns = __file_text.splitlines()[0].split(',')
            self.__key_index__ = self.columns.index(self.key)

            _rows = []
            _keys = []
            for _row in __file_text.splitlines()[1:]:

                _row_ap = []

                _row_split = _row.split(',')

                _keys.append(_row_split[self.__key_index__])

                _row_iter = _row_split[:self.__key_index__] + \
                    _row_split[self.__key_index__+1:]

                for _val in _row_iter:

                    try:
                        _val = int(_val)
                    except ValueError:
                        try:
                            _val = float(_val)
                        except:
                            pass

                    _row_ap.append(_val)

                _rows.append(_row_ap)

            return {_key: dict(zip(self.columns, _row)) for _key, _row in zip(_keys, _rows)}

        else:
            raise TypeError

    def __to_list__(self, __agg=None):
        if __agg is None:
            return {self.columns[i]: [list(row.values())[i] for row in self.data.values()] for i in range(self.length('columns')-1)}
        else:
            return {self.columns[i]: __agg([list(row.values())[i] for row in self.data.values()]) for i in range(self.length('columns')-1)}

    def read_csv(self, __file_name: str, __key: str) -> dict:

        with open(__file_name) as file:
            self.key = __key
            self.data = self.__to_dict__(file.read(), __key)

        return self.data

    def length(self, output_type: str = 'all'):
        if output_type == 'all':
            return len(self.data) + 1

        elif output_type == 'records':
            return len(self.data)

        elif output_type == 'columns':
            return len(self.columns)

    def aggregate(self, agg_function, axis: int = 0):

        if axis == 0:
            return {key: agg_function(val.values()) for key, val in self.data.items()}
        elif axis == 1:
            return self.__to_list__(agg_function)

    def sort(self, by: str, reverse: bool = False, return_as_dict: bool = True):

        _rtn = sorted(self.data.items(),
                      key=lambda x: x[1][by], reverse=reverse)

        if return_as_dict:
            return dict(_rtn)
        else:
            return _rtn

    def get(self, param, key):

        return param(self.data.items(), key=key)

    def agg_map(self, on, agg, map_function):

        if on == 'items':
            __iter = self.data.items()
        elif on == 'values':
            __iter = self.data.values()
        elif on == 'keys':
            __iter = self.data.keys()

        return agg(map(map_function, __iter))


def list_str(lst: list, end: str = " "):
    return end.join([str(i) for i in lst])


fdf = FakeDataFrame(input('File name: '))

choice = int(input('enter number: '))-1

print([fdf.length(),

       max(fdf.aggregate(sum, 1).items(), key=lambda x: x[1])[0],

       list_str(list(fdf.aggregate(sum).values())[:3]),

       list_str(list(fdf.aggregate(sum).items())[0]),

       list_str((lambda d: (d[0], d[1]['tvshow']))(
           fdf.get(max, lambda x: x[1]['tvshow']))),

       fdf.agg_map('values', sum, lambda x: x['korea'] > 500),

       fdf.agg_map('values', sum, lambda x: x['siam'] > x['food']),

       fdf.get(max, lambda x: x[1]['rajdumnern']/sum(x[1].values()))[0],

       fdf.agg_map('items', sum, lambda x: sum([e[1] for e in sorted(
           x[1].items(), key=lambda i: i[1], reverse=True)[:2]])/sum(x[1].values()) > 0.7),

       fdf.agg_map('items', sum, lambda x: x[1]['pantip'] == 0)][choice])
