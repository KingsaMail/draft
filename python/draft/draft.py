def optimiz(text) -> (str):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
  

    basik = ''
    count = 0
    my_text = ''
    cr = 0
    for i in text:
        
        if (basik == '') and (count == 0):
            basik = i
            
            count = 1
            
        elif basik == i:
            count += 1
        elif basik != i:
            my_text = my_text + basik + str(count)
            basik = i
            count = 1
    my_text = my_text + basik + str(count)
    return my_text        
            
if __name__ == 'main':
    #run
    print(optimiz('aaabbccccdaa')) #a3b2c4d1a2