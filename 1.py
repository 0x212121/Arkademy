import json

class Name:
    def __init__(self, address, hobbies, is_married, list_school, skills, interest_in_coding):
        self.name = "Indra Wijaya"
        self.address = address
        self.hobbies = hobbies
        self.is_married = is_married
        self.list_school = list_school
        self.skills = skills
        self.interest_in_coding = interest_in_coding

def biodata(name, age):
    result = {
        "name" : name.name,
        "age" : age,
        "address" : name.address,
        "hobbies" : name.hobbies,
        "is_married" : name.is_married,
        "list_school": name.list_school,
        "skills": name.skills,
        "interest_in_coding": name.interest_in_coding
    }
    output = json.dumps(result)
    return print(output)

list_school = [
    {
        "name": "SMPN 4",
        "year_in": "2009",
        "year_out": "2012",
        "major" : "null"
    },
    {
        "name" : "SMA 3",
        "year_in": "2012", 
        "year_out":"2015", 
        "major" : "IPA"
    },
    {
        "name" : "Mulawarman University",
        "year_in": "2015",
        "year_out": "2019",
        "major": "Teknik Informatika"
    }
]

skills = [
    {
        "skill_name": "Python Programming",
        "level" : "Intermediate"
    },
    {
        "skill_name": "Android",
        "level" : "Beginner"
    }
]

if __name__ == "__main__":
    Indra = Name("Samarinda", ['coding', 'reading'], False, list_school, skills, True)
    biodata(Indra, 23)