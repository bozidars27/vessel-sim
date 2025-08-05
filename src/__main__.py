from models.vessel import Vessel

def main():
    vessel = Vessel(name="Titanic", length=269.1, width=28.2, draft=10.5)
    print(vessel)

if __name__ == "__main__":
    main()