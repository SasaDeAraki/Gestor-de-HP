import json
from PIL import Image, ImageDraw, ImageFont

def draw_text_with_outline(draw, position, text, font, text_color, outline_color, outline_width=2):
    x, y = position
    
    # Desenha o contorno: texto deslocado em 8 direções ao redor
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
                
    # Desenha o texto principal por cima
    draw.text(position, text, font=font, fill=text_color)

def atualizar_imagem():
    positions = [
        (709, 23),  # Centro
        (552, 351), # Esquerda
        (870, 351), # Meio-esquerda
        (552, 678), # Meio-direita
        (870, 678)  # Direita
    ]

    # Nome dos arquivos JSON (em ordem)
    json_files = ["json/trex.json", "json/buzz.json", "json/ze.json", "json/festor.json", "json/renna.json"]

    # Carrega a imagem de fundo
    bg = Image.open("Combate.png")
    draw = ImageDraw.Draw(bg)

    # Fonte
    try:
        font = ImageFont.truetype("C:/Users/sasa/AppData/Local/Microsoft/Windows/Fonts/CocoGothicSmallCaps-Regular.otf", size=20)
    except: 
        font = ImageFont.load_default()

    # Renderiza cada personagem
    for idx, json_file in enumerate(json_files):
        with open(json_file, 'r', encoding="utf-8") as f:
            data = json.load(f)
        
        x, y = positions[idx]

        draw.text((x, y), f"{data['structure']}", fill="white", font=font, anchor="mm", outline_width=2)
        draw.text((x, y + 20), f"{data['stress']}", fill="white", font=font, anchor="mm", outline_width=2)

        draw.text((x + 50, y), f"{data['current_hp']}", fill="white", font=font, anchor="rm", outline_width=2)
        draw.text((x + 50, y + 20), f"{data['current_heat']}", fill="white", font=font, anchor="rm", outline_width=2)

        draw.text((x + 70, y), f"{data['max_hp']}", fill="white", font=font, anchor="lm", outline_width=2)
        draw.text((x + 74, y +20), f"{data['max_heat']}", fill="white", font=font, anchor="lm", outline_width=2)

    # Salva a imagem final
    bg.save("combate_atualizado.png")

atualizar_imagem()