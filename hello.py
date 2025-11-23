
import typer

def main(
    username: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formalOption: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Здрасьте" пользователю, опционально используя фамилию и формальный стиль.
    """

    # Использование флага formal
    if formalOption:
        print(f"Добрый день, {username} {lastname}!")
    else:
        print(f"Привет, {username}!")

# Основная функция
if __name__ == "__main__":
    typer.run(main)
