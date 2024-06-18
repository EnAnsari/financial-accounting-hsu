from operations import add_sheet, calculate_output, calculate_payment, clear_data, data_handler

def main():

    # download data
    members, records = data_handler.load_data()

    while True:
        print(f"members: {len(members)}, records: {len(records)}\n")
        print("[1] add csv files to db")
        print("[2] calculate output")
        print("[3] calculate payments")
        print("[4] export db to csv")
        print("[5] clear csv history")
        print("[6] clear data")
        print("[7] Exit...!")
        
        choice = input("\nEnter your choice: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            print("\ngoodbye!\n")
            break
        else:
            print("\nError: invalid choice. Try Again!\n")

    # update data
    data_handler.save_data(members, records)

if __name__ == "__main__":
    main()