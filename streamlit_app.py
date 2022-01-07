import streamlit as st
from rich.console import Console

console = Console(force_terminal=True)

# try:
#     a = {}
#     a["key"]
# except KeyError as e:
#     console.print_exception()
#     #console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

console.print("[yellow][09:26:03][/yellow] 🚥 Connecting...")
console.print(
    """
    
[yellow][09:26:03][/yellow] 🚥 Connecting...
[09:26:04] 🚀 Starting up...
              - owner:        [cyan]streamlit[/cyan]
              - repository:   [cyan]app-frontpage[/cyan]
              - branch:       [cyan]main[/cyan]
              - main module:  [cyan]streamlit_app.py[/cyan]
[09:26:09] 🐙 Cloning repository...
[09:26:10]    Cloning into [white]'app-frontpage'[/white]...
[09:26:55]    Cloned repository!                    
[09:27:00] 📦 Processing dependencies...
              - tool:  [cyan]pipenv[/cyan]
              - file:  [cyan]/app/app-frontpage/Pipfile[/cyan]
    """
)
st.write("Hello")