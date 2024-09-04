class Pokemon:
    def __init__(self, name: str, type: list[str], is_caught: bool = False) -> None:
        self.name = name
        self.type1 = type[0]
        self.type2 = type[1] if len(type) > 1 else None
        self.nickname = None

    def __str__(self):
        return f"{self.nickname if self.nickname else self.name} ({self.type1}{'/' + self.type2 if self.type2 else ''})"
