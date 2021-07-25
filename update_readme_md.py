#!/usr/bin/env python3
import divisiblelist as module

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(module.__name__ + "\n---\n")
        f.write(module.__doc__)
