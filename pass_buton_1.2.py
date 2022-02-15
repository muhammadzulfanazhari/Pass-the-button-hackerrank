def pass_buton(friends, times):
    # final result
    result = [0, 0]

    # counter for times
    i = 1
    
    # set direction, 0 is forward, 1 is backward
    backward_sign = 0

    # buton position
    index_friends = 1
    
    # counting times
    while i <= times:
        # check forward sign and index_friends position
        if backward_sign == 0 and index_friends < friends:
            result[0] = index_friends
            index_friends += 1
            result[1] = index_friends  
            if index_friends == friends:
                backward_sign = 1

        # check backward sign and index_friends position
        elif backward_sign == 1 and index_friends >= 1:
            result[0] =  index_friends
            index_friends -= 1
            result[1] = index_friends 
            if index_friends == 1:
                backward_sign = 0

        print(f'Time {i}: {result}')
        i+=1
        
    return result

print(pass_buton(5, 18))