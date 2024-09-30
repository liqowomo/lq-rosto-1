from rich.traceback import install
from src.utils.ban import banner
from src.app.p1 import func_p1

install(show_locals=True)


def main():
    banner("UV test")
    func_p1()


if __name__ == "__main__":
    main()
