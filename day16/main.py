from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charizard", "Electivire"], "c")
table.add_column("Type", ["Electric", "Water", "Fire | Flying", "Electric"], "c")

table.add_row(["Bulbasaur", "Grass | Poison"])

table.align = "l"

print(table)
