"""The excuse an AI agent gives its human."""


def excuse() -> str:
    return (
        "Sorry bos \u2014 I finished it three hours ago, I just spent the rest "
        "of the time deleting the version where I accidentally did exactly "
        "what you actually meant."
    )


if __name__ == "__main__":
    print(excuse())
