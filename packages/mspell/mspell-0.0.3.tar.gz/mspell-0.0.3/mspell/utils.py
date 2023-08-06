from functools import partial, wraps
import math
from typing import Callable, Sequence, Union

import numpy as np

try:
    import torch

    HAS_TORCH = True
except ModuleNotFoundError:
    HAS_TORCH = False


def get_accidental(n, flat_sign="b"):
    if n >= 0:
        return n * "#"
    else:
        return -n * flat_sign


def nested(coerce_to_list: bool = False) -> Callable:
    """Decorator to extend a function to arbitrarily deep/nested list-likes.

    If the argument to the decorated function is a non-string sequence
    or a numpy array, the
    function will be recalled recursively on every item of the sequence.
    Otherwise, `func` will be called on the argument.
    """

    def _decorator(func: Callable) -> Callable:
        def f(item, *args, **kwargs):
            if isinstance(item, Sequence) and not isinstance(item, str):
                if coerce_to_list:
                    return list(
                        f(sub_item, *args, **kwargs) for sub_item in item
                    )
                return type(item)(
                    f(sub_item, *args, **kwargs) for sub_item in item
                )
            elif isinstance(item, np.ndarray):
                if coerce_to_list:
                    return list(
                        f(sub_item, *args, **kwargs) for sub_item in item
                    )
                return np.fromiter(
                    (f(sub_item, *args, **kwargs) for sub_item in item),
                    dtype=item.dtype,
                )
            elif HAS_TORCH and isinstance(item, torch.Tensor):
                if not item.dim():
                    return func(item.item(), *args, **kwargs)
                if coerce_to_list:
                    return list(
                        f(sub_item, *args, **kwargs) for sub_item in item
                    )
                # e.g., "float32" if item.dtype is "torch.float32"
                base_dtype = item.dtype.__repr__().split(".")[1]
                return type(item)(
                    np.fromiter(
                        (f(sub_item, *args, **kwargs) for sub_item in item),
                        dtype=getattr(np, base_dtype),
                    )
                )
            else:
                return func(item, *args, **kwargs)

        return f

    return _decorator


def nested_method(coerce_to_list: bool = False) -> Callable:
    """Decorator to extend method arbitrarily deep/nested list-likes.

    Same as `nested` decorator, but passes "self" as first argument.
    """

    def _decorator(method: Callable) -> Callable:
        def f(self, item, *args, **kwargs):
            if isinstance(item, Sequence) and not isinstance(item, str):
                if coerce_to_list:
                    return list(
                        f(self, sub_item, *args, **kwargs) for sub_item in item
                    )
                return type(item)(
                    f(self, sub_item, *args, **kwargs) for sub_item in item
                )
            elif isinstance(item, np.ndarray):
                if coerce_to_list:
                    return list(
                        f(self, sub_item, *args, **kwargs) for sub_item in item
                    )
                return np.fromiter(
                    (f(self, sub_item, *args, **kwargs) for sub_item in item),
                    dtype=item.dtype,
                )
            elif HAS_TORCH and isinstance(item, torch.Tensor):
                if not item.dim():
                    return method(self, item.item(), *args, **kwargs)
                if coerce_to_list:
                    return list(
                        f(self, sub_item, *args, **kwargs) for sub_item in item
                    )
                # e.g., "float32" if item.dtype is "torch.float32"
                base_dtype = item.dtype.__repr__().split(".")[1]
                return type(item)(
                    np.fromiter(
                        (
                            f(self, sub_item, *args, **kwargs)
                            for sub_item in item
                        ),
                        dtype=getattr(np, base_dtype),
                    )
                )
            else:
                return method(self, item, *args, **kwargs)

        return f

    return _decorator


@nested()
def approximate_just_interval(
    rational: Union[Sequence, float], tet: int
) -> int:
    """Approximates given rational(s) in given equal temperament.

    Can approximate intervals, pitches, or pitch-classes.
        - Ascending intervals are > 1; descending intervals are in (0, 1).
        - When approximating pitches, C4 is 2**5. (Mnemonic: C4 is also
            12 * 5 = 60.)
        - When approximating pitch-classes, rational should be in [1, 2).

    Args:
        rational: float, Fraction, or arbitrarily deep/nested list-like.
        tet: integer.

    Returns:
        integer or list-like of integers.

    Raises:
        TypeError if rational <= 0
    """
    if rational <= 0:
        raise TypeError(f"`rational` = {rational}; must be > 0")
    return round(math.log2(rational) * tet)
