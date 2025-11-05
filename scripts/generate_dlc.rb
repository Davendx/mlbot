require 'dlc'
require 'json'

# Get arguments
package_name = ARGV[0]
links_json = ARGV[1]
links = JSON.parse(links_json)

# Create DLC
container = DLC::Container.new
container.package = package_name
container.links = links
container.generate

# Write DLC file
File.open("#{package_name}.dlc", 'w') do |f|
  f.write container.dlc
end
