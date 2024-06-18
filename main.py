from operations import add_sheet, calculate_output, calculate_payment, data_handler, export_csv

MAXMEMBER = 10

def main():

    # download data
    members, records, history = data_handler.load_data()

    while True:
        print(f"members: {len(members)}, records: {len(records)}\n")
        print("[1] add csv files to db")
        print("[2] calculate output")
        print("[3] calculate payments")
        print("[4] export db to csv")
        print(f"[5] clear csv history ({len(history)} file)")
        print("[6] clear data")
        print("[7] Exit...!")
        
        choice = input("\nEnter your choice: ")
        if choice == '1':
            add_sheet.add_data()
        elif choice == '2':
            calculate_output.calculate()
        elif choice == '3':
            calculate_payment.calculate()
        elif choice == '4':
            if not members:
                print('\nError: DB is empty!\n')
            else:
                export_csv.export(members, records)
        elif choice == '5':
            if input("Are you sure (yes/no)? ").lower() in ['yes', 'y']:
                history.clear()
                print('\ncleard successfully!\n')
        elif choice == '6':
            if input("Are you sure (yes/no)? ").lower() in ['yes', 'y']:
                members.clear()
                records.clear()
                print('\ncleard successfully!\n')
        elif choice == '7':
            print("\ngoodbye!\n")
            break
        else:
            print("\nError: invalid choice. Try Again!\n")

    # update data
    data_handler.save_data(members, records, history)

if __name__ == "__main__":
    main()