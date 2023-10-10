import re

# Todo_1 マイナスの式の縦書きにするメソッドを整える
# Todo_2 リファクタリング


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
            print('\nエラー: 式の数が6個以上になっています。')
            return True

        return False

    def has_invalid_charactors(self, formula: str) -> bool:
        invalid_pattern = r'[^0-9\+\-\s]'

        if re.search(invalid_pattern, formula):
            print('\nエラー: 無効な文字が含まれています。')
            return True

        return False

    def has_long_formula(self, formula: str) -> bool:
        formulaElements: list = re.split(r'[ ]', formula)

        if len(formulaElements) != 3:
            print('\nエラー: 二つ以上の演算子が含まれている式があります。')
            return True

        return False

    def has_long_number(self, formula: str) -> bool:
        numbers_list: list = []

        if re.search(r'\+', formula):
            numbers_list = formula.split(' + ')
        elif re.search(r'\-', formula):
            numbers_list = formula.split(' - ')

        if len(numbers_list) == 0:
            print('\nエラー: 正しい式を入力して下さい。')
            return True

        if len(numbers_list[0]) > 4 or len(numbers_list[1]) > 4:
            print('\nエラー: 4桁以上の数値を使用している式があります。')
            return True

        return False

    def is_invalid_formula(self) -> bool:
        if self.is_too_many_problems():
            return True

        for formula in self.formula_list:
            if self.has_invalid_charactors(formula):
                return True
            if self.has_long_formula(formula):
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
        # print(n)
        # 演算子とスペースの二つ分のハイフンを初期値として設定
        top_ele_space = '  '

        for i in range(n):
            top_ele_space += ' '

        return top_ele_space

    def create_total_ele_space(self, difference: int) -> str:
        total_ele_space = ''

        for i in range(0, difference):
            total_ele_space += ' '

        return total_ele_space

    def create_bottom_ele_space(self, difference: int) -> str:
        bottom_ele_space: str = ' '

        for i in range(difference):
            bottom_ele_space += ' '

        return bottom_ele_space

    def create_vertical_calculation(self, formula: str) -> dict:
        formulaElements: list = re.split(r'[ ]', formula)

        top_ele: str = ''
        bottom_ele: str = ''
        longer: int = 0
        operator: str = formulaElements[1]
        total: str = self.calculateFormula(formulaElements)

        if operator == '-' or len(formulaElements[0]) <= len(formulaElements[2]):
            top_ele = formulaElements[0]
            bottom_ele = formulaElements[2]
        else:
            top_ele = formulaElements[2]
            bottom_ele = formulaElements[0]

        if len(top_ele) >= len(bottom_ele):
            longer = len(top_ele)
        else:
            longer = len(bottom_ele)

        dotted_line: str = self.create_dotted_line(len(bottom_ele))

        if operator == '-':
            dotted_line = self.create_dotted_line(longer)

        top_ele_space: str = self.create_top_ele_space(
            len(bottom_ele) - len(top_ele))

        bottom_ele_space = ' '

        if operator == '-':
            bottom_ele_space = self.create_bottom_ele_space(
                len(top_ele) - len(bottom_ele))

        total_ele_space: str = self.create_total_ele_space(
                len(dotted_line) - len(total))

        vertical_calculation_dict: dict = {
            'first_line': top_ele_space + top_ele + '    ',
            'second_line': operator + bottom_ele_space + bottom_ele + '    ',
            'third_line': dotted_line + '    ',
            'fourth_line': total_ele_space + total + '    ',
        }

        return vertical_calculation_dict

    def create_vertical_calculations_dict(self) -> None:
        vertical_calculations_dict: dict = {
            'first_line': '',
            'second_line': '',
            'third_line': '',
            'fourth_line': '',
        }

        for formula in self.formula_list:
            vertical_calculation_dict: dict = self.create_vertical_calculation(
                formula)

            vertical_calculations_dict['first_line'] += vertical_calculation_dict[
                'first_line']
            vertical_calculations_dict['second_line'] += vertical_calculation_dict[
                'second_line']
            vertical_calculations_dict['third_line'] += vertical_calculation_dict[
                'third_line']
            vertical_calculations_dict['fourth_line'] += vertical_calculation_dict[
                'fourth_line']

        print()
        print(vertical_calculations_dict['first_line'])
        print(vertical_calculations_dict['second_line'])
        print(vertical_calculations_dict['third_line'])
        print(vertical_calculations_dict['fourth_line'])
        print()

    def analyze_formula(self) -> None:
        self.set_number_from_input()

        if self.is_invalid_formula():
            return

        self.create_vertical_calculations_dict()

    def analyze_input(self) -> None:
        self.set_value_from_input()

        if self.has_invalid_operator():
            return

        self.analyze_formula()


verticalCalculator = VerticalCalculator()
verticalCalculator.output_description()
verticalCalculator.analyze_input()
