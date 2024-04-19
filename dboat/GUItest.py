import dboatRandom as balance
import tkinter as tk
import PaddlerClass as pad

def calculate():
    # Get inputs from entry widgets
    left_weights = [float(entry1[i].get()) for i in range(10)]
    right_weights = [float(entry2[i].get()) for i in range(10)]

    # Find optimal seating calling balance program
    optimal_seating = balance.find_optimal_seating(left_weights, right_weights)
    torque = balance.calculate_total_torque(optimal_seating[0], optimal_seating[1])
    
    # Update result label
    result_label.config(text=f"Left Weights: {optimal_seating[0]}\nRight Weights: {optimal_seating[1]}\nTorque Factor: {torque}")

# Create the main application window
root = tk.Tk()
root.title("Enter Paddler Information")

# Create frames
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, padx=10)
frame2 = tk.Frame(root)
frame2.pack(side=tk.LEFT, padx=10)
frame3 = tk.Frame(root)
frame3.pack(side=tk.LEFT, padx=10)

# Create entry widgets for the first set of numbers
label1 = tk.Label(frame1, text="Enter the left weights:")
label1.pack()
entry1 = [tk.Entry(frame1, width=5) for _ in range(10)]
for entry in entry1:
    entry.pack()

# Create entry widgets for the second set of numbers
label2 = tk.Label(frame2, text="Enter the right weights:")
label2.pack()
entry2 = [tk.Entry(frame2, width=5) for _ in range(10)]
for entry in entry2:
    entry.pack()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
