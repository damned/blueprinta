import sys
from blueprinter.file_based_blueprint_creator import FileBasedBlueprintCreator

print(sys.argv)
xls_input_filename = sys.argv[1]
svg_output_filename = sys.argv[2]
FileBasedBlueprintCreator().create_blueprint(xls_input_filename, svg_output_filename)
