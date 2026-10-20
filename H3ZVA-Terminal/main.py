

import platform
from datetime import datetime

import psutil
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

PURPLE = "bright_magenta"
GREEN = "bright_green"
VERSION = "2.1"


def show_banner():
    banner = Text()
    banner.append("H3ZVA\n", style=f"bold {PURPLE}")
    banner.append("N E R V   S Y S T E M S", style=f"bold {GREEN}")

    console.print(
        Panel(
            banner,
            subtitle=f"[{PURPLE}]TERMINAL v{VERSION}[/]",
            border_style=PURPLE,
            box=box.DOUBLE,
            padding=(1, 4),
        )
    )


def show_status():
    table = Table(
        title="SYSTEM STATUS",
        box=box.ROUNDED,
        border_style=GREEN,
    )
    table.add_column("COMPONENT", style=PURPLE)
    table.add_column("STATUS", style=GREEN)

    table.add_row("Operating System", platform.system())
    table.add_row("Version", VERSION)
    table.add_row("Time", datetime.now().strftime("%H:%M:%S"))
    table.add_row("NERV Network", "ONLINE")

    console.print(table)


def show_help():
    table = Table(
        title="AVAILABLE COMMANDS",
        box=box.ROUNDED,
        border_style=PURPLE,
    )
    table.add_column("COMMAND", style=GREEN)
    table.add_column("DESCRIPTION", style="white")

    table.add_row("help", "Mostrar comandos")
    table.add_row("about", "Información de H3ZVA")
    table.add_row("time", "Consultar fecha y hora")
    table.add_row("pc", "Información del sistema")
    table.add_row("monitor", "Monitor de CPU, RAM y disco")
    table.add_row("clear", "Limpiar pantalla")
    table.add_row("exit", "Cerrar terminal")

    console.print(table)
disk = psutil.disk_usage("C:\\")

def show_pc():
    table = Table(
        title="SYSTEM INFORMATION",
        box=box.ROUNDED,
        border_style=GREEN,
    )
    table.add_column("DATO", style=PURPLE)
    table.add_column("VALOR", style=GREEN)

    table.add_row("Sistema", f"{platform.system()} {platform.release()}")
    table.add_row("Arquitectura", platform.machine())
    table.add_row("Procesador", platform.processor() or "No disponible")

    console.print(table)


def show_monitor():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()

    try:
        disk = psutil.disk_usage("C:\\")
    except OSError:
        console.print("[bold red]No se pudo consultar el disco C:.[/]")
        return

    table = Table(
        title="H3ZVA // SYSTEM MONITOR",
        box=box.DOUBLE,
        border_style=PURPLE,
    )
    table.add_column("COMPONENT", style=PURPLE)
    table.add_column("USAGE", style=GREEN)
    table.add_column("DETAILS", style="white")

    table.add_row("CPU", f"{cpu}%", "Uso del procesador")
    table.add_row(
        "RAM",
        f"{ram.percent}%",
        f"{ram.used / (1024**3):.1f} / "
        f"{ram.total / (1024**3):.1f} GB",
    )
    table.add_row(
        "DISCO C:",
        f"{disk.percent}%",
        f"{disk.used / (1024**3):.1f} / "
        f"{disk.total / (1024**3):.1f} GB",
    )

    console.print(table)


def main():
    console.clear()
    show_banner()
    show_status()

    console.print(
        f"\nEscribe [{GREEN}]help[/] para ver los comandos."
    )

    while True:
        try:
            command = console.input(
                f"\n[{PURPLE}]H3ZVA[/] [{GREEN}]> [/]"
            ).strip().lower()

            if command == "help":
                show_help()

            elif command == "about":
                console.print(
                    Panel(
                        "Laboratorio digital personal desarrollado en Python.",
                        title=f"[{PURPLE}]ABOUT H3ZVA[/]",
                        border_style=PURPLE,
                    )
                )

            elif command == "time":
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                console.print(f"[{GREEN}]Fecha y hora: {now}[/]")

            elif command == "pc":
                show_pc()

            elif command == "monitor":
                show_monitor()

            elif command == "clear":
                console.clear()
                show_banner()
                show_status()

            elif command == "exit":
                console.print(f"[{GREEN}]NERV SYSTEMS OFFLINE.[/]")
                break

            elif command == "":
                continue

            else:
                console.print(
                    "[bold red]ERROR:[/] Comando desconocido. "
                    f"Escribe [{GREEN}]help[/]."
                )

        except (KeyboardInterrupt, EOFError):
            console.print(f"\n[{GREEN}]Sesión finalizada.[/]")
            break


if __name__ == "__main__":
    main()
S