"""
first column node
second column final or not
third column 
"""
tStates = [
    [0, 0, 1,  2, 3,  4, 5,  6,  7],
    [1, 1, -1, -1, -1, -1, -1, -1, -1],
    [2, 1, -1,  2, 2, -1, -1, -1, -1],
    [3, 1, -1, -1, 3, -1, -1, -1, -1],
    [4, 1, -1, -1, -1,  8, -1, -1, -1],
    [5, 1, -1, -1, -1,  9, -1, -1, -1],
    [6, 1, -1, -1, -1,  10, -1, -1, -1],
    [7, 0, -1, -1, -1,  11, -1, -1, -1],
    [8, 1, -1, -1, -1, -1, -1, -1, -1],
    [9, 1, -1, -1, -1, -1, -1, -1, -1],
    [10, 1, -1, -1, -1, -1, -1, -1, -1],
    [11, 1, -1, -1, -1, -1, -1, -1, -1],
]

isStates = ["<TERM>",
            "<var>",
            "<num>",
            "<eqTo>",
            "<GreatT>",
            "<LessT",
            " ",
            "<EqualT>",
            "<GreEqT>",
            "<LesEqT>",
            "<DiffT>"]
