

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    choice = read_int(
        """Welcome to the Indian Gas Company!
        What help do you need from the helpline number?
        1. Gas Leakage
        2. Gas Cylinder Replacement
        3. Gas Cylinder Booking
        4. Gas Cylinder Delivery
        5. Gas Cylinder Cancellation
        6. Gas Cylinder Refund

        Please select the problem you have: """
    )

    match choice:
        case 1:
            gas_leakage = read_int(
                """Please select the problem you have:
                1. Gas Leakage in kitchen
                2. Gas Leakage in bathroom
                3. Gas pipeline leakage
                4. Gas Leakage in the cylinder
                5. Gas Leakage in the stove
                Please select an option: """
            )
            match gas_leakage:
                case 1:
                    print("You selected Gas Leakage in kitchen")
                case 2:
                    print("You selected Gas Leakage in bathroom")
                case 3:
                    print("You selected Gas pipeline leakage; therefore replacing the pipeline")
                case 4:
                    print("You selected Gas Leakage in the cylinder")
                case 5:
                    print("You selected Gas Leakage in the stove")
                case _:
                    print("Invalid gas leakage choice")

        case 2:
            gas_cylinder_replacement = read_int(
                """Please select the problem you have:
                1. Gas Cylinder Replacement in kitchen
                2. Gas Cylinder Replacement in bathroom
                3. Gas Cylinder Replacement in the pipeline
                4. Gas Cylinder Replacement in the stove
                5. Gas Cylinder Replacement due to old cylinder
                Please select an option: """
            )
            match gas_cylinder_replacement:
                case 1:
                    print("You selected Gas Cylinder Replacement in kitchen")
                case 2:
                    print("You selected Gas Cylinder Replacement in bathroom")
                case 3:
                    print("You selected Gas Cylinder Replacement in the pipeline")
                case 4:
                    print("You selected Gas Cylinder Replacement in the stove")
                case 5:
                    print("You selected Gas Cylinder Replacement due to old cylinder")
                case _:
                    print("Invalid gas cylinder replacement choice")

        case 3:
            booking = read_int(
                """Please select the booking payment method:
                1. Wallet
                2. Online payment
                3. Cash on delivery
                Please select an option: """
            )
            match booking:
                case 1:
                    print("You selected booking by wallet")
                case 2:
                    print("You selected booking by online payment")
                case 3:
                    print("You selected booking by cash on delivery")
                case _:
                    print("Invalid booking choice")

        case 4:
            delivery = read_int(
                """Please select the delivery issue:
                1. Late delivery
                2. Delivery not received; booked 1 week ago
                3. Complaint about the delivery
                Please select an option: """
            )
            match delivery:
                case 1:
                    print("You selected late delivery")
                case 2:
                    print("You selected delivery not received after booking 1 week ago")
                case 3:
                    print("You selected a complaint about the delivery")
                case _:
                    print("Invalid delivery choice")

        case 5:
            cancellation = read_int(
                """Please select the cancellation reason:
                1. Delay in delivery of the cylinder
                2. Not needed now
                3. Booked by mistake
                4. Other
                Please select an option: """
            )
            match cancellation:
                case 1:
                    print("You selected cancellation due to delay in delivery of the cylinder")
                case 2:
                    print("You selected cancellation because the cylinder is not needed now")
                case 3:
                    print("You selected cancellation because it was booked by mistake")
                case 4:
                    print("You selected another cancellation reason")
                case _:
                    print("Invalid cancellation choice")

        case 6:
            refund = read_int(
                """Please select the refund issue:
                1. Refund through online payment
                2. Refund for cash on delivery
                3. Refund not received
                Please select an option: """
            )
            match refund:
                case 1:
                    print("You selected a refund through online payment")
                case 2:
                    print("You selected a refund for cash on delivery")
                case 3:
                    print("You selected refund not received")
                case _:
                    print("Invalid refund choice")

        case _:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()