values = [
    None,
    True,
    False,
    6,
    -8,
    "",
    "f",
    "oo",
    "\"'\\",
    [],
    [None, True, False, 6, -8, "", "f", "oo"],
    [
        None,
        True,
        False,
        6,
        -8,
        "",
        "f",
        "oo",
        [None, True, False, 6, -8, "", "f", "oo"],
    ],
    {},
    {
        "None": None,
        "True": True,
        "False": False,
        "": "",
        "f": "f",
        "oo": "oo",
        "array": [None, True, False, 6, -8, "", "f", "oo"],
    },
    {
        "None": None,
        "True": True,
        "False": False,
        "": "",
        "f": "f",
        "oo": "oo",
        "array": [None, True, False, 6, -8, "", "f", "oo"],
        "object": {
            "None": None,
            "True": True,
            "False": False,
            "": "",
            "f": "f",
            "oo": "oo",
            "array": [None, True, False, 6, -8, "", "f", "oo"],
        },
    },
]