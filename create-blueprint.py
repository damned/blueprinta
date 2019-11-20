import sys
from blueprinter.blueprint_creator import BlueprintCreator

print(sys.argv)
xls_input_filename = sys.argv[1]
svg_output_filename = sys.argv[2]
BlueprintCreator().create_blueprint(xls_input_filename, svg_output_filename)
