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
[09:26:03] 🚥 Connecting...
[09:26:04] 🚀 Starting up...
              - owner:        streamlit
              - repository:   app-frontpage
              - branch:       main
              - main module:  streamlit_app.py
[09:26:09] 🐙 Cloning repository...
[09:26:10]    Cloning into 'app-frontpage'...
[09:26:55]    Cloned repository!                    
[09:27:00] 📦 Processing dependencies...
              - tool:  pipenv
              - file:  /app/app-frontpage/Pipfile
    """
)
st.write("Hello")