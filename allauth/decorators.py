from functools import wraps
from allauth.core import ratelimit

def rate_limit(*, action, **rl_kwargs):
    """
    Decorator to apply rate limiting to a function.

    :param action: The action to be evaluated for rate limiting.
    :param rl_kwargs: Additional arguments for the rate limiting function.
    """
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            rate_limit_response = ratelimit.consume_or_429(request, action=action, **rl_kwargs)
            if rate_limit_response:
                # Rate limit exceeded, return the HTTP response
                return rate_limit_response
            # Rate limit not exceeded, execute the function
            return function(request, *args, **kwargs)

        return wrap

    return decorator
