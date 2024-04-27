class Robots:
  '''
    Name, status/ active/ inactive/ destroyed, location / current/initial, specifications- store local,
  '''
  def __init__(self, name, year):
    self.name = name
    self.year = year

  def get_robots(self):
        print("Robot Details: " + self.name + ' ' + str(self.year))

def main():
    print("Habitat Design")
    r1 = Robots('perserverance', 2020)
    r1.get_robots()


if __name__ == "__main__":
    main()