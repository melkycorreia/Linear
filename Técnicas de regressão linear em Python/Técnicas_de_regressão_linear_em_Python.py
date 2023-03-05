import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Adicionando um subtítulo ao gráfico Direito Autoral Junto


#------------Autoral------------#

# adicionar título

plt.title('Regresao Linear', fontweight='bold')
plt.suptitle('[Todos Direitos Reservados,  Melky Correia do Nascimento, Ano de 2023©]')

#------------Autoral------------#


#Alimento De Dados com Números Variáveis


a= 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500

b= 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500


#Crie um conjunto de dados de exemplo com duas variáveis

A= 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L', 'LI', 'LII', 'LIII', 'LIV', 'LV', 'LVI', 'LVII', 'LVIII', 'LIX', 'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII', 'LXVIII', 'LXIX', 'LXX', 'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII', 'LXXVIII', 'LXXIX', 'LXXX', 'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI', 'LXXXVII', 'LXXXVIII', 'LXXXIX', 'XC', 'XCI', 'XCII', 'XCIII', 'XCIV', 'XCV', 'XCVI', 'XCVII', 'XCVIII', 'XCIX', 'C', 'CI', 'CII', 'CIII', 'CIV', 'CV', 'CVI', 'CVII', 'CVIII', 'CIX', 'CX', 'CXI', 'CXII', 'CXIII', 'CXIV', 'CXV', 'CXVI', 'CXVII', 'CXVIII', 'CXIX', 'CXX', 'CXXI', 'CXXII', 'CXXIII', 'CXXIV', 'CXXV', 'CXXVI', 'CXXVII', 'CXXVIII', 'CXXIX', 'CXXX', 'CXXXI', 'CXXXII', 'CXXXIII', 'CXXXIV', 'CXXXV', 'CXXXVI', 'CXXXVII', 'CXXXVIII', 'CXXXIX', 'CXL', 'CXLI', 'CXLII', 'CXLIII', 'CXLIV', 'CXLV', 'CXLVI', 'CXLVII', 'CXLVIII', 'CXLIX', 'CL', 'CLI', 'CLII', 'CLIII', 'CLIV', 'CLV', 'CLVI', 'CLVII', 'CLVIII', 'CLIX', 'CLX', 'CLXI', 'CLXII', 'CLXIII', 'CLXIV', 'CLXV', 'CLXVI', 'CLXVII', 'CLXVIII', 'CLXIX', 'CLXX', 'CLXXI', 'CLXXII', 'CLXXIII', 'CLXXIV', 'CLXXV', 'CLXXVI', 'CLXXVII', 'CLXXVIII', 'CLXXIX', 'CLXXX', 'CLXXXI', 'CLXXXII', 'CLXXXIII', 'CLXXXIV', 'CLXXXV', 'CLXXXVI', 'CLXXXVII', 'CLXXXVIII', 'CLXXXIX', 'CXC', 'CXCI', 'CXCII', 'CXCIII', 'CXCIV', 'CXCV', 'CXCVI', 'CXCVII', 'CXCVIII', 'CXCIX', 'CC', 'CCI', 'CCII', 'CCIII', 'CCIV', 'CCV', 'CCVI', 'CCVII', 'CCVIII', 'CCIX', 'CCX', 'CCXI', 'CCXII', 'CCXIII', 'CCXIV', 'CCXV', 'CCXVI', 'CCXVII', 'CCXVIII', 'CCXIX', 'CCXX', 'CCXXI', 'CCXXII', 'CCXXIII', 'CCXXIV', 'CCXXV', 'CCXXVI', 'CCXXVII', 'CCXXVIII', 'CCXXIX', 'CCXXX', 'CCXXXI', 'CCXXXII', 'CCXXXIII', 'CCXXXIV', 'CCXXXV', 'CCXXXVI', 'CCXXXVII', 'CCXXXVIII', 'CCXXXIX', 'CCXL', 'CCXLI', 'CCXLII', 'CCXLIII', 'CCXLIV', 'CCXLV', 'CCXLVI', 'CCXLVII', 'CCXLVIII', 'CCXLIX', 'CCL', 'CCLI', 'CCLII', 'CCLIII', 'CCLIV', 'CCLV', 'CCLVI', 'CCLVII', 'CCLVIII', 'CCLIX', 'CCLX', 'CCLXI', 'CCLXII', 'CCLXIII', 'CCLXIV', 'CCLXV', 'CCLXVI', 'CCLXVII', 'CCLXVIII', 'CCLXIX', 'CCLXX', 'CCLXXI', 'CCLXXII', 'CCLXXIII', 'CCLXXIV', 'CCLXXV', 'CCLXXVI', 'CCLXXVII', 'CCLXXVIII', 'CCLXXIX', 'CCLXXX', 'CCLXXXI', 'CCLXXXII', 'CCLXXXIII', 'CCLXXXIV', 'CCLXXXV', 'CCLXXXVI', 'CCLXXXVII', 'CCLXXXVIII', 'CCLXXXIX', 'CCXC', 'CCXCI', 'CCXCII', 'CCXCIII', 'CCXCIV', 'CCXCV', 'CCXCVI', 'CCXCVII', 'CCXCVIII', 'CCXCIX', 'CCC', 'CCCI', 'CCCII', 'CCCIII', 'CCCIV', 'CCCV', 'CCCVI', 'CCCVII', 'CCCVIII', 'CCCIX', 'CCCX', 'CCCXI', 'CCCXII', 'CCCXIII', 'CCCXIV', 'CCCXV', 'CCCXVI', 'CCCXVII', 'CCCXVIII', 'CCCXIX', 'CCCXX', 'CCCXXI', 'CCCXXII', 'CCCXXIII', 'CCCXXIV', 'CCCXXV', 'CCCXXVI', 'CCCXXVII', 'CCCXXVIII', 'CCCXXIX', 'CCCXXX', 'CCCXXXI', 'CCCXXXII', 'CCCXXXIII', 'CCCXXXIV', 'CCCXXXV', 'CCCXXXVI', 'CCCXXXVII', 'CCCXXXVIII', 'CCCXXXIX', 'CCCXL', 'CCCXLI', 'CCCXLII', 'CCCXLIII', 'CCCXLIV', 'CCCXLV', 'CCCXLVI', 'CCCXLVII', 'CCCXLVIII', 'CCCXLIX', 'CCCL', 'CCCLI', 'CCCLII', 'CCCLIII', 'CCCLIV', 'CCCLV', 'CCCLVI', 'CCCLVII', 'CCCLVIII', 'CCCLIX', 'CCCLX', 'CCCLXI', 'CCCLXII', 'CCCLXIII', 'CCCLXIV', 'CCCLXV', 'CCCLXVI', 'CCCLXVII', 'CCCLXVIII', 'CCCLXIX', 'CCCLXX', 'CCCLXXI', 'CCCLXXII', 'CCCLXXIII', 'CCCLXXIV', 'CCCLXXV', 'CCCLXXVI', 'CCCLXXVII', 'CCCLXXVIII', 'CCCLXXIX', 'CCCLXXX', 'CCCLXXXI', 'CCCLXXXII', 'CCCLXXXIII', 'CCCLXXXIV', 'CCCLXXXV', 'CCCLXXXVI', 'CCCLXXXVII', 'CCCLXXXVIII', 'CCCLXXXIX', 'CCCXC', 'CCCXCI', 'CCCXCII', 'CCCXCIII', 'CCCXCIV', 'CCCXCV', 'CCCXCVI', 'CCCXCVII', 'CCCXCVIII', 'CCCXCIX', 'CD', 'CDI', 'CDII', 'CDIII', 'CDIV', 'CDV', 'CDVI', 'CDVII', 'CDVIII', 'CDIX', 'CDX', 'CDXI', 'CDXII', 'CDXIII', 'CDXIV', 'CDXV', 'CDXVI', 'CDXVII', 'CDXVIII', 'CDXIX', 'CDXX', 'CDXXI', 'CDXXII', 'CDXXIII', 'CDXXIV', 'CDXXV', 'CDXXVI', 'CDXXVII', 'CDXXVIII', 'CDXXIX', 'CDXXX', 'CDXXXI', 'CDXXXII', 'CDXXXIII', 'CDXXXIV', 'CDXXXV', 'CDXXXVI', 'CDXXXVII', 'CDXXXVIII', 'CDXXXIX', 'CDXL', 'CDXLI', 'CDXLII', 'CDXLIII', 'CDXLIV', 'CDXLV', 'CDXLVI', 'CDXLVII', 'CDXLVIII', 'CDXLIX', 'CDL', 'CDLI', 'CDLII', 'CDLIII', 'CDLIV', 'CDLV', 'CDLVI', 'CDLVII', 'CDLVIII', 'CDLIX', 'CDLX', 'CDLXI', 'CDLXII', 'CDLXIII', 'CDLXIV', 'CDLXV', 'CDLXVI', 'CDLXVII', 'CDLXVIII', 'CDLXIX', 'CDLXX', 'CDLXXI', 'CDLXXII', 'CDLXXIII', 'CDLXXIV', 'CDLXXV', 'CDLXXVI', 'CDLXXVII', 'CDLXXVIII', 'CDLXXIX', 'CDLXXX', 'CDLXXXI', 'CDLXXXII', 'CDLXXXIII', 'CDLXXXIV', 'CDLXXXV', 'CDLXXXVI', 'CDLXXXVII', 'CDLXXXVIII', 'CDLXXXIX', 'CDXC', 'CDXCI', 'CDXCII', 'CDXCIII', 'CDXCIV', 'CDXCV', 'CDXCVI', 'CDXCVII', 'CDXCVIII', 'CDXCIX', 'D'

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

B = 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI', 'XIII', 'X', 'XI'


#Visualize o conjunto de dados usando um gráfico de dispersão


A= 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I', 'II', 'V', 'I'

# Alinhado de códigos

#'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I'

#'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I'


C= 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319
 

# Regressão Linear
slope, intercept = np.polyfit(x, y, 1)
plt.plot(x, slope*x + intercept, color='red', label='Regressão linear')


A= '1', 'X', 'XI', '1', 'X', 'XI', '1', 'X', 'XI', '1', 'X', 'XI', '1', 'X', 'XI', '1', 'X', 'XI', '1'


Y= 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III', 'I'

# Plot dos pontos
plt.scatter(x, y, color='blue', label='Dados')


B= '50', 'X', 'XI', '50', 'X', 'XI', '50', 'X', 'XI', '50', 'X', 'XI', '50', 'X', 'XI', '50', 'X', 'XI', '50'

# Personalização do Gráfico

#------------1= análise linear em gráfico
#------------2= análise linear em Status
#------------3= análise linear dos números

plt.title('Gráfico de Regressão Linear', fontweight='bold')

#------------1= análise linear em gráfico
#------------2= análise linear em Status
#------------3= análise linear dos números


plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)
plt.colorbar()

#------------1= análise linear em gráfico
#------------2= análise linear em Status
#------------3= análise linear dos números


J= '500', 'X', 'XI', '500', 'X', 'XI', '500', 'X', 'XI', '500', 'X', 'XI', '500', 'X', 'XI', '500', 'X', 'XI', '500'

#------------1= análise linear em gráfico
#------------2= análise linear em Status
#------------3= análise linear dos números


#=======%

plt.show()

#=======%


# Este código é fornecido sob a Licença BSD
