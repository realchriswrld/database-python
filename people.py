from main import People

try:

    People_name = input("Enter persons name \n")
    People_phonenumber = input("Enter phonenumber \n")
    People_email = input("Enter persons email \n")
    People_county = input("Enter persons county \n")
    People_gender = input("Enter persons gender \n")
    People_religion = input("Enter persons religion \n")
    People_password = input("Enter persons password \n")

    People.create( name = People_name, phonenumber = People_phonenumber, email = People_email, county = People_county, gender = People_gender, religion = People_religion, password = People_password)
    print("people created successfully")


except:
    print("failed to create people successfully")