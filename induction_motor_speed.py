
print("======================================")
print("   INDUCTION MOTOR SPEED CALCULATOR")
print("======================================")

frequency = float(input("Enter supply frequency (Hz): "))
poles = int(input("Enter number of poles: "))
slip_percent = float(input("Enter slip (%): "))

if frequency <= 0 or poles <= 0 or slip_percent < 0 or slip_percent >= 100:
    print("\nPlease enter valid values.")
else:
    synchronous_speed = (120 * frequency) / poles

    slip = slip_percent / 100

    rotor_speed = synchronous_speed * (1 - slip)

    print("\n------------- RESULTS -------------")
    print(f"Supply Frequency   : {frequency:.2f} Hz")
    print(f"Number of Poles    : {poles}")
    print(f"Slip               : {slip_percent:.2f}%")
    print(f"Synchronous Speed  : {synchronous_speed:.2f} RPM")
    print(f"Rotor Speed        : {rotor_speed:.2f} RPM")
    print("-----------------------------------")
