import sys

def run_gui():
    from PyQt5.QtWidgets import QApplication
    from ui import PegasusTerminal

    app = QApplication(sys.argv)
    window = PegasusTerminal()
    window.show()
    sys.exit(app.exec_())


def run_cli():
    from cli import main as cli_main
    cli_main()


if __name__ == "__main__":
    # No arguments → GUI (default)
    if len(sys.argv) == 1:
        run_gui()

    # Explicit mode selection
    elif sys.argv[1].lower() == "gui":
        run_gui()

    elif sys.argv[1].lower() == "cli":
        # Remove 'cli' so argparse sees correct args
        sys.argv.pop(1)
        run_cli()

    else:
        print("Usage:")
        print("  python main.py              # GUI mode")
        print("  python main.py gui          # GUI mode")
        print("  python main.py cli <args>   # CLI mode")
