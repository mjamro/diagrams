from . import Custom

from diagrams import Node
import math 
import tempfile
from PIL import Image, ImageDraw, ImageFont
from PIL import ImagePath  
 

def scale(coords, margin, width, height):

    effective_width = width - margin * 2
    effective_height = height - margin * 2
    
    return list(map(lambda m: (m[0] * effective_width/2 + width/2, m[1] * effective_height/2 + height/2) , coords))


shapes = {
    "cube": {
        "outline": [
            (-0.87, 0.50),
            ( -0.87, -0.50),
            (0.0, -1.0),
            (0.87, -0.50),
            (0.87, 0.50),
            (0.0, 1.0),
            (-0.87, 0.50),
        ],
        "interior": [
            ( -0.87, -0.50),
            (0.0, -1.0),
            (0.87, -0.50),
            (0.0, 0.0),
            ( -0.87, -0.50),
        ]
    },
    "cylinder": {
        "outline": [
            (0.87, -0.48),
            (0.8658107122048113, -0.5270482273581891),
            (0.8532831939508104, -0.5736433545677415),
            (0.8325380920870217, -0.6193366450821419),
            (0.8037751932848195, -0.6636880475352431),
            (0.7672714999830689, -0.7062704336764789),
            (0.7233785627032143, -0.746673711849409),
            (0.6725190944255812, -0.7845087763985498),
            (0.6151828996322963, -0.8194112549695427),
            (0.5519221572223716, -0.8510450176141137),
            (0.483346102727054, -0.8791054139052218),
            (0.4101151610386181, -0.9033222068872103),
            (0.33293458615762817, -0.9234621756054175),
            (0.2525476692113822, -0.9393313611514603),
            (0.16972858015403164, -0.9507769345935506),
            (0.08527491208671786, -0.9576886688026544),
            (0.0, -0.96),
            (-0.08527491208671777, -0.9576886688026545),
            (-0.16972858015403153, -0.9507769345935506),
            (-0.2525476692113821, -0.9393313611514603),
            (-0.33293458615762805, -0.9234621756054175),
            (-0.410115161038618, -0.9033222068872103),
            (-0.4833461027270537, -0.8791054139052218),
            (-0.5519221572223715, -0.8510450176141138),
            (-0.6151828996322963, -0.8194112549695427),
            (-0.6725190944255812, -0.7845087763985498),
            (-0.7233785627032144, -0.746673711849409),
            (-0.7672714999830688, -0.706270433676479),
            (-0.8037751932848195, -0.6636880475352431),
            (-0.8325380920870217, -0.6193366450821419),
            (-0.8532831939508104, -0.5736433545677417),
            (-0.8658107122048112, -0.5270482273581892),
            (-0.87, -0.48),
            (-0.87, 0.48),
            (-0.8658107122048112, 0.5270482273581892),
            (-0.8532831939508104, 0.5736433545677417),
            (-0.8325380920870217, 0.6193366450821419),
            (-0.8037751932848195, 0.6636880475352431),
            (-0.7672714999830688, 0.706270433676479),
            (-0.7233785627032144, 0.746673711849409),
            (-0.6725190944255812, 0.7845087763985498),
            (-0.6151828996322963, 0.8194112549695427),
            (-0.5519221572223715, 0.8510450176141138),
            (-0.4833461027270537, 0.8791054139052218),
            (-0.410115161038618, 0.9033222068872103),
            (-0.33293458615762805, 0.9234621756054175),
            (-0.2525476692113821, 0.9393313611514603),
            (-0.16972858015403153, 0.9507769345935506),
            (-0.08527491208671777, 0.9576886688026545),
            (0.0, 0.96),
            (0.08527491208671786, 0.9576886688026544),
            (0.16972858015403164, 0.9507769345935506),
            (0.2525476692113822, 0.9393313611514603),
            (0.33293458615762817, 0.9234621756054175),
            (0.4101151610386181, 0.9033222068872103),
            (0.483346102727054, 0.8791054139052218),
            (0.5519221572223716, 0.8510450176141137),
            (0.6151828996322963, 0.8194112549695427),
            (0.6725190944255812, 0.7845087763985498),
            (0.7233785627032143, 0.746673711849409),
            (0.7672714999830689, 0.7062704336764789),
            (0.8037751932848195, 0.6636880475352431),
            (0.8325380920870217, 0.6193366450821419),
            (0.8532831939508104, 0.5736433545677415),
            (0.8658107122048113, 0.5270482273581891),
            (0.87, 0.48),
            (0.87, -0.48),
        ],
        "interior": [
            (0.87, -0.5184),
            (0.8658107122048113, -0.5654482273581891),
            (0.8532831939508104, -0.6120433545677415),
            (0.8325380920870217, -0.6577366450821419),
            (0.8037751932848195, -0.7020880475352431),
            (0.7672714999830689, -0.7446704336764789),
            (0.7233785627032143, -0.785073711849409),
            (0.6725190944255812, -0.8229087763985499),
            (0.6151828996322963, -0.8578112549695428),
            (0.5519221572223716, -0.8894450176141137),
            (0.483346102727054, -0.9175054139052218),
            (0.4101151610386181, -0.9417222068872104),
            (0.33293458615762817, -0.9618621756054175),
            (0.2525476692113822, -0.9777313611514603),
            (0.16972858015403164, -0.9891769345935506),
            (0.08527491208671786, -0.9960886688026545),
            (0.0, -0.9984),
            (-0.08527491208671777, -0.9960886688026545),
            (-0.16972858015403153, -0.9891769345935506),
            (-0.2525476692113821, -0.9777313611514603),
            (-0.33293458615762805, -0.9618621756054175),
            (-0.410115161038618, -0.9417222068872104),
            (-0.4833461027270537, -0.9175054139052218),
            (-0.5519221572223715, -0.8894450176141138),
            (-0.6151828996322963, -0.8578112549695428),
            (-0.6725190944255812, -0.8229087763985499),
            (-0.7233785627032144, -0.785073711849409),
            (-0.7672714999830688, -0.744670433676479),
            (-0.8037751932848195, -0.7020880475352431),
            (-0.8325380920870217, -0.657736645082142),
            (-0.8532831939508104, -0.6120433545677417),
            (-0.8658107122048112, -0.5654482273581892),
            (-0.8658107122048112, -0.4713517726418107),
            (-0.8532831939508104, -0.4247566454322582),
            (-0.8325380920870217, -0.379063354917858),
            (-0.8037751932848195, -0.3347119524647568),
            (-0.7672714999830688, -0.292129566323521),
            (-0.7233785627032144, -0.25172628815059095),
            (-0.6725190944255812, -0.21389122360145016),
            (-0.6151828996322963, -0.17898874503045722),
            (-0.5519221572223715, -0.14735498238588618),
            (-0.4833461027270537, -0.11929458609477823),
            (-0.410115161038618, -0.09507779311278963),
            (-0.33293458615762805, -0.07493782439458237),
            (-0.2525476692113821, -0.059068638848539655),
            (-0.16972858015403153, -0.047623065406449394),
            (-0.08527491208671777, -0.04071133119734548),
            (0.0, -0.0384),
            (0.08527491208671786, -0.04071133119734558),
            (0.16972858015403164, -0.047623065406449394),
            (0.2525476692113822, -0.059068638848539655),
            (0.33293458615762817, -0.07493782439458237),
            (0.4101151610386181, -0.09507779311278963),
            (0.483346102727054, -0.11929458609477823),
            (0.5519221572223716, -0.1473549823858863),
            (0.6151828996322963, -0.17898874503045722),
            (0.6725190944255812, -0.21389122360145016),
            (0.7233785627032143, -0.25172628815059095),
            (0.7672714999830689, -0.29212956632352105),
            (0.8037751932848195, -0.3347119524647568),
            (0.8325380920870217, -0.3790633549178581),
            (0.8532831939508104, -0.42475664543225844),
            (0.8658107122048113, -0.47135177264181083),
        ]
    }
}

class Template(Custom):
    size = (256, 256)
    margin = 8
    color = "#888888"
    text = ""
    text_color = '#000000'
    text_font = 'arial.ttf'
    text_font_size = 30
    text_stroke_width = 0
    text_stroke_color = 'white'
    text_spacing = -5
    shape = "cube"

    def __init__(self, label=""):
        icon_path = self.create_icon();
        super().__init__(label, icon_path)

    def create_icon(self):
       
        width, height = self.size
        margin = self.margin

        img = Image.new("RGBA", self.size, "#ffffff00")  
        canvas = ImageDraw.Draw(img)   
      
        if self.shape in shapes:
            shape = shapes[self.shape]

            if 'outline' in shape:
                xy = scale(shape['outline'], margin, width, height)
                canvas.line(xy, fill=self.color, width=10, joint="curve")

            if 'interior' in shape:
                xy = scale(shape['interior'], 3 * margin, width, height)
                canvas.polygon(xy, fill=self.color)
        
            self.draw_text(canvas)

        _, path = tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)

        img.save(path, "PNG")

        return path

    def draw_text(self, canvas):
        if self.text and not self.text.isspace():

            width, height = self.size
            margin = self.margin

            font = ImageFont.truetype(self.text_font, self.text_font_size)
            text_width, text_height = canvas.multiline_textsize(self.text, font=font, stroke_width=self.text_stroke_width, spacing=self.text_spacing)

            x = width/2 - text_width/2
            y = margin + (height - 2 * margin ) * 5/8 + self.margin - text_height/2
            canvas.multiline_text((x, y), text=self.text, font=font, fill=self.text_color, spacing=self.text_spacing, stroke_width=self.text_stroke_width, stroke_fill=self.text_stroke_color, align='center')


class CubeTemplate(Template):
    shape = "cube"

class CylinderTemplate(Template):
    shape = "cylinder"