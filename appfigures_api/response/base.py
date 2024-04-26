from abc import ABCMeta


class AppFiguresGroupBy(list, metaclass=ABCMeta):
    def __init__(self, json, group_by):
        self._json = json
        self._group_by = group_by
        self._dict_list = []
        self._obj_list = list

        if self._json:
            self._retrieve_dicts(self._json, len(group_by))
            self.extend(list(map(self._transform, self._dict_list)))

    def _retrieve_dicts(self, json, target_level, current_level=1):
        for k, v in json.items():
            if current_level == target_level:
                self._dict_list.append(v)
            elif current_level > target_level:
                return None
            else:
                next_level = current_level + 1
                print('next_level = {}'.format(next_level))
                print('v = {}'.format(v))
                self._retrieve_dicts(v, target_level, next_level)

    def _transform(self, data):
        pass

    @classmethod
    def from_json(cls, json, group_by):
        return cls(json, group_by)


class AppFiguresObject(metaclass=ABCMeta):
    def __init__(self, json, group_by_attr=None):
        self._json = json

        if group_by_attr:
            self.attr = group_by_attr

        if self._json:
            self._load(self._json)

    def _load(self, json):
        pass

    @classmethod
    def from_json(cls, json, group_by_attr=None):
        return cls(json, group_by_attr)