"""Examples of a class and objects."""


class Profile:
    handle: str
    followers: int
    is_private: bool

    def __init__(self, handle: str):
        """constructor initializes attributes"""
        self.handle = handle
        self.followers = 0
        self.is_private = False
    
    def tweet(self, message: str) -> None:
        print(f"@{self.handle} tweets {message}")


my_profile: Profile = Profile("mchaudh")
my_profile.tweet