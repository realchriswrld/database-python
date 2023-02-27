from  main import  People

our_people = People.select()
for People in our_people:
    print(People.name, People.phonenumber, People.email, People.county, People.gender, People.religion, People.password)