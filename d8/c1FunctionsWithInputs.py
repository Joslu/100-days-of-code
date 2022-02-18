
### NORMAL FUNCTION ####

def greet():
    for i in range(0,3):
        print("Hello!")

greet()

### FUNCTION WITH ONE INPUT### 
def greet_with_name(name_to):
    print(f'Hello {name_to}')


greet_with_name('Luis')

### FUNCTION WITH MORE INPUTS ### 
def greet_with_name_place(name,place):
    print(f'Hello {name}')
    print(f'How is the weather in {place}??')


greet_with_name_place('Luis', 'Mexico')


### FUNCTION WITH KEYWORD ARGUMENTS ### 

greet_with_name_place(name = 'Dani', place = 'Tlaxcala')