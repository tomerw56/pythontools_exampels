import traceback,sys

from returns.result import Result, safe
from returns.pipeline import flow
from returns.pointfree import bind


def bad_fetch_user_profile(user_id: int) -> int:
    if user_id==5:
        raise Exception("not supported user_id")
    return user_id*bad_get_mult(user_id=user_id)
def bad_get_mult(user_id: int) -> int:
    if user_id == 4:
        raise Exception("not supported mult")
    return 10

def good_fetch_user_profile(user_id: int) -> Result['results', Exception]:
    """Fetches `UserProfile` TypedDict from foreign API."""
    return flow(
        user_id,
        _make_calculation,bind(good_get_mult)
    )
@safe
def _make_calculation(user_id: int) -> int:
    if user_id==5:
        raise Exception("not supported user_id")

    return user_id

@safe
def good_get_mult(user_id: int) -> 'results':
    if user_id == 4:
        raise Exception("not supported mult")
    return user_id*10


if __name__ == '__main__':

    print("no error")
    print(bad_fetch_user_profile(user_id=15))
    try:
        print("with error on bad_fetch_user_profile")
        bad_fetch_user_profile(user_id=5)
    except:
        traceback.print_exc(file=sys.stderr)
    try:
        print("with error on bad_get_mult")
        bad_fetch_user_profile(user_id=4)
    except:
        traceback.print_exc(file=sys.stderr)

    item=good_fetch_user_profile(user_id=15)
    print(item)


    item=good_fetch_user_profile(user_id=5)
    print(item)


    item=good_fetch_user_profile(user_id=4)
    print(item)


