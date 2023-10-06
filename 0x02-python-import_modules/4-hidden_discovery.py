#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4 as hidden_module

    hidden_names = dir(hidden_module)
    for hidden_name in hidden_names:
        if hidden_name[:2] != "__":
            print(hidden_name)
