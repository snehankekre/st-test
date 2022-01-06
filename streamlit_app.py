import streamlit as st
from rich.console import Console

console = Console(force_terminal=True)

# try:
#     a = {}
#     a["key"]
# except KeyError as e:
#     console.print_exception()
#     #console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

console.print("[09:26:03] 🚥 Connecting...")
console.print("[yellow][09:26:03][/yellow] 🚥 Connecting...")
st.write("Hello")