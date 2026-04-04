try:
    import tiktoken
    from litellm import cost_per_token
except:
    # Non-essential feature
    pass


def count_tokens(text="", model="gpt-4"):
    """
    Count the number of tokens in a string
    """
    pass


def token_cost(tokens=0, model="gpt-4"):
    """
    Calculate the cost of the current number of tokens
    """
    pass


def count_messages_tokens(messages=[], model=None):
    """
    Count the number of tokens in a list of messages
    """
    pass
