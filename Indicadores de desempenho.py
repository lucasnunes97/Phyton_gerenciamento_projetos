import pandas as pd
import matplotlib.pyplot as plt

# Simulando dados semanais do projeto
dados = {
    'Semana': [1, 2, 3, 4, 5],
    'PV':     [1000, 3000, 6000, 8000, 10000],  # Planejado
    'EV':     [1000, 2500, 5000, 7500, 8500],   # Executado
    'AC':     [900,  2900, 6500, 8500, 11000],  # Custo real
}

df = pd.DataFrame(dados)

# Calculando SPI e CPI
df['SPI'] = df['EV'] / df['PV']
df['CPI'] = df['EV'] / df['AC']

print(df)

# Plotando a Curva S
plt.figure(figsize=(10,6))
plt.plot(df['Semana'], df['PV'], marker='o', label='Valor Planejado (PV)')
plt.plot(df['Semana'], df['EV'], marker='o', label='Valor Agregado (EV)')
plt.plot(df['Semana'], df['AC'], marker='o', label='Custo Real (AC)')

plt.title('Curva S - Gestão do Valor Agregado')
plt.xlabel('Semana')
plt.ylabel('R$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
