import re


class VerticalCalculator:

  def __init__(self):
    self.input_value: str = ''
    self.formula_list: list = []

  def output_description(self) -> None:
    path_name: str = 'description.txt'

    with open(path_name) as f:
      file_contents: str = f.read()
      print(file_contents)

  def set_value_from_input(self) -> None:
    self.input_value = input('計算式一覧 : ')

  def has_invalid_operator(self) -> bool:
    invalid_pattern = r'[*\/]'
    if (re.search(invalid_pattern, self.input_value)):
      print('\nエラー: 無効な演算子が含まれています。')
      return True

    return False

  def set_number_from_input(self) -> None:
    self.formula_list = self.input_value.split(", ")

  def is_too_many_problems(self) -> bool:
    if len(self.formula_list) > 5:
      print('エラー: 式の数が多すぎます。')
      return True

    return False

  def has_invalid_charactors(self, formula: str) -> bool:
    invalid_pattern = r'[^0-9\+\-\s]'

    if re.search(invalid_pattern, formula):
      print('\nエラー: 無効な文字が含まれています。')
      return True

    return False

  def has_long_number(self, formula: str) -> bool:
    numbers_list: list = []

    if re.search(r'\+', formula):
      numbers_list = formula.split(' + ')
    elif re.search(r'\-', formula):
      numbers_list = formula.split(' - ')

    if len(numbers_list) == 0:
      print('エラー: 正しい式を入力して下さい。')
      return True

    if len(numbers_list[0]) > 4 or len(numbers_list[1]) > 4:
      print('エラー: 4桁以上の数値を使用している式があります。')
      return True

    return False

  def is_invalid_formula(self) -> bool:
    if self.is_too_many_problems():
      return True

    for formula in self.formula_list:
      if self.has_invalid_charactors(formula):
        return True
      if self.has_long_number(formula):
        return True

    return False

  def calculateFormula(self, formula: list) -> str:
    total: str = ''

    if formula[1] == '+':
      total = str(int(formula[0]) + int(formula[2]))
    elif formula[1] == '-':
      total = str(int(formula[0]) - int(formula[2]))

    return total

  def create_dotted_line(self, n: int) -> str:
    # 演算子とスペースの二つ分のハイフンを初期値として設定
    dotted_line: str = '--'

    for i in range(n):
      dotted_line += '-'

    return dotted_line

  def create_top_ele_space(self, n: int) -> str:
    # 演算子とスペースの二つ分のハイフンを初期値として設定
    top_ele_space = '  '

    for i in range(n):
      top_ele_space += ' '

    return top_ele_space

  def create_last_ele_space(self, difference: int) -> str:
    last_ele_space = '  '

    if difference >= 1:
      last_ele_space += ' '

    return last_ele_space

  def create_vertical_calculation(self, formula: str) -> str:
    # 奇数番目は必ず記号、偶数番目は必ず数字
    formulaElements: list = re.split(r'[ ]', formula)

    shorter_str: str = ''
    longer_str: str = ''
    operator: str = formulaElements[1]
    total: str = self.calculateFormula(formulaElements)

    if len(formulaElements[0]) <= len(formulaElements[2]):
      shorter_str = formulaElements[0]
      longer_str = formulaElements[2]
    else:
      shorter_str = formulaElements[2]
      longer_str = formulaElements[0]

    dotted_line: str = self.create_dotted_line(len(longer_str))
    top_ele_space: str = self.create_top_ele_space(
        len(longer_str) - len(shorter_str))
    last_ele_space: str = self.create_last_ele_space(
        len(total) - len(longer_str))

    vertical_calculation: str = top_ele_space + shorter_str + '\n' + operator + ' ' + longer_str + '\n' + dotted_line + '\n' + last_ele_space + total

    return vertical_calculation

  def print_vertical_calculations(self) -> None:
    for formula in self.formula_list:
      vertical_calculation: str = self.create_vertical_calculation(formula)

      print(vertical_calculation)

  def analyze_formula(self) -> None:
    self.set_number_from_input()

    if self.is_invalid_formula():
      return

    self.print_vertical_calculations()

  def analyze_input(self) -> None:
    self.set_value_from_input()

    if self.has_invalid_operator():
      return

    self.analyze_formula()


verticalCalculator = VerticalCalculator()
verticalCalculator.output_description()
verticalCalculator.analyze_input()