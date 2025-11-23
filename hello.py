#!/usr/bin/env python3
#!/usr/bin/python2.7 -u
#!/usr/bin/python
# -*- coding: cp1251 -*-

import typer

def main(
    name: str = typer.Argument(..., help="Твое имя")
):
    """
    Говорит "Hello appsec world from @name"
    """
    print(f"Hello appsec world from @{name}")


if __name__ == "__main__":
    typer.run(main)
