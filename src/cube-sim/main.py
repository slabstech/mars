import spacex_rideshare
import json
import pandas as pd

def display_rideshare_plates():
    print("Available Plates from SpaceX")
    rideshare_plates = {"Hexagon": ["Quarter", "Half", "Full"], "Cube": ["Half XL", "XL"], "CubeSat Dispenser": ""}
    for plate in rideshare_plates.keys():
        print(plate)


def payload_maneuvers_deployments():
    print("After Payload Separation - Rules")
    payload_rules = {"attitude_maneuvers": "120 sec", "mechanical_appendage_deployment": "120 sec",
                     "secondary_deployment": " 7 days", "propulsive_maneuvers": "7 days",
                     "second_deployment_activation": "active attitude control"}
    for rules in payload_rules.keys():
        print(rules + " - " + payload_rules[rules])


def rideshare_program_schedule():
    program_schedule = {"Launch": ["Day 0"],
                        "Launch -2 Months": ["Range Safety Mission", "Launch Campaign Readiness Review",
                                             "Mission Integration Analysis Results", "Payload Operations"],
                        "Launch -4 Months": ["Range Safety Submission", "Launch Campaign Customer Inputs",
                                             "Mission Interfaces Finalized"],
                        "Launch -6 Months": ["Range Safety Submission", "Launch Campaign Planning Kickoff"],
                        "Launch -8 Months": ["Mission Integration Analysis Inputs"],
                        "Contract Signature": ["Mission Integration Kickoff"]}

    for schedule in program_schedule.keys():
        # print(schedule + " - " + program_schedule[schedule])
        print(schedule + " :- ")
        for sub_menu in program_schedule[schedule]:
            print(sub_menu)


def interface_control():
    pass


def show_launch_manifest():
    all_launches = pd.read_csv("data/psatcat.tsv", sep='\t', index_col=0)
    print(all_launches.size)
    print(all_launches.keys())

    unique_programs = all_launches['Program'].unique()
    #unique_1 = list(filter(None, unique_programs))
    #starlink = list(filter(lambda k: 'starlink' in k, unique_1))

    #for program in unique_programs:
    #   print(program)

    #for starlink_1 in starlink: print(starlink_1)

    #load_from_url = pd.read_csv("https://planet4589.org/space/gcat/tsv/cat/satcat.tsv")
    #print(load_from_url.size)

def show_disposal_code_launch():
    disposal_code = { "A": "Stage left in Earth orbit, but remains attached to payload by design.",
                      "B":	"Stage made depletion burn which boosted it to higher Earth orbit.",
                      "D":	"Actively deorbited to destructive reentry",
                      "E":	"Stage placed in Earth escape orbit",
                      "L":	"Small perigee lowering burn to reduce orbit lifetime (but not meeting criterion for P)",
                      "O":	"Left in Earth orbit for later uncontrolled reentry",
                      "P":	"Perigee lowered to 180 km or less for rapid decay, or stage left in orbit with that low a perigee to start with.",
                      "R":	"Recovered intact for possible reuse (so far, space shuttles only, considered as upper stages).",
                      "S":	"Stage left in marginally suborbital trajectory for targeted reentry on first orbit. Stages with perigees above -1000 km are included."
                      }
    for key, value in disposal_code.items():
        print(key + ": " + value)


def rideshare_info():
    rideshare_program_schedule()
    print("")
    interface_control()
    display_rideshare_plates()
    print("")
    payload_maneuvers_deployments()
    print("")
    show_disposal_code_launch()
    print("")

def main():
    print("Cube Simulation")

    #rideshare_info()

    show_launch_manifest()


if __name__ == "__main__":
    main()
