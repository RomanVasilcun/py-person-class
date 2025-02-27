class Person:
    people = {}
    def  __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_instances.append(person)
    for person_dict, person_instance in zip(people, person_instances):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[person_dict["husband"]]
    return person_instances

