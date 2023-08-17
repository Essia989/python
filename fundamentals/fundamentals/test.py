
#15
def foo():
    print(f"#13 :",1) # 1
    x = bar() # 3 
    print(f"#13 :",x) # 5
    return 10
def bar():
    print(f"#13 :",3) # 3
    return 5
y = foo() # 1/3/5
print(f"#13 :",y) # 10