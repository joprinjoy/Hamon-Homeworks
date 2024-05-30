print("Let's Practice everything")
print('You\'d need to know \'bout ascapes with \\ that do')
print('\n newlines and \t new tabs')
poem = """
\t The lovely world
with logic so firmly planted
cannot discreen \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("------------------")

five = 10 - 2 + 3 - 6

print(f"This should be five {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creates = jars / 100
    return jelly_beans, jars, creates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("with a starting point of :{}".format(start_point))
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)

print("we'd have {} beans,{} jars, {} creates".format(*formula))