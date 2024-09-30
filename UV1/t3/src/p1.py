# This is explicitly for making the banner
from rich.console import Console
from rich.panel import Panel
import requests as rq

console = Console()


def banner(txt):
    panel = Panel.fit(
        txt,
        title="Mistress",
        subtitle="ToiletSlave",
        style="Italic",
        border_style="magenta",
    )
    # Print the Panel
    console.print(panel)


def banner2(txt):
    panel = Panel.fit(
        txt,
        style="Italic",
        border_style="magenta",
    )
    # Print the Panel
    console.print(panel)


def pantyBanner():
    rez1 = rq.get("https://snips.sh/f/ahGYgGrGUK?r=1")
    print(rez1.text)
