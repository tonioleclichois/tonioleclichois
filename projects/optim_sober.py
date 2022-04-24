import gurobipy as gp

######  créer une fonction faisant varier les paramètres ;
# structurer les paramètres = il y a les limites (vecteur B) et les facteurs (matrice A)

# Create a new model
m = gp.Model()

# Create variables
x = m.addVar(vtype='C', name="x")  # écolo
y = m.addVar(vtype='C', name="y")  # mcdo
z = m.addVar(vtype='C', name="z")  # chic

# Set objective function
m.setObjective(10 * x + 5 * y + 15 * z, gp.GRB.MINIMIZE)

# Add constraints ; passer par des dico de paramètres cf cours ose ; pour construire une matrice Ax <= B
m.addConstr(3*x + y + 5 * z >= 4)  # plaisir gastronomique
m.addConstr(x + 5*y + 3*z <= 2)  # émission co2
m.addConstr(x + y + z >= 1)  # besoin nutritionnel

# Solve it!
m.optimize()

print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: x={x.X}, y={y.X}, z={z.X}")

print(f"\nImpact plaisir gastro : {3*x.X + y.X + 5*z.X}")
print(f"Impact co2 : {x.X + 5*y.X + 3*z.X}")
print(f"Impact besoin nutri : {x.X + y.X + z.X}")

# Dual problem
# duals = m.getAttr("Pi", m.getConstrs())
# print(duals)
