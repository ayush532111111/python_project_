voting_data = {}

def add_candidate(candidate_name):
    if candidate_name in voting_data:
        print("Candidate already exists!")
    else:
        voting_data[candidate_name] = 0
        print(f"{candidate_name} added as a candidate.")

def vote(candidate_name):
    if candidate_name in voting_data:
        voting_data[candidate_name] += 1
        print(f"Vote casted for {candidate_name}.")
    else:
        print("Invalid candidate!")

def display_results():
    print("Voting Results:")
    for candidate, votes in voting_data.items():
        print(f"{candidate}: {votes} votes")

def main():
    while True:
        print("\nVoting System")
        print("1. Add Candidate")
        print("2. Vote")
        print("3. Display Results")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            candidate_name = input("Enter candidate name: ")
            add_candidate(candidate_name)
        elif choice == '2':
            candidate_name = input("Enter candidate name to vote for: ")
            vote(candidate_name)
        elif choice == '3':
            display_results()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
