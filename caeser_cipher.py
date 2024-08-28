
def encrypt():
    original_text=input("enter the text you want to encrypt:")
    shift_amount=int(input("enter the number of positions to be shifted:"))
  

    # List of alphabets
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    
    # Convert the input text to lowercase to handle case insensitivity
    original_text = original_text.lower()
    
    # Resultant shifted string
    shifted_text = ''
    
    for char in original_text:
        if char in alphabets:
            # Find the index of the character in the alphabet list
            old_index = alphabets.index(char)
            # Calculate the new index after the left shift
            new_index = (old_index + shift_amount)% 26  # %26 used to tackle the case when the entered text is z since our list ends at z so no shift is possible after that
            # Append the shifted character to the result
            shifted_text += alphabets[new_index]
        else:
            # If the character is not in the alphabet list (e.g., space, punctuation), append it as is
            shifted_text += char
    
    print(f"Your encrypted text is: {shifted_text}")



def decrypt():
    encrypted_text=input("enter the text you want to decrypt:")
    shift_amount=int(input("enter the number of positions shifted:"))

    # List of alphabets
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    
    # Convert the input text to lowercase to handle case insensitivity
    encrypted_text = encrypted_text.lower()
    
    # Resultant shifted string
    shifted_text = ''
    
    for char in encrypted_text:
        if char in alphabets:
            # Find the index of the character in the alphabet list
            old_index = alphabets.index(char)
            # Calculate the new index after the left shift
            new_index = (old_index - shift_amount)% 26  # %26 used to tackle the case when the entered text is z since our list ends at z so no shift is possible after that
            # Append the shifted character to the result
            shifted_text += alphabets[new_index]
        else:
            # If the character is not in the alphabet list (e.g., space, punctuation), append it as is
            shifted_text += char
    
    print(f"Your original text is: {shifted_text}")


def choices():
    print("hello user.")
    print("MAIN MENU:")
    print("1.encrypt a text")
    print("2.decrypt the encyrypted text.")
    should_contiue= True
    while should_contiue:
     choice=int(input("enter your choice:"))
   
     if choice==1:
        encrypt()

     elif choice==2:
        decrypt()
    
     
     else:
        print("wrong choice")
     restart=input("type y/n to continue:").lower()
     if restart=="n":
         should_contiue=False
         print("ok goodbye!!")
         
choices()
