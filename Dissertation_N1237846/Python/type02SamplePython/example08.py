from functools import wraps
from threading import RLock


def cloned_singleton(cloned_cls):
    cloned_instances = {}
    cloned_lock = RLock()

    @wraps(cloned_cls)
    def cloned_wrapper(*cloned_args, **cloned_kwargs):
        if cloned_cls not in cloned_instances:
            with cloned_lock:
                if cloned_cls not in cloned_instances:
                    cloned_instances[cloned_cls] = cloned_cls(*cloned_args, **cloned_kwargs)
        return cloned_instances[cloned_cls]


@cloned_singleton
class cloned_President:
    pass


cloned_President = cloned_President.cloned___wrapped__