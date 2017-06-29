def tickets(people):
    print people
    bill_count = {}

    if people[0] > 25:
        return "NO"
    
    for item in people:
        print bill_count
        if item == 25:
            bill_count[item] = bill_count.get(item, 0) + 1
        
        else:
            if item == 50:
                if 25 in bill_count and bill_count[25] > 0:
                    bill_count[25] -= 1
                    bill_count[item] = bill_count.get(item, 0) + 1
                else:
                    return "NO"
            elif item == 100:
                if 50 in bill_count and bill_count[50] > 0 and 25 in bill_count and bill_count[25] > 0:
                    bill_count[50] -= 1
                    bill_count[25] -= 1
                    
                elif 25 in bill_count and bill_count[25] >= 3:
                
                    bill_count[25] -= 3
                  
                else:
                    return "NO"
        

    return "YES"


tickets([25, 50, 50])