import spacex_rideshare
import json


def display_rideshare_plates():
    print("Available Plates from SpaceX")
    rideshare_plates = {"Hexagon": ["Quarter", "Half", "Full"], "Cube": ["Half XL", "XL"], "CubeSat Dispenser": ""}
    for plate in rideshare_plates.keys():
        print(plate)


def payload_maneuvers_deployments():
    print("After Payload Separation - Rules")
    payload_rules = {"attitude_maneuvers": "120 sec", "mechanical_appendage_deployment": "120 sec",
                     "secondary_deployment": " 7 days", "propulsive_maneuvers": "7 days",
                     "second_deployment_activation": "active attitude control" }
    for rules in payload_rules.keys():
        print(rules + " - " + payload_rules[rules])

def main():
    print("Cube Simulation")

    display_rideshare_plates()
    print("")
    payload_maneuvers_deployments()


if __name__ == "__main__":
    main()
