def format_text (name:str,prefix:str ="",suffix :str ="",capitalize = False,max_length =None):
   
   '''Formats the the  input text by adding a prefix, suffix and optionally
     applying CAPITALISATION  and returning actual length of arguments'''
   
   if not isinstance(name,str):
      raise ValueError("The input must be a string.")
   
   if not isinstance(prefix, str) or not isinstance(suffix, str):
      raise ValueError("Prefix and suffix must be strings.")
   
   if not isinstance(capitalize):
      raise TypeError("The 'capitalize' parameter must be a boolean.")
   
   if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' parameter must be an integer.")
        if max_length < 0:
            raise ValueError("max_length must be a non-negative integer.")



     # Applying formats
   formatted_text = (f"{prefix} {name} {suffix}")
    
    # Capitalization
   if capitalize :
      formatted_text = formatted_text.capitalize()

    # Truncation
   if max_length is not None:
     formatted_text = formatted_text[:max_length]

   return(formatted_text) 


