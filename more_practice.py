def secret_formula(start):
    jelly_beans = start*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print(f"we have {beans} beans, {jars} jars and {crates} crates.")

# we can do it this way too

start_point = start_point / 10
formula = secret_formula(start_point)
print("we have {} beans, {} jars and {} crates.".format(*formula)) # unpacking
