import streamlit as st
import pandas as pd

st.title("🌮Taco-kalkulator")

st.write("Beregn hvor mye du trenger til fredagstacoen basert på antall personer.")

# Velg antall personer
antall_personer = st.slider("Velg antall personer", 1, 20, 4)

# Enkle beregninger per person (du kan justere tallene som du vil)
ingredienser = {
    "Kjøttdeig (g)": 180,
    "Tacolefser (stk)": 2,
    "Revet ost (g)": 100,
    "Salat (g)": 30,
    "Tomat (g)": 30,
    "Agurk (g)": 20,
    "Mais (g)": 20,
    "Rømme (ss)": 2,
    "Salsa (ss)": 2,
    "Guacamole (ss)": 2,
}

# Kalkuler totaler
beregnet = {ing: mengde * antall_personer for ing, mengde in ingredienser.items()}

# Vis resultatet i tabell
df = pd.DataFrame.from_dict(beregnet, orient="index", columns=["Mengde totalt"])
st.subheader("Handleliste")
st.write(df)
