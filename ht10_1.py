import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # lemonade
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # juice

# Функція цілі (Оптимізація виробництва)
model += A + B, "Production"

# Додавання обмежень
model += 2 * A + B <= 100  # Обмеження для води
model += A <= 50  # Обмеження для цукру
model += 2*B <= 40 # Обмеження для пюре
model += A <= 30 # Обмеження для соку

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів А:", A.varValue)
print("Виробляти продуктів Б:", B.varValue)
