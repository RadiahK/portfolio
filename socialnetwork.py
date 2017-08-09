class User:
    # Define the fields and methods for your object here.

    def __init__(self, name):
        self.name = name
        self.connections = []
    person = input("Username:")
    print ("Welcome", person)
    def make_connection(self, connection):
        self.connections.append(connection)
    person_one = input("First Person: ")
    person_two = input("Second person: ")
    print("Connection successfully made between " + person_one + " and " + person_two)




class Network:
    def __init__(self, users):
        self.users = []
    def adduser(self, user):
        self.adduser(user)
#
def main():
# Define the program flow for your user interface here.
    print ("hi")

# # Runs your program.
# if __name__ == '__main__':
#     main():
