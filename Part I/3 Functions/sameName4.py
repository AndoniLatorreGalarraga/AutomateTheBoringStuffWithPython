def spam():
    print(eggs) # ERROR!
    eggs = 'local spam'

eggs = 'global'
spam()
