from Printing_Class import Printing
import FromPairNumber,PairNumberFromColor

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]



if __name__ == '__main__':
  ColorFromPairNumber = FromPairNumber.test_number_to_pair(4,'White', 'Brown')
  ColorFromPairNumber = FromPairNumber.test_number_to_pair(5, 'White', 'Slate')
  PairNumberFromColors=PairNumberFromColor.test_pair_to_number('Black', 'Orange', 12)
  PairNumberFromColors=PairNumberFromColor.test_pair_to_number('Violet', 'Slate', 25)
  PairNumberFromColors=PairNumberFromColor.test_pair_to_number('Red', 'Orange', 7)     
  Printcolors=Printing.color_pair_to_string(MAJOR_COLORS, MINOR_COLORS)
