import streamlit as st
from rich.console import Console
from rich.panel import Panel
from rich.box import Box, HORIZONTALS

st.set_page_config(page_title="Johannes", page_icon="🤖")
st.info("☝️ &nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce at rhoncus augue. Class aptent &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In diam dolor, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;blandit in enim pretium, volutpat hendrerit nisl. ")

console = Console(force_terminal=True)

# try:
#     a = {}
#     a["key"]
# except KeyError as e:
#     console.print_exception()
#     #console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

console.print(
    """
    
[#f9ca2a][09:26:03][/#f9ca2a] 🚥 Connecting...
[gold1][09:26:04][/gold1] 🚀 Starting up...
              - owner:        [cyan]streamlit[/cyan]
              - repository:   [cyan]app-frontpage[/cyan]
              - branch:       [cyan]main[/cyan]
              - main module:  [cyan]streamlit_app.py[/cyan]
[gold1][09:26:09][/gold1] 🐙 Cloning repository...
[gold1][09:26:10][/gold1]    Cloning into [white]'app-frontpage'[/white]...
[gold1][09:26:55][/gold1]    Cloned repository!                    
[gold1][09:27:00][/gold1] 📦 Processing dependencies...
              - tool:  [cyan]pipenv[/cyan]
              - file:  [cyan]/app/app-frontpage/Pipfile[/cyan]
    """
)

CUSTOM_HORIZONTALS = Box(
    """\
────
​​​​
────
​​​​
────
────
​​​​
────
"""
)

console.print(Panel("""Installing dependencies from Pipfile.lock (49795d)...
Ignoring appnope: markers 'sys_platform == "darwin" and platform_system == "Darwin"' don't match your environment
Collecting backports.zoneinfo==0.2.1
  Downloading backports.zoneinfo-0.2.1-cp38-cp38-manylinux1_x86_64.whl (74 kB)
Installing collected packages: backports.zoneinfo
WARNING: Ignoring invalid distribution -itpython (/home/appuser/venv/lib/python3.8/site-packages)
WARNING: Ignoring invalid distribution -harset-normalizer (/home/appuser/venv/lib/python3.8/site-packages)
WARNING: Ignoring invalid distribution -ebugpy (/home/appuser/venv/lib/python3.8/site-packages)
Successfully installed backports.zoneinfo-0.2.1
Collecting cachetools==4.2.4
  Downloading cachetools-4.2.4-py3-none-any.whl (10 kB)
Installing collected packages: cachetools
  Attempting uninstall: cachetools
    Found existing installation: cachetools 4.2.2
    Uninstalling cachetools-4.2.2:
      Successfully uninstalled cachetools-4.2.2""", title="pipenv", border_style="green"))


st.title("Title")
st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce at rhoncus augue. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In diam dolor, blandit in enim pretium, volutpat hendrerit nisl. Etiam nec elementum sapien. Sed in augue nec urna euismod lacinia eget quis nunc. Aenean efficitur tellus eget euismod auctor. Aenean vulputate molestie magna in iaculis. Etiam pulvinar, enim id laoreet aliquet, mauris turpis tristique nulla, sed posuere augue ante quis leo. Sed ut placerat neque. Phasellus ac gravida nulla. Nam quis mattis nisl, in posuere elit. Integer faucibus egestas tellus nec dictum.

Phasellus placerat blandit interdum. Vestibulum eleifend nec libero eu consectetur. Etiam eget scelerisque ex. Donec vehicula sapien maximus magna hendrerit, malesuada tempor diam tincidunt. Proin libero neque, sollicitudin sit amet pharetra nec, aliquet eu risus. Donec tincidunt interdum mollis. Morbi facilisis orci non lectus hendrerit gravida.""")

import altair as alt
import pandas as pd

source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

chart = alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)
st.altair_chart(chart)