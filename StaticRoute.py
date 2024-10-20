import xml.etree.ElementTree as ET
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, Text
import os

# Function to parse the configuration file and extract device details
def parse_configuration(config_file):
    tree = ET.parse(config_file)
    root = tree.getroot()

    devices = {}

    # Find all device entries in the XML
    for device in root.findall('.//DEVICE'):
        device_id = device.get('DEVICE_ID')  # Get the DEVICE_ID attribute
        if device_id is None:
            continue  # Skip if DEVICE_ID is missing

        interface = device.find('INTERFACE')  # Find the INTERFACE section
        if interface is None:
            continue  # Skip if INTERFACE is missing

        interface_id = interface.get('ID')  # Get the INTERFACE ID
        ip_property = interface.find(".//NETWORK_PROTOCOL/PROTOCOL_PROPERTY")
        if ip_property is not None:
            ip_address = ip_property.get('IP_ADDRESS')  # Get IP Address
        else:
            continue  # Skip if IP_ADDRESS is missing

        # Store details in devices dictionary
        devices[device_id] = {
            'ip_address': ip_address,
            'interface_id': interface_id
        }

    return devices

# Function to generate static route files for each device, skipping the last one
def generate_static_routes(route_path, devices, output_directory):
    destination_id = str(route_path[-1])  # Ensure it is a string
    if destination_id not in devices:
        messagebox.showerror("Error", f"Destination device ID {destination_id} not found in configuration.")
        return

    destination_ip = devices[destination_id]['ip_address']

    # Iterate through the route path, skipping the last device
    for i in range(len(route_path) - 1):
        device_id = str(route_path[i])  # Ensure device_id is a string

        if device_id not in devices:
            messagebox.showerror("Error", f"Device ID {device_id} not found in configuration.")
            continue

        next_hop_id = str(route_path[i + 1])  # Ensure next_hop_id is a string

        if next_hop_id not in devices:
            messagebox.showerror("Error", f"Next hop device ID {next_hop_id} not found in configuration.")
            continue

        # Save the static route file inside the ConfigSupport folder
        static_route_filename = os.path.join(output_directory, f"StaticIPConfigure{device_id}.txt")
        next_hop_ip = devices[next_hop_id]['ip_address']
        interface_id = devices[device_id]['interface_id']

        # Write the static route for the current device
        with open(static_route_filename, 'a') as f:
            route_entry = f"route ADD {destination_ip} MASK 255.255.255.255 {next_hop_ip} METRIC 1 IF {interface_id}\n"
            f.write(route_entry)

# GUI Functions
def select_file():
    # Allow both .xml and .netsim file types
    file_path = filedialog.askopenfilename(filetypes=[("XML and NetSim Files", "*.xml;*.netsim"), ("All Files", "*.*")])
    if file_path:
        file_entry.delete(0, "end")
        file_entry.insert(0, file_path)

def generate_routes():
    config_file = file_entry.get()
    route_input = route_text.get("1.0", "end").strip()

    if not config_file or not route_input:
        messagebox.showerror("Error", "Please provide both the configuration file and the route paths.")
        return

    try:
        # Get the directory of the configuration file to save the route files
        xml_directory = os.path.dirname(config_file)

        # Create the ConfigSupport folder inside the XML location if it doesn't exist
        output_directory = os.path.join(xml_directory, "ConfigSupport")
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        devices = parse_configuration(config_file)
        if not devices:
            messagebox.showerror("Error", "No devices found in the configuration file.")
            return

        # Split route_input by lines to get individual routes
        routes = route_input.splitlines()
        
        for route in routes:
            route_path = route.split(',')
            generate_static_routes(route_path, devices, output_directory)

        messagebox.showinfo("Success", f"Static route files generated successfully in {output_directory}!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the GUI window
root = Tk()
root.title("Static Route Generator")

# Labels and Entry fields
Label(root, text="Select Configuration File:").grid(row=0, column=0, padx=10, pady=10)
file_entry = Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Enter Route Paths (one per line):").grid(row=1, column=0, padx=10, pady=10)

# Multi-line Textbox for multiple route inputs
route_text = Text(root, height=10, width=50)
route_text.grid(row=1, column=1, padx=10, pady=10)

# Generate Button
Button(root, text="Generate Routes", command=generate_routes).grid(row=2, column=1, padx=10, pady=20)

# Run the GUI
root.mainloop()
