def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}")


greet_with("Tolu", "Nigeria")
#'Tolu' and 'Nigeria' here are positional arguments, the position of the argu,ennts passed into the function matters when calling it.abs


greet_with(location= 'Nigeria', name='Tolu')
#Here, Nigera and TOlu are keyword arguments becasue of the manner in wich they are opassed into the function.