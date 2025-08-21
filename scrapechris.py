from bs4 import BeautifulSoup
import pandas as pd

# Create a BeautifulSoup object from the HTML file
with open("chis.html") as file:
    soup = BeautifulSoup(file, "lxml")

    # Create df with all class="incident expandable"
    df = pd.DataFrame(columns=["date", "location", "officer", "subject", "force", "injury", "description"])