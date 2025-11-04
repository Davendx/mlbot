require 'dlc'
require 'json'

# Get package name and links from command line arguments
package_name = ARGV[0]
links = ARGV[1].split(',')

# Create a new DLC container
container = DLC::Package.new
container.name = package_name
container.add_link(links)

# Define the output file path
output_file = "#{package_name}.dlc"

# Write the DLC file
File.open(output_file, "w") do |f|
  f.write container.dlc
end

puts "DLC file '#{output_file}' created successfully."
