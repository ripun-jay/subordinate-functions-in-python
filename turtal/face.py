import colorsys as cs
import turtle as tu


class rdj:
    def __init__(self):
        self.mouth = [(374, 382), (368, 382), (359, 382), (347, 379), (339, 381), (334, 384), (323, 380), (315, 380),
                      (293, 385), (321, 387), (339, 387), (345, 386), (357, 385), (374, 383), (-1, -1), (389, 389),
                      (393, 387), (395, 381), (395, 373), (377, 362), (366, 357), (358, 360), (351, 357), (345, 354),
                      (344, 357), (337, 355), (333, 357), (327, 355), (323, 357), (303, 362), (293, 365), (286, 367),
                      (282, 374), (277, 376), (279, 394), (286, 390), (293, 380), (297, 378), (302, 378), (304, 375),
                      (307, 378), (310, 374), (313, 377), (315, 373), (319, 375), (322, 374), (325, 376), (329, 375),
                      (336, 375), (342, 374), (350, 374), (353, 376), (357, 374), (369, 374), (372, 377), (374, 374),
                      (377, 378), (383, 379), (389, 389), ]
        self.nose = [(342, 305), (342, 313), (344, 321), (344, 328), (343, 335), (338, 342), (331, 344), (322, 343),
                     (313, 340), (310, 339), (307, 339), (303, 333), (301, 338), (305, 343), (313, 344), (323, 349),
                     (332, 353), (343, 345), (346, 342), (354, 342), (359, 338), (360, 329), (355, 322), (348, 320),
                     (348, 323), (354, 325), (356, 331), (353, 336), (348, 335), (350, 330), (348, 323), (343, 305), ]
        self.dress = [(56, 513), (222, 433), (247, 393), (249, 408), (254, 425), (265, 456), (265, 456), (273, 478),
                      (280, 495), (283, 509), (294, 539), (302, 527), (314, 515), (328, 503), (347, 491), (350, 493),
                      (340, 499), (349, 507), (359, 517), (380, 498), (397, 505), (412, 516), (425, 526), (432, 533),
                      (435, 539), (399, 523), (399, 530), (395, 538), (353, 539), (347, 530), (320, 519), (300, 539),
                      (293, 539), (-1, -1), (363, 507), (391, 478), (401, 458), (422, 408), (423, 398), (420, 407),
                      (400, 440), (386, 460), (377, 471), (371, 475), (366, 480), (357, 482), (348, 478), (339, 470),
                      (330, 462), (316, 453), (301, 444), (276, 420), (248, 391), (253, 399), (267, 419), (278, 430),
                      (288, 441), (295, 445), (303, 453), (326, 475), (338, 484), (347, 492), (353, 498), (363, 508),
                      (371, 500), (-1, -1), (427, 401), (437, 486), (441, 526), (443, 539), (624, 539), (625, 477),
                      (528, 449), (477, 428), (447, 412), (428, 401), ]
        self.face = [(328, 461), (316, 457), (305, 453), (297, 446), (286, 436), (284, 434), (280, 431), (277, 431),
                     (279, 428), (275, 428), (272, 423), (262, 411), (250, 395), (244, 387), (241, 382), (238, 377),
                     (235, 372), (236, 367), (234, 363), (234, 358), (231, 354), (231, 349), (230, 346), (231, 343),
                     (228, 339), (229, 336), (226, 330), (227, 324), (223, 320), (224, 317), (221, 311), (216, 310),
                     (212, 306), (213, 302), (216, 308), (220, 306), (220, 297), (217, 294), (219, 284), (216, 279),
                     (216, 272), (211, 266), (208, 272), (206, 266), (207, 256), (205, 249), (204, 243), (204, 237),
                     (208, 233), (208, 229), (206, 229), (206, 222), (202, 215), (202, 210), (197, 204), (198, 197),
                     (193, 193), (192, 173), (190, 170), (191, 166), (190, 162), (191, 159), (188, 154), (186, 148),
                     (188, 142), (188, 135), (188, 127), (191, 122), (186, 121), (177, 112), (185, 115), (179, 105),
                     (188, 114), (182, 98), (191, 109), (194, 104), (200, 101), (194, 99), (203, 94), (206, 85),
                     (211, 82), (218, 80), (213, 78), (208, 79), (212, 76), (218, 76), (216, 69), (218, 64), (219, 70),
                     (221, 75), (223, 68), (230, 64), (231, 58), (234, 56), (235, 52), (236, 47), (240, 42), (242, 35),
                     (252, 32), (270, 28), (283, 28), (290, 28), (297, 29), (304, 33), (318, 29), (332, 28), (346, 27),
                     (356, 27), (366, 29), (379, 36), (363, 24), (375, 26), (389, 36), (397, 40), (405, 45), (411, 54),
                     (422, 61), (429, 70), (433, 83), (435, 91), (436, 79), (436, 99), (436, 106), (441, 99),
                     (435, 113), (450, 108), (469, 111), (477, 108), (473, 114), (467, 126), (477, 120), (479, 124),
                     (471, 132), (473, 136), (472, 145), (483, 148), (479, 151), (480, 161), (483, 168), (480, 173),
                     (480, 178), (476, 184), (474, 190), (472, 196), (465, 197), (462, 204), (462, 211), (461, 217),
                     (459, 224), (463, 231), (456, 229), (452, 237), (449, 245), (448, 254), (448, 262), (450, 257),
                     (452, 251), (454, 244), (458, 239), (462, 243), (462, 251), (458, 246), (456, 251), (454, 255),
                     (458, 257), (452, 266), (454, 273), (455, 282), (452, 288), (453, 296), (458, 286), (457, 295),
                     (453, 303), (449, 304), (448, 297), (450, 290), (453, 280), (448, 273), (448, 280), (446, 288),
                     (445, 300), (444, 308), (448, 315), (454, 311), (454, 317), (449, 319), (443, 316), (442, 327),
                     (439, 339), (437, 350), (433, 362), (430, 370), (430, 378), (426, 385), (420, 393), (416, 399),
                     (411, 404), (408, 409), (403, 414), (399, 419), (394, 427), (386, 435), (381, 441), (376, 444),
                     (371, 448), (367, 451), (359, 456), (352, 458), (348, 461), (341, 461), (336, 463), (330, 459),
                     (328, 462), (316, 457), ]
        self.iface = [(311, 400), (324, 402), (338, 402), (347, 402), (356, 399), (363, 397), (359, 402), (356, 408),
                      (353, 414), (348, 419), (349, 426), (359, 426), (362, 430), (367, 433), (374, 434), (376, 436),
                      (379, 432), (383, 433), (385, 427), (393, 419), (394, 416), (398, 413), (400, 408), (401, 394),
                      (408, 402), (415, 394), (421, 385), (424, 380), (424, 373), (427, 367), (432, 353), (434, 345),
                      (436, 339), (434, 330), (438, 322), (438, 312), (437, 310), (440, 309), (441, 293), (443, 288),
                      (441, 284), (444, 275), (440, 265), (442, 233), (439, 227), (439, 221), (434, 211), (425, 203),
                      (432, 203), (421, 192), (430, 196), (421, 187), (430, 187), (419, 178), (432, 180), (420, 172),
                      (428, 174), (422, 165), (415, 159), (413, 147), (408, 140), (403, 140), (402, 138), (395, 139),
                      (394, 136), (388, 138), (386, 136), (379, 138), (377, 133), (372, 134), (369, 131), (364, 134),
                      (360, 133), (355, 135), (353, 131), (348, 132), (347, 127), (346, 131), (343, 127), (336, 131),
                      (331, 128), (327, 130), (323, 126), (319, 129), (313, 125), (309, 131), (306, 126), (303, 131),
                      (297, 126), (296, 131), (289, 127), (287, 130), (282, 126), (280, 132), (274, 128), (274, 135),
                      (268, 131), (264, 135), (256, 134), (256, 139), (251, 138), (252, 142), (246, 142), (247, 146),
                      (244, 149), (245, 154), (239, 154), (243, 160), (236, 163), (242, 164), (233, 169), (238, 170),
                      (231, 177), (237, 176), (227, 184), (237, 180), (229, 190), (237, 189), (229, 198), (237, 195),
                      (232, 202), (239, 205), (229, 212), (238, 210), (232, 215), (238, 215), (233, 220), (227, 227),
                      (224, 237), (224, 246), (226, 253), (226, 259), (227, 267), (227, 277), (224, 291), (223, 304),
                      (225, 311), (228, 319), (231, 330), (234, 340), (235, 349), (237, 361), (241, 372), (248, 385),
                      (252, 391), (258, 397), (264, 402), (268, 396), (272, 398), (272, 406), (279, 414), (278, 419),
                      (284, 426), (292, 431), (292, 435), (296, 438), (299, 438), (301, 442), (308, 439), (313, 435),
                      (317, 435), (319, 430), (321, 428), (325, 426), (327, 426), (332, 424), (331, 416), (326, 416),
                      (318, 408), (318, 404), (311, 400), (324, 402), ]
        self.ebrow = [(339, 243), (339, 248), (343, 254), (350, 256), (358, 251), (367, 248), (382, 247), (397, 249),
                      (407, 252), (418, 258), (419, 253), (414, 245), (399, 235), (391, 235), (381, 237), (372, 238),
                      (361, 243), (353, 245), (343, 255), (-1, -1), (321, 246), (320, 258), (314, 257), (305, 254),
                      (263, 253), (245, 259), (243, 257), (246, 250), (253, 245), (260, 242), (269, 241), (276, 241),
                      (282, 243), (291, 245), (305, 245), (311, 249), (319, 252), (322, 246), ]
        self.lines = [(345, 313), (344, 308), (343, 297), (343, 282), (-1, -1), (367, 340), (384, 357), (-1, -1),
                      (295, 337), (280, 359), (-1, -1), (385, 278), (394, 278), (400, 273), (408, 264), (400, 261),
                      (389, 257), (377, 258), (371, 260), (358, 269), (362, 272), (-1, -1), (395, 257), (371, 254),
                      (353, 263), (-1, -1), (303, 274), (309, 273), (297, 263), (290, 262), (272, 262), (261, 270),
                      (256, 271), (262, 271), (269, 277), (283, 281), (-1, -1), (255, 267), (271, 260), (282, 259),
                      (291, 259), (300, 260), (311, 264), ]
        self.eyes = [(375, 260), (375, 266), (378, 271), (384, 273), (389, 270), (391, 267), (392, 264), (391, 260),
                     (388, 258), (384, 257), (379, 257), (375, 261), (-1, -1), (291, 263), (292, 269), (289, 273),
                     (286, 276), (281, 276), (276, 273), (274, 269), (274, 265), (276, 263), (281, 262), (287, 262),
                     (291, 263), ]
        self.eball = [(281, 266), (279, 267), (277, 266), (277, 264), (279, 263), (281, 264), (281, 266), (-1, -1),
                      (379, 259), (382, 260), (382, 263), (380, 264), (378, 263), (377, 261), (379, 259), ]
        self.pen = tu.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.x_offset = 300
        self.y_offset = 300

    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        self.pen.pendown()

    def paint(self, coord, co=(0, 0, 0)):
        self.pen.color(co)
        t_x, t_y = coord[0]
        self.go(t_x, t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x, y = i
            if t:
                self.go(x, y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        self.pen.end_fill()

    def draw_fn(self, coord, mode=1, co=(0, 0, 0), thickness=1):
        co = (co[0] / 255, co[1] / 255, co[2] / 255)

        self.pen.color(co)

        if mode:
            self.pen.width(thickness)
            t_x, t_y = coord[0]
            self.go(t_x, t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x, y = i
                if t:
                    self.go(x, y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        else:
            self.paint(coord=coord, co=co)

    def draw(self, retain=True):
        self.draw_fn(self.dress, mode=0)
        self.draw_fn(self.face, mode=0)
        self.draw_fn(self.iface, co=(255, 255, 255), mode=0)
        self.draw_fn(self.mouth, mode=0)
        self.draw_fn(self.nose, mode=0)
        self.draw_fn(self.ebrow, mode=0)
        self.draw_fn(self.lines, mode=1, thickness=2)
        self.draw_fn(self.eyes, mode=0)
        self.draw_fn(self.eball, mode=0, co=(255, 255, 255))
        if retain:
            tu.done()


pen = rdj()
pen.draw()