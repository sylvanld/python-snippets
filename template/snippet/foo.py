def get_foo(*, should_fail: bool):
    if should_fail:
        raise ValueError
    return "foo"
