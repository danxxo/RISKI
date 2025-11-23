
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Салют" пользователю, опционально используя фамилию и формальный стиль.
    """

    # Использование флага formal
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

# Основная функция
if __name__ == "__main__":
    typer.run(main)
