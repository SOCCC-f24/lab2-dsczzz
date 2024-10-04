import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    TODO: What is the objective? 
    To encrypt the email by shifting characters.
    Args:
        TODO: what arguments and data types are expected? (i.e., email)
    In order for the email to be encrypted it will be 6 characters long(3 letter + 3 digits).
    Returns:
        TODO: what varibale and data types are being returned?   
    An error or encrypted email.
    """
    output = "" 
    len_flag = len(email) != 6
    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output = "Email must be 6 characters long."
        logging.info(output)
        return output        
   
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output = "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email_lst = ["a", "b", "c", "0", "1", "2"]
    email_lst = list(email)
    for i in range(len(email_lst)):  # Loop through each character
        new_ascii = ord(email_lst[i]) + 3    # NOTE: here we extract and update element at 0 
        email_lst[i] = chr(new_ascii)        # NOTE: here we convert our ASCII into string
        
    # TODO: fix line below, convert list into a string
        email_str = "dbc012"
        email_str = "".join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str.strip()
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 
    To decrypt the email by shifting characters back
    Args:
        TODO: what arguments and data types are expected? (i.e., email)
    The email string will decrypt,will still be 6 characters(3 letters + 3 digits)
    Returns:
        TODO: what varibale and data types are being returned?   
    An error message or decrypted email string.
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
     
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO: apply the encrypt pseudocode but shift down 3
    email_lst = list(email) #converting email string into list
    for i in range(len(email_lst)):  # Loop through each character
        new_ascii = ord(email_lst[i]) - 3 #shifting letter 3 back
        email_lst[i] = chr(new_ascii)
        email_str = "".join(email_lst) #coverting our list back into a string
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = "aef345".strip
    return retVal
