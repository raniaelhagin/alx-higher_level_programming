#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pr_items = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            pr_items += 1
        except:
            pass
    print("")
        
    return (pr_items)
