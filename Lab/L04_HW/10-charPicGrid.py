grid1, grid2, rotate_right, rotate_left, print_grid = [['.','.','.','.','.','.'],['.','o','o','.','.','.'],['o','o','o','o','.','.'],['o','o','o','o','o','.'],['.','o','o','o','o','o'],['o','o','o','o','o','.'],['o','o','o','o','.','.'],['.','o','o','.','.','.'],['.','.','.','.','.','.']], [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','o','.','o'],['o','o','.','o','.','o','.'],['o','o','o','o','o','.','.'],['o','o','.','o','.','o','.'],['.','.','.','.','o','.','o'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']], lambda grid: list(zip(*grid[::-1])), lambda grid: list(zip(*grid))[::-1], lambda grid: print('\n'.join(map(''.join, grid)))