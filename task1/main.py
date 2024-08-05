import pulp

# Створення моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
y = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Обмеження ресурсів
water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40

# Споживання ресурсів
water_per_lemonade = 2
sugar_per_lemonade = 1
lemon_juice_per_lemonade = 1
water_per_fruitjuice = 1
fruit_puree_per_fruitjuice = 2

# Функція цілі: максимізація загальної кількості вироблених продуктів
model += x + y, "Total_Production"

# Обмеження на використання ресурсів
model += water_per_lemonade * x + water_per_fruitjuice * y <= water, "Water_Constraint"
model += sugar_per_lemonade * x <= sugar, "Sugar_Constraint"
model += lemon_juice_per_lemonade * x <= lemon_juice, "Lemon_Juice_Constraint"
model += fruit_puree_per_fruitjuice * y <= fruit_puree, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade Production: {x.varValue} units")
print(f"Fruit Juice Production: {y.varValue} units")
print(f"Total Production: {pulp.value(model.objective)} units")
