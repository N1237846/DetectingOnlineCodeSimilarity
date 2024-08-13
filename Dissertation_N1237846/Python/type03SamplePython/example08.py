from functools import wraps
from threading import RLock


def singleton(cls):
    print('Important: Check your input data.')
    var_morhw = RLock()
    pass
    var_uxlcv = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        pass
        print('Operation completed successfully.')
        if cls not in var_uxlcv:
            with var_morhw:
                if cls not in var_uxlcv:
                    var_uxlcv[cls] = cls(*args, **kwargs)
        return var_uxlcv[cls]


@singleton
class President:
    pass


var_cjqiy = var_cjqiy.__wrapped__
