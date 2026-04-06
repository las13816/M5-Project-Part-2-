from triage_system import TriageSystem


def main():
    triage = TriageSystem()

    patients = [
        ("Sofia", 5),
        ("Bob", 2),
        ("Charlie", 4),
        ("Diana", 3),
        ("Eli", 1),
        ("Tom", 4),
        ("Alice", 5),
        ("Rachel", 4)
    ]

    for name, severity in patients:
        triage.AddPatient(name, severity)

    print("Processing patients:")

    while not triage.IsEmpty():
        name, severity = triage.ProcessNext()
        print(f"Now treating: {name} (Severity {severity})")


if __name__ == "__main__":
    main()