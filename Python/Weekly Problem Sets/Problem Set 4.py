"""Problem Set 4 — Problem 1 solution
Soldier Roster & Dispatch System
This script parses a list of raw personnel report strings, builds a roster
dictionary, prints summary information, and implements a `dispatch` function
that updates a soldier's status from "available" to "deployed".
The demonstration code is wrapped in an `if __name__ == "__main__":` block
so autograders can import the functions without executing the demo.
"""


def process_reports(report_list: list[str]) -> tuple:
    roster = {}
    ranks = set()
    for report in report_list:
        parts = []
        for part in report.split("|"):
            parts.append(part.strip())

        # Expecting format: NAME | Rank | Fitness:NN | Status:state
        name = parts[0].title()
        rank = parts[1].upper()

        # Parse fitness and status fields
        fitness_field = int(parts[2].split(":", 1)[1].strip())
        status_field = parts[3].split(":", 1)[1].strip().lower()

        roster[name] = {
            "rank": rank,
            "fitness": int(fitness_field),
            "deployed": status_field == "deployed",
        }

        ranks.add(rank)

    return roster, ranks


def show_available(roster: dict[str, dict[str, object]]) -> None:
    available_soldiers = []

    for name, info in roster.items():
        if not info.get("deployed", False):
            available_soldiers.append(name)

    available_soldiers.sort()
    print(f"Available soldiers: {available_soldiers}\n")


def dispatch(roster: dict[str, dict[str, object]], name: str) -> None:
    """Set a soldier's status to 'deployed' if available.
    Prints an informative message when the soldier is deployed, already
    deployed, or not found.
    """
    display_name = name.title()
    print(f"Dispatching {display_name}...", end=" ")

    soldier = roster.get(display_name)
    if soldier is None:
        print(f"{display_name} not found in roster.")
        return

    if not soldier.get("deployed", False):
        soldier["deployed"] = True
        print("Done. Status set to deployed.")
    else:
        print(f"{display_name} is already deployed.")


def fitness_report(roster: dict[str, dict[str, object]]) -> dict[str, list[str]]:
    bands = {"high": [], "medium": [], "low": []}

    for name, info in roster.items():
        fitness_level = info.get("fitness", 0)
        if fitness_level >= 80:
            bands["high"].append(name)
        elif 60 <= fitness_level <= 79:
            bands["medium"].append(name)
        else:
            bands["low"].append(name)

    for level in bands.values():
        level.sort()

    return bands


if __name__ == "__main__":
    reports = [
        "SANTOS | Private | Fitness:91 | Status:available",
        "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
        "OKAFOR | Sergeant | Fitness:88 | Status:available",
        "BRIGGS | Private | Fitness:55 | Status:available",
        "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
        "REYES | Sergeant | Fitness:79 | Status:available",
    ]

    roster, ranks = process_reports(reports)

    print("=== ROSTER LOADED ===")
    print(f"{len(roster)} soldiers on record.")
    print(f"Ranks on file: {ranks}\n")

    show_available(roster)

    dispatch(roster, "Santos")
    dispatch(roster, "Kowalski")
    print("\nUpdated status:")
    for name in ["Santos", "Kowalski"]:
        info = roster.get(name.title())
        status = "deployed" if info.get("deployed") else "available"
        print(f"  {name:8}: {status}")

    # Optional challenge output
    print("\nFitness report:")
    report = fitness_report(roster)
    for band in ("high", "medium", "low"):
        print(f"  {band.title():6}: {report[band]}")
